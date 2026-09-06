---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/delete-saml-app.html
---

# Delete the custom application in IAM Identity Center
<a name="delete-saml-app"></a>

In this step, delete the SAML2.0 application you created using the instructions in the [Create SAML application](create-saml-app.md) section.

To delete the application:

1. Log in to the account where the IAM Identity Center is enabled (usually the Organization Management account), and the IDC stack is deployed.

1. Navigate to the [AWS IAM Identity Center](https://console.aws.amazon.com/singlesignon/) console, and choose the Innovation Sandbox home region.

1. From the left pane, choose **Groups**.

1. To remove users from the three Innovation Sandbox [groups](assign-groups-application.md):

   1. Select a group.

   1. Choose the **Users** tab.

   1. Select all the users.

   1. Choose **Remove users from group**.

   1. If there are more than one page of users, repeat this for all users.

1. Under **Application assignments**, choose **Applications**.

1. Choose the **Customer managed** tab, and select the name of your application to view details.

1. Under **Assigned users and groups**, select all the groups and users associated with the application, and choose **Remove access**.

1. Navigate back to the list of **Customer managed** applications.

1. Select the application name, and under **Actions**, choose **Remove**.

This will remove users from all groups, and delete the SAML2.0 application from your IAM Identity Center.
