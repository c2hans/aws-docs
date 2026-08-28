---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/encryption-static-key-set-up.html
---

# Implementing CDN authorization with AWS Elemental MediaPackage
<a name="encryption-static-key-set-up"></a>

Use content delivery network (CDN) authorization to ensure only authorized devices can access your content. With CDN authorization, playback requests must include the appropriate header and authorization code that you create. MediaPackage refuses playback requests that don't include the correct code.

For more information about CDN authorization, see [CDN authorization in AWS Elemental MediaPackage](cdn-auth.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
