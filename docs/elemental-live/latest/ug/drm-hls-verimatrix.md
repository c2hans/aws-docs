---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/drm-hls-verimatrix.html
---

# HLS output with Verimatrix
<a name="drm-hls-verimatrix"></a>

Encryption mode: Always AES CTR (AES-128)

Supported client players: Consult with the key provider (DRM implementer) for supported players.

| Description | DRM technology provider | Key provider (DRM implementer) | Version of server API from DRM implementer | Client player | Encryption mode | Key rotation |
| --- | --- | --- | --- | --- | --- | --- |
| The customer uses the Verimatrix VCAS DRM solution for protecting HLS output. This solution uses the Verimatrix-proprietary DRM technology. The end user plays the content on a Verimatrix-approved player. | Verimatrix Content Authority System<br />(VCAS) | Verimatrix | VCAS for Internet TV 4.2 Integration Guide | Verimatrix-approved player | AES CBC<br />(AES-128) | Static, Rotating |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
