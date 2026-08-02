---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-05.html
---

# WKLD.05 Detect and remediate exposed secrets
<a name="wkld-05"></a>

In [WKLD.03 Use ephemeral secrets or a secrets-management service](wkld-03.md) and [WKLD.04 Prevent application secrets from being exposed](wkld-04.md), you put measures in place to protect secrets. In this control, you set up tooling to detect secrets that were accidentally committed or exposed, and take action to revoke or rotate them.

An exposed secret can be exploited and risks unauthorized access to your AWS resources and data. Rotate or revoke it immediately after detection.

Scan code repositories regularly for accidentally committed secrets. [Kiro CLI](https://aws.amazon.com/kiro/) includes built-in secret detection that scans your codebase for patterns matching API keys, access tokens, passwords, and other credential formats. It identifies secrets across files in your repository and reports their location so you can remediate them before they are exploited. Use Kiro CLI or the open-source tools listed in [WKLD.04](wkld-04.md) and integrate the tool into your local development or CI/CD pipeline. If you identify an exposed secret, remediate it immediately. Rotate or revoke the exposed credential to prevent further use, and remove it from source control history.

**To detect exposed secrets using Kiro CLI**

1. Install Kiro CLI in your development environment. For more information, see [Kiro CLI](https://kiro.dev/docs/cli/) in the Kiro documentation.

1. Configure Kiro CLI to scan your code repositories, focusing on high-risk repositories such as production or public-facing code.

1. Schedule regular scans. Consider daily scans for production repositories and weekly scans for development repositories.

1. Review scan results and identify any exposed secrets.

**To remediate exposed secrets**

1. Rotate or revoke the exposed secret immediately in the originating service (for example, regenerate an API key or reset a password).

1. Create a new secret in AWS Secrets Manager or AWS Systems Manager Parameter Store.

1. Update your applications to retrieve the new secret from the secure storage service.

1. Remove the exposed secret from your code repository history by using `git filter-repo`.

The open-source tools listed in [WKLD.04](wkld-04.md) can also detect secrets that are already present in your repository.

**Note**
Kiro CLI is available at no charge under the Free tier. For more information, see [Kiro pricing](https://kiro.dev/pricing/).
