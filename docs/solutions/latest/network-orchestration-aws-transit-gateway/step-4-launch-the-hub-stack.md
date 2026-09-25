---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-4-launch-the-hub-stack.html
---

# Step 4: Launch the hub stack
<a name="step-4-launch-the-hub-stack"></a>

Follow the step-by-step instructions in this section to configure and deploy the hub stack into your hub account.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) with your AWS network hub account.

1. Choose **Create stack**, then choose **With new resources (standard)**.

1. On the **Create stack** page, select **Upload a template file**, choose **Choose file**, and upload `network-orchestration-hub.template` from `./deployment/global-s3-assets/`.

1. Choose **Next**.

1. Select the AWS Region where you want to deploy, using the Region selector in the console navigation bar. See [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions) for more information on selecting a Region.

1. On the **Specify stack details** page, assign a name to your stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

   For **Parameters**, review the parameters for the template and modify them as necessary. This stack uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Account Structure Settings</b> </td><td></td><td></td></tr>
  <tr><td> <b>Principal Type</b> </td><td> <code>AWS Organization ARN</code> </td><td>Choose whether to use the default Organization ARN or a list of accounts. For guidance, refer to <a href="aws-accounts-for-multi-account-environments.md">AWS accounts</a>.</td></tr>
  <tr><td> <b>Account List or AWS Organizations ARN</b> </td><td> {{&lt;Requires input&gt;}} </td><td>To use Organizations, enter the Organization ARN to share the transit gateway with the principals. For example:<pre>arn:<AWS_PARTITION>:organizations::<ORG_MANAGEMENT_ACCOUNT_ID>:organization/<ORG-ID></pre><br />For additional guidance to identify the ARN value, refer to <a href="deploy-the-guidance.md#identify-the-organizations-arn">Identify the Organizations ARN</a>.<br />To use an account list, enter a comma-separated list of AWS account numbers. For example, <code>123456789012</code>.</td></tr>
  <tr><td> <b>Allow External Principals</b> </td><td> <code>Yes</code> </td><td>Choose whether to enable or disable sharing the transit gateway with principals outside the organization. NOTE: You must set this parameter to <code>Yes</code> if you’re using the <code>List of Accounts</code> value for the <b>Principal Type</b> parameter.</td></tr>
  <tr><td> <b>(Optional) IAM Role ARN of Management Account</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>To tag attachments with the account name and OU path, provide the ARN for the role in the management account which can be assumed by the hub account. Leave this value blank if you’re deploying in your management account.</td></tr>
  <tr><td> <b>Web UI Settings</b> </td><td></td><td></td></tr>
  <tr><td> <b>Web User Interface</b> </td><td> <code>Yes</code> </td><td>Option to deploy web UI to manage and audit the changes in the network. Select <code>No</code> to skip creation of the Console bucket, CloudFront, Amazon Cognito user pool, AWS WAF, and other support resources. NOTE: If you select <code>No</code> for this parameter, skip the remaining parameters in the <b>Web UI Settings</b> section.</td></tr>
  <tr><td> <b>Allow Listed Ranges</b> </td><td> <code>0.0.0.0/1,128.0.0.0/1</code> </td><td>Comma-separated list of CIDR ranges allowed to access GraphQL API. Default allows the entire internet.</td></tr>
  <tr><td> <b>Cognito Domain Prefix</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The prefix to the Cognito hosted domain name that will be associated with the user pool. Must be unique per AWS Region and must not contain reserved word 'cognito'.</td></tr>
  <tr><td> <b>Console Login Information Email</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The email address of the administrator user for the web UI. After launch, the stack sends an email to this address with a temporary password for the web UI.</td></tr>
  <tr><td> <b>Admin Username</b> </td><td> <code>adminuser</code> </td><td>The username for network administrators with full read and write permissions to the web UI.</td></tr>
  <tr><td> <b>Read-Only Username</b> </td><td> <code>readonlyuser</code> </td><td>The username for users with read-only permission to the web UI.</td></tr>
  <tr><td> <b>Set MFA for Cognito to '`ON' or '`OPTIONAL'</b> </td><td> <code>OPTIONAL</code> </td><td> <code>ON</code> - Amazon Cognito users will need to set up multi-factor authentication (MFA) on first login.<br /> <code>OPTIONAL</code> - Amazon Cognito users may opt to set up MFA.</td></tr>
  <tr><td> <b>SAML Provider Name</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>If you want to connect an external identity provider, specify a name that appears on the UI.</td></tr>
  <tr><td> <b>SAML Provider Metadata URL</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>If you want to connect an external identity provider, enter the URL to the metadata file of your SAML-based identity provider. The URL must begin with <code>https://</code>.</td></tr>
  <tr><td> <b>Transit Gateway Settings</b> </td><td></td><td></td></tr>
  <tr><td> <b>(Optional) Do you wish to use an existing transit gateway? If yes, you must provide the transit gateway id below.</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>The existing transit gateway ID in the current Region. For example, <code>tgw-a1b2c3d4e5</code>.<br />If you don’t provide a value, the Guidance creates a new transit gateway.<br />If you do provide a value, the Guidance uses your existing transit gateway. You must ensure that:<ul><li> The existing transit gateway has enabled the <code>AutoAcceptSharedAttachments</code> flag. The Guidance does not create additional transit gateway route tables for you. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#create-tgw">Create a transit gateway</a>. </li><li> The existing transit gateway isn’t already registered with an existing global network ID provided in the parameter <b>(Optional) Do you wish to use an existing global network? If yes, you must provide the global network id below.</b>  </li></ul><br />If you’re updating an existing deployment, provide a value.</td></tr>
  <tr><td> <b>(Optional) Do you wish to register the transit gateway with a global network?</b> </td><td> <code>Yes</code> </td><td>Choose whether to register the transit gateway with the global network. NOTE: You must set this parameter to <code>No</code> if either of the following is true:<br /> <b> The transit gateway managed by this deployment is already registered with an existing global network. </b> The global network is not available in your selected AWS Region. Refer to <a href="https://docs.aws.amazon.com/network-manager/latest/tgwnm/what-are-global-networks.html#nm-available-regions">Region availability</a> in the <i>AWS Global Networks for Transit Gateways User Guide</i>.</td></tr>
  <tr><td> <b>(Optional) Do you wish to use an existing global network? If yes, you must provide the global network id below.</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>You can skip this section if you chose <code>No</code> for the previous parameter.<br />The existing global network ID. To register the transit gateway ID (see previous parameter), provide an existing global network ID. For example, <code>global-network-01231231231231231</code>.<br />If you don’t provide a value, the Guidance creates a new global network.<br />If you provide a value, make sure the existing transit gateway isn’t already registered with the global network ID. You specify this transit gateway in the <b>(Optional) Do you wish to use an existing transit gateway?</b> parameter. NOTE: If you deploy in more than one Region, we recommend registering all transit gateways in all Regions to the same global network. Use the global network ID created by the first deployment.</td></tr>
  <tr><td> <b>VPC Route Table Settings</b> </td><td></td><td></td></tr>
  <tr><td> <b>Choose the type of destination for target Transit Gateway</b> </td><td> <code>All-traffic (0/0)</code> </td><td>Specify the default route setting for the route table associated with the tagged subnets. Choose from <code>All-traffic (0/0)</code>, <code>RFC-1918 (10/8, 172.16/12, 192.168/16)</code>, <code>Custom-Destinations</code>, or <code>Configure-Manually</code>. NOTE: If the route already exists, the Guidance does not overwrite it.</td></tr>
  <tr><td> <b>If selected '`Custom-Destinations', provide a comma separated list of CIDR Blocks.</b> </td><td> <i>&lt;Optional Input&gt;</i> </td><td>Option to provide CIDR block(s). For example, <code>192.168.1.0/24, 192.168.2.0/24</code>. NOTE: Optional if providing prefix list ID(s).</td></tr>
  <tr><td> <b>If selected '`Custom-Destinations', provide a comma separated list of Customer-managed Prefix List IDs.</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>Option to provide customer-managed prefix list ID(s). For example, <code>pl-abcd1234, pl-efgh5678</code>. NOTE: Optional if providing CIDR block(s).</td></tr>
  <tr><td> <b>Tag Settings</b> </td><td></td><td></td></tr>
  <tr><td> <b>Tag key for subnets - Adds subnet to VPC attachment and add routes to route table associated with the tagged subnet.</b> </td><td> <code>Attach-to-tgw</code> </td><td>Specify a custom tag key name to initiate the transit gateway attachment workflow. NOTE: After initial deployment, don’t change this default parameter. If you change this parameter after deployment, you must manually update the tags on your VPCs.</td></tr>
  <tr><td> <b>Tag key for subnets - Only adds routes to route table associated with the tagged subnet.</b> </td><td> <code>Route-to-tgw</code> </td><td>Specify a custom tag key name to skip the transit gateway attachment workflow and only update route table associated with the subnet being tagged.</td></tr>
  <tr><td> <b>Tag key for TGW Route Table Association with TGW Attachment</b> </td><td> <code>Associate-with</code> </td><td>Specify a custom tag key name to initiate the transit gateway route table association with the transit gateway attachment workflow. NOTE: After initial deployment, don’t change this default parameter. If you change this parameter after deployment, you must manually update the tags on your VPCs.</td></tr>
  <tr><td> <b>Tag key for Route Propagation to TGW Route Table(s)</b> </td><td> <code>Propagate-to</code> </td><td>Specify a custom tag key name to initiate the route propagation to the transit gateway route table(s) workflow. NOTE: After initial deployment, don’t change this default parameter. If you change this parameter after deployment, you must manually update the tags on your VPCs.</td></tr>
  <tr><td> <b>(Optional) Comma separated list of VPC tag keys to copy from VPC to TGW Attachments</b> </td><td> <code>Associate-with,Propagate-to</code> </td><td>Comma-separated list of tag keys (don’t include <code>Name</code>). If the VPC has these tag keys, the tag key and value are copied to the created TGW attachment(s).</td></tr>
  <tr><td> <b>Transit Gateway Peering Tag</b> </td><td> <code>TgwPeer</code> </td><td>Transit Gateway tag to monitor for peering connections. The tag value must follow the format <code>tgw-id_aws-region/tgw-id_aws-region</code>. For example, use <code>tgw-12345678_us-east-1/tgw-567890123_us-east-2</code> to create peering attachments with the two peers. You can update the value at any time.</td></tr>
  <tr><td> <b>Notification Settings</b> </td><td></td><td></td></tr>
  <tr><td> <b>Receive Approval Notifications</b> </td><td> <code>No</code> </td><td>Choose whether to receive approval notifications.</td></tr>
  <tr><td> <b>Approval Notification Email</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>The email address for approval notifications. To use this parameter, you must set the <b>Receive Approval Notifications</b> parameter to <code>Yes</code>.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of **CREATE\_COMPLETE** in approximately 25 minutes.

After the stack is created, you receive two emails that contain temporary passwords for the read-only user and the admin user. If you enabled approval notification, Amazon SNS sends a subscription confirmation email with a link to the web UI. You can also find the link to the web UI in the CloudFormation stack **Outputs** tab. The link is the **Value** of the **Console URL**. The system-generated password must be changed the first time you sign in.

**Note**
The temporary account expires if you don’t sign in within seven days. Your new password must be at least 10 characters long.
