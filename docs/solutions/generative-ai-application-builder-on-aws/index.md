---
source_url: https://docs.aws.amazon.com//solutions/generative-ai-application-builder-on-aws//index.html
---

---
title: 'Generative AI Application Builder on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/generative-ai-application-builder-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Generative AI Application Builder on AWS

Rapidly develop and deploy production-ready Agentic AI applications

- **Version**: 4.1.24
- **Released**: 8/2026
- **Author**: AWS
- **Est. deployment time**: 10 mins
- **Estimated cost**: [See details](/solutions/latest/generative-ai-application-builder-on-aws/cost.html)

## Overview

Building and managing agentic AI applications can be challenging for teams without deep AI infrastructure or orchestration expertise. Generative AI Application Builder (GAAB) on AWS eliminates that complexity by unifying all the key components of modern agentic systems into one integrated solution. GAAB brings together the Model Context Protocol (MCP), agents, and multi-agent orchestration with built-in authentication, permissioning, networking, and application management—so teams can focus on iterating and improving their applications instead of managing infrastructure. With GAAB, you can deploy local MCP servers as remote endpoints using AWS Lambda, container images, or OpenAPI and Smithy API specifications. The platform enables developers to create agents, assign MCP tools, and orchestrate complex behaviors through the Agent-as-a-Tool framework. Once an agentic application is ready, teams can collaborate instantly by accessing the application out of the box or integrating it with their own client through a single WebSocket connection. GAAB accelerates the path from prototype to production by simplifying the deployment, management, and scaling of secure, extensible agentic applications built on AWS.

## Benefits

### Rapid experimentation

You can experiment with different model, system prompt, and memory configurations for the same use case to compare outputs and performance directly from the GAAB management dashboard. Once you have completed your testing iterations, you can easily deploy the GAAB created applications with the default user interface or integrate the agentic application with your existing system.

### Configurability

Centralize the deployment and management of Model Context Protocol (MCP) servers, AI Agents, and Multi-agent workflows while governing and decentralizing access to the deployed agentic applications across your teams.

### Production-ready

Built with AWS Well-Architected design principles, this solution offers enterprise-grade security and scalability with high availability and low latency, ensuring seamless integration into your applications with high performance standards.

### Extensible modular architecture

Extend this solution’s functionality by integrating your existing projects or natively connecting additional AWS services. GAAB is an open-source application, enabling you to use the included Strands and LangChain orchestration layers and Lambda functions to connect with the services of your choice.

## How it works

### Build and Deploy Agents

The Agent Builder use case enables you to quickly configure, deploy, and manage AI Agents from the Management Dashboard. Configure the Agent's model, tools, memory, system prompt, and integration pattern before deploying the AI Agent stack.

[Open implementation guide](/solutions/latest/generative-ai-application-builder-on-aws/architecture-overview.html)Step 1Admin users deploy the use case using the Deployment Dashboard. Business users sign in to the use case UI.

Step 2Amazon CloudFront delivers the web UI which is hosted in an Amazon S3 bucket.

Step 3The web UI leverages a WebSocket integration built using Amazon API Gateway. The API Gateway is backed by a custom AWS Lambda authorizer function, which returns the appropriate AWS Identity and Access Management (IAM) policy based on the Amazon Cognito group the authenticating user belongs to. The policy is stored in Amazon DynamoDB.

Step 4Amazon Cognito authenticates users and backs both the CloudFront web UI and API Gateway.

Step 5Incoming requests from the business user are passed from API Gateway to an Amazon Simple Queue Service queue and then to the Lambda function. The queue enables the asynchronous operation of the API Gateway to Lambda integration. The queue passes connection information to the Lambda function which will then post results directly back to the API Gateway websocket connection to support long running inference calls.

Step 6The Lambda function retrieves the agent configuration from DynamoDB.

Step 7Using the user input and any relevant use case configurations, the Lambda function builds and sends a request payload to the agent, running on Amazon Bedrock AgentCore Runtime

Step 8The agent connects to associated MCP servers and registers the tools to the strands agent instance. The agent then autonomously selects and performs actions based on tool descriptions and task requirements.

Step 9When the response comes back from the AgentCore runtime, the Lambda function streams the response back through the API Gateway WebSocket to be consumed by the client application.

### Multi-Agent Applications

The Multi-Agent use case enables you to quickly orchestrate multiple Agents to address complex tasks from the Management Dashboard. Configure the orchestration Agent's model, the AI Agents to use as tools, the orchestration prompt, and integration pattern before deploying the Multi-Agent stack.

[Open implementation guide](/solutions/latest/generative-ai-application-builder-on-aws/architecture-overview.html)Step 1Admin users deploy the workflow using the Deployment Dashboard, selecting Agent Builder agents to include as specialized agents.

Step 2Amazon CloudFront delivers the web UI which is hosted in an Amazon S3 bucket.

Step 3The web UI leverages a WebSocket integration built using Amazon API Gateway. The API Gateway is backed by a custom AWS Lambda authorizer function, which returns the appropriate AWS Identity and Access Management (IAM) policy based on the Amazon Cognito group the authenticating user belongs to. The policy is stored in Amazon DynamoDB.

Step 4Amazon Cognito authenticates users and backs both the CloudFront web UI and API Gateway.

Step 5Incoming requests from the business user are passed from API Gateway to an Amazon Simple Queue Service queue and then to the Lambda function. The queue enables the asynchronous operation of the API Gateway to Lambda integration.

Step 6The Lambda function retrieves workflow configuration from DynamoDB, including the list of specialized Agent Builder agents.

Step 7Using the user input and workflow configuration, Lambda sends requests to the Amazon Bedrock AgentCore Runtime hosting the supervisor agent.

Step 8The supervisor agent creates local instances of all specialized Agent Builder agents within the AgentCore Runtime environment. These specialized agents are registered as tools using the Agents as Tools pattern. The supervisor then autonomously selects and delegates work to specialized agents based on agent descriptions and task requirements.

Step 9The supervisor agent aggregates results from specialized agents and formulates the final response, returning it to the Lambda to be streamed back to the client application through the API Gateway Websocket.

### Deploy Remote MCP Servers

The MCP Server use case enables you to quickly deploy and manage MCP Servers from the Management Dashboard. You can connect to any existing MCP Server by providing its endpoint URL, or deploy and host your own MCP Server via an image, Lambda function, OpenAPI spec, or Smithy file, providing the flexibility to integrate external third-party services or self-hosted MCP Servers for use in Agent Builder and Multi-Agent Use cases.

[Open implementation guide](/solutions/latest/generative-ai-application-builder-on-aws/architecture-overview.html)Step 1Admin users deploy the MCP Server use case using the Deployment Dashboard, selecting either Gateway or Runtime deployment method.

Step 2This action is authenticated with Amazon Cognito.

Step 3For the Gateway deployment, the solution creates an Amazon Bedrock AgentCore Gateway that transforms existing AWS Lambda functions, APIs, or external MCP servers into MCP-compliant tools. For the Runtime deployment, the solution deploys containerized MCP servers on AgentCore Runtime using provided Amazon Elastic Container Registry images.

Step 4Gateway deployments retrieve the necessary API/Lambda/Smithy schemas from their uploaded location in Amazon Simple Storage Service (Amazon S3), or connect directly to MCP Server URL endpoints.

Step 5Runtime deployments retrieve the containerized MCP server provided by the user from Amazon ECR.

Step 6The MCP Server is instrumented with an AgentCore Identity OAuth client.

Step 7The MCP Server makes the associated tools available at the /mcp endpoint for Agents to discover.

Step 8Amazon CloudWatch collects operational metrics and logs from MCP server deployments for monitoring and troubleshooting.

### Retrieval Augmented Generation (RAG) Chatbots

The RAG Chatbot use case enables you to quickly deploy and manage a Retrieval Augmented Generation (RAG) enabled chatbot. Configure the chatbot’s model, RAG knowledgebase, and guardrails to implement safeguards and reduce hallucinations before deploying the chatbot stack.

[Open implementation guide](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/architecture-overview.html)Step 1Admin users deploy the use case using the Deployment Dashboard. Business users log in to the use case UI.

Step 2CloudFront delivers the web UI which is hosted in an S3 bucket.

Step 3The web UI leverages a WebSocket integration built using API Gateway. The API Gateway is backed by a custom Lambda authorizer function, which returns the appropriate AWS Identity and Access Management (IAM) policy based on the Amazon Cognito group the authenticating user belongs to. The policy is stored in DynamoDB.

Step 4Amazon Cognito authenticates users and backs both the CloudFront web UI and API Gateway.

Step 5Incoming requests from the business user are passed from API Gateway to an Amazon SQS queue and then to the LangChain Orchestrator. The LangChain Orchestrator is a collection of Lambda functions and layers that provide the business logic for fulfilling requests coming from the business user. The queue enables the asynchronous operation of the API Gateway to Lambda integration. The queue passes connection information to the Lambda functions which will then post results directly back to the API Gateway websocket connection to support long running inference calls.

Step 6The LangChain Orchestrator uses Amazon DynamoDB to get the configured LLM options and necessary session information (such as the chat history).

Step 7If the deployment has a knowledge base enabled, then the LangChain Orchestrator leverages Amazon Kendra or Knowledge Bases for Amazon Bedrock to run a search query to retrieve document excerpts.

Step 8Using the chat history, query, and context from the knowledge base, the LangChain Orchestrator creates the final prompt and sends the request to the LLM hosted on Amazon Bedrock or Amazon SageMaker AI.

Step 9When the response comes back from the LLM, the LangChain Orchestrator streams the response back through the API Gateway WebSocket to be consumed by the client application.

Step 10Using Amazon CloudWatch, this solution collects operational metrics from various services to generate custom dashboards that allow you to monitor the deployment’s performance and operational health.

Step 11If feedback collection is enabled, a REST API endpoint, leveraging Amazon API Gateway is made available for the collection of user feedback.

Step 12The feedback backing lambda, augments the submitted feedback with additional use case specific metadata (e.g. model used) and stores the data in Amazon S3 for later analysis and reporting by the DevOps users.

### Management Dashboard

The Management Dashboard is a web UI management console for admin users to create and manage remote MCP Servers, Agents, Multi-Agent workflows, and RAG chatbot deployments. This dashboard enables customers to rapidly experiment with configurations across models, tools, and memory before deploying governed and production-ready Agentic applications.

[Open implementation guide](/solutions/latest/generative-ai-application-builder-on-aws/architecture-overview.html)Step 1Admin users log in to the Deployment Dashboard user interface (UI).

Step 2Amazon CloudFront delivers the web UI, which is hosted in an Amazon Simple Storage Service (Amazon S3) bucket.

Step 3AWS WAF protects the APIs from attacks. This solution configures a set of rules called a web access control list (web ACL) that allows, blocks, or counts web requests based on configurable, user defined web security rules and conditions.

Step 4The web UI leverages a set of REST APIs that are exposed using Amazon API Gateway.

Step 5Amazon Cognito authenticates users and backs both the CloudFront web UI and API Gateway.

Step 6AWS Lambda provides the business logic for the REST endpoints. This backing Lambda function manages and creates the necessary resources to perform use case deployments using AWS CloudFormation.

Step 7Amazon DynamoDB stores the list of deployments.

Step 8When a new use case is created by the admin user, the backing Lambda function initiates a CloudFormation stack creation event for the requested use case.

Step 9All of the LLM configuration options provided by the admin user in the deployment wizard are saved in DynamoDB. The deployment uses this DynamoDB table to configure the LLM at runtime.

Step 10Using Amazon CloudWatch, this solution collects operational metrics from various services to generate custom dashboards that allow you to monitor the solution’s performance and operational health.

## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/generative-ai-application-builder-on-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Launch in the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?&templateURL=https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/generative-ai-application-builder-on-aws.template&redirectId=SolutionWeb)

## Deployment options

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/generative-ai-application-builder-on-aws.template)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/generative-ai-application-builder-on-aws)

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](/pdfs/solutions/latest/generative-ai-application-builder-on-aws/generative-ai-application-builder-on-aws.pdf)

## Related content

- **Amazon Bedrock**: The easiest way to build and scale generative AI applications with foundation models.

[Learn more](https://aws.amazon.com/bedrock/)

- **Generative AI Deployments using Amazon SageMaker JumpStart**: This Guidance demonstrates how to deploy a generative artificial intelligence (AI) model provided by Amazon SageMaker JumpStart to create an asynchronous SageMaker endpoint with the ease of the AWS Cloud Development Kit (AWS CDK).

[Go to Guidance](https://aws.amazon.com/solutions/guidance/generative-ai-deployments-using-amazon-sagemaker-jumpstart/)

- **Natural Language Queries of Relational Databases on AWS**: This Guidance demonstrates how to build an application enabling users to ask questions directly of relational databases using natural language queries (NLQ).

[Go to Guidance](https://aws.amazon.com/solutions/guidance/natural-language-queries-of-relational-databases-on-aws/)

- **Generative AI for every business**: Boost productivity, build differentiated experiences, and innovate faster with AWS.

[Learn more](https://aws.amazon.com/ai/generative-ai/)

- **Launching a High-Accuracy Chatbot Using Generative AI Solutions on AWS with Megamedia**: This case study demonstrates how broadcast company Megamedia created a generative AI–powered chatbot to simplify access to important public information using AWS.

[Read the case study](https://aws.amazon.com/solutions/case-studies/megamedia-case-study/)

- **Amazon Bedrock AgentCore**: An agentic platform for building and deploying production-ready agents at scale. Features secure runtime, intelligent memory, gateway for tool access, controls, and performance monitoring. Works with any framework and model—no infrastructure needed.

[Learn more](https://aws.amazon.com/bedrock/agentcore/)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/generative-ai-application-builder-on-aws/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/generative-ai-application-builder-on-aws/latest/rss.xml)
