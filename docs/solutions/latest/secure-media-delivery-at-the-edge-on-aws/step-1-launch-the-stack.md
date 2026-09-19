---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-1-launch-the-stack.html
---

# Step 1: Launch the stack
<a name="step-1-launch-the-stack"></a>

 Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 5-10 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `SECURESTREAM.template` AWS CloudFormation template.

   [![Secure Media Delivery at the Edge on AWS launch solution button](https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://s3.amazonaws.com/solutions-reference/secure-media-delivery-at-the-edge-on-aws/latest/secure-media-delivery-at-the-edge-on-aws.template)

1.  The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1.  On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1.  On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

    **Session Revocation**

<table>
<thead>
  <tr><th> Parameter </th><th> Default </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <b>Retention </b></td><td> <code>30 </code></td><td> Expressed in minutes. Retention time for the sessions submitted for the revocation. After retention time elapses session is no longer considered for blocking and will be removed from WAF Rule Group next time it is updated. </td></tr>
  <tr><td> <b>Web ACL capacity units (WCU) </b></td><td> <code>100 </code></td><td> WCU limit allocated to the AWS WAF Rule Group created to store the rules to block revoked sessions. Note this value is immutable and can’t be changed after Rule Group is created. Single session ID included in the Rule Group utilizes 2 WCU from the configured limit. </td></tr>
</tbody>
</table>

    **Key Rotation Frequency**

<table>
<thead>
  <tr><th> Parameter </th><th> Default </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <b>Week of the month</b> </td><td> N/A </td><td> Specify the week number in each month that key rotation will be scheduled for. This parameter can be set to a value from a range 1 to 4. </td></tr>
  <tr><td><b> Day of the week</b> </td><td> N/A </td><td> After selecting a week in a month, provide a specific day in that week when key rotation should occur. Value from 1 to 7, where 1 means Monday and 7 means Sunday. </td></tr>
  <tr><td> <b>Hours </b></td><td> N/A </td><td> An hour when key rotation workflow will be triggered. </td></tr>
  <tr><td> <b>Minutes </b></td><td> N/A </td><td> A minute in the selected hour when key rotation workflow will be triggered. </td></tr>
</tbody>
</table>

   **DASH Stream **

    If you do not have a video asset available in DASH format, you can leave the inputs empty in which case example values will be set. You can augment these inputs after the stack is deployed.

<table>
<thead>
  <tr><th> Parameter </th><th> Default </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <b>Hostname for asset delivery</b> </td><td> <code>https://d1234.cloudfront.net </code></td><td> Domain name served by CloudFront distribution hosting video following protocol prefix (<b>http://</b> or <b>https://</b>). If no input is provided an example, default value will be set in the target DynamoDB table. </td></tr>
  <tr><td> <b>URL path for asset delivery </b></td><td><code> /video/2/index.mpd </code></td><td> Full URL path of the video asset. This parameter must start with ‘/’ and point to an object used by the player to initiate a playback, like master manifest (mpd file). If no input is provided an example, default value will be set in the target DynamoDB table. </td></tr>
  <tr><td> <b>TTL for token</b> </td><td><code> +30m </code></td><td> <b>Mandatory.</b> Time period determining for how long newly issued token will be valid. If not specified, example values will be populated. </td></tr>
</tbody>
</table>

    **HLS Stream**

    If you do not have a video asset available in HLS format, you can leave the inputs empty in which case example values will be set. You can augment these inputs after the stack is deployed.

<table>
<thead>
  <tr><th> Parameter </th><th> Default </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <b>Hostname for asset delivery </b></td><td> https://d1234.cloudfront.net </td><td> Domain name served by CloudFront distribution hosting video following protocol prefix (<b>http://</b> or <b>https://</b>). If no input is provided an example, default value will be set in the target DynamoDB table. </td></tr>
  <tr><td> <b>URL path for asset delivery </b></td><td> /video/1/index.m3u8 </td><td> Full URL path of the video asset. This parameter must start with ‘/’ and point to an object used by the player to initiate a playback, like master manifest (m3u8 file). If no input is provided an example, default value will be set in the target DynamoDB table. </td></tr>
  <tr><td> <b>TTL for token </b></td><td> +30m </td><td> <b>Mandatory.</b> Time period determining for how long newly issued token will be valid. If not specified, example values will be populated. </td></tr>
</tbody>
</table>

1.  Choose **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1.  Choose **Submit** to deploy the stack.

    You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 5 to 10 minutes.
