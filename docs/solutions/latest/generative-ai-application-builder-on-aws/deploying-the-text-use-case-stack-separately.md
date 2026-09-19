---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/deploying-the-text-use-case-stack-separately.html
---

# Deploying a standalone Text use case
<a name="deploying-the-text-use-case-stack-separately"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 10-30 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the CloudFront template that you want to deploy.

<table>
<thead>
  <tr><th> <b>BedrockChat.template</b> </th><th> <a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/BedrockChat.template&amp;stackName=&amp;redirectId=ImplementationGuide">https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/BedrockChat.template&amp;stackName=&amp;redirectId=ImplementationGuide</a> </th></tr>
</thead>
<tbody>
  <tr><td> <b>SageMakerChat.template</b> </td><td> <a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/SageMakerChat.template&amp;stackName=&amp;redirectId=ImplementationGuide">https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/SageMakerChat.template&amp;stackName=&amp;redirectId=ImplementationGuide</a> </td></tr>
</tbody>
</table>

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

   Note: This solution uses Amazon Kendra and Amazon Bedrock, which are not currently available in all AWS Regions. If using these features, you must launch this solution in an AWS Region where these services are available. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack \*page, verify that the correct template URL is in the \*Amazon S3 URL \*text box and choose \*Next**.

1. On the \*Specify stack details \*page, assign a name to your solution stack. For information about naming character limitations, see [IAM and STS Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<tbody>
  <tr><td> <b>UseCaseUUID</b> </td><td> {{&lt;_Requires input_&gt;}} </td><td>36 character long UUIDv4 to identify this deployed use case within an application.</td></tr>
  <tr><td> <b>UseCaseConfigRecordKey</b> </td><td> {{&lt;_Requires input_&gt;}} </td><td>Key corresponding of the record containing configurations required by the chat provider Lambda at runtime. The record in the table must have a <b>key</b> attribute matching this value, and a <b>config</b> attribute containing the desired configuration. This record will be populated by the deployment platform if in use. For standalone deployments of this use case, a manually created entry in the table defined in <b>UseCaseConfigTableName</b> is required.</td></tr>
  <tr><td> <b>UseCaseConfigTableName</b> </td><td> {{&lt;_Requires input_&gt;}} </td><td>The stack will read the configuration from the table with this name at the key <b>UseCaseConfigRecordKey</b> </td></tr>
  <tr><td> <b>ExistingRestApiId</b> </td><td> <i>(Optional input)</i> </td><td>Existing API Gateway REST API ID to use. If not provided, a new API Gateway REST API will be created. Typically provided when deploying from the Deployment dashboard.<br />Note: Using Existing APIs can help reduce resource duplication and simplify management of APIs when you need to deploy multiple standalone use cases. When supplying existing APIs for a standalone use case, you are responsible for ensuring that the API is configured with the required route(s) with expected models. A required pre-configured /details route (fetches use case details during chat) and optionally, a /feedback route (if <b>FeedbackEnabled</b> is set to <code>Yes</code> to enable collection of feedback for LLM chat responses) must be configured. Additionally, <b>ExistingApiRootResourceId</b>, <b>ExistingCognitoUserPoolId</b> and <b>ExistingCognitoGroupPolicyTableName</b> must also be provided.</td></tr>
  <tr><td> <b>ExistingApiRootResourceId</b> </td><td> <i>(Optional input)</i> </td><td>Existing API Gateway REST API Root Resource ID to use. REST API Root Resource ID can be obtained from the AWS console by selecting the root resource (/) in the "Resources" section of the API. The Resource ID will then be displayed in the Resource details panel. You can alternatively run a describe API call on your REST API to find the Root Resource ID.</td></tr>
  <tr><td> <b>FeedbackEnabled</b> </td><td> <code>No</code> </td><td>If set to No, the deployed use case stack will not have access to the feedback feature.</td></tr>
  <tr><td> <b>ExistingModelInfoTableName</b> </td><td> <i>(Optional input)</i> </td><td>DynamoDB table name for the table which contains model info and defaults. Used by the deployment platform. If omitted, a new table will be created to house model defaults.</td></tr>
  <tr><td> <b>DefaultUserEmail</b> </td><td> <code>placeholder@example.com</code> </td><td>Email of the default user for this use case. An Amazon Cognito user for this email is created to access the use case. If not provided, the Cognito Group and User will not be created. You may also use <code>placeholder@example.com</code> to create the Group but not the User. Refer to <a href="step-4-post-deployment-configuration.md#manual-user-pool-configuration">Manual User Pool Configuration</a> for information on setting up your user pool.</td></tr>
  <tr><td> <b>ExistingCognitoUserPoolId</b> </td><td> <i>(Optional input)</i> </td><td> <b>UserPoolId</b> of an existing Amazon Cognito user pool which this use case will be authenticated with. Typically provided when deploying from the Deployment dashboard, but can be omitted when deploying this use case stack standalone.</td></tr>
  <tr><td> <b>CognitoDomainPrefix</b> </td><td> <i>(Optional input)</i> </td><td>Enter a value if you want to provide a domain for the Cognito User Pool Client. If you don’t provide a value, the deployment will generate one.</td></tr>
  <tr><td> <b>ExistingCognitoUserPoolClient</b> </td><td> <i>(Optional input)</i> </td><td>Provide a User Pool Client (App Client) to use an existing one. If you don’t provide a User Pool Client, a new one will be created. This parameter can only be provided if an existing User Pool Id is provided.</td></tr>
  <tr><td> <b>ExistingCognitoGroupPolicyTableName</b> </td><td> <i>(Optional input)</i> </td><td>Name of the DynamoDB table containing user group policies. This is used by the custom authorizer on the use case’s API. Typically, you can provide an input when deploying from the deployment platform, but can be omitted when deploying this use case stack standalone.</td></tr>
  <tr><td> <b>RAGEnabled</b> </td><td> <code>true</code> </td><td>If set to true, the deployed use case stack uses the provided Amazon Kendra index created to provide RAG functionality. If set to <code>false</code>, the user interacts directly with the LLM.</td></tr>
  <tr><td> <b>KnowledgeBaseType</b> </td><td>Bedrock</td><td>Knowledge base type to be used for RAG. Only set if RAGEnabled is <code>true</code>. Can be Bedrock or Kendra.<br />Note: Only relevant if <b>RAGEnabled</b> is true.</td></tr>
  <tr><td> <b>ExistingKendraIndexId</b> </td><td> <i>(Optional input)</i> </td><td>Index ID of an existing Kendra index to be used for the use case. If none is provided and <b>KnowledgeBaseType</b> is Kendra, a new index will be created for you.<br />Note: Only relevant if <b>RAGEnabled</b> is <code>true</code> and <b>KnowledgeBaseType</b> is <code>Kendra</code>.</td></tr>
  <tr><td> <b>NewKendraIndexName</b> </td><td> <i>(Optional input)</i> </td><td>Name for the new Kendra index to be created for this use case. Only applies if <b>ExistingKendraIndexId</b> is not supplied.<br />Note: Only relevant if <b>RAGEnabled</b> is true and <b>KnowledgeBaseType</b> is Kendra.</td></tr>
  <tr><td> <b>NewKendraQueryCapacityUnits</b> </td><td>0</td><td>Additional query capacity units for the new Amazon Kendra index to be created for this use case. Only applies if <b>ExistingKendraIndexId</b> is not supplied, see <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_CapacityUnitsConfiguration.html">CapacityUnitsConfiguration</a>.<br />Note: Only relevant if <b>RAGEnabled</b> is <code>true</code> and <b>KnowledgeBaseType</b> is <code>Kendra</code>.</td></tr>
  <tr><td> <b>NewKendraStorageCapacityUnits</b> </td><td> <code>0</code> </td><td>Additional storage capacity units for the new Amazon Kendra index to be created for this use case. Only applies if <b>ExistingKendraIndexId</b> is not supplied, see <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_CapacityUnitsConfiguration.html">CapacityUnitsConfiguration</a>.<br />Note: Only relevant if <b>RAGEnabled</b> is <code>true</code> and <b>KnowledgeBaseType</b> is <code>Kendra</code>.</td></tr>
  <tr><td> <b>NewKendraIndexEdition</b> </td><td> <i>(Optional input)</i> </td><td>The edition of Amazon Kendra to use for the new Amazon Kendra index to be created for this use case. Only applies if <b>ExistingKendraIndexId</b> is not supplied, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html#kendra-editions">Amazon Kendra Editions</a>.<br />Note: Only relevant if <b>RAGEnabled</b> is <code>true</code> and <b>KnowledgeBaseType</b> is <code>Kendra</code>.</td></tr>
  <tr><td> <b>BedrockKnowledgeBaseId</b> </td><td> <i>(Optional input)</i> </td><td>ID of the bedrock knowledge base to use in a RAG use case. Cannot be provided if <b>ExistingKendraIndexId</b> or <b>NewKendraIndexName</b> are provided.<br />Note: Only relevant if <b>RAGEnabled</b> is <code>true</code> and <b>KnowledgeBaseType</b> is <code>Bedrock</code>.</td></tr>
  <tr><td> <b>VpcEnabled</b> </td><td> <code>No</code> </td><td>Should the stacks resources be deployed within a VPC.</td></tr>
  <tr><td> <b>CreateNewVpc</b> </td><td> <code>No</code> </td><td>Select <code>Yes</code>, if you want the solution to create a new VPC for you and be used for this use case.<br />Note: Only relevant if <b>VpcEnabled</b> is <code>Yes</code>.</td></tr>
  <tr><td> <b>IPAMPoolId</b> </td><td> <i>(Optional input)</i> </td><td>If you want to assign the CIDR range using Amazon VPC IP Address Manager, provide the IPAM pool Id to use.<br />Note: Only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>ExistingVpcId</b> </td><td> <i>(Optional input)</i> </td><td>VPC ID of an existing VPC to be used for the use case.<br />Note: Only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>ExistingPrivateSubnetIds</b> </td><td> <i>(Optional input)</i> </td><td>Comma separated list of subnet IDs of existing private subnets to be used to deploy the Lambda function.<br />Note: Only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>ExistingSecurityGroupIds</b> </td><td> <i>(Optional input)</i> </td><td>Comma separated list of security groups of the existing VPC to be used for configuring Lambda functions.<br />Note: Only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>VpcAzs</b> </td><td> <i>(Optional input)</i> </td><td>Comma separated list of AZs in which subnets of the VPCs are created<br />Note: Only relevant if <b>VpcEnabled</b> is <code>Yes</code> and <b>CreateNewVpc</b> is <code>No</code>.</td></tr>
  <tr><td> <b>UseInferenceProfile</b> </td><td> <code>No</code> </td><td>If the model configured is Bedrock, you can indicate if you are using Bedrock Inference Profile. This will ensure that the required IAM policies will be configured during stack deployment. For more details, refer to the following https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html</td></tr>
  <tr><td> <b>DeployUI</b> </td><td>Yes</td><td>Select the option to deploy the frontend UI for this deployment. Selecting No, will only create the infrastructure to host the APIs, the authentication for the APIs, and backend processing.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 10-30 minutes.
