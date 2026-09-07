---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/deploy-self-hosted.html
---

# Launch the stack (Headless)
<a name="deploy-self-hosted"></a>

## Launch the stack
<a name="self-hosted-launch-the-stack"></a>

1. Sign in to the AWS Management Console and select the button to launch the CloudFormation template.

    [![Launch solution with the headless template](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-headless.template&redirectId=ImplementationGuide)

   Alternatively, you can [download the template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-headless.template) as a starting point for your own implementation.

1. The template is launched in the US East (N. Virginia) Region by default. To launch in a different AWS Region, use the region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito, which is currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where Amazon Cognito is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This template uses the same parameters as the [default template](launch-the-stack.md) (Administrator Name, Administrator Email, VPC/subnet configuration, Egress CIDR, Auto-update Container Image, and Deploy Optional MCP Server). No additional parameters are required.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 15 minutes.

## Post-deployment configuration
<a name="self-hosted-post-deployment"></a>

After the stack creation completes, you can interact with the solution using the [DLT CLI](dlt-cli.md) to access the REST API directly from your terminal or host the web console on your own web server.

To host the web console:

1. Navigate to the **Outputs** tab of the CloudFormation stack.

1. Choose the **ConsoleAssetsBucket** output link to open the S3 bucket in the console.

1. Download the `dlt-web-console.zip` file from the console bucket.

1. Extract the zip contents and host the website on your web server.

1. Configure Amazon Cognito to allow your web server’s URL:

   1. Open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/) and select the user pool created by the stack.

   1. Choose **App clients** and select the app client. The app client ID can be found in the CloudFormation stack **Outputs** tab as **CognitoAppClientID**.

   1. In the **Login pages** section, choose **Edit**.

   1. Under **Allowed callback URLs**, add your web server’s URL and the URL with a trailing slash (for example, `https://dlt.example.com` and `https://dlt.example.com/`).

   1. Under **Allowed sign-out URLs**, add the same URLs.

   1. Choose **Save changes**.

      For more information, refer to [Application-specific settings with app clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html) in the *Amazon Cognito Developer Guide*.

**Important**
If you host the web console, you are responsible for configuring HTTPS, access controls, and security hardening on your web server. We strongly recommend HTTPS for production use.

**Note**
The web console assets include a configuration file with the API endpoint URL and Cognito settings. These values are pre-configured during stack creation. If you move the assets to a different server, ensure the configuration file remains intact.
