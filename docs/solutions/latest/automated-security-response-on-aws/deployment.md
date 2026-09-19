---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/deployment.html
---

# Automated deployment - Stacks
<a name="deployment"></a>

**Note**
For multi-account customers, we strongly recommend [deployment with StackSets](deployment-stackset.md).

Before you launch the solution, review the architecture, solution components, security, and design considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 30 minutes

## Prerequisites
<a name="prerequisites"></a>

Before you deploy this solution, ensure that AWS Security Hub is in the same AWS Region as your primary and secondary accounts. If you have previously deployed this solution, you must uninstall the existing solution. For more information, refer to [Update the solution](update-the-solution.md).

## Deployment overview
<a name="deployment-overview"></a>

Use the following steps to deploy this solution on AWS.

 [(Optional) Step 0: Launch a ticket system integration stack](#step-0)
+ If you intend to use the ticketing feature, deploy the ticketing integration stack into your Security Hub admin account first.
+ Copy the Lambda function name from this stack and provide it as input to the admin stack (see Step 1).

 [Step 1: Launch the admin stack](#step-1)
+ Launch the `automated-security-response-admin.template` AWS CloudFormation template into your AWS Security Hub admin account.
+ Choose which security standards to install.
+ Choose an existing Orchestrator log group to use (choose `Yes` if `SO0111-ASR-Orchestrator` already exists from a previous installation).

 [Step 2: Install the remediation roles into each AWS Security Hub member account](#step-2)
+ Launch the `automated-security-response-member-roles.template` AWS CloudFormation template into one Region per member account.
+ Enter the 12-digit account ID for the AWS Security Hub admin account.

 [Step 3: Launch the member stack](#step-3)
+ Specify the name of the CloudWatch Logs group to use with CIS 3.1-3.14 remediations. It must be the name of a CloudWatch Logs log group that receives CloudTrail logs.
+ Choose whether to install the remediation roles. Install these roles only once for each account.
+ Choose which playbooks to install.
+ Enter the account ID of the AWS Security Hub admin account.

 [Step 4: (Optional) Adjust the available remediations](#step-4)
+ Remove any remediations on a per-member account basis. This step is optional.

## (Optional) Step 0: Launch a ticket system integration stack
<a name="step-0"></a>

1. If you intend to use the ticketing feature, launch the respective integration stack first.

1. Choose the provided integration stacks for Jira or ServiceNow, or use them as a blueprint to implement your own custom integration.

    **To deploy the Jira stack**:

   1. Enter a name for your stack.

   1. Provide the URI to your Jira instance.

   1. Provide the project key for the Jira project that you want to send tickets to.

   1. Create a new key-value secret in Secrets Manager that holds your Jira `Username` and `Password`.
**Note**
You can choose to use a Jira API key in place of your password by providing your username as `Username` and your API key as the `Password`.

   1. Add the ARN of this secret as input to the stack.

       **Provide a stack name, Jira project information, and Jira API credentials.**
![Jira ticket system integration stack configuration](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/ticket-system-integration-stack-jira.png)

       **Jira Field Configuration**:

      For information on customizing Jira ticket fields, refer to the Jira Field Configuration section in [Step 0 of the StackSet deployment](deployment-stackset.md#step-0-stackset).

       **To deploy the ServiceNow stack**:

   1. Enter a name for your stack.

   1. Provide the URI of your ServiceNow instance.

   1. Provide your ServiceNow table name.

   1. Create an API key in ServiceNow with permission to modify the table you intend to write to.

   1. Create a secret in Secrets Manager with the key `API_Key` and provide the secret ARN as input to the stack.

       **Provide a stack name, ServiceNow project information, and ServiceNow API credentials.**
![ServiceNow ticket system integration stack configuration](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/ticket-system-integration-stack-servicenow.png)

       **To create a custom integration stack**: Include a Lambda function that the solution orchestrator Step Functions can call for each remediation. The Lambda function should take the input provided by Step Functions, construct a payload according to the requirements of your ticketing system, and make a request to your system to create the ticket.

## Step 1: Launch the admin stack
<a name="step-1"></a>

**Important**
This solution includes data collection. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

This automated AWS CloudFormation template deploys the Automated Security Response on AWS solution in the AWS Cloud. Before you launch the stack, you must enable Security Hub and complete the [prerequisites](#prerequisites).

**Note**
You are responsible for the cost of the AWS services used while running this solution. For more details, see the [Cost](cost.md) section in this guide, and refer to the pricing webpage for each AWS service used in this solution.

1. Sign in to the AWS Management Console from the account where the AWS Security Hub is currently configured, and choose the button below to launch the `automated-security-response-admin.template` AWS CloudFormation template.

    [![automated-security-response-admin-template launch button](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=automated-security-response-on-aws-admin&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-admin.template&redirectId=ImplementationGuide)

   You can also [download the template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-admin.template) as a starting point for your own implementation.

1. The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the AWS Management Console navigation bar.
**Note**
This solution uses AWS Systems Manager which is currently available in specific AWS Regions only. The solution works in all of the Regions that support this service. For the most current availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and then choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and STS limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. On the **Parameters** page, choose **Next**.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Load SC Admin Stack</b> </td><td> <code>yes</code> </td><td>Specify whether to install the admin components for automated remediation of SC controls.</td></tr>
  <tr><td> <b>Load AFSBP Admin Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the admin components for automated remediation of FSBP controls.</td></tr>
  <tr><td> <b>Load CIS120 Admin Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the admin components for automated remediation of CIS120 controls.</td></tr>
  <tr><td> <b>Load CIS140 Admin Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the admin components for automated remediation of CIS140 controls.</td></tr>
  <tr><td> <b>Load CIS300 Admin Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the admin components for automated remediation of CIS300 controls.</td></tr>
  <tr><td> <b>Load PCI321 Admin Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the admin components for automated remediation of PCI321 controls.</td></tr>
  <tr><td> <b>Load NIST Admin Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the admin components for automated remediation of NIST controls.</td></tr>
  <tr><td> <b>Reuse Orchestrator Log Group</b> </td><td> <code>no</code> </td><td>Select whether or not to reuse an existing <code>SO0111-ASR-Orchestrator</code> CloudWatch Logs group. This simplifies reinstallation and upgrades without losing log data from a previous version. Reuse existing <code>Orchestrator Log Group</code> choose <code>yes</code> if the <code>Orchestrator Log Group</code> still exists from an earlier deployment in this account, otherwise <code>no</code>. If you are performing a stack update from an earlier version than v2.3.0 choose <code>no</code> </td></tr>
  <tr><td> <b>ShouldDeployWebUI</b> </td><td> <code>yes</code> </td><td>Deploy the Web UI components including API Gateway, Lambda functions, and CloudFront distribution. Choose "yes" to enable the web-based user interface for viewing findings and remediation status.</td></tr>
  <tr><td> <b>AdminUserEmail</b> </td><td> <i>(Optional input)</i> </td><td>Email address for the initial admin user. This user will have full administrative access to the ASR Web UI. Required <b>only</b> when Web UI is enabled.</td></tr>
  <tr><td> <b>Use CloudWatch Metrics</b> </td><td> <code>yes</code> </td><td>Specify whether to enable CloudWatch Metrics for monitoring the solution. This will create a CloudWatch Dashboard for viewing metrics.</td></tr>
  <tr><td> <b>Use CloudWatch Metrics Alarms</b> </td><td> <code>yes</code> </td><td>Specify whether to enable CloudWatch Metrics Alarms for the solution. This will create Alarms for certain metrics collected by the solution.</td></tr>
  <tr><td> <b>RemediationFailureAlarmThreshold</b> </td><td> <code>5</code> </td><td>Specify the threshold for percentage of remediation failures per control ID. For example, if you enter <code>5</code>, you receive an alarm if a control ID fails more than 5% of remediations at a given day.<br />This parameter functions only if alarms are created (see the <b>Use CloudWatch Metrics Alarms</b> parameter).</td></tr>
  <tr><td> <b>EnableEnhancedCloudWatchMetrics</b> </td><td> <code>no</code> </td><td>If <code>yes</code>, creates additional CloudWatch metrics to track all control IDs individually on the CloudWatch dashboard and as CloudWatch alarms.<br />See the <a href="cost.md#additional-cost-enhanced-metrics">Cost</a> section to understand the additional cost that this incurs.</td></tr>
  <tr><td> <b>TicketGenFunctionName</b> </td><td> <i>(Optional input)</i> </td><td>Optional. Leave blank if you don’t want to integrate a ticketing system. Otherwise, provide the Lambda function name from the stack output of <a href="#step-0">Step 0</a>, for example: <code>SO0111-ASR-ServiceNow-TicketGenerator</code>.</td></tr>
</tbody>
</table>

**Note**
You must manually enable automatic remediations in the Admin account after deploying or updating the solution’s CloudFormation stacks.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 15 minutes.

## Step 2: Install the remediation roles into each AWS Security Hub member account
<a name="step-2"></a>

The `automated-security-response-member-roles.template` StackSet must be deployed in only one Region for each member account. It defines the global roles that allow cross-account API calls from the ASR Orchestrator step function.

1. Sign in to the AWS Management Console for each AWS Security Hub member account (including the admin account, which is also a member). Choose the button to launch the `automated-security-response-member-roles.template` AWS CloudFormation template. You can also [download the template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member-roles.template) as a starting point for your own implementation.

    [![Launch solution](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=automated-security-response-on-aws-member-roles&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-member-roles.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the AWS Management Console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is in the Amazon S3 URL text box and then choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to IAM and STS limits in the AWS Identity and Access Management User Guide.

1. On the **Parameters** page, specify the following parameters and choose Next.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Namespace</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Enter a string of up to 9 lowercase alphanumeric characters. Unique namespace to be added as a suffix to remediation IAM role names. The same namespace should be used in the Member Roles and Member stacks. This string should be unique for each solution deployment, but does not need to be changed during stack updates. The namespace value does <b>not</b> need to be unique per member account.</td></tr>
  <tr><td> <b>Sec Hub Admin Account</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Enter the 12-digit account ID for the AWS Security Hub admin account. This value grants permissions to the admin account’s solution role.</td></tr>
</tbody>
</table>

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 5 minutes. You may continue with the next step while this stack loads.

## Step 3: Launch the member stack
<a name="step-3"></a>

**Important**
This solution includes data collection. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

The `automated-security-response-member` stack must be installed into each Security Hub member account. This stack defines the runbooks for automated remediation. The admin for each member account can control what remediations are available via this stack.

1. Sign in to the AWS Management Console for each AWS Security Hub member account (including the admin account, which is also a member). Choose the button to launch the `automated-security-response-member.template` AWS CloudFormation template.

    [![automated-security-response-member.template, Launch solution](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=automated-security-response-on-aws-member&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-member.template&redirectId=ImplementationGuide)

You can also [download the template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member.template) as a starting point for your own implementation. . The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the AWS Management Console navigation bar.

\+

**Note**
This solution uses AWS Systems Manager, which is currently available in the majority of AWS Regions. The solution works in all of the Regions that support these services. For the most current availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and then choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and STS limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. On the **Parameters** page, specify the following parameters and choose **Next**.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Provide the name of the LogGroup to be used to create Metric Filters and Alarms</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Specify the name of a CloudWatch Logs group where CloudTrail logs API calls. This is used for CIS 3.1-3.14 remediations.</td></tr>
  <tr><td> <b>Load SC Member Stack</b> </td><td> <code>yes</code> </td><td>Specify whether to install the member components for automated remediation of SC controls.</td></tr>
  <tr><td> <b>Load AFSBP Member Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the member components for automated remediation of FSBP controls.</td></tr>
  <tr><td> <b>Load CIS120 Member Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the member components for automated remediation of CIS120 controls.</td></tr>
  <tr><td> <b>Load CIS140 Member Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the member components for automated remediation of CIS140 controls.</td></tr>
  <tr><td> <b>Load CIS300 Member Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the member components for automated remediation of CIS300 controls.</td></tr>
  <tr><td> <b>Load PCI321 Member Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the member components for automated remediation of PCI321 controls.</td></tr>
  <tr><td> <b>Load NIST Member Stack</b> </td><td> <code>no</code> </td><td>Specify whether to install the member components for automated remediation of NIST controls.</td></tr>
  <tr><td> <b>Create S3 Bucket For Redshift Audit Logging</b> </td><td> <code>no</code> </td><td>Choose <code>yes</code> to create the S3 bucket for the FSBP RedShift.4 remediation. For details of the S3 bucket and the remediation, review the <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html#fsbp-redshift-4">Redshift.4 remediation</a> in the <i>AWS Security Hub User Guide</i>.</td></tr>
  <tr><td> <b>Sec Hub Admin Account</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Enter the 12-digit account ID for the AWS Security Hub admin account.</td></tr>
  <tr><td> <b>Namespace</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Enter a string of up to 9 lowercase alphanumeric characters. This string becomes part of the IAM role names and Action Log S3 bucket. Use the same value for member stack deployment and member roles stack deployment. String should be unique for each solution deployment, but does not need to be changed during stack updates.</td></tr>
  <tr><td> <b>EnableCloudTrailForASRActionLog</b> </td><td> <code>no</code> </td><td>Select <code>yes</code> if you want to monitor management events conducted by the solution on the CloudWatch dashboard. The solution creates a CloudTrail trail in each member account where you select <code>yes</code>. You must deploy the solution into an AWS Organization to enable this feature. <b>Additionally, you can only enable this feature in a single region within the same account.</b> See the <a href="cost.md#additional-cost-action-log">Cost</a> section to understand the additional cost that this incurs.</td></tr>
</tbody>
</table>

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 15 minutes.

## Step 4: (Optional) Adjust the available remediations
<a name="step-4"></a>

If you want to remove specific remediations from a member account, you can do so by updating the nested stack for the security standard. For simplicity, the nested stack options are not propagated to the root stack.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) and select the nested stack.

1. Choose **Update**.

1. Select **Update nested stack** and choose **Update stack**.

    **Update nested stack**
![Update nested stack dialog](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/nested-stack.png)

1. Select **Use current template** and choose **Next**.

1. Adjust the available remediations. Change the values for desired controls to `Available` and undesired controls to `Not available`.
**Note**
Turning off a remediation removes the solution’s remediation runbook for the security standard and control.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Update stack**.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 15 minutes.
