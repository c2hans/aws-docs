---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/configure-cognito.html
---

# Configure Cognito
<a name="configure-cognito"></a>

Workload Discovery on AWS uses Amazon Cognito to manage authentication. You can create users directly in the Cognito user pool or you can use a third-party IdP using SAML or OIDC.

## Manage users via Cognito user pool
<a name="manage-users-via-cognito-user-pool"></a>

<a name="manage-users-via-cognito-user-pool.manage-users-via-cognito-user-pool.title"></a>On deployment, the solution creates a user for you and sends an email to the address provided in the `AdminUserEmailAddress` CloudFormation parameter with temporary credentials. To add more users follow these steps.

### Create additional users:
<a name="create-additional-users"></a>

1. Sign in to the [AWS Cognito console](https://console.aws.amazon.com/cognito/).

1. Choose **Manage User Pools**.

1. Choose **WDCognitoUserPool-** {{<ID-string>}}.

1. In the navigation pane, under **General Settings**, choose **Users and groups**.

1. On the **Users** tab, choose **Create user**.

1. On the **Create user** box, enter values for all required fields.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/configure-cognito.html)

1. Choose **Create user**.

Repeat this process to create as many users as you need.

**Note**
Every user will have the same level of access to resources discovered. We recommend provisioning a separate deployment of Workload Discovery on AWS for accounts that contain sensitive workloads or data. This allows you to restrict access to only the users that need it.

## Manage users via third-party IdP
<a name="manage-users-via-third-party-idp"></a>

<a name="manage-users-via-third-party-idp.manage-users-via-third-party-idp.title"></a>You can set up user sign-in with an OIDC IdP or a SAML IdP.

### Set up user sign-in with an OIDC IdP
<a name="set-up-user-sign-in-with-an-oidc-idp.set-up-user-sign-in-with-an-oidc-idp.title"></a>

1. Set up an OIDC client application in your IdP according to your provider’s documentation. You will require the following values:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/configure-cognito.html)

1. The OIDC IdP will provide you with a OIDC discovery URL, client ID and a client secret. Note these values.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Select the main Workload Discovery on AWS stack and choose **Update**.

1. On the **Update stack** page, select **Use existing template**.

1. Update the following CloudFormation parameters:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/configure-cognito.html)

1. Choose Next.

1. On the **Review** page, review and confirm the settings. Select the boxes acknowledging that the template creates IAM resources and requires certain capabilities.

1. Choose **Update stack** to deploy the stack.

### Set up user sign-in with a SAML IdP
<a name="set-up-user-sign-in-with-an-saml-idp.set-up-user-sign-in-with-an-saml-idp.title"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Choose **View nested** to display the nested stacks that make up the deployment. Depending on your preferences, nested stacks might already be displayed.

1. Select the **Workload Discovery on AWS Amazon Cognito** stack. It will be named {{<wd-stack-name>}} `-CognitoStack-` {{<ID-string>}}.

1. Select the **Outputs** tab and note the ID in the **Value** column associated with the **UserPoolId** key.

1. Configure your SAML IdP to accept requests and send responses to your user pool. The documentation for your SAML IdP will contain information about how to add your user pool as a relying party or application for your SAML 2.0 IdP. You will require the following values:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/configure-cognito.html)

1. Download SAML metadata from your IdP, or retrieve the URL to your metadata endpoint.

1. Return to the CloudFormation console.

1. Select the main Workload Discovery on AWS stack and choose **Update**.

1. On the **Update stack** page, select **Use existing template**.

1. Update the following CloudFormation parameters:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/configure-cognito.html)

1. Choose Next.

1. On the **Review** page, review and confirm the settings. Select the boxes acknowledging that the template creates IAM resources and requires certain capabilities.

1. Choose **Update stack** to deploy the stack.
