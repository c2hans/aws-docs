---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/step-1-launch-the-stack.html
---

# Step 1: Launch the stack
<a name="step-1-launch-the-stack"></a>

This automated AWS CloudFormation template deploys the QnABot on AWS guidance in the AWS Cloud. You must set up an AWS account before launching the stack.

**Note**
You are responsible for the cost of the AWS services used while running this guidance. For more details, see the [Cost](cost.md) section in this guide, and reference to the pricing webpage for each AWS service used in this guidance.

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `qnabot-on-aws-main.template` AWS CloudFormation template.

    **Launch guidance**

    [![Launch Stack](https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/launch-solution.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create?templateURL=https://solutions-reference.s3.amazonaws.com/qnabot-on-aws/latest/qnabot-on-aws-main.template&redirectId=ImplementationGuide)

   The template launches in the US East (N. Virginia) Region by default. To launch the guidance in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This guidance uses Amazon Lex, which is not currently available in all AWS Regions. You must launch this guidance in an AWS Region where Amazon Lex is available. For the most current availability by Region, see the [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) list.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your guidance stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this guidance template and modify them as necessary. This guidance uses the following default values.
**Note**
Amazon Lex V1 has been deprecated and removed from QnABot v6.1.0. Amazon Lex V2 is used by default.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Authentication</b> </td><td></td><td></td></tr>
  <tr><td> <b>Email</b> </td><td> <code> &lt;Requires input&gt; </code> </td><td>Email address for the admin user. This email address will receive a temporary password to access the QnABot on AWS content designer.</td></tr>
  <tr><td> <b>Username</b> </td><td> <code> &lt;Requires input&gt; </code> </td><td>This username will be used to sign in to the QnABot on AWS content designer console and client if the client is private.</td></tr>
  <tr><td> <b>PublicorPrivate</b> </td><td> <code>PUBLIC</code> </td><td>Choose whether access to the QnABot on AWS client should be publicly available or restricted to users in the QnABot in the Cognito user pool.</td></tr>
  <tr><td> <b>Language</b> </td><td> <code>English</code> </td><td>The primary language for your QnABot on AWS deployment. NOTE: Selecting <code>non-English</code> might correspond with limited functionalities.</td></tr>
  <tr><td> <b>Amazon Kendra Integration </b> </td><td></td><td></td></tr>
  <tr><td> <b>Amazon KendraWebPageIndexId</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>ID of the Amazon Kendra index to use for the web crawler. A custom data source will automatically be added to the specified index.</td></tr>
  <tr><td> <b>Amazon KendraFaqIndexId</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>ID of the Amazon Kendra index to use for syncing OpenSearch questions and answers.</td></tr>
  <tr><td> <b>AltSearchAmazon KendraIndexes</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>A comma separated string value specifying IDs of one or more Amazon Kendra indexes to be used for Amazon Kendra fallback.</td></tr>
  <tr><td> <b>AltSearchAmazon KendraIndexAuth</b> </td><td> <code>FALSE</code> </td><td>Choosing <code>TRUE</code> enables the guidance to send an OpenID token to Amazon Kendra index(es) to limit results to which the user is entitled.</td></tr>
  <tr><td> <b>Amazon OpenSearch Service </b> </td><td></td><td></td></tr>
  <tr><td> <b>OpenSearchDedicatedMasterNodes</b> </td><td> <code>DISABLED</code> </td><td>Enable OpenSearch add dedicated master nodes to increase cluster stability. Please note that deploying additional nodes will increase cost, see - https://aws.amazon.com/opensearch-service/pricing/.</td></tr>
  <tr><td> <b>OpenSearchMasterNodeInstanceType</b> </td><td> <code>m6g.large.search</code> </td><td>Required when OpenSearchDedicatedMasterNodes is ENABLED. OpenSearch instance type for master nodes in the domain. Default recommendation for production deployments is <code>m6g.large.search</code> (see https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html for other options).</td></tr>
  <tr><td> <b>OpenSearchMasterNodeCount</b> </td><td> <code>3</code> </td><td>Required when OpenSearchDedicatedMasterNodes is ENABLED. Number of dedicated master nodes to add in your Amazon OpenSearch Service domain. 3 is the minimum default value. See - https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html#dedicatedmasternodes-number.</td></tr>
  <tr><td> <b>OpenSearchNodeInstanceType</b> </td><td> <code>m6g.large.search</code> </td><td>OpenSearch instance type for data nodes in the domain. Default recommendation for production deployments is <code>m6g.large.search</code>. For details, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html">Supported instance types in Amazon OpenSearch Service</a> in the <i>Amazon OpenSearch Service Developer Guide</i>.</td></tr>
  <tr><td> <b>OpenSearchNodeCount</b> </td><td> <code>4</code> </td><td>Number of data nodes in Amazon OpenSearch Service domain. We recommend 4 for fault-tolerant production deployments.</td></tr>
  <tr><td> <b>OpenSearchEBSVolumeSize</b> </td><td> <code>10</code> </td><td>The size in GB of the OpenSearch node instances. <code>10</code> is the minimum default volume size.</td></tr>
  <tr><td> <b>OpenSearchDashboardsRetentionMinutes</b> </td><td> <code>43200</code> </td><td>To conserve storage in Amazon OpenSearch Service, metrics and feedback data used to populate the OpenSearch Dashboards are automatically deleted after this period (default <code>43200</code> minutes = 30 days). Monitor the free storage space for your OpenSearch Service domain to ensure that you have sufficient space available to store data for the desired retention period.</td></tr>
  <tr><td> <b>OpenSearchFineGrainAccessControl</b> </td><td> <code>TRUE</code> </td><td>Set to <code>FALSE</code> if fine-grained access control does not need to be enabled by default. Once fine-grained access control is enabled, it cannot be disabled. Note that it may take an additional 30-60 minutes for OpenSearch Service to apply these settings to the OpenSearch domain after the stack has been deployed. For details, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html">Fine-grained access control in Amazon OpenSearch Service</a> in the <i>Amazon OpenSearch Service Developer Guide</i>.</td></tr>
  <tr><td> <b>Amazon LexV2</b> </td><td></td><td></td></tr>
  <tr><td> <b>LexV2BotLocaleIds</b> </td><td> <code>en_US,es_US,fr_CA</code> </td><td>Languages for QnABot on AWS voice interaction using LexV2. Specify as a comma-separated list of valid locale IDs without empty spaces. For details, see the <a href="https://github.com/aws-solutions/aws-qnabot/blob/main/source/docs/multilanguage_support/README.md">Supported languages</a> section in the GitHub repository.</td></tr>
  <tr><td> <b>Semantic Search and Embeddings</b> </td><td></td><td></td></tr>
  <tr><td> <b>EmbeddingsApi</b> </td><td> <code>DISABLED</code> </td><td>Enable QnABot semantics search using embeddings from a pre-trained LLM. Selecting <code>LAMBDA</code> allows for configuration with other models. Disabled by default.</td></tr>
  <tr><td> <b>EmbeddingsLambdaArn</b> </td><td> <code> &lt;Requires input&gt; </code> </td><td>Required when <b>EmbeddingsApi</b> is set to <code>LAMBDA</code>. Provide the ARN for a Lambda function that takes JSON <code>{"inputtext":"string"}</code>, and returns JSON <code>{"embedding":[…​]}.</code> </td></tr>
  <tr><td> <b>EmbeddingsLambdaDimensions</b> </td><td> <code>1536</code> </td><td>Required when <b>EmbeddingsApi</b> is set to <code>LAMBDA</code>. Provides the number of dimensions for embeddings returned from the Lambda function.</td></tr>
  <tr><td> <b>EmbeddingsBedrockModelId</b> </td><td> <code>amazon.nova-2-multimodal-embeddings-v1</code> </td><td>Required when <b>EmbeddingsApi</b> is set to <code>BEDROCK</code>. Select the embeddings model from the list of available models. Check account and Region availability and ensure that the model is enabled in the Amazon Bedrock console before deploying. For details, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html">Model support by AWS Region</a> in the <i>Amazon Bedrock User Guide</i>.</td></tr>
  <tr><td> <b>LLM Integration</b> </td><td></td><td></td></tr>
  <tr><td> <b>LLMApi</b> </td><td> <code>DISABLED</code> </td><td>Enable question disambiguation and generative responses using an LLM model. Selecting the <code>LAMBDA</code> option allows for configuration with other LLMs.</td></tr>
  <tr><td> <b>LLMBedrockModelId</b> </td><td> <code>global.anthropic.claude-haiku-4-5-20251001-v1:0</code> </td><td>Required when <b>LLMApi</b> is set to <code>BEDROCK</code>. Provide a valid model or inference profile ID. QnABot supports all <code>TEXT</code> input/output modality-based based Bedrock foundation models or inference profiles. Check account and Region availability and ensure that the model is enabled in the Amazon Bedrock console before deploying.</td></tr>
  <tr><td> <b>LLMLambdaArn</b> </td><td> <code> &lt;Requires input&gt; </code> </td><td>Required if <b>LLMApi</b> is set to <code>LAMBDA</code>. Provide the ARN for a Lambda function that takes JSON <code>{"prompt":"string", "settings":{key:value,..}}</code>, and returns JSON <code>{"generated_text":"string"}</code>.</td></tr>
  <tr><td> <b>BedrockKnowledgeBaseId</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>ID of an existing Amazon Bedrock knowledge base. This setting enables the use of Amazon Bedrock knowledge bases as a fallback mechanism when a match is not found in OpenSearch.</td></tr>
  <tr><td> <b>BedrockKnowledgeBaseModel</b> </td><td> <code>global.anthropic.claude-haiku-4-5-20251001-v1:0</code> </td><td>Required if <b>BedrockKnowledgeBaseId</b> is not empty. Provide a valid model or inference profile ID. Sets the preferred LLM model to use with the Amazon Bedrock knowledge base. QnABot supports all <code>TEXT</code> input/output modality-based based Bedrock foundation models or inference profiles. Check account and Region availability and ensure that the model is enabled in the Amazon Bedrock console before deploying.</td></tr>
  <tr><td> <b>Other parameters</b> </td><td></td><td></td></tr>
  <tr><td> <b>InstallLexResponseBots</b> </td><td> <code>TRUE</code> </td><td>Configures your chatbot to ask questions and process your end user’s answers for surveys and quizzes. If the Elicit Response feature is not needed, choose <code>FALSE</code> to skip the installation of the sample Lex response bots. For details, see <a href="https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/configuring-the-chatbot-to-ask-the-questions-and-use-response-bots.html">Configuring the chatbot to ask the questions and use response bots</a>.</td></tr>
  <tr><td> <b>FulfillmentConcurrency</b> </td><td> <code>0</code> </td><td>The amount of provisioned concurrency for the <code>Fulfillment</code> Lambda function. For details, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html">Configuring reserved concurrency</a>.</td></tr>
  <tr><td> <b>VPCSubnetIdList</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>Set to a comma delimited list of subnet IDs belonging to the target VPC you want to deploy QnABot on AWS in.</td></tr>
  <tr><td> <b>VPCSecurityGroupIdList</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>Set to a comma delimited list of security group IDs used by QnABot when deployed within a VPC.</td></tr>
  <tr><td> <b>XraySetting</b> </td><td> <code>FALSE</code> </td><td>Configure Lambda functions with <a href="https://aws.amazon.com/xray/">AWS X-Ray</a> enabled.</td></tr>
  <tr><td> <b>LogRetentionPeriod</b> </td><td> <code>0</code> </td><td>The number of days that logs are kept before expiring. By default, logs never expire.</td></tr>
  <tr><td> <b>EnableStreaming</b> </td><td> <code>FALSE</code> </td><td>Configures your QnABot to use streaming responses. For details, see <a href="https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/llm-streaming-responses.html">Enabling Streaming Responses from QnABot</a> </td></tr>
  <tr><td> <b>AlexaSkillIds</b> </td><td> <i>&lt;Optional input&gt;</i> </td><td>One or more Alexa Skill IDs to turn on Alexa integration. Enter as a comma-separated list with no spaces (for example, <code>amzn1.ask.skill.xxx-xxx-xxx,amzn1.ask.skill.yyy-yyy-yyy</code>). Leave blank to keep Alexa access turned off. You can add up to 30 skill IDs. For details, see <a href="step-4-interact-with-the-chatbot.md#getting-answers-using-amazon-alexa">Getting answers using Amazon Alexa</a>.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, keep the default settings.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template might create IAM resources with custom names, and the box acknowledging that AWS CloudFormation might require the CAPABILITY\_AUTO\_EXPAND capability.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 30-45 minutes.

When the stack deployment is complete, the **Output** tab displays the following information:
+  **ContentDesignerURL** - URL to launch the content designer UI
+  **ClientURL** - URL to launch the end user client webpage
+  **CloudWatchDashboardURL** - URL to launch the CloudWatch dashboard for monitoring
+  **FeedbackSNSTopic** - Topic name to allow feedback notifications
+  **LexV2 bot information** - Data for configuring integration with contact centers and web clients.

**Note**
In addition to the primary AWS Lambda functions, this guidance includes the `solution-helper` Lambda function, which runs only during initial configuration or when resources are updated or deleted.
When you run this guidance, the `solution-helper` Lambda function is not regularly active; however, you must not delete it because it is necessary to manage associated resources.
