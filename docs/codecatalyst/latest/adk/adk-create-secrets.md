---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/adk/adk-create-secrets.html
---

# Creating secrets
<a name="adk-create-secrets"></a>

As a developer, you might have API keys, secrets, or tokens. You can create secrets to use sensitive data in your workflows. The action is the main building block of a CodeCatalyst workflow and used by the workflow to integrate the action within the workflow itself. values shouldn't be used directly in any workflow definitions because they will be visible as files in your repository. With CodeCatalyst, you can protect these values by adding a secret to your project, and then referencing the secret in your workflow definition file. For more information, see [Creating a secret](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-secrets.html#workflows-secrets.creating). To learn more about workflows and actions, see [ Working with workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/working-with-workflows.html) and [ Working with actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-actions.html).

## Example: Creating AWS access key and ID
<a name="adk-create-secrets-example"></a>

In this example, two secrets are created: AWS access key ID and an AWS secret access key that will be passed to the action.

**To create secrets**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the navigation pane, choose **CI/CD**, and then choose **Secrets**.

1. Choose **Create secret**.

1. Enter the following information:

   For **Name**, enter *AWS\_ACCESS\_KEY\_ID*. This is the name for your secret.

   For **Value**, enter *AWS Access Key ID*. Enter the value for the secret. This is the sensitive information that you want to hide from view. By default, the value is not displayed. To display the value, choose **Show value**.

   (Optional) For **Description**, enter a description for your secret.

1. Choose **Create**. The secret can later be accessed using the reference ID (`$(Secrets.AWS_SECRET_ACCESS_KEY)`).

1. Choose **Create secret** to create a second secret.

1. Enter the following information:

   For **Name**, enter *AWS\_ACCESS\_KEY*. This is the name for your secret.

   For **Value**, enter *AWS Secrets Access Key*. Enter the value for the secret. This is the sensitive information that you want to hide from view. By default, the value is not displayed. To display the value, choose **Show value**.

   (Optional) For **Description**, enter a description for your secret.

1. Choose **Create**. The secret can later be accessed using the reference ID (`$(Secrets.AWS_SECRET_ACCESS_KEY)`).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
