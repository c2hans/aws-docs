---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/step-1-launch-the-hub-stack.html
---

# Step 1: Launch the Hub stack
<a name="step-1-launch-the-hub-stack"></a>

**Important**
Launch the Hub stack before launching the Spoke stack and Org-Management stack.

Follow the step-by-step instructions in this section to configure and deploy the solution into your Hub account.

 **Time to deploy:** Approximately 20 minutes

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and select the button to launch the `account-assessment-for-aws-organizations-hub.template` CloudFormation template.

 [![Launch Stack](https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/account-assessment-for-aws-organizations/latest/account-assessment-for-aws-organizations-hub.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito that is not currently available in all AWS Regions. You must launch this solution in an AWS Region where Amazon Cognito is available. For the most current availability of AWS services by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Solution Setup</b> </td><td></td><td></td></tr>
  <tr><td>Provide the unique namespace value</td><td> {{&lt;Requires input&gt;}} </td><td>Chose a unique string as prefix for resource names. NOTE: Use the same namespace in the Spoke stack and Org-Management stack.</td></tr>
  <tr><td>DynamoDB Configuration</td><td></td><td></td></tr>
  <tr><td>Provide Time to live (in days) for DynamoDB items</td><td> <code>90</code> </td><td>Time period in days all DynamoDB tables will delete stored items.</td></tr>
  <tr><td> <b>Web UI Configuration</b> </td><td></td><td></td></tr>
  <tr><td>Provide Web UI Login User Email</td><td> {{&lt;Requires input&gt;}} </td><td>Admin user will be created at deployment time. Provide an email address to create this initial Cognito user.</td></tr>
  <tr><td>Provide a prefix for the hosted Amazon Cognito domain</td><td> {{&lt;Requires input&gt;}} </td><td>Pick a globally unique prefix to become part of the url of the login page (Cognito Hosted UI)</td></tr>
  <tr><td>Set MFA for Cognito to "ON" or "OPTIONAL" </td><td> <i> &lt;Optional input&gt; </i> </td><td> <code>ON</code> - Amazon Cognito users will need to set up multi-factor authentication (MFA) on first login. <code>OPTIONAL</code> - Amazon Cognito users may opt to set up MFA</td></tr>
  <tr><td> <b>Security Configuration</b> </td><td></td><td></td></tr>
  <tr><td>Provide CIDR ranges that allow the console to access the API</td><td> {{&lt;Requires input&gt;}} </td><td>Comma separated list of CIDR ranges that allow access to the API. To allow the entire internet, use the following list of two CIDR blocks as the value: <code>0.0.0.0/1,128.0.0.0/1</code> </td></tr>
  <tr><td>Application Manager Configuration</td><td></td><td></td></tr>
  <tr><td>Provide the AWS Organization ID</td><td> <i>&lt;Requires input&gt;</i> </td><td>Organization ID to support multi-account deployment. Leave blank for single account deployments.</td></tr>
  <tr><td>Management Account ID</td><td> <i>&lt;Optional input&gt;</i> </td><td>Account ID for the management account of the AWS Organization. Leave blank for single account deployments.</td></tr>
</tbody>
</table>

1. Choose **Next**\*

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a `CREATE_COMPLETE` status in approximately five minutes.

**Note**
In addition to its primary Lambda functions, this solution includes the `solution-helper` Lambda function, which runs only during initial configuration or when resources are updated or deleted.
When you run this solution, you will notice all Lambda functions in the AWS console. Only the primary functions are regularly active. However, you must not delete the `solution-helper` function, as it is necessary to manage associated resources.
