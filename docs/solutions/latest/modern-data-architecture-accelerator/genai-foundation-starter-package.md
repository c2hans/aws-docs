---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/genai-foundation-starter-package.html
---

# GenAI Foundation Starter Package
<a name="genai-foundation-starter-package"></a>

The GenAI Foundation Starter Package delivers a production-ready foundation for building sophisticated AI agents using Amazon Bedrock. Out of the box, it demonstrates a customer support assistant that can understand queries, search knowledge bases, and take actions - but this is just the beginning.

 **GenAI Foundation starter kit architecture**

![GenAI Foundation starter kit — Bedrock agent with RAG knowledge bases and guardrails.](https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/genai_foundation.png)

Built on AWS best practices, this package provides the building blocks to create any type of agentic AI application. Whether you need sales assistants, technical troubleshooters, or domain-specific experts, the modular architecture adapts to your unique requirements.

This architecture is particularly effective when:

1. You need to deploy intelligent agents with autonomous decision-making capabilities that can perform complex tasks.

1. Your organization requires governed access to AI resources with appropriate content safety measures.

Deploy this package when you need a scalable, secure foundation that supports your organization’s agentic AI initiatives with enterprise-grade controls.

The GenAI Foundation Starter Package provides a complete environment for developing and deploying agentic AI applications. This package is organized into multiple domains that work together to create a comprehensive AI platform:

## Shared Domain Components
<a name="shared-domain-components-3"></a>
+  **IAM Roles** - Comprehensive roles including data-admin with Bedrock permissions, agent execution roles, and Lambda execution roles
+  **Data Lake** - KMS-encrypted S3 buckets for knowledge base data sources and document storage
+  **Access Policies** - Granular permissions for AI resource management and data access

## GenAI Domain Components
<a name="genai-domain-components"></a>
+  **Bedrock Agents** - Intelligent agents with custom instructions and action groups
+  **Knowledge Bases** - RAG-enabled knowledge bases with vector stores for efficient retrieval
+  **Lambda Functions** - Custom functions for agent action groups and document processing
+  **Guardrails** - Content safety controls that filter prompts and model responses and block content that violates policy
+  **Vector Stores** - Efficient knowledge retrieval using Amazon OpenSearch Serverless

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

1. A VPC with at least two private subnets (required for OpenSearch Serverless)

1. Access to Bedrock foundation models in your region

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
+ Edit the `mdaa.yaml` file to set your organization name and VPC/subnet information:

```
organization: <your-unique-org-name>
context:
  vpc_id: <your vpc id>
  subnet_id_1:  <your subnet id 1>
  subnet_id_2:  <your subnet id 2>
  subnet_id_3:  <your subnet id 3>
  llm_model: <your_model> # e.g. anthropic.claude-3-5-sonnet-20240620-v1:0 or an ARN
  kb_embedding_model: <kb_embedding_model> # e.g. amazon.titan-embed-text-v2:0
  kb_parsing_model: <kb_parsing_model> # e.g. anthropic.claude-3-5-sonnet-20240620-v1:0
```

 **Important Notes:**
+  **Cross-region inference**: Use inference profile ARN in llm\_model (e.g., `arn:aws:bedrock:us-east-1:<account_id>:inference-profile/anthropic.claude-3-7-sonnet-20250219-v1:0`)
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

 **Step 4: Verify deployment** \* Check the AWS CloudFormation console to verify all stacks have been created successfully \* Verify the Bedrock agents, knowledge bases, S3 buckets, and other resources have been created

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
   + Upload documents to the support-docs prefix for customer support materials
   + Upload documents to the product-docs prefix for product documentation
   + Verify documents are uploaded with KMS encryption

### Using Bedrock Agents
<a name="using-bedrock-agents"></a>

1.  **Assume the data-admin role**
   + This role is configured with AssumeRole trust to the local account by default
   + It has comprehensive permissions for managing Bedrock resources

1.  **Sync knowledge bases**
   + Navigate to the Amazon Bedrock console
   + Go to Knowledge Bases and select your deployed knowledge base
   + Check if your documents are automatically synced to the knowledge base

1.  **Test the Bedrock Agent**
   + In the Amazon Bedrock console, go to Agents
   + Select the customer-support-agent
   + Use the Test Agent interface to interact with the agent
   + Ask questions related to the documents you uploaded

1.  **Monitor agent performance**
   + Use CloudWatch logs to monitor agent interactions
   + Review Bedrock traces for detailed execution information
   + Monitor Lambda function logs for action group executions

### Advanced Usage
<a name="advanced-usage"></a>

1.  **Customize agent behavior**
   + Modify the agent instructions in the bedrock-builder.yaml configuration
   + Update Lambda functions for custom action groups
   + Adjust guardrails for content safety requirements

1.  **Expand knowledge bases**
   + Add additional data sources to existing knowledge bases
   + Create new knowledge bases for different domains
   + Configure custom transformation Lambda functions

For more detailed information about the configuration files and their purposes, refer to the README.md file in the starter\_kits/genai\_foundation directory of the MDAA repository.
