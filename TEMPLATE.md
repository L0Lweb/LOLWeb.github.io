# LOLWeb Entry Template

This file documents the YAML format for a `_lolwebs/<technology>` entry.
Copy the block below to `_lolwebs/<technology>` (no `.md` extension) and fill it in.

---

```yaml
---
comment: |
  Optional top-level comment describing the technology, the attack surface,
  or any important prerequisites (e.g., required configuration, access level
  context not captured by the function metadata).
functions:
  rce:
    - comment: |
        Describe the specific attack vector for this RCE example.
        Explain the mechanism (e.g., which endpoint, what feature is abused).
      code: |
        <payload code here>
      contexts:
        admin:
        console:

  reverse-shell:
    - comment: |
        Describe how and why this reverse shell works.
      code: |
        <payload code here>
      listener: tcp-server
      contexts:
        admin:
        ci_cd:
          code: |
            <alternative payload for CI/CD context>

  webshell:
    - comment: |
        Describe the deployment method (e.g., plugin upload, file editor).
      code: |
        <webshell payload here>
      contexts:
        admin:

  file-read:
    - code: |
        <file read payload here>
      contexts:
        authenticated:
...
```

---

## Field reference

| Field       | Required | Description                                                                 |
|-------------|----------|-----------------------------------------------------------------------------|
| `comment`   | No       | Human-readable explanation. Use pipe `\|` style for multi-line text.        |
| `version`   | No       | Platform version constraint that enables this technique.                    |
| `code`      | Yes*     | The payload. Required at top level OR in each context, not both.            |
| `blind`     | No       | `true` if command output is not returned to the attacker.                   |
| `tty`       | No       | `false` if the shell is not a full TTY (defaults to `true`).               |
| `binary`    | No       | `false` if the function cannot handle binary data (defaults to `true`).    |
| `listener`  | No       | Listener type for `reverse-shell`. Use a key from `_data/functions.yml`.   |
| `connector` | No       | Connector type for `bind-shell`. Use a key from `_data/functions.yml`.     |

Valid contexts: `unauthenticated`, `authenticated`, `admin`, `console`, `ci_cd`, `api_token`, `plugin`

Valid functions: `rce`, `reverse-shell`, `bind-shell`, `webshell`, `file-read`, `file-write`, `ssrf`

Valid listener keys: `tcp-server`, `tcp-server-tty`, `tls-server`

Valid connector keys: `tcp-client`, `tcp-client-tty`
