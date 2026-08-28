---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/aws-managed-applications-view-details.html
---

# Viewing and changing details about an AWS managed application
<a name="aws-managed-applications-view-details"></a>

After you connect an AWS managed application to IAM Identity Center by using the console or APIs for the application, the application is registered with IAM Identity Center. After an application is registered with IAM Identity Center, you can view and change details about the application in the IAM Identity Center console.

Information about the application includes whether user and group assignments are required, and if applicable, assigned users and groups and trusted applications for identity propagation. For information about trusted identity propagation, see [Trusted identity propagation overview](trustedidentitypropagation-overview.md).

**To view and change information about an AWS managed application in the IAM Identity Center console**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Applications**.

1. Choose the **AWS managed** tab.

1. Choose the link for the managed application you'd like to open and view.

1. If you want to change information about an AWS managed application, choose **Action** and then choose **Edit Details**.

1. You can change the application's display name, description, as well as the user and group assignment method.

   1. To change the display name, enter the desired name in the **Display name** field and choose **Save changes**.

   1. To change the description, enter the desired description in the **Description** field and choose **Save changes**.

   1. To change the user and group assignment method, make the desired change and choose **Save changes**. For more information, see [Users, groups, and provisioning in IAM Identity Center](users-groups-provisioning.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
