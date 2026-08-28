---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/share-project-information-iam-based.html
---

# Share Project Information
<a name="share-project-information-iam-based"></a>

This feature simplifies user onboarding by providing all necessary access information in a formatted message that can be copied and shared via email or other communication channels.

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. Choose the project name from the Projects list.

1. On the project details page, choose **Share info**.

1. In the Share project information dialog, review the generated welcome message that includes:
   + Welcome text explaining the project setup
   + URL - Direct link to the Amazon SageMaker Unified Studio portal
   + IAM role - The specific IAM role the user should use to access the project

1. Choose **Copy message** to copy the entire welcome message to your clipboard.

1. Choose **Close** to close the dialog.

1. Paste the copied message into your preferred communication method (email, chat, documentation) to share with project members.

The welcome message provides users with complete information needed to access their project, including login instructions and the specific IAM role they should use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
