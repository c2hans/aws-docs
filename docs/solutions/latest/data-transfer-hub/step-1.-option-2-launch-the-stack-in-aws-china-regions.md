---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/step-1.-option-2-launch-the-stack-in-aws-china-regions.html
---

# Step 1. (Option 2) Launch the stack in AWS China Regions
<a name="step-1.-option-2-launch-the-stack-in-aws-china-regions"></a>

**Important**
The following deployment instructions apply to AWS China Regions only. For deployment in AWS Regions refer to [Option 1](step-1.-option-1-launch-the-stack-in-aws-regions.md).

## Prerequisites
<a name="prerequisites"></a>

1.  [Create an OIDC User Pool](#prerequisite-1-create-an-oidc-user-pool).

1.  [Configure domain name service (DNS) resolution](#prerequisite-2-configure-domain-name-service-resolution).

1.  Make sure a domain registered by [ICP](https://www.amazonaws.cn/en/support/icp/) is available.

### Prerequisite 1: Create an OIDC user pool
<a name="prerequisite-1-create-an-oidc-user-pool"></a>

 In AWS Regions where Amazon Cognito is not yet available, you can use OIDC to provide authentication. The following procedure uses AWS Partner [Authing](https://www.authing.cn/) as an example, but you can also choose any available provider.

1.  Go to the [Authing console](https://console.authing.cn/login?app_id=5f6265c67ff6fdae64ec516e&protocol=oidc&finish_login_url=%2Finteraction%2Foidc%2F1bfa5665-ec45-4a32-8ba7-699f7a18d147%2Flogin&login_page_context=).

1.  Create a new user pool if you don’t have one.

1.  Select the user pool.

1.  On the left navigation bar, select **Self-built App** under **Applications**.

1.  Click the **Create** button.

1.  Enter the **Application Name**, and **Subdomain**.

1.  Save the App ID (that is, `client_id`) and Issuer to a text file from Endpoint Information, which will be used later.
![Endpoint Information table with App ID and Issuer fields highlighted with red boxes.](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/oidc-app-setting-1.png)

1.  Update the **Login Callback URL** and **Logout Callback URL** to your ICP recorded domain name.
![Authentication Configuration form with Subdomain, Login Callback URL, and Logout Callback URL fields.](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/oidc-app-setting-2.png)

1.  Set the Authorization Configuration.
![Authorization flow set to authorization_code, return type set to code, and RS256 selected.](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/oidc-app-setting-3.png)

1.  Update login control.

   1.  Select and enter the **Application** interface from the left sidebar, select **Login Control**, and then select **Registration and Login**.

   1.  Please select only **Password Login: Email** for the login method.

   1.  Please **uncheck** all options in the registration method.

   1.  Select **Save**.

1.  Create an admin user.

   1.  From **User & Roles**, select **Users**, then choose **Create user**.

   1.  Enter the email for the user.

   1.  Choose **OK**.

   1.  Check the email for a temporary password.

   1.  Reset the user password.
**Note**
Because the Guidance does not support application roles, all the users will receive admin rights.

### Prerequisite 2: Configure domain name service resolution
<a name="prerequisite-2-configure-domain-name-service-resolution"></a>

 Configure domain name service (DNS) resolution to point the ICP licensed domain to the CloudFront default domain name. Optionally, you can use your own DNS resolver.

 The following is an example for configuration an Amazon Route 53.

1.  Create a hosted zone in Amazon Route 53. For more information refer to the [Amazon Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html).

1.  Create a CNAME record for the console URL.

   1.  From the hosted zone, choose **Create Record**.

   1.  In the **Record name** input box, enter the host name.

   1.  From **Record type** select **CNAME**.

   1.  In the value field, enter the CloudFormation output PortalUrl.

   1.  Select **Create records**.

1.  Add alternative domain names to the CloudFront distribution.

   1.  Configure the corresponding domain name in CloudFront to open the CloudFront console by finding the distribution ID for PortalURL in the list and selecting **ID** (or check the check box, and then select **Distribution Settings**).

   1.  Edit the distribution and add the Route 53 record to the alternative domain Names (CNAMEs).

## Deploy the AWS CloudFormation template for Option 2 – AWS China Regions
<a name="deploy-the-template-for-option-2"></a>

 This automated AWS CloudFormation template deploys Data Transfer in the AWS Cloud. You must Create an ODIC User Pool and Configure DNS resolution before launching the stack.

**Note**
You are responsible for the cost of the AWS services used while running this Guidance. For more details, visit the [Cost](cost.md) section in this guide, and refer to the pricing webpage for each AWS service used in this Guidance.

1. Sign in to the AWS Management Console and select the button to launch the `DataTransferHub-openid.template` AWS CloudFormation template. Alternatively, you can [download the template](https://s3.amazonaws.com/solutions-reference/data-transfer-hub/latest/DataTransferHub-openid.template) as a starting point for your own implementation.

   [![Blue oval button with white text reading "Launch solution".](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/launch-solution.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/create/template?stackName=DataTransferHub&templateURL=https://s3.amazonaws.com/solutions-reference/data-transfer-hub/latest/DataTransferHub-openid.template)

1.  The template launches in your console’s default Region. To launch the Guidance in a different AWS Region, use the Region selector in the console navigation bar.

1.  On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1.  On the **Specify stack details** page, assign a name to your Guidance stack. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this Guidance template and modify them as necessary. This Guidance uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/step-1.-option-2-launch-the-stack-in-aws-china-regions.html)

1.  Choose **Next**.

1.  On the **Configure Stack Options** page, keep the default values and choose **Next**.

1.  On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1.  Choose **Create Stack** to deploy the stack.

 You can view the status of your stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 15 minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
