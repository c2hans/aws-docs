---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/step-2-launch-the-stack.html
---

# Step 2: Launch the stack
<a name="step-2-launch-the-stack"></a>

 Follow the step-by-step instructions in this section to configure and deploy the guidance into your account.

 **Time to deploy:** Approximately 7–10 minutes.

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and upload the file created in previous step `./deployment/global-s3-assets/centralized-network-inspection-on-aws.template`

1.  The template launches in the US East (N. Virginia) Region by default. To launch the guidance in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
 This guidance uses Network Firewall, which is not currently available in all AWS Regions. You must launch this guidance in an AWS Region where AWS Network Firewall is available. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
 You can deploy this guidance multiple times in the same Region to allow users to set up a new network firewall and related resources for an existing transit gateway.

1.  On the **Specify stack details** page, assign a name to your guidance stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this guidance template and modify them as necessary. This guidance uses the following default values.

<table>
<thead>
  <tr><th> Parameter </th><th> Default </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b> VPC configuration </b></td></tr>
  <tr><td><b>Provide the CIDR bock for the inspection VPC </b></td><td><code>192.168.1.0/26</code></td><td>CIDR block for VPC. Must be <code>/26</code> or larger CIDR block.</td></tr>
  <tr><td colspan="3"><b> Transit Gateway configuration </b></td></tr>
  <tr><td><b>Provide the existing AWS Transit Gateway ID you wish to attach to the Inspection VPC</b> </td><td><i>Optional input</i></td><td> The existing transit gateway ID in the current Region. Example: <code>tgw-a1b2c3d4e5</code>  If the transit gateway ID is removed or updated and the stack is updated, the transit gateway attachment won't be deleted in the account. You must <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#delete-vpc-attachment">delete the transit gateway attachment manually</a>. </td></tr>
  <tr><td><b>Provide the AWS Transit Gateway Route Table to be associated with the Inspection VPC TGW Attachment</b></td><td><i>Optional input</i></td><td> The existing transit gateway route table ID. Example: <code>Firewall Route Table</code>. Example: <code>tgw-rtb-0a1b2c3d</code>  If the transit gateway route table ID is removed and the stack is updated, the transit gateway attachment is not deleted in the account. You must delete the transit gateway attachment manually.  </td></tr>
  <tr><td><b>Provide the AWS Transit Gateway Route Table to receive 0.0.0.0/0 route to the Inspection VPC TGW Attachment </b></td><td><i>Optional input</i></td><td> The existing transit gateway route table ID for propagation. Example: <code>Spoke VPC Route Table</code>. Example: <code>tgw-rtb-183ae12f</code>  If the transit gateway ID, or transit gateway route table ID and transit gateway route table ID for default route, are removed and the stack is updated, the default route in the transit gateway route table, route entry for <code>0.0.0.0/0</code>, is not deleted. You must <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html">delete the route manually</a>. </td></tr>
  <tr><td colspan="3"><b> Firewall Logging configuration </b></td></tr>
  <tr><td><b>Select the type of log destination for the Network Firewall </b></td><td><code>CloudWatchLogs</code></td><td> The type of storage destination for logs. You can send logs to an S3 bucket or a CloudWatch <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html">log group</a>.  The default value is <code>CloudWatchLogs</code>. This guidance will create a log group for the firewall logs. You can also store logs in an S3 bucket. If no logging needs to be configured, select <code>ConfigureManually</code>.  <br /> If this parameter is being updated after your first deployment, you must <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html">start CodePipeline manually</a> to update the log destination. </td></tr>
  <tr><td><b>Select the type of log to send to the defined log destination. </b></td><td><code>FLOW</code></td><td> The type of log to send. Alert logs report traffic that matches a stateful rule with an action setting that sends an alert log message. Flow logs are standard network traffic flow logs.  You can set this to ALERT logs or enable both types of logs. For details, refer to <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html">Logging network traffic from AWS Network Firewall</a> in the <i>AWS Network Firewall Developer Guide.</i>  </td></tr>
  <tr><td><b>Select the log retention period for Network Firewall Logs. </b></td><td><code>90</code></td><td> Log retention period in days. This setting is also applicable to Inspection VPC Flow Logs retention period. </td></tr>
</tbody>
</table>

1.  Select **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1.  Choose **Submit** to deploy the stack.

    You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 7–10 minutes.
