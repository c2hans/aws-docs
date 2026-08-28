---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account-delete.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Deleting account connections (in CodeCatalyst)
<a name="ipa-connect-account-delete"></a>

You can delete an account connection that you no longer need. For this procedure, you will use CodeCatalyst to delete an account connection that you have previously added to your space. This deletes the account connection from your space, provided that the account is not the billing account for the space.

**Important**
After an account connection is deleted, you cannot reconnect it. You must create a new account connection and then associate IAM roles and environments, or set up billing, as needed.

A billing account must be designated for your CodeCatalyst space, even if usage for the space will not exceed the Free tier. Before you can remove a space for an account that is a designated billing account, you will need to add another account for your space. See [Managing billing](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing.html) in the Amazon CodeCatalyst Administrator Guide.

**Important**
While you can use these steps to remove an account, this is not recommended. The account might also be set up to support workflows in CodeCatalyst.

To manage account connections for your space, you must have the **Space administrator** or **Power user** role.

An account that has been removed can be added again later, but you must create a new connection between the account and the space. You will need to re-associate any IAM roles to the added account.

**To delete an account connection**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose **AWS accounts**.

1. Under **Amazon CodeCatalyst display name**, choose the selector next to the account connection that you want to remove.

1. Choose **Remove AWS account**. Confirm the deletion by entering the name in the field, and then choose **Remove**.

   A success banner displays, and the account connection is removed from the list of connections.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
