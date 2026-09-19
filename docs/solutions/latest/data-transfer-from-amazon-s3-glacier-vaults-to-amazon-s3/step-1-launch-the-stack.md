---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/step-1-launch-the-stack.html
---

# Step 1: Launch the stack
<a name="step-1-launch-the-stack"></a>

 Follow the step-by-step instructions in this section to configure and deploy the Guidance into your account.

 **Time to deploy:** Approximately 5–10 minutes

**Note**
The archive transfer can take up to one day to complete. If you need to move your data faster, contact [AWS Support](https://aws.amazon.com/premiumsupport) (AWS Developer Support plan or above).

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `data-retrieval-from-amazon-s3-glacier-vaults-to-amazon-s3.template` AWS CloudFormation template.

   [![Launch Guidance button.](https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create?stackName=DataTransferS3GlacierVaultsToS3&templateURL=https://solutions-reference.s3.amazonaws.com/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3.template&redirectId=ImplementationGuide)

1.  The template launches in the US East (Ohio) Region by default. To launch the Guidance in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
 This Guidance uses AWS services that are not currently available in all AWS Regions. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1.  On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1.  On the **Specify stack details** page, assign a name to your Guidance stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this Guidance template and modify them as necessary. This Guidance uses the following default values.

<table>
<thead>
  <tr><th> Parameter </th><th> Default </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td><b>DestinationBucket</b></td><td><code>empty</code></td><td>The name of the destination Amazon S3 bucket. Referring a bucket in a different region than S3 Glacier vault will incur additional costs. Refer to the <a href="cost.md">cost</a> section for more details.  The destination Amazon S3 bucket must be created in the same account as the Glacier vault, which is also the account where the Guidance is deployed. Currently, the Guidance does not support cross-account transfers."  </td></tr>
  <tr><td><b>DynamoDB Backup</b></td><td><code>false</code></td><td>Enter <code>true</code> to enable DynamoDB table backups for tables created by the Guidance. </td></tr>
  <tr><td><b>Lambda Tracing</b></td><td><code>false</code></td><td> Enter <code>true</code> to enable <a href="https://aws.amazon.com/xray/">AWS X-Ray</a> tracing for Lambda functions created by the Guidance. </td></tr>
  <tr><td><b>Step Function Logging</b></td><td><code>false</code></td><td> Enter <code>true</code> to enable logging for Step Functions created by the Guidance. </td></tr>
  <tr><td><b>Step Function Tracing</b></td><td><code>false</code></td><td> Enter <code>true</code> to enable X-Ray tracing for Step Functions created by the Guidance. </td></tr>
</tbody>
</table>

**Note**
It is advisable to review and modify any [Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_s3.html) (SCP) on the destination bucket that may block or prevent PUT operations. If you are using CloudTrail on your destination Amazon S3 bucket, please review and modify the CloudTrail export configurations to prevent excessive API charges.

1.  Select **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1.  Choose **Create stack** to deploy the stack.

    You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 5–10 minutes.
