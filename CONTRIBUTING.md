---
layout: page
title: Contributing
description: Get involved in LOLWeb.
permalink: /contributing/
---

## File format

Feel free to use any file in the [`_lolwebs/`] folder as an example.

Each entry is a [YAML][] file placed in the [`_lolwebs/`][] folder, named after the target technology (e.g., `jenkins`, `wordpress`), without any extension. The file contains a single YAML document with the following general structure:

```yaml
---
comment: …
functions:
  <function>:
    - comment: …
      version: …
      code: …
      contexts:
        <context>:
          comment: …
          code: …
        # …
    # …
  # …
...
```

Where `<function>` and `<context>` are defined in the [`_data/functions.yml`][] and [`_data/contexts.yml`][] files respectively.

The optional `version` field outlines any particular platform version or configuration requirement that enables the function.

When a context specifies a specialized `code` field, it is used in place of the global value. The global `code` can be omitted if every context provides its own specialization. `comment` instances are always optional. Ultimately, exactly one `code` must be present per context, either inherited from the top level or defined per-context.

### Functions

| Function        | Additional Fields            |
|-----------------|------------------------------|
| `rce`           | `blind`                      |
| `reverse-shell` | `blind`, `tty`, `listener`   |
| `bind-shell`    | `blind`, `tty`, `connector`  |
| `webshell`      | n/a                          |
| `file-read`     | `binary`                     |
| `file-write`    | `binary`                     |
| `ssrf`          | n/a                          |

Where:

- the optional `blind` field indicates whether the function returns command output to the attacker (`false`, the default) or not (`true` — output requires an out-of-band channel);

- the optional `tty` field indicates whether the shell is a full TTY (`true`, the default) or a limited non-interactive shell (`false`);

- the optional `binary` field indicates whether the function handles arbitrary binary data (`true`, the default) or text only (`false`);

- the optional `listener` field describes how the attacker receives the shell. It can be a string key from [`_data/functions.yml`][] (e.g., `tcp-server`), or a custom object with optional `comment` and `code` fields;

- the optional `connector` field describes how the attacker connects to the bind shell, using the same format as `listener`.

### Contexts

| Context          | Description                                          |
|------------------|------------------------------------------------------|
| `unauthenticated`| No credentials required                              |
| `authenticated`  | Valid credentials for any user role                  |
| `admin`          | Administrative or privileged account                 |
| `console`        | Application script or admin console                  |
| `ci_cd`          | CI/CD pipeline build step                            |
| `api_token`      | Valid API token with sufficient permissions          |
| `plugin`         | Via plugin, theme, or extension install/edit         |

### Aliases

To create an alias for an existing entry:

```yaml
---
alias: <lolweb>
...
```

## Conventions

### Placeholders

Use the following placeholder values where appropriate:

| Type                 | Value                  |
|----------------------|------------------------|
| Attacker host domain | `attacker.com`         |
| Victim host domain   | `victim.com`           |
| Network port         | `12345`                |
| Input file           | `/path/to/input-file`  |
| Output file          | `/path/to/output-file` |

### Code snippets

Payloads should be self-contained and functional. Do not truncate code with comments like `// ... truncated`. If a payload requires setup steps, document them in the `comment` field of the function or context.

## Local development

To test local changes, start a local instance with:

```
make serve
```

This spins up a Docker container that builds the website and serves it at <http://0.0.0.0:4000>. Changes to local files are applied automatically.

Before submitting a pull request, run the linter:

```
make vet
```

This validates both the schema and the formatting of YAML files. If formatting issues are reported, `make format` will fix them automatically.

Use `make clean` to clean up the build environment.

[YAML]: https://yaml.org/
[`_data/functions.yml`]: https://github.com/L0Lweb/WebShellBins/blob/master/_data/functions.yml
[`_data/contexts.yml`]: https://github.com/L0Lweb/WebShellBins/blob/master/_data/contexts.yml
[`_lolwebs/`]: https://github.com/L0Lweb/WebShellBins/tree/master/_lolwebs
