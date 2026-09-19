---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/launch-the-stack.html
---

# Launch the stack
<a name="launch-the-stack"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately five minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `live-streaming-on-aws-with-amazon-s3.template` AWS CloudFormation template.

    [![Live Streaming on AWS with S3 launch button](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=LiveStreamingonAWSwithAmazonS3&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Flive-streaming-on-aws-with-amazon-s3%2Flatest%2Flive-streaming-on-aws-with-amazon-s3.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses MediaLive, which is currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where this service is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Source Input Type</b> </td><td> <code>URL_PULL</code> </td><td>Specify the input type for MediaLive: <code>RTP_PUSH</code>, <code>RTMP_PUSH</code>, <code>URL_PULL (HLS)</code>, or <code>INPUT_DEVICE</code> (AWS Elemental Link). Detailed instructions for each input type can be found in the appendix.</td></tr>
  <tr><td> <b>Source URL</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>If you selected <code>URL_PULL</code> for <b>Source Input Type</b>, enter the URL for your source stream. By default, this parameter contains the primary demo source URL.</td></tr>
  <tr><td> <b>Source Username</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>If you selected <code>URL_PULL</code> for <b>Source Input Type</b>, enter the username for your source stream if using authentication. This value will be stored securely in AWS Systems Manager Parameter Store.</td></tr>
  <tr><td> <b>Source Password</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>If you selected <code>URL_PULL</code> for <b>Source Input Type</b>, enter the password for you source stream if using authentication. This value will be stored securely in AWS Systems Manager Parameter Store.</td></tr>
  <tr><td> <b>Input Security Group CIDR Block</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>For <code>RTP_PUSH</code> and <code>RTMP_PUSH</code> input types, specify the CIDR block to restrict access to the MediaLive input endpoint. This should be the IP or IP range of you your source stream location/network.</td></tr>
  <tr><td> <b>Encoding Profile</b> </td><td> <code>HD-720p</code> </td><td>Specify the encoding profile to use with MediaLive.</td></tr>
  <tr><td> <b>Start MediaLive Channel</b> </td><td> <code>No</code> </td><td>Choose whether to start the MediaLive channel when the solution is created. We recommend starting the channel if using the demo preview player.</td></tr>
</tbody>
</table>

1. Select **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately five minutes.
**Note**
To test the live stream playback, navigate to the AWS CloudFormation stack **Outputs** tab, copy the Amazon CloudFront URL, and open the URL in any player compatible with HTTP Live Streaming (HLS). For more details, refer to [Amazon CloudWatch metrics](amazon-cloudwatch-metrics.md).
