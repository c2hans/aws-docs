---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/step-1-launch-the-stack.html
---

# Step 1: Launch the stack
<a name="step-1-launch-the-stack"></a>

 Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 25 minutes

1.  Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the media2cloud AWS CloudFormation template. [![Media2Cloud on AWS launch button](https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fmedia2cloud%2Flatest%2Fmedia2cloud.template&redirectId=ImplementationGuide)

1.  The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1.  On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1.  On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th> Parameter </th><th> Default </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <b>Email</b></td><td> {{<i>&lt;Requires Input&gt;</i>}} </td><td> Email address of the user that will be created in the Amazon Cognito identity pool and subscribed to the Amazon SNS topic. Subscribed users will receive ingestion, analysis, labeling, and error notifications. <br /> After launch, two emails will be sent to this address: one with instructions for logging in to the web interface and one confirming the Amazon SNS subscription. </td></tr>
  <tr><td> <b>Price Class</b> </td><td><code>Use Only U.S., Canada and Europe </code></td><td>A dropdown box with price classes for the edge location from which Amazon CloudFront serves your requests. Choose <code>Use Only U.S., Canada and Europe</code>; <code>Use U.S., Canada, Europe, Asia and Africa</code>; or <code>Use All Edge Locations</code>. For more information, refer to <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html">Choosing the price class</a>. </td></tr>
  <tr><td> <b>Amazon OpenSearch Service Cluster Size </b></td><td><code> Development and Testing </code></td><td>A drop-down box with four Amazon OpenSearch Service cluster sizes: <code>Development and Testing</code>, <code>Suitable for Production Workloads</code>, <code>Recommended for Production Workloads</code>, and <code>Recommended for Large Production Workloads</code>. </td></tr>
  <tr><td><b>Analysis Feature(s) </b></td><td><code>Default </code></td><td>A drop-down box with nine presets: <code>Default</code>, <code>All</code>, <code>Video analysis</code>, <code>Audio analysis</code>, <code>Image analysis</code>, <code>Document analysis</code>, <code>Celebrity recognition only</code>, <code>Video segment detection only</code>, and <code>Speech to text only</code>. For more information about the presets, refer to <a href="analysis-workflow.md">Analysis workflow</a>. </td></tr>
  <tr><td><b>(Optional) User Defined Amazon S3 Bucket for ingest</b> </td><td> {{<i>&lt;Requires Input&gt;</i>}} </td><td> If you have an existing bucket that you would like to store uploaded contents, specify the bucket name. Otherwise, leave it blank to auto create a new bucket. </td></tr>
  <tr><td> <b>(Optional) Allow autostart on ingest S3 bucket</b></td><td><code>NO </code></td><td> A drop-down box to specify if you would like to automatically start workflow when directly upload assets to Amazon S3 ingestion bucket. </td></tr>
</tbody>
</table>

1.  Select **Next**.

1.  On the **Configure stack options** page, choose **Next.**

1.  On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1.  Choose **Submit** to deploy the stack.

    You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 25 minutes.
