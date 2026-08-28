---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/upgrade-data-transfer-hub.html
---

# Upgrade Data Transfer Hub
<a name="upgrade-data-transfer-hub"></a>

 Time to upgrade: Approximately 20 minutes

## Upgrade overview
<a name="upgrade-overview"></a>

 Use the following steps to upgrade the Guidance on AWS console.
+  Step 1. Update the CloudFormation Stack
+  Step 2. (Optional) Update the OIDC configuration
+  Step 3. Refresh the web console

## Step 1. Update the CloudFormation stack
<a name="step-1.-update-the-cloudformation-stack"></a>

1.  Go to the[ AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1.  Select the Data Transfer Hub main stack, and choose** Update**.

1.  Choose **Replace current template**, and enter the specific Amazon S3 URL according to your initial deployment type. Refer to [Deployment Overview](deploy-the-solution.md#deployment-overview) for more details.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/upgrade-data-transfer-hub.html)

1.  Under **Parameters**, review the parameters for the template and modify them as necessary.

1.  Choose **Next**.

1.  On Configure stack options page, choose **Next**.

1.  On Review page, review and confirm the settings. Check the box **I acknowledge that AWS CloudFormation might create IAM resources**.

1.  Choose **Update stack** to deploy the stack.

 You can view the status of the stack in the AWS CloudFormation console in the Status column. You should receive a UPDATE\_COMPLETE status in approximately 15 minutes.

## Step 2. (Optional) Update the OIDC configuration
<a name="step-2.-optional-update-the-oidc-configuration"></a>

 If you have deployed the Guidance in China Region with OIDC, refer to the [deployment](step-1.-option-2-launch-the-stack-in-aws-china-regions.md) section to update the authorization and authentication configuration in OIDC.

## Step 3. Refresh the web console
<a name="step-4.-refresh-the-web-console"></a>

 Now you have completed all the upgrade steps. Please click the refresh button in your browser.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
