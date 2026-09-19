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

<table>
<thead>
  <tr><th> Type </th><th> Link </th></tr>
</thead>
<tbody>
  <tr><td> Launch in AWS Regions </td><td> <code>https://s3.amazonaws.com/solutions-reference/data-transfer-hub/latest/DataTransferHub-cognito.template</code> </td></tr>
  <tr><td> Launch in AWS China Regions </td><td> <code>https://s3.amazonaws.com/solutions-reference/data-transfer-hub/latest/DataTransferHub-openid.template</code> </td></tr>
</tbody>
</table>

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
