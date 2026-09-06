---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/create-first-user.html
---

# Step 4: Create the first user
<a name="create-first-user"></a>

## Create the initial user and log in to the solution
<a name="create-the-initial-user-and-log-in-to-the-solution"></a>

Use the following procedure to create the initial user.

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. From the navigation pane, choose **User pools**.

1. On the **User pools** page, choose the user pool that starts with the `migration-factory` prefix.

1. Select the **Users** tab and choose **Create user**.

1. In the **Create user** screen, **User information** section, do the following:

   1. Verify that the **Send an invitation** option is selected.

   1. Enter an email address.
**Important**
This email address must be different from the one you used in the `ServiceAccountEmail` parameter, which the solution uses when deploying the primary CloudFormation template.

   1. Select **Set a password**.

   1. In the **Password** field, enter a password.
**Note**
The password must be at least eight characters in length, including upper- and lower-case letters, numbers, and special characters.

1. Choose **Create user**.

**Note**
You will receive an email with the temporary password. Until you change the temporary password, the **Account status** for this user will display as **Force change password**. You can update the password later in the deployment.

## Add a user to the admin group
<a name="add-a-user-to-the-admin-group"></a>

In the Amazon Cognito console, use the following procedure to add a user to the default Admin group.

1. Navigate to the Amazon Cognito console.

1. From the navigation menu, choose **User pools**.

1. On the **User pools** page, choose the user pool that starts with the `migration-factory` prefix.

1. Select the **Groups** tab and open the group named **admin** by selecting the name.

1. Choose **Add user to group**, then select the user name to add.

1. Choose **Add**.

   The chosen user will now be added to the members list of the group. This default admin group authorizes the user to manage all aspects of the solution.
**Note**
After you create the initial users, you can manage group membership in the solution UI by selecting **Administration**, then **Permissions**, then **Groups**.

## Identify the CloudFront URL (Public and Public with AWS WAF deployments only)
<a name="identify-the-cloudfront-url"></a>

Use the following procedure to identify the solution’s Amazon CloudFront URL. This allows you to log in and change the password.

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) and select the solution’s stack.

1. On the **Stacks** page, select the **Outputs** tab and select the **Value** for the **MigrationFactoryURL**.
**Note**
If you launched the solution in an AWS Region other than US East (N. Virginia), CloudFront may take longer to deploy and the **MigrationFactoryURL** may not be accessible immediately (you will receive an access denied error). It can take up to four hours before the URL becomes available. The URL includes `cloudfront.net` as part of the string.

1. Sign in with your username and temporary password, then create a new password and choose **Change Password**.
**Note**
The password must be at least eight characters in length, including upper- and lower-case letters, numbers, and special characters.
