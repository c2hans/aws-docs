---
source_url: https://docs.aws.amazon.com/inspector/latest/user/remove-delegated-admin.html
---

# Removing the delegated administrator in Amazon Inspector
<a name="remove-delegated-admin"></a>

 You might need to remove the Amazon Inspector delegated administrator account. You can do this from the AWS Organizations management account. When you remove the Amazon Inspector delegated administrator account, Amazon Inspector is still activated in the account and in all of its member accounts. The delegated administrator account and all of its member accounts become standalone accounts and retain their original scan settings.

**Note**
 If AWS Organizations policies are managing Amazon Inspector enablement, removing the delegated administrator does not affect policy enforcement. Accounts will remain enabled according to the organization policy settings, though member account findings will no longer be visible in a central delegated administrator console until a new delegated administrator is designated.

 This section describes how to remove the delegated administrator account.

## Remove the Amazon Inspector delegated administrator
<a name="w2aac47c13c15b9"></a>

 The following procedures describe how to remove the Amazon Inspector delegated administrator and how to associate member accounts from the delegated administrator account.

 For information about how to assign an Amazon Inspector delegated admninistrator, see [Designating a delegated administrator account for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/designating-admin.html).

**Note**
 After you assign an Amazon Inspector delegated administrator, the Amazon Inspector delegated administrator must associate member accounts manually.

**To remove the delegated administrator**

1.  Sign in to the AWS Management Console using the AWS Organizations management account.

1.  Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home).

1.  Use the region selector to choose the AWS Region where you want to remove the delegated administrator.

1.  From the navigation pane, choose **General settings**.

1.  Under **Delegated administrator**, choose **Remove**, and then confirm your action.

**To associate members with a new delegated administrator**

1.  Sign in using the delegated administrator account credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home).

1.  Use the region selector to choose the AWS Region where you want to associate members.

1.  From the navigation pane, choose **Account management**.

1.  Under **Organization**, select the box next to **Account number**.

1.  Choose **Actions**, and then choose **Add member**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
