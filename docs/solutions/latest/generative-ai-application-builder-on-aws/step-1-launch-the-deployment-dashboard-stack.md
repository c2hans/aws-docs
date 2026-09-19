---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/step-1-launch-the-deployment-dashboard-stack.html
---

# Step 1: Launch the Deployment dashboard stack
<a name="step-1-launch-the-deployment-dashboard-stack"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 10 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console) and select the button to launch the `generative-ai-application-builder-on-aws.template` CloudFormation template. [![Launch solution](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/generative-ai-application-builder-on-aws.template&stackName=&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses Amazon Kendra and Amazon Bedrock, which are not currently available in all AWS Regions. If using these features, you must launch this solution in an AWS Region where these services are available. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and STS Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Admin User Email</b> </td><td> <code>No</code> </td><td>The email address of the admin user who will have access to the Deployment dashboard. If provided, an Amazon Cognito group and user will be created with permissions to deploy and manage use cases. You may also use <code>placeholder@example.com</code> to create the Group but not the User. Refer to <a href="step-4-post-deployment-configuration.md#manual-user-pool-configuration">Manual User Pool Configuration</a> for information on setting up your user pool.</td></tr>
  <tr><td> <b>VpcEnabled</b> </td><td> <code>No</code> </td><td>Should the Deployment dashboard be deployed within a VPC</td></tr>
  <tr><td> <b>CreateNewVpc</b> </td><td> <code>No</code> </td><td>Only available, if <b>VpcEnabled</b> is <code>Yes</code>. If the value is <code>Yes</code>, the stack will create the VPC and deploy the solution within the created VPC.<br />If <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>, then you must provide an existing VPC configuration (<b>ExistingVpcId</b>, <b>ExistingPrivateSubnetIds</b>, <b>ExistingSecurityGroupIds</b>, <b>VpcAzs</b>).</td></tr>
  <tr><td> <b>IPAMPoolId</b> </td><td> <i>(Optional input)</i> </td><td>You can configure IPAM and provide the created id as input to assign the IP address range that the deployment of this stack should use. For details regarding IPAM, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html">How IPAM works.</a> </td></tr>
  <tr><td> <b>DeployUI</b> </td><td> <code>Yes</code> </td><td>You have the option to deploy the Deployment dashboard without the web user interface (and the AWS resources required for the web deployment). In which case, the solution will deploy all infrastructure including REST API endpoints. This option is useful to integrate your own web interface with the Deployment dashboard APIs.</td></tr>
  <tr><td> <b>ExistingVpcId</b> </td><td> <i>(Optional input)</i> </td><td>Required only if you want to deploy the solution in an existing VPC that you have created.</td></tr>
  <tr><td> <b>ExistingPrivateSubnetIds</b> </td><td> <i>(Optional input)</i> </td><td>Required only if you want to deploy the solution in an existing VPC that you have created. The Lambda functions will be deployed in this subnet.</td></tr>
  <tr><td> <b>ExistingSecurityGroupIds</b> </td><td> <i>(Optional input)</i> </td><td>Required only if you want to deploy the solution in an existing VPC that you have created. Ensure that security groups have the permissions for an outbound TCP connection.</td></tr>
  <tr><td> <b>VpcAzs</b> </td><td> <i>(Optional input)</i> </td><td>Required only if you want to deploy the solution in an existing VPC that you have created.</td></tr>
  <tr><td> <b>CognitoDomainPrefix</b> </td><td> <i>(Optional input)</i> </td><td>Required only if you want to deploy the solution in an existing Amazon Cognito user pool that you created. If you don’t provide a value, the solution generates it.</td></tr>
  <tr><td> <b>ExistingCognitoUserPoolId</b> </td><td> <i>(Optional input)</i> </td><td>Required only if you want to deploy the solution in an existing Amazon Cognito user pool that you created.</td></tr>
  <tr><td> <b>ExistingCognitoUserPoolClient</b> </td><td> <i>(Optional input)</i> </td><td>Required only if you want to deploy the solution in an existing Amazon Cognito user pool that you created. If you don’t provide a value, the solution creates a user pool client. This parameter can only be provided if you provide an <b>ExistingCognitoUserPoolId</b> value.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next.**

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 10 minutes.
