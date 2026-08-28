---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/howtoremovepermissionset.html
---

# Remove permission sets in IAM Identity Center
<a name="howtoremovepermissionset"></a>

You can remove a permission set from IAM Identity Center users and groups in the IAM Identity Center console. You can also remove a permission set from an AWS account. For more information about permission sets and how they are used in IAM Identity Center, see [Manage AWS accounts with permission sets](permissionsetsconcept.md).

**Note**
To use permission sets, you'll need to use an Organization instance of IAM Identity Center. For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md).

------
#### [ Remove permission set from a user ]

**Remove permission set from a user**

Use this procedure to remove a permission set from a user with the IAM Identity Center console.

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/).

1. Under **IAM Identity Center**, select **Users**.

1. Select the username of the user you want to remove a permission set from.

1. On the user details page, select the **AWS accounts** tab. Under **AWS account access**, select your AWS account.

1. In the right pane, the applied permissions for the selected user appears. Select the permission set you want to remove. Under **Account Access details**, select **Remove**.

1. A dialog box appears asking if you want to remove this permission set. Select **Remove**.
![AWS accounts tab for an IAM Identity Center user in the IAM Identity Center console.](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/remove-permission-set-tutorial.png)

------
#### [ Remove permission set from a group ]

**Remove permission set from a group**

Use this procedure to remove a permission set from a group with the IAM Identity Center console.

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/).

1. Under **Multi-account permissions**, select **AWS accounts**. Select the link to your management account.
![AWS accounts tab in the IAM Identity Center console.](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/sso-aws-accounts-tab.png)

1. Under the **Assigned users and groups** tab, select the group you want to remove the permission set from and then select **Change permission set**.

1. On the **Change permission sets** page, clear the permission set you want to remove and then select **Save changes**.

------
#### [ Remove permission set from an AWS account ]

Use this procedure to remove a permission set from the AWS account with the IAM Identity Center console.

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/).

1. Under **Multi-account permissions**, select **AWS accounts**. Select the name of the AWS account from which you want to remove the permission set.

1. On the **Overview** page of the AWS account, choose the **Permission sets** tab. Select the permission set you want to remove. Then select **Remove**.

1. In the **Remove permission set** dialog box, confirm that the correct permission set is selected, type **Delete** to confirm removal, and then choose **Remove access**.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
