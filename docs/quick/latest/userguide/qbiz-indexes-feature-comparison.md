---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-feature-comparison.html
---

# Feature comparison
<a name="qbiz-indexes-feature-comparison"></a>

The following table compares key features between IDC and Amazon Q Business implementations:

| Feature | IDC Implementation | Non-IDC Implementation |
| --- | --- | --- |
| User management | AWS Identity Center | Amazon Quick |
| Amazon Quick authentication methods | Identity Center Only | Native identities (username/password), AWS Managed Microsoft AD, IAM federation |
| Amazon Q Business authentication methods | `AWS_IAM_IDC` | `AWS_QUICKSIGHT_IDP` |
| Share permissions | Amazon Q Business Console and Knowledge base permissions page | Amazon Quick Knowledge Base Permission page (Automatic) |
| Index compatibility | All indexes | All indexes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
