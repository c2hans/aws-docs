---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/launch-the-stack.html
---

# Step 2: Launch the stack
<a name="launch-the-stack"></a>

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/).
To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your template and deploy the solution. For more information, refer to the [Anonymized data collection](anonymized-data-collection.md) section of this guide.

This automated AWS CloudFormation template deploys the Cloud Migration Factory on AWS solution in the AWS Cloud.

**Note**
You are responsible for the cost of the AWS services used while running this solution. Refer to the [Cost](cost.md) section for more details. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

1. Sign into [AWS Management Console](https://aws.amazon.com/console) and select the button to launch `cloud-migration-factory-solution` CloudFormation template. [![Launch solution](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fcloud-migration-factory-on-aws%2Flatest%2Faws-cloud-migration-factory-solution.template)

   You can also [download the template](https://solutions-reference.s3.amazonaws.com/cloud-migration-factory-on-aws/latest/aws-cloud-migration-factory-solution.template&redirectId=ImplementationGuide) as a starting point for your own implementation.

1. The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito and Amazon QuickSight, which are currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where these services are available. For the most current availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
When deployed in Public and Public with WAF deployment types, the solution also uses Amazon CloudFront logging to Amazon S3. Today, log delivery from Amazon CloudFront to Amazon S3 is only available in specific Regions. Refer to [Choosing an Amazon S3 bucket for your standard logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html#access-logs-choosing-s3-bucket) to verify your Region is supported.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Application name</b> </td><td> <code>migration-factory</code> </td><td>Enter a prefix to the AWS CloudFormation <b>Physical ID</b> that identifies the AWS services deployed by this solution.NOTE: The <b>Application name</b> is used as a prefix to identify the AWS resources that are deployed: {{&lt;application-name&gt;}}-{{&lt;environment-name&gt;}}-{{&lt;aws-resource&gt;}}. If you change the default name, we recommend that you keep the combined prefix labels to 40 characters or less to ensure that you don’t exceed character limitations.</td></tr>
  <tr><td> <b>Environment name</b> </td><td> <code>test</code> </td><td>Enter a name to identify the network environment where the solution is deployed. We recommend a descriptive name such as <code>test</code>, <code>dev</code>, or <code>prod</code>. NOTE: The <b>Environment name</b> is used as a prefix to identify the AWS resources that are deployed: {{&lt;application-name&gt;}}-{{&lt;environment-name&gt;}}-{{&lt;aws-resource&gt;}}. If changing the default name, we recommend that you keep the combined prefix labels to 40 characters or less to ensure that you do not exceed character limitations.</td></tr>
  <tr><td> <b>Migration Tracker</b> </td><td> <code>true</code> </td><td>By default, the optional migration tracker dashboard is activated, but you can deactivate it by changing this parameter to <code>false</code>.</td></tr>
  <tr><td> <b>Replatform EC2</b> </td><td> <code>true</code> </td><td>By default, the Replatform EC2 feature is activated, but you can deactivate it by changing this parameter to <code>false</code>.</td></tr>
  <tr><td> <b>ServiceAccountEmail</b> </td><td> <code>serviceaccount@yourdomain.com</code> </td><td>Default service account email address, the migration factory automation scripts use this account to connect to the factory API.</td></tr>
  <tr><td> <b>Allow additional identity provider to be configured in Cognito</b> </td><td> <code>false</code> </td><td>By default, the solution uses Amazon Cognito to create and manage access. Changing this parameter to <code>true</code> will configure the solution to allow external SAML identity providers to be added to Amazon Cognito and used to sign in.</td></tr>
  <tr><td> <b>Deployment Type</b> </td><td> <code>Public</code> </td><td>By default, the deployment type is <code>Public</code>, and all Cloud Migration Factory endpoints are publicly accessible with user authentication.<br /> <b>Public with AWS WAF</b>: Access to CMF endpoints is restricted to customizable CIDR ranges. We recommend this option based on AWS security best practices.<br /> <b>Private</b>: All Cloud Migration Factory endpoints are accessible only from your VPC networks and the Cloud Migration Factory Web UI must be hosted on a private web server deployed separately.</td></tr>
  <tr><td> <b>(Optional) Private Deployment Type Only</b> </td><td></td><td></td></tr>
  <tr><td> <b>Full URL used to access web user interface</b> </td><td> <code>[not set]</code> </td><td>Required when <b>Deployment Type</b> is set to <code>Private</code>. Specify the migration factory web interface URL that will serve the static web content. Example https://cmf.yourdomain.local. <ul><li> Do not add a trailing forward slash to the URL, this will cause the web interface to fail when loading. <ul><li> In private deployments a web server is required to host the static content and needs to be deployed before deployment of the CloudFormation template. </li></ul> </li></ul> </td></tr>
  <tr><td> <b>VPC ID to host API Gateway Endpoints</b> </td><td> <code>[not set]</code> </td><td>Required when <b>Deployment Type</b> is set to <code>Private</code>. Specify a single VPC ID where the private API Gateway endpoints will be created.</td></tr>
  <tr><td> <b>Subnets to host API Gateway Interface Endpoints</b> </td><td> <code>[not set]</code> </td><td>Required when <b>Deployment Type</b> is set to <code>Private</code>. Specify a two Subnet IDs where the private API Gateway endpoints will be created. The Subnet IDs specified have to be within the VPC specified above.</td></tr>
  <tr><td> <b>(Optional) Public with AWS WAF Deployment Type Only</b> </td><td></td><td></td></tr>
  <tr><td> <b>Allowed CIDR</b> </td><td> <code>[not set]</code> </td><td>Required when <b>Deployment Type</b> is set to <code>Public with AWS WAF</code>. Specify two CIDR ranges from which the users and the automation server will be accessing the endpoints from. <ul><li> You must specify 2 CIDR ranges. </li><li> The IP address of the CMF automation server OR the outgoing NAT Gateway IP must be included in the allowed IP addresses. Without the internal IP of the CMF EC2 instance OR the NAT Gateway IP, the CMF automation scripts will fail to access the solution endpoints. </li><li> Once deployed, it is possible to add additional ranges and restrictions to the AWS WAF rules as required. </li></ul> </td></tr>
  <tr><td> <b>WPM (Wave Planning Manager)</b> </td><td> <code>true</code> </td><td>By default, the Wave Planning Manager is deployed, but you can deactivate it by changing this parameter to <code>false</code>.</td></tr>
  <tr><td> <b>Deploy Bedrock Guardrail</b> </td><td> <code>true</code> </td><td>By default, the Bedrock Guardrail is deployed, which help enforce security controls and compliance policies for your generative AI applications. Guardrails provide additional protection by filtering and monitoring content generated through Bedrock APIs. You can deactivate it by changing this parameter to <code>false</code>.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the boxes acknowledging that the template will create [AWS Identity and Access Management](https://aws.amazon.com/iam) (IAM) resources and that it might require the capability **CAPABILITY\_AUTO\_EXPAND**.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 20 minutes.

**Important**
If you are using AWS MGN, you must complete the prerequisite for AWS MGN before continuing to Step 3.
