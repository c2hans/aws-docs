---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-amazon-cognito-user-pool.html
---

# Launch with Amazon Cognito User Pool
<a name="launch-with-amazon-cognito-user-pool"></a>

 **Time to deploy**: Approximately 15 minutes

## Deployment Overview
<a name="deployment-overview"></a>

Use the following steps to deploy this solution on AWS.
+  [Step 1. Launch the stack](#step-1.-launch-the-stack)
+  [Step 2. Launch the web console](#step-2.-launch-the-web-console)

## Step 1. Launch the stack
<a name="step-1.-launch-the-stack"></a>

This AWS CloudFormation template automatically deploys the Centralized Logging with OpenSearch solution on AWS.

1. Sign in to the AWS Management Console and select the button to launch the AWS CloudFormation template.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-amazon-cognito-user-pool.html)

1. The template is launched in the default Region after you log in to the console. To launch the Centralized Logging with OpenSearch solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is shown in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for the template and modify them as necessary.
   + If you are launching the solution in a new VPC, this solution uses the following parameters:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-amazon-cognito-user-pool.html)
   + If you are launching the solution in an existing VPC, this solution uses the following parameters:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-amazon-cognito-user-pool.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Add new tag** and type in the following key and value:
   + Key: `CLOSolutionCostAnalysis`
   + Value: `CLOSolutionCostAnalysis`

   You can activate the `CLOSolutionCostAnalysis` tag after all resources have been successfully deployed. Choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 15 minutes.

## Step 2. Launch the web console
<a name="step-2.-launch-the-web-console"></a>

After the stack is successfully created, this solution generates a CloudFront domain name that gives you access to the Centralized Logging with OpenSearch web console. Meanwhile, a generated temporary password (excluding the last digit) will be sent to your email address.

1. Sign in to the AWS CloudFormation console.

1. On the **Stacks** page, select the solution’s stack.

1. Choose the **Outputs** tab and record the domain name.

1. Open the **WebConsoleUrl** using a web browser, and navigate to a sign-in page.

1. Enter the **Email** and the temporary password.

1. a. Set a new account password.

1. b. (Optional) Verify your email address for account recovery.

1. After the verification is complete, the system opens the Centralized Logging with OpenSearch web console.

Once you have logged into the Centralized Logging with OpenSearch console, you can [import an Amazon OpenSearch Service domain](getting-started.md#step-1-import-an-amazon-opensearch-domain) and build log analytics pipelines.
