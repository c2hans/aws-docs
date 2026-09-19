---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/deploying-a-standalone-agent-use-case.html
---

# Deploying a standalone Bedrock Agent use case
<a name="deploying-a-standalone-agent-use-case"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 10-30 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the CloudFront template.

<table>
<tbody>
  <tr><td> <b>BedrockAgent.template</b> </td><td> <a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/BedrockAgent.template&amp;stackName=&amp;redirectId=ImplementationGuide">https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/BedrockAgent.template&amp;stackName=&amp;redirectId=ImplementationGuide</a> </td></tr>
</tbody>
</table>

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses Amazon Bedrock, which is not currently available in all AWS Regions. If you’re using these features, you must launch this solution in an AWS Region where these services are available. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see {https---docs-aws-amazon-com-https---docs-aws-amazon-com-IAM-latest-UserGuide-reference-iam-limits-html}[IAM and AWS STS quotas] in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default entry</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>UseCaseUUID</b> </td><td> {{&lt;_Requires input_&gt;}} </td><td>36 character long UUIDv4 to identify this deployed use case within an application.</td></tr>
  <tr><td> <b>UseCaseConfigRecordKey</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Key corresponding to the record that contains configurations required by the chat provider Lambda function at runtime.<br />The record in the table must have a <b>key</b> attribute matching this value, and a <b>config</b> attribute containing the desired configuration.<br />This record will be populated by the deployment platform if it’s in use. For standalone deployments of this use case, a manually created entry in the table defined in <b>UseCaseConfigTableName</b> is required.</td></tr>
  <tr><td> <b>UseCaseConfigTableName</b> </td><td> {{&lt;Requires input&gt;`}} </td><td>The stack will read the use case configuration from the table provided here and using the record key defined in <b>UseCaseConfigRecordKey</b>.</td></tr>
  <tr><td> <b>DefaultUserEmail</b> </td><td> <code>placeholder@example.com</code> </td><td>Email of the default user for this use case. The solution creates an Amazon Cognito user for this email to access the use case.</td></tr>
  <tr><td> <b>ExistingRestApiId</b> </td><td> <i>(Optional input)</i> </td><td>Existing API Gateway REST API ID to use. If not provided, a new API Gateway REST API will be created. Typically provided when deploying from the Deployment dashboard.<br />Note: Using Existing APIs can help reduce resource duplication and simplify management of APIs when you need to deploy multiple standalone use cases. When supplying existing APIs for a standalone use case, you are responsible for ensuring that the API is configured with the required route(s) with expected models. A required pre-configured /details route (fetches use case details during chat) and optionally, a /feedback route (if <b>FeedbackEnabled</b> is set to <code>Yes</code> to enable collection of feedback for LLM chat responses) must be configured. Additionally, <b>ExistingApiRootResourceId</b>, <b>ExistingCognitoUserPoolId</b> and <b>ExistingCognitoGroupPolicyTableName</b> must also be provided.</td></tr>
  <tr><td> <b>ExistingApiRootResourceId</b> </td><td> <i>(Optional input)</i> </td><td>Existing API Gateway REST API Root Resource ID to use. REST API Root Resource ID can be obtained from the AWS console by selecting the root resource (/) in the "Resources" section of the API.The Resource ID will then be displayed in the Resource details panel. You can alternatively run a describe API call on your REST API to find the Root Resource ID.</td></tr>
  <tr><td> <b>FeedbackEnabled</b> </td><td> <code>No</code> </td><td>If set to No, the deployed use case stack will not have access to the feedback feature.</td></tr>
  <tr><td> <b>CognitoDomainPrefix</b> </td><td> <i>(Optional input)</i> </td><td>Enter a value if you want to provide a domain for the Amazon Cognito user pool client. If you don’t provide a value, the solution generates one.</td></tr>
  <tr><td> <b>ExistingCognitoUserPoolId</b> </td><td> <i>(Optional input)</i> </td><td> <b>UserPoolId</b> of an existing Amazon Cognito user pool that you want to authenticate this use case with. NOTE: You typically provide this ID when deploying from the Deployment dashboard, but you can omit it when deploying this use case stack standalone.</td></tr>
  <tr><td> <b>ExistingCognitoUserPoolClient</b> </td><td> <i>(Optional input)</i> </td><td>Provide a user pool client (app client) to use an existing one. If you don’t provide a user pool client, the solution creates one. You can only provide this parameter if you provided an <b>ExistingCognitoUserPoolId</b>.</td></tr>
  <tr><td> <b>ExistingCognitoGroupPolicyTableName</b> </td><td> <i>(Optional input)</i> </td><td>Name of the DynamoDB table containing user group policies. This is used by the custom authorizer on the use case’s API. NOTE: You typically provide this name when deploying from the Deployment dashboard, but you can omit it when deploying this use case stack standalone.</td></tr>
  <tr><td> <b>VpcEnabled</b> </td><td> <code>No</code> </td><td>Whether the stacks resources be deployed within a VPC.</td></tr>
  <tr><td> <b>CreateNewVpc</b> </td><td> <code>No</code> </td><td>Select <code>Yes</code> if you want the solution to create a new VPC for you and to use it for this use case. NOTE: This parameter is only relevant if <b>VpcEnabled</b> is <code>Yes</code>.</td></tr>
  <tr><td> <b>IPAMPoolId</b> </td><td> <i>(Optional input)</i> </td><td>If you want to assign the CIDR range using IPAM, provide the IPAM pool ID to use. NOTE: This parameter is only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>ExistingVpcId</b> </td><td> <i>(Optional input)</i> </td><td>VPC ID of an existing VPC to be used for the use case. NOTE: This parameter is only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>ExistingPrivateSubnetIds</b> </td><td> <i>(Optional input)</i> </td><td>Comma separated list of subnet IDs of existing private subnets to be used to deploy the Lambda function. NOTE: This parameter is only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>ExistingSecurityGroupIds</b> </td><td> <i>(Optional input)</i> </td><td>Comma-separated list of security groups of the existing VPC to be used for configuring Lambda functions. NOTE: This parameter is only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>VpcAzs</b> </td><td> <i>(Optional input)</i> </td><td>Comma separated list of AZs in which subnets of the VPCs are created<br />Note: Only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>BedrockAgentId</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The ID of the Amazon Bedrock Agent to be used.</td></tr>
  <tr><td> <b>BedrockAgentAliasId</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The alias ID of the Amazon Bedrock Agent to be used.</td></tr>
  <tr><td> <b>DeployUI</b> </td><td> <code>Yes</code> </td><td>Select the option to deploy the frontend chat UI for this deployment. Selecting <code>No</code> results in creating the infrastructure to host the APIs, the authentication for the APIs, and backend processing without the chat UI.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 10-30 minutes.
