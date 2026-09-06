---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/gaia-chatbot-starter-package.html
---

# GAIA Chatbot Starter Package
<a name="gaia-chatbot-starter-package"></a>

The GAIA Chatbot Starter Package deploys a production-ready GenAI chatbot backend using Amazon Bedrock Knowledge Bases, Guardrails, and serverless APIs. You provide the frontend application and documents for the knowledge base; the starter kit deploys the full backend.

 **GAIA Chatbot starter kit architecture**

![GAIA Chatbot starter kit — GenAI backend with Cognito auth and AppSync streaming.](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/ai-gaia.png)

This architecture is particularly effective when:

1. You need a RAG-powered chatbot with enterprise authentication.

1. You need document Q&A over internal knowledge bases (PDF, TXT, MD, HTML, DOCX).

1. You need real-time streaming chat via WebSocket (AppSync Events).

1. You need content-filtered AI responses with Bedrock Guardrails.

## Authentication and API Components
<a name="authentication-and-api-components"></a>
+  **Cognito User Pool** - Email/password or enterprise SSO authentication
+  **REST API (API Gateway)** - Session management, feedback, and admin operations
+  **WebSocket API (AppSync Events)** - Real-time chat streaming
+  **CloudFront CDN** - Serves `aws-exports.json` configuration
+  **WAF** - Optional web application firewall

## GenAI Components
<a name="genai-components"></a>
+  **Bedrock Knowledge Base** - OpenSearch Serverless vector store
+  **Bedrock Guardrails** - Content filtering and PII protection
+  **VPC-Deployed Lambda Functions** - Serverless compute for API handlers
+  **KMS-Encrypted S3 Data Lake** - Document storage

## Deployment Instructions
<a name="deployment-instructions-8"></a>

### Manual CLI Deploy Method
<a name="manual-cli-deploy-method-6"></a>

#### Prerequisites
<a name="prerequisites-11"></a>

Before deploying the GAIA Chatbot Starter Package using the CLI method, verify you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK bootstrapped in your target account and region

1. If deploying outside `us-east-1`: **also bootstrap CDK in `us-east-1` in the same account**. CloudFront WAF resources must be deployed in `us-east-1`; the module creates a cross-region stack there automatically via the `additional_stacks` configuration.

1. A VPC with private subnets and a NAT Gateway (required — AppSync Events has no VPC endpoint).

1. Bedrock model access enabled in the AWS console for your target region.

#### Deployment Steps
<a name="deployment-steps-10"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the starter kit files:

```
cp -r starter_kits/genai_gaia_chatbot my_gaia_chatbot
cd my_gaia_chatbot
```
+ Edit `mdaa.yaml`:

```
organization: <your-unique-org-name>
context:
  vpc_id: <your vpc id>
  app_subnet_id_1: <private subnet with NAT route>
  app_subnet_id_2: <private subnet with NAT route>
  data_subnet_id_1: <data subnet>
  data_subnet_id_2: <data subnet>
  inference_model_arn: <Bedrock model ARN or inference profile ARN>
  embedding_model: <embedding model ID>
  waf_allowed_cidrs: [<your ip>, <NAT gateway IP>]
```

 **Step 3: Deploy the solution**

```
npx @aws-mdaa/cli ls
npx @aws-mdaa/cli synth
npx @aws-mdaa/cli deploy
```

 **Step 4: Verify deployment**
+ Verify the Cognito User Pool, API Gateway REST API, AppSync API, CloudFront distribution, Bedrock Knowledge Base, and OpenSearch Serverless collection are created.

## Usage Instructions
<a name="usage-instructions-8"></a>

1.  **Upload documents** — Upload documents to the S3 data lake under `data/bedrock-knowledge-base/` and sync the knowledge base in the Bedrock console.

1.  **Fetch `aws-exports.json` ** — CloudFront serves the config file consumed by your frontend application.

1.  **Authenticate a user** — Create a Cognito user (or configure external SSO) and sign in from your frontend.

1.  **Chat via WebSocket** — The AppSync Events API streams responses in real time; WAF must allow your NAT Gateway’s public IP for responses to reach Lambda.

For more detailed information, refer to the README.md and docs/USAGE.md files in the starter\_kits/genai\_gaia\_chatbot directory of the MDAA repository.
