---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/drm-hls-securemedia.html
---

# HLS output with SecureMedia
<a name="drm-hls-securemedia"></a>

Encryption mode: Always AES CTR (AES-128)

Supported client players: Consult with the key provider (DRM implementer) for supported players.

| Description | Key provider (DRM implementer) | Version of server API from DRM implementer | Key rotation |
| --- | --- | --- | --- |
| The customer uses the Arris SecureMedia DRM solution for protecting HLS output using the SecureMedia DRM technology. The end user plays the content on a SecureMedia-approved player. | SecureMedia | No versioning information is available from Arris. | Static, Rotating |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
