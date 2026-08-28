---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-secrets.creating.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Creating a secret
<a name="workflows-secrets.creating"></a>

Use the following procedure to create a secret. The secret contains the sensitive information that you want to hide from view.

**Note**
Secrets are visible to actions and are not masked when written to a file.

**To create a secret**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the navigation pane, choose **CI/CD**, and then choose **Secrets**.

1. Choose **Create secret**.

1. Enter the following information:
**Name**
Enter a name for your secret.
**Value**
Enter the value for the secret. This is the sensitive information that you want to hide from view. By default, the value is not displayed. To display the value, choose **Show value**.
**Description**
(Optional) Enter a description for your secret.

1. Choose **Create**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
