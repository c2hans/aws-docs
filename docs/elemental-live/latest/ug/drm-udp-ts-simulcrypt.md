---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/drm-udp-ts-simulcrypt.html
---

# UDP/TS outputs with DVB Simulcrypt Standard
<a name="drm-udp-ts-simulcrypt"></a>

Encryption mode: Always AES CBC as described in ATIS-0800006

Supported client players: Consult with the key provider (DRM implementer) for supported players.

| Description | Key provider (DRM implementer) | Version of server API from DRM implementer | Key rotation |
| --- | --- | --- | --- |
| The customer uses the Verimatrix MultiCAS/DVB DRM solution for protecting UDP/TS output in compliance with the DVB Simulcrypt standard. The end user plays the content on a Verimatrix-approved player. | Verimatrix | ECMG interface as described in ETSI TS 101 197 | Rotating |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
