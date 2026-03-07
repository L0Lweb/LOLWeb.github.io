from .error import LinterError

from pathlib import Path
import schema
import yaml


def _string(x):
    if isinstance(x, str) and len(x.strip()) > 0:
        return True
    else:
        raise schema.SchemaError(f'{x!r} should be a non-empty string')


def _check_code_coherence(example):
    has_code = bool(example.get('code'))
    all_contexts_have_code = all(
        context and context.get('code')
        for context in example.get('contexts', {}).values()
    )
    if has_code != all_contexts_have_code:
        return True
    else:
        raise schema.SchemaError(f'{example!r} should provide the code')


def _context(name):
    return {
        schema.Optional(name): schema.Or(None, {
            schema.Optional('code'): _string,
            schema.Optional('comment'): _string,
        })
    }


def _function(name, per_function_schema):
    # Build the contexts schema dynamically from contexts.yml
    contexts_schema = {}
    for ctx_name in _contexts:
        contexts_schema.update(_context(ctx_name))

    return {
        schema.Optional(name): schema.And(len, [
            schema.And({
                schema.Optional('code'): _string,
                schema.Optional('comment'): _string,
                schema.Optional('version'): schema.Or(_string, int, float),
                schema.Optional('mitre'): [
                    schema.Regex(r'^T[0-9]+(\.[0-9]+)?$'),
                ],
                schema.Optional('platform'): schema.Or('linux', 'windows'),
                **per_function_schema,
                'contexts': contexts_schema,
            }, _check_code_coherence),
        ]),
    }


_root = Path(__file__).parent / '..'
_functions = yaml.safe_load((_root / '_data' / 'functions.yml').read_text())
_contexts = yaml.safe_load((_root / '_data' / 'contexts.yml').read_text())


_additional_example = {
    schema.Or('code', 'comment'): _string,
}


_binary = {
    schema.Optional('binary'): bool,
}


_blind = {
    schema.Optional('blind'): bool,
}


_tty = {
    schema.Optional('tty'): bool,
}


_listener = {
    schema.Optional('listener'): schema.Or(
        _additional_example,
        *_functions['reverse-shell']['extra']['listener'].keys(),
    )
}


_connector = {
    schema.Optional('connector'): schema.Or(
        _additional_example,
        *_functions['bind-shell']['extra']['connector'].keys(),
    )
}


_SCHEMA = schema.Or(
    {
        'alias': _string,
    },
    {
        schema.Optional('comment'): _string,
        schema.Optional('docker'): {
            schema.Optional('note'): _string,
            schema.Optional('compose'): _string,
        },
        'functions': schema.And(len, {
            **_function('rce', {
                **_blind,
            }),
            **_function('reverse-shell', {
                **_tty,
                **_blind,
                **_listener,
            }),
            **_function('bind-shell', {
                **_tty,
                **_blind,
                **_connector,
            }),
            **_function('webshell', {
            }),
            **_function('file-read', {
                **_binary,
            }),
            **_function('file-write', {
                **_binary,
            }),
            **_function('ssrf', {
            }),
        }),
    }
)


def validate(data):
    try:
        _SCHEMA.validate(data)
    except schema.SchemaError as e:
        raise LinterError(str(e.autos[-1]))
