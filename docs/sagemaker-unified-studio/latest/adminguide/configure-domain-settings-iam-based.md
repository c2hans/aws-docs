---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configure-domain-settings-iam-based.html
---

# Configure Domain Settings
<a name="configure-domain-settings-iam-based"></a>

The Settings section in domain administration provides access to domain-level configuration options that apply across all projects in your Amazon SageMaker Unified Studio domain. Domain administrators can view domain details and configure networking settings.

1. From the domain administration page, choose **Settings** in the left navigation pane.

1. The Settings page displays the **Domain details** section with the following information:
   + Account - AWS account ID where the domain is hosted
   + Region - AWS region where the domain is deployed
   + Domain ID - Unique identifier for the Amazon SageMaker Unified Studio domain
   + Admin login role - IAM role ARN for domain administrator login
   + Admin execution role - IAM role ARN for domain administrator execution
   + Creation date - When the domain was created
   + KMS key ARN - AWS KMS key used for domain encryption

1. Review the **Networking** section to view or configure:
   + VPC configuration settings
   + Subnet assignments
   + Network security parameters

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
