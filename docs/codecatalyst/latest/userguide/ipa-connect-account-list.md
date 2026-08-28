---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account-list.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Viewing account connections
<a name="ipa-connect-account-list"></a>

You can view a list of your connections and view details about each connection.

You must have the **Space administrator** or **Power user** role to manage connections for your space.

**To view all connections for a CodeCatalyst space**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to the space with the account connection that you want to view.

1. Choose the **AWS accounts** tab.

1. Under **AWS accounts**, view the list of account connections for the space, including the account ID and status for each connection.

**To view account connection details**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose **AWS accounts**.

1. In **Amazon CodeCatalyst display name**, choose the connection name. On the **Details** page, view the list of IAM roles associated with the connection along with other details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
