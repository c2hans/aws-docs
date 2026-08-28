---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/link-byol-account.html
---

# Link BYOL accounts in WorkSpaces
<a name="link-byol-account"></a>

You can use BYOL linking to link accounts and share BYOL configurations. BYOL configurations include the CIDR range used by your accounts and the images you use to create WorkSpaces with your Windows license. All accounts that are linked share the same underlying hardware infrastructure.

The account enabled for BYOL linking is the primary owner of the underlying hardware infrastructure, and is called the Source account. The Source account manages access to the underlying hardware infrastructure. Target accounts are the accounts that are linked to the Source account.

**Important**
APIs for BYOL account linking are not available in the AWS GovCloud (US) Region.

**Note**
The AWS accounts that you want to link with must be part of your organization and under the same payer account. You can only link accounts within the same Region.

**To link the Source and Target accounts**

1. Send an invitation link from your Source account to the Target account by using the **[ CreateAccountLinkInvitation](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateAccountLinkInvitation.html)** API.

1. Accept the pending link from your Target account by using the **[ AcceptAccountLinkInvitation](https://docs.aws.amazon.com/workspaces/latest/api/API_AcceptAccountLinkInvitation.html)** API.

1. Verify the link has been established by using the **[ GetAccountLink](https://docs.aws.amazon.com/workspaces/latest/api/API_GetAccountLink.html)** or **[ListAccountLinks](https://docs.aws.amazon.com/workspaces/latest/api/API_ListAccountLinks.html)** API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
