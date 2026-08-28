---
source_url: https://docs.aws.amazon.com/artifact/latest/ug/assurance-assistant-setting-up.html
---

# Setting up
<a name="assurance-assistant-setting-up"></a>

## Prerequisites
<a name="assurance-assistant-prerequisites"></a>

To use Assurance Assistant, attach one of the following AWS IAM managed policies to your AWS account:

**IAM managed policies for Assurance Assistant**

| IAM policy | What it allows |
| --- | --- |
| [`AWSArtifactComplianceInquiriesReadOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSArtifactComplianceInquiriesReadOnlyAccess.html) | View responses and export results |
| [`AWSArtifactComplianceInquiriesFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSArtifactComplianceInquiriesFullAccess.html) | Submit questions, review responses, and export results |

For instructions on attaching managed policies, see [Granting user access to AWS Artifact](grant-access.md).

## Navigating to Assurance Assistant
<a name="assurance-assistant-navigating"></a>

In the AWS Artifact console homepage, choose **Assurance Assistant** in the left navigation panel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
