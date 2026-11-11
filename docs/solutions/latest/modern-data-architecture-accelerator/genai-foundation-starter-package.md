---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/genai-foundation-starter-package.html
---

# GenAI Foundation Starter Package
<a name="genai-foundation-starter-package"></a>

The GenAI Foundation Starter Package delivers a production-ready foundation for building sophisticated AI agents using Amazon Bedrock AgentCore. Out of the box, it demonstrates a customer support assistant that can understand queries, search knowledge bases, and take actions - but this is just the beginning.

 **GenAI Foundation starter kit architecture**

![GenAI Foundation starter kit — AgentCore Harness agent with gateway tools](https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/genai_foundation.png)

Built on AWS best practices, this package provides the building blocks to create any type of agentic AI application. Whether you need sales assistants, technical troubleshooters, or domain-specific experts, the modular architecture adapts to your unique requirements.

This architecture is particularly effective when:

1. You need to deploy intelligent agents with autonomous decision-making capabilities that can perform complex tasks.

1. Your organization requires governed access to AI resources with appropriate content safety measures.

Deploy this package when you need a scalable, secure foundation that supports your organization’s agentic AI initiatives with enterprise-grade controls.

The GenAI Foundation Starter Package provides a complete environment for developing and deploying agentic AI applications. This package is organized into multiple domains that work together to create a comprehensive AI platform:

## Shared Domain Components
<a name="shared-domain-components-3"></a>
+  **IAM Roles** - Comprehensive roles including data-admin with Bedrock and AgentCore permissions, data-user, the harness execution role, the knowledge base execution role, and Lambda execution roles
+  **Data Lake** - KMS-encrypted S3 buckets for knowledge base data sources and document storage
+  **Access Policies** - Granular permissions for AI resource management and data access

## GenAI Domain Components
<a name="genai-domain-components"></a>
+  **AgentCore Harness** - The customer support agent: a managed agent loop with a system prompt, a Bedrock model, and gateway tools, running in your VPC subnets
+  **AgentCore Gateway** - Serves the customer support tools and knowledge base search to the agent, with AWS IAM authentication
+  **Knowledge Bases** - RAG-enabled knowledge bases with vector stores for efficient retrieval, exposed to the agent as a gateway tool
+  **Lambda Functions** - Custom functions for the customer support tools, which serve mock account and ticket data, and for document processing
+  **Guardrails** - Content safety controls that filter prompts and model responses and block content that violates policy
+  **Vector Stores** - Efficient knowledge retrieval using Amazon Aurora Serverless (PostgreSQL with pgvector)

This package accelerates your agentic AI initiatives by providing a ready-to-use environment with AWS best practices built in. It’s ideal for organizations looking to establish or enhance their AI capabilities with autonomous agents, intelligent task execution, and enterprise-grade AI governance.

## Deployment Instructions
<a name="deployment-instructions-3"></a>

Step-by-step guide for deploying the GenAI Foundation Starter Package

You can deploy the GenAI Foundation Starter Package using Manual CLI Deploy Method

### Manual CLI Deploy Method
<a name="manual-cli-deploy-method"></a>

#### Prerequisites
<a name="prerequisites-6"></a>

Before deploying the GenAI Foundation Starter Package using the CLI method, verify you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK installed (`npm install -g aws-cdk`)

1. CDK bootstrapped in your target account and region

1. A target region where both the AgentCore harness and Amazon Bedrock Knowledge Bases are available. The harness is offered in fewer regions than the rest of AgentCore, so check its row in [AgentCore supported Regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html).

1. A VPC with three private subnets and a security group:
   + The subnets must route outbound traffic through a NAT gateway, which the agent harness and the vector store’s password rotation function use to reach AWS services. For subnets without a NAT gateway, see the Private VPC section of `docs/USAGE.md` in the starter kit.
   + Each subnet must be in an Availability Zone that [AgentCore supports for VPC connectivity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html), or the harness fails to create.
   + The security group must allow outbound HTTPS. The agent harness sessions use it.

1. Access to the Bedrock models you set in `mdaa.yaml`

#### Deployment Steps
<a name="deployment-steps-5"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the sample configuration files:

```
cp -r starter_kits/genai_foundation my_genai_config
cd my_genai_config
```
+ Edit the `mdaa.yaml` file to set your organization name, VPC/subnet information, and security group:

```
organization: <your-unique-org-name>
context:
  vpc_id: <your vpc id>
  subnet_id_1:  <your subnet id 1>
  subnet_id_2:  <your subnet id 2>
  subnet_id_3:  <your subnet id 3>
  security_group_id: <your security group id> # used by the agent harness sessions; must allow outbound HTTPS
  llm_model: <your_model> # model ID or inference profile ID, e.g. global.anthropic.claude-sonnet-4-6
  kb_embedding_model: <kb_embedding_model> # e.g. amazon.titan-embed-text-v2:0
  kb_parsing_model: <kb_parsing_model> # e.g. anthropic.claude-3-5-sonnet-20240620-v1:0
```

 **Important Notes:**
+  **Cross-region inference**: Use the inference profile ID in llm\_model (e.g., `global.anthropic.claude-sonnet-4-6`)
+  **Single region**: Use model ID directly

 **Step 3: Deploy the solution** \* Verify you are authenticated to your target AWS account.
+ Optionally, run the following command to understand what stacks will be deployed:

```
npx @aws-mdaa/cli ls
```
+ Optionally, run the following command to review the produced templates:

```
npx @aws-mdaa/cli synth
```
+ Run the following command to deploy all modules:

```
npx @aws-mdaa/cli deploy
```

 **Step 4: Verify deployment** \* Check the AWS CloudFormation console to verify all stacks have been created successfully \* Verify the AgentCore harness and gateway, knowledge base, guardrail, S3 buckets, and other resources have been created

## Usage Instructions
<a name="usage-instructions-3"></a>

How to effectively use the GenAI Foundation Starter Package after deployment

Once the MDAA deployment is complete, follow these steps to interact with the GenAI platform:

### Initial Setup and Document Upload
<a name="initial-setup-and-document-upload"></a>

1.  **Assume the data-user role**
   + This role is configured with AssumeRole trust to the local account by default
   + It has permissions to upload documents to the knowledge base S3 buckets

1.  **Upload documents to knowledge base buckets**
   + Upload customer support materials to the `data/` prefix of the `<org>-dev-shared-datalake-customer-support-docs` bucket
   + Upload product documentation to the `data/` prefix of the `<org>-dev-shared-datalake-product-docs` bucket
   + The buckets apply KMS encryption by default

### Using the AgentCore Harness
<a name="using-the-agentcore-harness"></a>

1.  **Assume the data-admin role**
   + This role is configured with AssumeRole trust to the local account by default
   + It has permissions to invoke the harness and to manage the Bedrock and AgentCore resources

1.  **Check knowledge base ingestion**
   + The knowledge base ingests new documents within about 5 minutes
   + To check progress, navigate to the Amazon Bedrock console, go to Knowledge Bases, select `<org>-dev-genai-customer-support-agent-kb-test-customer-support`, and select the data source

1.  **Test the agent**
   + In the Amazon Bedrock AgentCore console, open the harness and chat with the agent. The harness name starts with `<org>_dev_genai_customer_su` and is truncated
   + Where the console test isn’t available, or from your own code, call the `InvokeHarness` API with the harness ARN. The ARN is published in SSM at `/<org>/genai/customer-support-agent/harness/customer-support-agent/arn`. Read it before you assume the data-admin role, because that role can’t read SSM parameters
   + Ask questions about the documents you uploaded, or try `What is the status of account acc-12345?`, `Create a support ticket for account acc-12345`, and `What is the status of ticket ticket-001?`
   + A session ends after 10 minutes idle or 8 hours, and the agent keeps no memory across sessions

1.  **Monitor agent performance**
   + Check the harness, gateway, and gateway target status in the Amazon Bedrock AgentCore console
   + Monitor the support tools Lambda function’s CloudWatch logs. A tool call that fails reaches the agent as a generic error, so the function’s logs hold the details

### Advanced Usage
<a name="advanced-usage"></a>

1.  **Customize agent behavior**
   + Modify the harness system prompt in the bedrock-builder.yaml configuration
   + Replace the mock account and ticket data in `lambda/src/support_function.py` with calls to your own systems, and update the tool definitions of the `support-actions` gateway target to match
   + Adjust guardrails for content safety requirements

1.  **Expand knowledge bases**
   + Add additional data sources to existing knowledge bases
   + Create new knowledge bases for different domains
   + Configure custom transformation Lambda functions

For more detailed information about the configuration files and their purposes, refer to the README.md and docs/USAGE.md files in the starter\_kits/genai\_foundation directory of the MDAA repository.
