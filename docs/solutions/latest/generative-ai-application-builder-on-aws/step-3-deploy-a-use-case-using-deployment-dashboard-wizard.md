---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/step-3-deploy-a-use-case-using-deployment-dashboard-wizard.html
---

# Step 3: Deploy a use case using the Deployment dashboard wizard
<a name="step-3-deploy-a-use-case-using-deployment-dashboard-wizard"></a>

In the Deployment dashboard wizard, you must choose between the following:
+  [Text use case](#step-3a-deploy-a-text-use-case) - Deploys a chat application, with optional RAG capabilities
+  [Bedrock Agent use case](#step-3b-deploy-an-agent-use-case) - Uses Amazon Bedrock Agents to complete tasks or automate repeated workflows
+  [MCP Server](#step-3c-deploy-an-mcp-server-use-case) - Deploy and manage MCP servers with gateway or runtime methods
+  [Agent Builder](#step-3d-deploy-an-agent-builder-use-case) - Build and deploy custom agents on AgentCore with MCP integration and memory management
+  [Workflow Builder](#step-3e-deploy-a-workflow-use-case) - Orchestrate multiple Agent Builder agents using hierarchical delegation

 **Shows five options: Create Text use case, Create Bedrock Agent use case, Create MCP Server Use Case, Create Agent Builder Use Case, or Create Workflow Use Case.**

![deploy a use case](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/deploy-a-use-case.png)

## Step 3a: Deploy a Text use case
<a name="step-3a-deploy-a-text-use-case"></a>

This section provides instructions for deploying a Text use case.

### Select use case
<a name="select-use-case"></a>

When you choose **Create Text use case**, the UI opens the **Select use case** screen. Provide the following information:
+ Use case name.
+ Optional email address for the default user of the use case to be added to the Amazon Cognito user pool for the use case, and to be given permissions to interact with it.
+ Whether you want to deploy a UI with this use case. If you don’t want to deploy a UI with the use case, you can use the deployed API endpoints for use with your application.

### Use case details
<a name="use-case-details"></a>

The use case details step allows you to configure additional settings for your deployment.

By default, the Text use case creates and configures an Amazon Cognito user pool for you when the solution deploys the Deployment dashboard. The solution authenticates new use cases with a newly created client in the same user pool. However, you can provide an existing user pool ID and client ID in this step if you want to use your own Amazon Cognito user pool and client with the use case.

**Important**
Admin users have access to all deployed use cases when the Amazon Cognito user pool is created via the deployment wizard. If you provide your own user pool during the deployment, you must ensure that the admin has the permissions to access the deployed use cases.
You will also need to update the Allowed callback URLs and Allowed sign-out URLs in your App clients in Cognito. To do this:
Navigate to the [Cognito console](https://console.aws.amazon.com/cognito)
Choose **User Pools**.
Choose your user pool.
Choose **App Clients** on the left menu.
Choose the app client you want to modify.
Choose the **Login pages** tab.
Choose **Edit** and add your URLs.
Choose **Save changes**.
Additionally, if you need to add more users to a use case, refer to the [Managing Cognito user pool](customization-guide.md) section.

### Select network configuration
<a name="select-network-configuration"></a>

This wizard step allows you to deploy the use case with a pre-existing or new [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC). If selecting pre-existing VPC, you are required to provide a VPC ID, up to 16 subnet Ids and up to 5 security group IDs to use with this VPC. If you’re not using a pre-existing VPC, these settings will be configured for you.

### Select model
<a name="select-model"></a>

In the **Select model** step, you can choose your model provider from the dropdown menu. There are two options: **Bedrock** and **SageMaker**.

If you select **SageMaker**, you can create a SageMaker AI model endpoint in the SageMaker AI console and provide the input schema that the model expects and output JSONPath for the LLM response. You can refer to the [Using Amazon SageMaker AI as an LLM Provider](use-the-solution.md#using-amazon-sagemaker-ai-as-an-llm-provider) section and [SageMaker AI payload examples](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/tree/main/docs/sagemaker-payload-examples) provided in the solution’s GitHub repository.

If you select **Amazon Bedrock**, you will be presented with four options:
+  **Quick Start Models** - Get started quickly with a collection of models with different price/performance characteristics. Recommended for building your first apps. This option allows you to select a model name from the provided list.
+  **Other Foundation Models** - Access the full range of foundation models with different capabilities and specializations. This option allows you to enter the model ID for your desired Bedrock on-demand foundation model.
+  **Inference Profiles** - Inference profiles leverage Bedrock’s cross-region inference to increase throughput and improve resiliency by routing your requests across multiple AWS Regions during peak utilization bursts. This option allows you to enter the ID of the inference profile you want to use.
+  **Provisioned Models** - Dedicated throughput capacity for production workloads requiring consistent performance. This option allows you to enter the ARN of the provisioned/custom model to use from Amazon Bedrock.

Model selection step also allows you to choose your advanced model settings. Refer to [Advanced LLM settings](advanced-llm-settings.md) for details on configuring Amazon Bedrock Guardrails, provisioned throughput for Amazon Bedrock, and additional model parameters.

 **Cross-region inference**

Cross-region inference helps Amazon Bedrock users to seamlessly manage unplanned traffic bursts by using compute across different AWS Regions. To use cross-region inference, you need the *inference profile*. An inference profile is an abstraction over an on-demand pool of resources from a configured set of AWS Regions. It can route your inference request, originating from your source Region, to another Region configured in that pool. This allows traffic distribution across multiple AWS Regions. This helps enable higher throughput and enhanced resilience during periods of peak demands.

Inference profiles are named after the model and Regions that they support. You must call an inference profile from one of the Regions that it includes. For example, as shown in the following table, the inference profile ID `us.anthropic.claude-3-haiku-20240307-v1:0` allows distribution of traffic over `us-east-1` and `us-west-2` Regions of the model you choose. Certain models are only available with an inference profile in a particular Region.

| Inference profile | Inference profile ID | Regions included |
| --- | --- | --- |
| US Anthropic Claude 3 Haiku |  `us.anthropic.claude-3-haiku-20240307-v1:0`  | US East (N. Virginia) (`us-east-1`)<br />US West (Oregon) (`us-west-2`) |

If you want to use an inference profile ID instead of a model ID, then you must identify the appropriate inference profile ID. See [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html) in the *Amazon Bedrock User Guide* for more information. In the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock), the cross-region inference option in the left navigation menu provides these inference profile IDs.

After you identify the inference profile ID to use, you can use this during the **Select model** stage by performing the following steps:

1. Select **Amazon Bedrock** as the model provider.

1. Select the **Inference Profiles** radio button option.

1. Enter your inference profile ID in the text box that appears.

Refer to [Improve resilience with cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) in the *Amazon Bedrock User Guide* for more details on inference profiles.

### Select knowledge base
<a name="select-knowledge-base"></a>

If you’re looking to deploy a non-Retrieval Augmented Generation (RAG) use case, you can skip this step.

However, if you wish to enable RAG as a part of your deployment, you can now provide either a pre-configured *Amazon Kendra Index Id* or an *Amazon Bedrock Knowledge Base ID*. You can also create a new Amazon Kendra Index for use with the solution. The solution currently supports Amazon Kendra and Amazon Bedrock Knowledge Bases as knowledge bases for your RAG-based use case deployment.

Refer to the [Configuring a Knowledge Base](configuring-a-knowledge-base.md) section for guidelines on ingesting data into the knowledge base for use with your RAG-based deployment.

#### Advanced RAG configurations
<a name="advanced-rag-configurations"></a>

The wizard allows you to select advanced options for use with your RAG deployment such as the **number of documents to retrieve** each time a query is sent to your knowledge base, a **static text response** from the LLM when no documents are found in the knowledge base, whether you wish to **display document sources** with your LLM response for sanity checks, etc. You can additionally also configure knowledge base specific configurations for Amazon Kendra such as [Role-based Access Control (RBAC)](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control.html), or [Override Search Type](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) when using Amazon OpenSearch Serverless with Amazon Bedrock Knowledge Bases. Refer to the [Advanced Knowledge Base settings](advanced-knowledge-base-settings.md) section for more details on these advanced settings.

**Note**
Your knowledge base must be in the same account and Region as the deployed Deployment dashboard and use case stacks.

#### Select prompts and token limits
<a name="select-prompts-and-token-limits"></a>

In this step, you can configure your prompt for use with the LLM. Prompts may require placeholders such as `{input}`, `{history}` and `{context}`. These placeholders instruct the LLM on where to draw user input, conversation history, and information retrieved from the knowledge base from.
+ For Bedrock model provider, the system prompt must be provided which has no restrictions for a non-RAG use-case. The disambiguation prompt for Bedrock model provider however, requires a minimum of two placeholders - `{input}` and `{history}`
+ For SageMaker model provider, system and disambiguation prompts, both require a minimum of two placeholders - `{input}` and `{history}`.
+ For RAG use cases, for each model provider, the `{context}` placeholder is additionally required.

For more information, see [Configuring your prompts](configuring-your-prompts.md). You can also refer to the [Tips for managing model token limits](tips-for-managing-model-token-limits.md) section while selecting token limit sizes for your prompts.

#### Enable multimodal input
<a name="enable-multimodal-input"></a>

This step allows you to enable multimodal input capabilities for your use case. When enabled, users can upload and send images and documents along with their text queries.

 **Supported file types and constraints:**
+  **Images:** Up to 20 images per message. Each image must be no more than 3.75 MB in size and 8,000 px in height and width. Supported formats: png, jpeg, gif, webp
+  **Documents:** Up to 5 documents per message. Each document must be no more than 4.5 MB in size. Supported formats: pdf, csv, doc, docx, xls, xlsx, html, txt, md

 **How to use multimodal input:**

1. Enable the **MultimodalEnabled** parameter during use case deployment

1. In the chat interface, users can upload files in two ways:
   + Clicking the upload button in the chat input box, or
   + Dragging and dropping files directly into the chat interface

1. Files are uploaded to Amazon S3 and processed by the selected model

1. Uploaded files are automatically deleted after 48 hours

 **File status tracking:**

DevOps users can monitor file metadata in DynamoDB, which includes upload time and processing status. Files can have the following statuses:
+  **pending** - File upload has been initiated but not yet completed. This is the initial status when a presigned URL is generated.
+  **uploaded** - File has been successfully uploaded to S3 and is ready for processing by the model.
+  **deleted** - File has been deleted by the user and should no longer be accessible for processing.
+  **invalid** - File failed validation checks (for example, file type mismatch or security validation failure).

Files in **pending** status that are never uploaded will be automatically cleaned up when their TTL expires. Only files with **uploaded** status can be processed by the model.

The S3 multimodal bucket and DynamoDB metadata table is available in the Deployment Dashboard outputs with the keys `MultimodalDataBucketName` and `MultimodalDataMetadataTable`, respectively.

**Note**
Not all models support multimodal input. Ensure your selected model supports image and document processing before enabling this feature. Refer to the [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) documentation to check which model support Image as an input modality.

**Important**
Files uploaded by users are stored in Amazon S3 with a 48-hour lifecycle policy. Metadata about uploaded files is stored in Amazon DynamoDB with a 24-hour TTL for conversation history.

#### Review and deploy
<a name="review-and-deploy"></a>

After this step, review the settings you selected and choose **Deploy Use Case**. The new use case then deploys and becomes visible in your Deployment dashboard view to manage further.

### Step 3b: Deploy a Bedrock Agent use case
<a name="step-3b-deploy-an-agent-use-case"></a>

The Bedrock Agent use case provides a powerful and secure mechanism for invoking Amazon Bedrock Agents within your use cases. This feature allows developers to seamlessly integrate the capabilities of AI-powered autonomous agents that can orchestrate and execute multi-step tasks across various foundation models, data sources, software applications, and user conversations while maintaining robust security measures.

#### Prerequisites
<a name="step-3b-prerequisites"></a>

Before creating an Amazon Bedrock agent, ensure that you have the following:

1. The AWS account where Generative AI Application Builder on AWS is deployed, with an access to the Amazon Bedrock console.

1. Appropriate IAM permissions to create and manage Amazon Bedrock Agents.

#### Creating an Amazon Bedrock Agent
<a name="creating-an-amazon-bedrock-agent"></a>

Refer to the [Create and configure agent manually](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html) in the *Amazon Bedrock User Guide* for detailed instructions on creating an agent. You can configure options such as:
+ Instructions (prompts) for your agent
+ Knowledge base, which is used to look up additional information based on user’s input
+ Agent’s memory to allow agents to remember information across multiple sessions (for a maximum of 30 days)

After you successfully create an Amazon Bedrock agent, you can proceed to the Generative AI Application Builder on AWS Bedrock Agent use case wizard flow. To do so, choose **Deploy a new use case** on the Deployment dashboard and select **Create Bedrock Agent Use Case**. Follow the wizard and use the following steps to configure the use case.

#### Select use case
<a name="select-use-case-1"></a>

This step is the same as the Text use case [described previously](#select-use-case).

#### Select network configuration
<a name="select-network-configuration-1"></a>

This step is the same as the Text use case [described previously](#select-network-configuration)

#### Select agent
<a name="select-agent"></a>

In this step, you must provide the **Agent ID** and **Alias ID** of the Amazon Bedrock agent that you created.

### Step 3c: Deploy an MCP Server use case
<a name="step-3c-deploy-an-mcp-server-use-case"></a>

The MCP (Model Context Protocol) Server use case enables you to deploy and manage MCP servers that can be integrated with AI models and agents. MCP servers provide a standardized way to expose tools, resources, and capabilities to AI applications. You can either create MCP servers from existing Lambda functions and APIs, or host custom MCP servers using container images.

#### Prerequisites
<a name="step-3c-prerequisites"></a>

Before deploying an MCP Server use case, ensure that you have the following:

1. The AWS account where Generative AI Application Builder on AWS is deployed.

1. Appropriate IAM permissions to create and manage Amazon Bedrock AgentCore resources.

1. Depending on your chosen creation method:
   +  **For Gateway method (Lambda/API/MCP Server)**: Lambda functions, API endpoints with their corresponding schema files (JSON format for Lambda, OpenAPI/Smithy for APIs), or MCP Server URL endpoints
   +  **For Runtime method (ECR)**: A Docker container image pushed to Amazon ECR containing your MCP server implementation

#### MCP Server creation methods
<a name="mcp-server-creation-methods"></a>

The solution supports two methods for creating MCP servers:

 **Create from Lambda, API, or MCP Server (Gateway method)**

This method creates an MCP gateway that wraps existing Lambda functions, REST APIs, or external MCP servers, making them accessible as MCP tools. The gateway handles protocol translation between MCP and your existing services.
+  **Lambda targets**: Integrate existing Lambda functions by providing the function ARN and a JSON schema file describing the function’s input/output format
+  **OpenAPI targets**: Integrate REST APIs using OpenAPI specifications (JSON or YAML format) with support for OAuth 2.0 or API Key authentication
+  **Smithy targets**: Integrate APIs defined using Smithy model files (.smithy or .json format)
+  **MCP Server targets**: Connect directly to external MCP servers via URL endpoints, allowing integration of existing MCP servers without deploying new infrastructure

You can configure multiple targets (up to 10) within a single MCP gateway, each representing a different tool or capability.

 **Hosting from ECR Image (Runtime method)**

This method deploys a containerized MCP server from an Amazon ECR image. Use this approach when you have a custom MCP server implementation that needs to run as a standalone service.
+ Provide the ECR image URI (must include a tag, e.g., `:latest` or `:v1.0.0`)
+ Optionally configure environment variables to pass configuration to your container
+ The container must implement the MCP protocol and expose the required endpoints

#### Deploying an MCP Server
<a name="deploying-an-mcp-server"></a>

To deploy an MCP Server use case, choose **Deploy a new use case** on the Deployment dashboard and select **Create MCP Server Use Case**. Follow the wizard and use the following steps to configure the use case.

##### Select use case
<a name="select-use-case-2"></a>

This step is the same as the Text use case [described previously](#select-use-case).

##### Select network configuration
<a name="select-network-configuration-2"></a>

Currently only public access is enabled and VPC is not supported for netwrok configuation.

##### Create MCP Server
<a name="create-mcp-server"></a>

In this step, you configure your MCP server deployment:

 **MCP server creation method**

Choose between the two creation methods:
+  **Create from Lambda, API, or MCP Server**: Create an MCP gateway from existing Lambda functions, API specifications, or external MCP server endpoints
+  **Hosting from ECR Image**: Deploy a custom MCP server from a container image

**Note**
The creation method cannot be changed after deployment. If you need to switch methods, you must deploy a new MCP Server use case.

 **Gateway Configuration (for Lambda/API/MCP Server method)**

If you selected the Gateway method, configure one or more targets:

1.  **Target name** (required): A friendly name to identify this target configuration

1.  **Target description** (optional): A brief description of what this target does

1.  **Target Type**: Select the type of target to configure:
   +  **Lambda**: For AWS Lambda functions
   +  **OpenAPI**: For REST APIs with OpenAPI specifications
   +  **Smithy**: For APIs with Smithy model definitions
   +  **MCP Server**: For direct connection to external MCP servers via URL endpoints

1.  **Schema File** (required): Upload the schema file that describes your target:
   + For Lambda: JSON schema file describing input/output format. For details on creating Lambda tool schemas, see [Lambda tool schema](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-lambda.html#gateway-lambda-tool-schema) in the *Amazon Bedrock AgentCore Developer Guide*.
   + For OpenAPI: OpenAPI specification file (JSON or YAML). For details on OpenAPI schema requirements, see [OpenAPI schema](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-schema-openapi.html) in the *Amazon Bedrock AgentCore Developer Guide*.
   + For Smithy: Smithy model file (.smithy or .json). For details on building Smithy targets, see [Building Smithy targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-smithy-targets.html) in the *Amazon Bedrock AgentCore Developer Guide*.

1.  **Lambda Function ARN** (required for Lambda targets): The ARN of the Lambda function to integrate

1.  **MCP Server URL** (required for MCP Server targets): The URL endpoint of the external MCP server to connect to. The URL must be properly encoded and the MCP server must support tool capabilities with MCP protocol versions 2025-06-18. For more information, see [MCP servers targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-MCPservers.html) in the *Amazon Bedrock AgentCore Developer Guide*.

1.  **Outbound Authentication** (required for OpenAPI targets): Configure authentication for REST API calls:
   +  **Authentication Type**: Choose OAuth 2.0 or API Key
   +  **Outbound Auth Provider ARN**: The ARN of the credential provider in Amazon Bedrock AgentCore token vault
   +  **Additional configurations**: Depending on authentication type:
     + For OAuth 2.0: Configure scopes and custom parameters
     + For API Key: Specify location (header or query parameter), parameter name, and optional prefix

You can add multiple targets (up to 10) by choosing **Add another target**. Each target represents a separate tool or capability exposed by your MCP server.

 **ECR Configuration (for ECR Image method)**

If you selected the Runtime method, provide:

1.  **ECR Image URI** (required): The full URI of your Docker image in Amazon ECR
   + Format: `account-id.dkr.ecr.region.amazonaws.com/repository-name:tag`
   + The image must be in the same AWS Region as your deployment
   + A tag is required (e.g., `:latest`, `:v1.0.0`)

1.  **Environment variables** (optional): Configure key-value pairs to pass to your container at runtime
   + Use these to provide configuration, credentials, or custom flags
   + You can add up to 10 environment variables

##### Review and deploy
<a name="review-and-deploy-mcp"></a>

After configuring your MCP server, review the settings you selected and choose **Deploy Use Case**. The new MCP Server use case then deploys and becomes visible in your Deployment dashboard view for further management.

**Note**
MCP Server deployments create resources in Amazon Bedrock AgentCore, including gateways, runtimes, and workload identities. These resources are automatically managed by the solution and will be cleaned up when you delete the use case.

### Step 3d: Deploy an Agent Builder use case
<a name="step-3d-deploy-an-agent-builder-use-case"></a>

The Agent Builder enables you to create, configure, and deploy production-ready AI agents on Amazon Bedrock AgentCore. This feature provides full control over agent behavior through system prompts, model selection, MCP server integration, and memory management.

The deployment process is primarily the same as for a Text use case, with some notable differences.

#### Select use case
<a name="select-use-case-2"></a>

This step is the same as the Text use case [described previously](#select-use-case).

#### Use case details
<a name="use-case-details-2"></a>

This step is the same as the Text use case [described previously](#select-use-case).

#### Configure agent
<a name="configure-agent"></a>

In this step, you configure the core agent settings including system prompt, available MCP servers/Strands tools, and memory.

 **System Prompt**

The system prompt defines the agent’s behavior, personality, and capabilities. You can:
+ Edit the default system prompt template
+ Use the **Reset to default** button to restore the original template
+ Include instructions for tool usage and response formatting

 **MCP Server Integration (Optional)**

Configure Model Context Protocol servers to provide your agent with access to enterprise tools and data:

1. Select from available MCP servers in the dropdown

1. Review available out of the box tools that will be accessible to the agent

**Note**
MCP servers must be configured and accessible before deployment. Refer to the MCP documentation for server setup instructions.

 **Memory Configuration**

Configure how the agent maintains context and knowledge:
+  **Short-term Memory**: Enabled by default for all agents. Maintains conversation context within sessions.
+  **Long-term Memory**: Toggle to enable extraction and storage of insights across sessions. Uses AgentCore Memory with semantic memory strategy.

#### Review and deploy
<a name="review-and-deploy-2"></a>

After this step, review the settings you selected and choose **Deploy Use Case**. The Agent Builder deployment typically completes in 10-15 minutes. The new use case then becomes visible in your Deployment dashboard view to manage further.

### Step 3e: Deploy a Workflow use case
<a name="step-3e-deploy-a-workflow-use-case"></a>

The Workflow Builder enables you to create supervisor agents that orchestrate multiple Agent Builder agents using the Agents as Tools delegation pattern. This feature allows you to build complex multi-agent workflows by reusing existing Agent Builder deployments.

The deployment process follows a similar pattern to Agent Builder, with additional steps for agent discovery and selection.

#### Select use case
<a name="select-use-case-3"></a>

This step is the same as the Text use case [described previously](#select-use-case).

#### Use case details
<a name="use-case-details-3"></a>

This step is the same as the Text use case [described previously](#select-use-case).

#### Configure supervisor agent
<a name="configure-supervisor-agent"></a>

In this step, you configure the supervisor agent that will coordinate the specialized Agent Builder agents.

 **System Prompt**

The system prompt defines how the supervisor agent delegates work to specialized agents. You can:
+ Edit the default system prompt template
+ Include instructions for agent selection and delegation
+ Define how to aggregate results from multiple agents
+ Use the **Reset to default** button to restore the original template

**Note**
The system prompt should clearly describe when and how to use each specialized agent. Agent descriptions are critical for proper delegation.

 **Model Selection**

Select the foundation model for the supervisor agent. The supervisor agent uses this model to:
+ Understand user requests
+ Select appropriate specialized agents
+ Coordinate agent execution
+ Aggregate and format responses

#### Select specialized agents
<a name="select-specialized-agents"></a>

In this step, you select which Agent Builder agents the supervisor can delegate work to.

 **Adding Agents**

1. Click **Add Agent** to open the agent selection dialog

1. Select one or more Agent Builder agents from the list

1. Review the agent descriptions that will be provided to the supervisor

1. Confirm the selection

**Note**
Workflows require at least 1 Agent Builder use case as a specialized agent
All specialized agents must be successfully deployed before creating the workflow

#### Review and deploy
<a name="review-and-deploy-3"></a>

Review the workflow configuration including:
+ Supervisor agent system prompt and model
+ List of specialized agents
+ Memory settings

Choose **Deploy Use Case**. The Workflow deployment typically completes in 15-20 minutes. The new workflow becomes visible in your Deployment dashboard view to manage further.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
