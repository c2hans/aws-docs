---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides reference implementation architecture diagrams for the components deployed with this solution.

## Architecture diagrams
<a name="architecture-diagram"></a>

To support multiple use cases and business needs, this solution provides six AWS CloudFormation templates:

1.  **Deployment dashboard** - The Deployment dashboard is a web interface that serves as a management console for admin users to view, manage, and create their use cases. This dashboard enables customers to rapidly experiment, iterate, and productionize various AI/ML workloads leveraging LLMs.

1.  **Text use case** - The Text use case enables users to experience a natural language interface using generative AI. This use case can be integrated into new or existing applications, and is deployable through the Deployment dashboard or independently through a provided URL.

1.  **Bedrock Agent use case** - The Bedrock Agent use case enables the use of existing Bedrock Agents to complete tasks or automate repeated workflows.

1.  **MCP Server** - The MCP Server use case enables deployment and management of Model Context Protocol servers that provide standardized tool and resource access to AI applications. Supports both gateway methods for wrapping existing Lambda functions, APIs, and external MCP servers, and runtime methods for deploying custom containerized MCP servers.

1.  **Agent Builder** - The Agent Builder enables creation and deployment of production-ready AI agents on Amazon Bedrock AgentCore with full configuration control, MCP server integration, and memory management capabilities.

1.  **Workflow Builder** - The Workflow Builder enables creation of supervisor agents that orchestrate multiple Agent Builder agents using the Agents as Tools delegation pattern for complex multi-agent workflows.

### Deployment dashboard
<a name="deployment-dashboard"></a>

 **Depicts Deployment dashboard architecture (when deployed with VPC option disabled)**

![deployment dashboard diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/deployment-dashboard-diagram.png)

 **Depicts Deployment dashboard architecture (when deployed with VPC option enabled)**

![deployment dashboard vpc arch diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/deployment-dashboard-vpc-arch-diagram.png)

**Note**
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1. Admin users log in to the Deployment Dashboard user interface (UI).

1.  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) delivers the web UI, which is hosted in an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket.

1.  [AWS WAF](https://aws.amazon.com/waf/) protects the APIs from attacks. This solution configures a set of rules called a web access control list (web ACL) that allows, blocks, or counts web requests based on configurable, user defined web security rules and conditions.

1. The web UI leverages a set of REST APIs that are exposed using [Amazon API Gateway](https://aws.amazon.com/api-gateway/).

1.  [Amazon Cognito](https://aws.amazon.com/cognito/) authenticates users and backs both the CloudFront web UI and API Gateway.

1.  [AWS Lambda](https://aws.amazon.com/lambda/) provides the business logic for the REST endpoints. This *backing* Lambda function manages and creates the necessary resources to perform use case deployments using [AWS CloudFormation](https://aws.amazon.com/cloudformation/).

1.  [Amazon DynamoDB](https://aws.amazon.com/dynamodb) stores the list of deployments.

1. When a new use case is created by the admin user, the *backing* Lambda function initiates a CloudFormation stack creation event for the requested use case.

1. All of the LLM configuration options provided by the admin user in the deployment wizard are saved in DynamoDB. The deployment uses this DynamoDB table to configure the LLM at runtime.

1. Using [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), this solution collects operational metrics from various services to generate custom dashboards that allow you to monitor the solution’s performance and operational health.

**Note**
If you choose to deploy this solution in an Amazon VPC, the data will be routed within your private network.
Although the Deployment dashboard can be launched in most AWS Regions, the deployed use cases have certain restrictions based on service availability. See [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions) for more details.

### Text use case
<a name="chat-use-case"></a>

 **Depicts Text use case architecture (when deployed with VPC option disabled)**

![text use case diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/text-use-case-diagram.png)

 **Depicts Text use case architecture (when deployed with VPC option enabled)**

![text use case vpc arch diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/text-use-case-vpc-arch-diagram.png)

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1. Admin users deploy the use case using the Deployment Dashboard. [Business users](concepts-and-definitions.md) log in to the use case UI.

1. CloudFront delivers the web UI which is hosted in an S3 bucket.

1. The web UI leverages a WebSocket integration built using API Gateway. The API Gateway is backed by a custom [Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) function, which returns the appropriate [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) policy based on the Amazon Cognito group the authenticating user belongs to. The policy is stored in DynamoDB.

1. Amazon Cognito authenticates users and backs both the CloudFront web UI and API Gateway.

1. Incoming requests from the business user are passed from API Gateway to an [Amazon SQS queue](https://aws.amazon.com/sqs/) and then to the *LangChain Orchestrator*. The *LangChain Orchestrator* is a collection of Lambda functions and layers that provide the business logic for fulfilling requests coming from the business user. The queue enables the asynchronous operation of the API Gateway to Lambda integration. The queue passes connection information to the Lambda functions which will then post results directly back to the API Gateway websocket connection to support long running inference calls.

1. The *LangChain Orchestrator* uses Amazon DynamoDB to get the configured LLM options and necessary session information (such as the chat history).

1. If the deployment has a knowledge base enabled, then the *LangChain Orchestrator* leverages [Amazon Kendra](https://aws.amazon.com/kendra/) or [Knowledge Bases for Amazon Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) to run a search query to retrieve document excerpts.

1. Using the chat history, query, and context from the knowledge base, the *LangChain Orchestrator* creates the final prompt and sends the request to the LLM hosted on [Amazon Bedrock](https://aws.amazon.com/bedrock/) or [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/).

1. When the response comes back from the LLM, the *LangChain Orchestrator* streams the response back through the API Gateway WebSocket to be consumed by the client application.

1. Using Amazon CloudWatch, this solution collects operational metrics from various services to generate custom dashboards that allow you to monitor the deployment’s performance and operational health.

1. If feedback collection is enabled, a REST API endpoint, leveraging Amazon API Gateway is made available for the collection of user feedback.

1. The feedback backing lambda, augments the submitted feedback with additional use case specific metadata (e.g. model used) and stores the data in Amazon S3 for later analysis and reporting by the DevOps users.

**Note**
If you choose to deploy this solution in an Amazon VPC, the data will be routed to your private network.

### Bedrock Agent use case
<a name="agent-use-case"></a>

 **Depicts Bedrock Agent use case architecture (when deployed with VPC option disabled)**

![agent use case diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/agent-use-case-diagram.png)

 **Depicts Bedrock Agent use case architecture (when deployed with VPC option enabled)**

![agent use case vpc arch diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/agent-use-case-vpc-arch-diagram.png)

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1. Admin users deploy the use case using the Deployment Dashboard. [Business users](concepts-and-definitions.md) sign in to the use case UI.

1. CloudFront delivers the web UI which is hosted in an S3 bucket.

1. The web UI leverages a WebSocket integration built using API Gateway. The API Gateway is backed by a custom Lambda authorizer function, which returns the appropriate [AWS Identity and Access Management](https://aws.amazon.com/iam/)(IAM) policy based on the Amazon Cognito group the authenticating user belongs to. The policy is stored in DynamoDB.

1. Amazon Cognito authenticates users and backs both the CloudFront web UI and API Gateway.

1. Incoming requests from the business user are passed from API Gateway to an [Amazon SQS queue](https://aws.amazon.com/sqs/) and then to the AWS Lambda function. The queue enables the asynchronous operation of the API Gateway to Lambda integration. The queue passes connection information to the Lambda function which will then post results directly back to the API Gateway websocket connection to support long running inference calls.

1. The AWS Lambda function uses Amazon DynamoDB to get the use case configurations as needed

1. Using the user input and any relevant use case configurations, the AWS Lambda function builds and sends a request payload to the configured [Amazon Bedrock Agent](https://aws.amazon.com/bedrock/agents/) to fulfill the user intent.

1. When the response comes back from the Amazon Bedrock Agent, the Lambda function streams the response back through the API Gateway WebSocket to be consumed by the client application.

1. Using Amazon CloudWatch, this solution collects operational metrics from various services to generate custom dashboards that allow you to monitor the deployment’s performance and operational health.

1. If feedback collection is enabled, a REST API endpoint, leveraging Amazon API Gateway is made available for the collection of user feedback.

1. The feedback backing lambda, augments the submitted feedback with additional use case specific metadata and stores the data in Amazon S3 for later analysis and reporting by the DevOps users.

**Note**
If you choose to deploy this solution in an Amazon VPC, data will be routed within your private network.

### MCP Server use case
<a name="mcp-server"></a>

 **Depicts MCP Server use case architecture**

![mcp server use case diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/mcp-server-use-case-diagram.png)

The MCP Server use case enables deployment and management of Model Context Protocol servers on Amazon Bedrock AgentCore. MCP servers provide a standardized interface for AI applications to access tools, resources, and enterprise data sources.

The solution supports two deployment methods:
+  **Gateway method**: Wraps existing Lambda functions, REST APIs, or external MCP servers as MCP tools, handling protocol translation automatically
+  **Runtime method**: Deploys custom containerized MCP servers from Amazon ECR images

The high-level process flow for MCP Server deployment is as follows:

1. Admin users deploy the MCP Server use case using the Deployment Dashboard, selecting either Gateway or Runtime deployment method.

1. This action is authenticated with Amazon Cognito.

1. For the Gateway deployment, the solution creates an Amazon Bedrock AgentCore Gateway that transforms existing Lambda functions, APIs, or external MCP servers into MCP-compliant tools. For the Runtime deployment, the solution deploys containerized MCP servers on Amazon Bedrock AgentCore Runtime using provided ECR images.

1. Gateway deployments retrieve the necessary API/Lambda/Smithy schemas from their uploaded location in Amazon S3, or connect directly to MCP Server URL endpoints.

1. Runtime deployments retrieve the containerized MCP server provided by the user from Amazon Elastic Container Registry (ECR)

1. The MCP Server is instrumented with an Amazon Bedrock AgentCore Identity OAuth client

1. The MCP Server makes the associated tools available at the /mcp endpoint for Agents to discover.

1. Amazon CloudWatch collects operational metrics and logs from MCP server deployments for monitoring and troubleshooting.

### Agent Builder use case
<a name="agent-builder"></a>

 **Depicts Agent Builder architecture**

![agent builder deployment diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/agent-builder-deployment-diagram.png)

The high-level process flow for the Agent Builder components deployed with the AWS CloudFormation template is as follows:

1. Admin users deploy the use case using the Deployment Dashboard. [Business users](concepts-and-definitions.md) sign in to the use case UI.

1. CloudFront delivers the web UI which is hosted in an S3 bucket.

1. The web UI leverages a WebSocket integration built using API Gateway. The API Gateway is backed by a custom Lambda authorizer function, which returns the appropriate [AWS Identity and Access Management](https://aws.amazon.com/iam/)(IAM) policy based on the Amazon Cognito group the authenticating user belongs to. The policy is stored in DynamoDB.

1. Amazon Cognito authenticates users and backs both the CloudFront web UI and API Gateway.

1. Incoming requests from the business user are passed from API Gateway to an [Amazon SQS queue](https://aws.amazon.com/sqs/) and then to the AWS Lambda function. The queue enables the asynchronous operation of the API Gateway to Lambda integration. The queue passes connection information to the Lambda function which will then post results directly back to the API Gateway websocket connection to support long running inference calls.

1. The AWS Lambda function retrieves the agent configuration from DynamoDB.

1. Using the user input and any relevant use case configurations, the AWS Lambda function builds and sends a request payload to the agent, running on [Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/).

1. The agent connects to associated MCP servers and registers the tools to the strands agent instance. The agent then autonomously selects and performs actions based on tool descriptions and task requirements.

1. When the response comes back from the Amazon Bedrock AgentCore runtime, the Lambda function streams the response back through the API Gateway WebSocket to be consumed by the client application.

**Note**
Agent processing is limited to Lambda execution timeout (15 minutes).

### Workflow Builder use case
<a name="workflow-builder"></a>

 **Depicts Workflow Builder architecture**

![workflow deployment diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/workflow-deployment-diagram.png)

The high-level process flow for the Workflow Builder components deployed with the AWS CloudFormation template is as follows:

1. Admin users deploy the workflow using the Deployment Dashboard, selecting Agent Builder agents to include as specialized agents.

1. CloudFront delivers the web UI which is hosted in an S3 bucket.

1. The web UI leverages a WebSocket integration built using API Gateway. The API Gateway is backed by a custom Lambda authorizer function, which returns the appropriate [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) policy based on the Amazon Cognito group the authenticating user belongs to. The policy is stored in DynamoDB.

1. Amazon Cognito authenticates users and backs both the CloudFront web UI and API Gateway.

1. Incoming requests from the business user are passed from API Gateway to an [Amazon SQS queue](https://aws.amazon.com/sqs/) and then to the AWS Lambda function. The queue enables the asynchronous operation of the API Gateway to Lambda integration.

1. The AWS Lambda function retrieves workflow configuration from DynamoDB, including the list of specialized Agent Builder agents.

1. Using the user input and workflow configuration, Lambda sends requests to the [Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/) hosting the supervisor agent.

1. The supervisor agent creates local instances of all specialized Agent Builder agents within the AgentCore Runtime environment. These specialized agents are registered as tools using the Agents as Tools pattern. The supervisor then autonomously selects and delegates work to specialized agents based on agent descriptions and task requirements.

1. The supervisor agent aggregates results from specialized agents and formulates the final response, returning it to the Lambda to be streamed back to the client application through the API Gateway Websocket.

**Note**
Workflow processing is limited to Lambda execution timeout (15 minutes).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
