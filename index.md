---
layout: page
title: LOLWeb
description: LOLWeb is a curated reference of web application platforms and their attack vectors for achieving Remote Code Execution, reverse shells, and persistent access.
---

![LOLWeb logo]({{ '/assets/logo.svg' | relative_url }}){:.logo}

{{ page.description }}

The project [documents]({{ '/scope/' | relative_url }}) how legitimate features of widely deployed web applications — CMS platforms, CI/CD servers, application frameworks, and admin panels — can be abused to execute OS commands, establish reverse shells, deploy persistent web shells, and read or write server-side files. Each entry focuses on a specific technology and maps its attack vectors to the access level required and the resulting capability.

LOLWeb is intended as a reference for authorized penetration testers, red teamers, and security researchers. Everyone can [get involved]({{ '/contributing/' | relative_url }}) by contributing new entries and techniques.

If you are looking for Linux binary LOLBins you should visit [GTFOBins][]. For Windows binaries, visit [LOLBAS][].

> Please note that this is **not** a list of vulnerabilities. The techniques documented here abuse legitimate features or common misconfigurations in web application platforms. Always obtain proper authorization before testing.

[GitHub][]
|
[Get involved]({{ '/contributing/' | relative_url }})
|
[Contributors][contributors]
|
[JSON API]({{ '/api.json' | relative_url }})
|
[MITRE ATT&CK® Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL={{ '/mitre.json' | absolute_url }})
{:.centered}

[contributors]: https://github.com/L0Lweb/WebShellBins/graphs/contributors
[GTFOBins]: https://gtfobins.github.io/
[LOLBAS]: https://lolbas-project.github.io/
[GitHub]: https://github.com/L0Lweb/WebShellBins

<div>{%- include lolwebs_table.html -%}</div>
