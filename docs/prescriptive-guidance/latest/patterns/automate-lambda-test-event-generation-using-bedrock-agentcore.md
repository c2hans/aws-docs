---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-lambda-test-event-generation-using-bedrock-agentcore.html
---

# Automate Lambda test event generation using Amazon Bedrock AgentCore
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore"></a>

*Ishita Gupta and Kriti Gupta, Amazon Web Services*

## Summary
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore-summary"></a>

This pattern delivers an AI-powered approach for automatically generating comprehensive test cases for AWS Lambda functions using Amazon Bedrock's generative AI capabilities. This pattern implements a three-agent architecture (Analyzer, Generator, and Validator) deployed on Amazon Bedrock AgentCore that analyzes actual Lambda function code to extract input/output patterns and generates positive, negative, and edge-case test scenarios with realistic data.

The architecture establishes an intelligent workflow where the Analyzer Agent fetches and analyzes Lambda code using Amazon Bedrock, the Generator Agent creates test cases based on learned patterns, and the Validator Agent ensures quality through deduplication and ranking. An Amazon DynamoDB-based memory store enables continuous learning from user feedback, improving test generation accuracy over time. Amazon Cognito provides secure user authentication with JSON Web Token (JWT)-based API authorization. Amazon Bedrock Guardrails provide prompt attack filtering, sensitive information redaction, and content safety enforcement on all Amazon Bedrock API calls. **Key Capabilities:**
+ **Multi-Language Support**: Python, Java, C\#, JavaScript/TypeScript, and Ruby Lambda functions
+ **Intelligent Code Chunking**: Automatically splits large codebases into manageable chunks for analysis
+ **Parallel Processing**: Concurrent Amazon Bedrock API calls for faster test generation (5 concurrent workers for code analysis, parallel per-chunk test generation)
+ **Target-Specific Analysis**: Focus on specific functions, classes, or files within Lambda code
+ **Pattern Learning**: Amazon DynamoDB-based memory store with target-specific and global pattern storage
+ **Rejection Avoidance**: Learns from rejected test cases to avoid common mistakes
+ **Continuation Mechanism**: Handles incomplete Amazon Bedrock responses with automatic continuation.
+ **Ignore Patterns**: Exclude test files, dependencies, and non-code files from analysis.
+ **Serverless Deployment**: Runs on Amazon Bedrock AgentCore with Cognito-based authentication
+ **Security Guardrails:** Amazon Bedrock Guardrails for prompt attack filtering, Personally identifiable information (PII) redaction, content safety, and denied topic blocking on all AI calls

  This pattern is ideal for development teams and organizations that want to accelerate Lambda testing, improve test coverage, and maintain high code quality through AI-assisted test generation. This pattern uses AWS managed services to simplify test creation, enhance quality through learning, and scale to meet evolving testing needs.

## Prerequisites and limitations
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore-prereqs"></a>

**Prerequisites **

To successfully implement this pattern, make sure that the following are in place:
+ **An active AWS account** - An AWS account with permissions to access Lambda functions, invoke Amazon Bedrock models, create DynamoDB tables, manage Cognito user pools, and deploy Amazon Bedrock AgentCore agents.
+ **Amazon Bedrock model access** - Anthropic Claude Sonnet 4 (us.anthropic.claude-sonnet-4-6) enabled in your AWS Region. For setup instructions, see Model access in the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).
+ **A development environment that consists of:**

  - [Python 3.11 or higher](https://www.python.org/downloads/)

  - [AWS CLI installed and configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

  - [Git](https://git-scm.com/install/) for cloning the repository
+ **AWS Lambda functions** - At least one deployed Lambda function with accessible source code for analysis. The function must include source files (.py, .js, .java, .cs, .rb) in the deployment package, not just compiled bytecode.
+ **Supported Lambda runtimes:**

  - Python 3.x (all versions)

  - Node.js (JavaScript/TypeScript)

  - Java 8, 11, 17, 21 (requires .java source files in deployment package)

  - .NET Core/.NET 6\+ (C\#) (requires .cs source files in deployment package)

  - Ruby 2.7, 3.2

**Limitations **
+ This requires Amazon Bedrock model access in us-east-1 region for Claude Sonnet 4.6. AWS Lambda functions can be in any region.
+ Pattern data in Amazon DynamoDB expires after 90 days (configurable via Time to Live (TTL)) to maintain relevance and control costs.
+ Java and C\# Lambda functions must include source files (.java, .cs) in deployment packages. Compiled-only packages (.class, .dll) cannot be analyzed.
+ The system implements in-memory per-user rate limiting (5 requests per 60 seconds). For distributed deployments with multiple AgentCore instances, rate limiting would need to be moved to DynamoDB or Redis for consistency.
+ Some AWS services aren't available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

**Product versions**
+ [Python 3.11 or higher](https://www.python.org/downloads/)
+ [Streamlit 1.28 or later](https://docs.streamlit.io/get-started/installation)
+ [Boto3 (AWS SDK for Python) 1.42.75 or later](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html#installation)
+ [AWS CLI 2.0 or later](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
+ Anthropic Claude Sonnet 4 (us.anthropic.claude-sonnet-4-6)
+ bedrock-agentcore 1.4.7 or later
+ bedrock-agentcore-starter-toolkit 0.3.3 or later

## Architecture
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore-architecture"></a>

**Target architecture **

The following diagram shows the architecture and workflow for this pattern:

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c9fc8d32-56ec-4231-8b57-34769d9bd6d3/images/b57ae65b-60a7-4d32-97d1-155c50f102ce.png)

In this workflow:

1. **User provides input: **Developer interacts with Streamlit UI (app.py) running locally, provides Lambda function name, optional custom instructions for test generation, target filter to focus on specific functions/classes/files, and ignore patterns to exclude test files or dependencies.

1. **Cognito Authentication:** Application authenticates request with Cognito and returns JWT (ID/Access token) to Streamlit.

1. **AgentCore API Invocation: **Streamlit invokes AgentCore API with Bearer Token \+ payload (function name, filters, instructions, ignore patterns).

1. **JWT Validation:** AgentCore API validates JWT using Cognito token signature.

1. **Request Routing: **AgentCore API routes request to Lambda Test Generator workflow (AgentCore Runtime).

1. **Code Analysis Request: **Analyzer Agent initiates a request to fetch the target Lambda function's code and metadata.

1. **AWS Authentication for Lambda Access: **Boto3 authenticates with AWS using the AgentCore execution role, requesting read access permissions.

1. **AWS Lambda Code Retrieval and Processing: **IAM role authorizes access and fetches Lambda function code as a ZIP file, extracts source files, filters out dependencies (node\_modules, venv, etc.) and non-code files, applies user-defined ignore patterns, and chunks code into manageable pieces.

1. **Amazon Bedrock Authentication: **Boto3 Amazon Bedrock client authenticates with AWS IAM for Amazon Bedrock access, requesting invoke model permissions to use Anthropic Claude Sonnet 4.6.

1. **AI-Powered Code Analysis: **IAM role authorizes and sends code chunks to Amazon Bedrock (us-east-1) using Anthropic Claude Sonnet 4 (us.anthropic.claude-sonnet-4-6) with Amazon Bedrock Guardrail applied for prompt attack filtering and content safety. Amazon Bedrock performs Regex \+ LLM enhanced analysis to extract actual input patterns (e.g., event['body'], headers['Authorization']), output patterns (e.g., statusCode, response body structure), dependencies, error handling patterns, and edge cases from the code.

1. **Analysis results are packaged: **Analyzer Agent packages the analysis results into an AnalysisResult object containing code chunks, input patterns, output patterns, dependencies, error patterns, and metadata, then passes it to the Generator Agent.

1. **Test generation process starts: **Generator Agent receives analysis results and initiates a request to generate test cases, first querying DynamoDB memory store for historical patterns to learn from.

1. **Amazon DynamoDB Authentication for Memory Access: **Boto3 DynamoDB client authenticates with AWS IAM for read access permissions to retrieve stored patterns.

1. **Historical patterns are retrieved from Database: **IAM role authorizes and queries DynamoDB memory store table (lambda-testcase-memory) to fetch previously accepted patterns and rejected patterns (failed tests with rejection reasons) for the specific Lambda function.

1. **Amazon Bedrock Authentication for Test Generation: **Boto3 Amazon Bedrock client authenticates again with AWS IAM for Amazon Bedrock access to generate test cases.

1. **AI Test Case Generation: **IAM role authorizes and sends analysis results combined with memory patterns to Amazon Bedrock. Amazon Bedrock generates test case schemas with realistic input events based on actual code patterns, creating positive tests (35%), negative tests (35%), and edge cases (30%). Generation happens per-chunk in parallel for efficiency, applies learned patterns from memory, avoids rejected patterns, and chunks generation if needed for large codebases. All Bedrock converse() calls include guardrailConfig for prompt attack filtering, PII redaction, and denied topic enforcement.

1. **Test validation begins: **Generator Agent passes the generated test case candidates to the Validator Agent for quality control, deduplication, and final selection.

1. **Validation process is configured: **Validator Agent receives test candidates and initiates validation process, requesting access to DynamoDB memory store for scoring and validation.

1. **DynamoDB Authentication for Validation: **Boto3 DynamoDB client authenticates with AWS IAM for read access to query memory patterns for validation scoring.

1. **Test quality is assessed: **IAM role authorizes and uses DynamoDB memory store to score test cases based on previous pattern success rates, function coverage and code complexity. Validator performs structural validation, deduplication using pattern hashing, quality scoring with confidence boosts for handler functions and error handling, diversity selection to cover different chunks and test types, and selects the top N highest-quality, most diverse test cases.

1. **Final test cases returned to AgentCore: **Validator Agent returns the final validated test cases with metadata (confidence scores, descriptions, input events, categories) to the main orchestrator, which formats and returns them back to the Amazon Bedrock AgentCore API

1. **Results delivered to UI:** AgentCore API returns the generated tests back to the Streamlit UI for display with analysis summary, generation metadata, and test case details.

1. **User reviews and provides feedback: **Developer reviews the displayed test cases in Streamlit UI, evaluates each test for quality and relevance, accepts good test cases or rejects poor ones with specific rejection reasons (missing\_auth\_headers, wrong\_status\_code, unrealistic\_data, missing\_required\_fields, incorrect\_event\_source, etc.) and optional custom notes explaining the rejection, then submits feedback.

1. **Feedback is submitted to the system: **Streamlit UI sends the collected feedback (accepted/rejected status, rejection reasons, custom notes) to the AgentCore API (save\_feedback).

1. **AgentCore routes feedback:** AgentCore API calls Validator agent which contains logic to store feedback in DynamoDB.

1. **Feedback storage process begins: **Validator Agent initiates the process to store the feedback.

1. **DynamoDB write access is authenticated: **Boto3 DynamoDB client authenticates with AWS IAM (AgentCore Execution role) for write access permissions to store feedback patterns.

1. **Learning patterns are stored: **IAM role authorizes and stores user feedback in DynamoDB memory store table. Each pattern is stored with a composite partition key (function\_name\#target\_function or function\_name\#GLOBAL), composite sort key (FEEDBACK\#accepted/rejected\#PATTERN\#hash), pattern hash for deduplication, test type, input pattern structure, feedback status, rejection reason (if rejected), custom notes, usage count, success rate, timestamp, and TTL of 90 days for automatic cleanup. This stored data enables the system to learn from user feedback and improve future test generation.

**Automation and scale**

This pattern scales automatically using AWS managed services. Amazon Bedrock handles AI inference on-demand with a 200K token context window and 64K token output per call, and Amazon DynamoDB uses on-demand billing that automatically adjusts to traffic patterns. The system uses parallel processing for speed, the Analyzer Agent makes 5 concurrent Bedrock calls to analyze code chunks (ThreadPoolExecutor with max\_workers=5), while the Generator Agent processes chunks in parallel with 5 concurrent workers. A continuation mechanism handles incomplete responses by automatically retrying requests. Rate limiting (5 requests per 60 seconds per user) prevents cost abuse from excessive Bedrock API calls.

Cost optimization includes TTL-based cleanup that removes patterns older than 90 days, composite key queries with begins\_with() for instant lookups without table scans, and BatchWriteItem operations that reduce DynamoDB write operations by approximately 90%. Performance depends on function size, small functions (under 10 files) generate 10 test cases in 30–60 seconds, medium functions (10–50 files) take 1–3 minutes, and large functions (50\+ files) take 3–5 minutes, though using target filters to focus on specific code sections reduces time by 50–70%.

## Tools
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore-tools"></a>

**AWS services**
+ [Amazon Bedrock](https://aws.amazon.com/bedrock/) – Provides generative AI capabilities through Anthropic Claude Sonnet 4 for code analysis, test generation, validation, and rejection summarization. Always uses us-east-1 region for model access.
+ [Amazon Bedrock AgentCore ](https://docs.aws.amazon.com/bedrock-agentcore/)– Provides serverless agent runtime for deploying and hosting the test generation backend with automatic scaling, OAuth-based authorization, and CloudWatch observability.
+ [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) – Provides ML-based security filtering on all Bedrock API calls including prompt attack detection (HIGH strength), content filtering, PII anonymization (email, phone, name), blocking of AWS access keys/private keys/JWT tokens, and denied topic enforcement (exploit code generation, raw source code output). Deployed via CloudFormation.
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) – Automates complete infrastructure provisioning including DynamoDB table, Cognito User Pool, Amazon Bedrock Guardrail with versioning, and IAM execution role for AgentCore.
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/) – Provides user authentication with email-based sign-up, JWT token issuance, and secure API authorization for the AgentCore backend.
+ [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) – Stores accepted and rejected test patterns with usage statistics for continuous learning and improvement. Uses composite keys (function\_target, pattern\_sk) for zero-scan queries and target-specific pattern storage.
+ [AWS Lambda ](https://aws.amazon.com/lambda/)– Source of function code for analysis, the GetFunction API retrieves code and configuration. The tool supports Python, Node.js, Java, .NET, and Ruby runtimes.

**Other tools**
+ [Python 3.11\+](https://www.python.org/downloads/) – Runtime environment for the application and agent orchestration.
+ [Streamlit](https://streamlit.io/) – Web-based user interface for authentication, test generation, feedback collection, and system status monitoring.
+ [Boto3](https://docs.aws.amazon.com/boto3/latest/) – AWS SDK for Python to interact with Lambda, Amazon Bedrock, DynamoDB, and Cognito services.

**Code repository**

The code for this pattern is available in Github - [Lambda Test Event Generator](https://github.com/aws-samples/sample-lambda-test-event-generator).

## Best practices
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore-best-practices"></a>

This pattern implements the following best practices:
+ Uses [least-privilege IAM policies ](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)for AWS Lambda (read-only), Amazon Bedrock (invoke), Amazon DynamoDB (query/write), and Amazon Cognito (authentication) access.
+ Implement target-specific pattern learning with global fallback for improved test accuracy.
+ Enable DynamoDB TTL for automatic cleanup of old patterns (90 days) to control storage costs.
+ Use zero-scan queries with composite keys (function\_target, pattern\_sk) for fast pattern retrieval.
+ Apply ignore patterns to exclude test files, dependencies, and non-code files from analysis.
+ Use multi-language code chunking with Abstract Syntax Tree (AST) parsing (Python) and regex patterns (Java, C\#, JS, Ruby).
+ Store patterns with actual values (not just structure) for true deduplication.
+ Deploy backend on Amazon Bedrock AgentCore for serverless scaling and managed infrastructure.
+ Authenticate users via Amazon Cognito with JWT token validation on every API request.
+ Apply Amazon Bedrock Guardrails on all converse() calls for prompt attack filtering, PII redaction, sensitive data blocking (AWS keys, private keys, JWTs), and denied topic enforcement.
+ Sanitize analysis results before returning to users - all raw source code chunks are removed from responses, ensuring Lambda source code never leaves the AgentCore runtime boundary.
+ Validate all API inputs with regex patterns and length limits (function name max 170 chars, custom instructions max 2000 chars, max 50 ignore patterns) to prevent injection and abuse.
+ Implement per-user rate limiting (5 requests per 60 seconds) to prevent cost abuse from excessive Bedrock API calls.
+ Sanitize error messages before returning to users - internal file paths, AWS SDK details, and infrastructure information are never exposed in error responses.

Consider the following additional best practices:
+ Provide specific feedback reasons when rejecting test cases to improve learning accuracy.
+ Generate tests iteratively (2-3 times) for the same function to allow the system to learn and improve.
+ Provide custom instructions when you need specific test scenarios or data formats.
+ Enable IAM Access Analyzer to monitor resource permissions and identify unintended access.
+ Start with small Lambda functions to understand the system before analyzing large codebases.
+ Review IAM policies regularly and remove unused permissions.
+ Use strong password policies and enable Cognito AdvancedSecurityMode for threat detection.

## Epics
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore-epics"></a>

### Prepare the environment
<a name="prepare-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Clone the GitHub repository to your local system and navigate to the project directory:<pre>git clone https://github.com/aws-samples/sample-lambda-test-event-generator.git<br /><br />cd sample-lambda-test-event-generator</pre><br />This repository contains the Python application, CloudFormation template, and configuration files. | App developer |
| Configure AWS Credentials. | Configure your AWS credentials to enable the AWS CLI to interact with your AWS account and to enable the application to access Lambda functions you want to test. <br />You can do this using the AWS CLI configuration command:<pre>aws configure</pre><br />When prompted, provide the following information:+ **AWS Access Key ID**: Your AWS access key<br />+ **AWS Secret Access Key**: Your AWS secret access key<br />+ **Default region name**: The AWS region where you want to deploy the resources (e.g., `us-east-1`)<br />+ **Default output format**: The preferred output format (e.g., `json`) | App developer |

### Deploy the complete infrastructure
<a name="deploy-the-complete-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy infrastructure using CloudFormation. | 1. Deploy the complete backend infrastructure (DynamoDB, Cognito, IAM roles) using the provided CloudFormation template. Run the following command in your CLI:<pre>aws cloudformation create-stack \<br />      --stack-name lambda-test-generator-infra \<br />      --template-body file://cloudformation/complete-infrastructure.yaml \<br />      --capabilities CAPABILITY_NAMED_IAM \<br />      --region us-east-1</pre><br />2. Wait for the stack deployment to complete:<pre>aws cloudformation wait stack-create-complete \<br />      --stack-name lambda-test-generator-infra \<br />      --region us-east-1</pre><br />3. Retrieve all outputs:<pre>aws cloudformation describe-stacks \<br />      --stack-name lambda-test-generator-infra \<br />      --query 'Stacks[0].Outputs' \<br />      --output table</pre>What gets created:+ DynamoDB table with TTL enabled, point-in-time recovery, and server-side encryption. <br />+ Cognito User Pool with email authentication, AdvancedSecurityMode ENFORCED, optional MFA (TOTP), and admin-only user creation. <br />+ Amazon Bedrock Guardrail with prompt attack filtering, PII redaction, content filtering, and denied topic blocking. <br />+ IAM execution role for AgentCore with least-privilege policies including bedrock:ApplyGuardrail permission.The stack creates all required resources. Ensure the CloudFormation template completes successfully before proceeding to the next step. | App developer |
| Export configuration variables. | Export all values from the CloudFormation stack outputs as environment variables:<pre>export AGENTCORE_ROLE_ARN=$(aws cloudformation describe-stacks \<br />      --stack-name lambda-test-generator-infra \<br />      --query 'Stacks[0].Outputs[?OutputKey==`AgentCoreExecutionRoleArn`].OutputValue' \<br />      --output text)<br /><br />export DISCOVERY_URL=$(aws cloudformation describe-stacks \<br />      --stack-name lambda-test-generator-infra \<br />      --query 'Stacks[0].Outputs[?OutputKey==`DiscoveryUrl`].OutputValue' \<br />      --output text)<br /><br />export CLIENT_ID=$(aws cloudformation describe-stacks \<br />      --stack-name lambda-test-generator-infra \<br />      --query 'Stacks[0].Outputs[?OutputKey==`ClientId`].OutputValue' \<br />      --output text)<br /><br />export DYNAMODB_TABLE=$(aws cloudformation describe-stacks \<br />      --stack-name lambda-test-generator-infra \<br />      --query 'Stacks[0].Outputs[?OutputKey==`DynamoDBTableName`].OutputValue' \<br />      --output text)<br /><br />export COGNITO_POOL_ID=$(aws cloudformation describe-stacks \<br />      --stack-name lambda-test-generator-infra \<br />      --query 'Stacks[0].Outputs[?OutputKey==`UserPoolId`].OutputValue' \<br />      --output text)<br /><br />export BEDROCK_GUARDRAIL_ID=$(aws cloudformation describe-stacks \<br />  --stack-name lambda-test-generator-infra \<br />  --query 'Stacks[0].Outputs[?OutputKey==`BedrockGuardrailId`].OutputValue' \<br />  --output text)<br /><br />export BEDROCK_GUARDRAIL_VERSION=$(aws cloudformation describe-stacks \<br />  --stack-name lambda-test-generator-infra \<br />  --query 'Stacks[0].Outputs[?OutputKey==`BedrockGuardrailVersion`].OutputValue' \<br />  --output text)</pre><br />These variables are used in subsequent steps for AgentCore configuration and .env file creation. | AWS administrator |

### Set up the application environment and deploy AgentCore
<a name="set-up-the-application-environment-and-deploy-agentcore"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Create virtual environment. | 1. Create and activate a Python virtual environment to isolate project dependencies::<pre>python3 -m venv venv<br /><br />source venv/bin/activate</pre><br />2. Install the required Python packages from the requirements file:<pre>pip install -r requirements.txt </pre><br />This installs all necessary libraries including boto3 for AWS SDK, python-dotenv for environment configuration, bedrock-agentcore-runtime for AgentCore integration, and Streamlit for the user interface.The virtual environment must be activated (using `source venv/bin/activate`) each time you open a new terminal session to run the application. | App developer |
| Configure and deploy AgentCore. | + Configure the AgentCore agent:<pre>agentcore configure \<br />  --entrypoint main.py \<br />  --name lambda_test_generator \<br />  --requirements-file requirements.txt \<br />  --region us-east-1 \<br />  --execution-role $AGENTCORE_ROLE_ARN</pre><br />+ When prompted:<br />1. Deployment type: 1 (Direct Code Deploy - no Docker needed)<br />2. Python version: 2 (PYTHON\_3\_11 or select your particular Python Version)<br />3. S3 bucket: Press Enter (auto-create)<br />4. OAuth authorizer: yes<br />5. Discovery URL: Paste $DISCOVERY\_URL value<br />6. Client IDs: Paste $CLIENT\_ID value<br />7. Audience: Press Enter (leave empty)<br />8. Scopes: Press Enter (leave empty)<br />9. Custom claims: Press Enter (leave empty)<br />10. Request headers: yes<br />11. Headers: Authorization<br />12. Memory: s (skip - using DynamoDB)<br />+ Deploy the agent:<pre>agentcore deploy \<br />  --env DYNAMODB_TABLE_NAME=$DYNAMODB_TABLE \<br />  --env AWS_REGION=us-east-1 \<br />  --env BEDROCK_GUARDRAIL_ID=$BEDROCK_GUARDRAIL_ID \<br />  --env BEDROCK_GUARDRAIL_VERSION=$BEDROCK_GUARDRAIL_VERSION</pre><br />+ Get the AgentCore runtime ID and endpoint:<pre>RUNTIME_ID=$(agentcore status | grep "Agent ARN:" | sed 's/.*runtime\///' | sed 's/[│ ].*//')<br />AGENTCORE_ENDPOINT="https://bedrock-agentcore-runtime.us-east-1.amazonaws.com/agents/${RUNTIME_ID}/endpoints/DEFAULT"</pre> | App developer |
| Create .env file for local development. | Create a .env file in the project root directory with all configuration values:<pre>cat > .env << EOF<br />AWS_REGION=us-east-1<br />DYNAMODB_TABLE_NAME=$DYNAMODB_TABLE<br />COGNITO_POOL_ID=$COGNITO_POOL_ID<br />COGNITO_CLIENT_ID=$CLIENT_ID<br />COGNITO_REGION=us-east-1<br />AGENTCORE_ENDPOINT=$AGENTCORE_ENDPOINT<br />BEDROCK_GUARDRAIL_ID=$BEDROCK_GUARDRAIL_ID<br />BEDROCK_GUARDRAIL_VERSION=$BEDROCK_GUARDRAIL_VERSION<br />EOF</pre><br />Test connectivity to AWS services:<pre>aws dynamodb describe-table --table-name $DYNAMODB_TABLE<br />aws bedrock list-foundation-models --region us-east-1</pre><br />Both commands should return successful responses. If you encounter permission errors, verify that the IAM policies are properly configured. | App developer |

### Create a Cognito User
<a name="create-a-cognito-user"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new Cognito User. | The Cognito User Pool is configured with admin-only user creation for security, so users cannot self-register. Create a user via the AWS CLI using the Cognito Pool ID and Client ID exported from the CloudFormation stack outputs. Create a new user (replace `user@example.com` with your email):<pre>aws cognito-idp admin-create-user \<br />  --user-pool-id $COGNITO_POOL_ID \<br />  --username user@example.com \<br />  --user-attributes Name=email,Value=user@example.com Name=email_verified,Value=true \<br />  --temporary-password '[PASSWORD]!' \<br />  --region us-east-1</pre><br />Set a permanent password (minimum 8 characters, must include uppercase, lowercase, and a number):<pre>aws cognito-idp admin-set-user-password \<br />  --user-pool-id $COGNITO_POOL_ID \<br />  --username user@example.com \<br />  --password '[PASSWORD]!' \<br />  --permanent \<br />  --region us-east-1</pre><br />Use these credentials to sign in through the Streamlit UI in the next step. | App developer |

### Generate and validate test cases
<a name="generate-and-validate-test-cases"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch Streamlit UI. | Start the application:<pre>streamlit run app.py</pre><br />The UI will open in your default browser at `http://localhost:8501`<br />Sign in with the credentials created in the previous step | App developer |
| Configure generation options | In the UI, configure the following options:1. **Lambda function name or ARN**: Enter the target Lambda function identifier<br />2. **Target Filter** (Optional): Specify a function, class, or file to focus on (e.g., `validate_user`, `UserService`, `auth.py`)<br />3. **Ignore Patterns** (Optional): Add file or folder patterns to exclude, one per line:`tests/` - Ignore tests directory`*.test.js` - Ignore test files`mock_data/` - Ignore mock data<br />4. **Custom Instructions** (Optional): Add specific testing requirements | App developer |
| Generate test cases. | Click the **"Generate Test Cases"** button. The system will:1. Authenticate with AgentCore using Cognito JWT token.<br />2. Fetch Lambda code from AWS.<br />3. Apply ignore patterns to exclude unwanted files.<br />4. Chunk code using language-specific strategies.<br />5. Apply target filter if specified.<br />6. Analyze code with Amazon Bedrock.<br />7. Query DynamoDB for learned patterns.<br />8. Generate test cases.<br />9. Validate and rank test cases. | App developer |
| Review generated tests. | Review each generated test case, which includes:+ **Type**: Positive (valid inputs), Negative (invalid inputs), or Edge (boundary conditions)<br />+ **Description**: What the test validates<br />+ **Test data**: The actual test event payload | DevOps engineer, App developer |
| Provide feedback. | For each test case, provide feedback:<br />**To accept a test case:**+ Click the **"Accept"** button<br />**To reject a test case:**1. Click the **"Reject"** button<br />2. Select a rejection reason from the dropdown or add a custom reason<br />3. Click the **"Submit Rejection"** button | Test engineer |
| Save feedback to memory. | After reviewing all test cases:1. Click the **"Save All Feedback to Memory"** button<br />2. The system validates that all rejected cases have submitted reasons<br />3. Feedback is sent to AgentCore API which routes to the Validator Agent.<br />4. Feedback is batch-stored to DynamoDB with pattern hash for deduplication.<br />5. View the feedback summary showing accepted/rejected counts | Test engineer |
| Iterate for improvement. | Generate tests 2-3 more times for the same function to improve quality:+ The system retrieves learned patterns from DynamoDB<br />+ Quality improves with each iteration based on your feedback<br />+ Use target filter for focused testing on specific components<br />+ Use ignore patterns to exclude irrelevant code and improve generation qualityThe learning system becomes more effective with repeated use. Each feedback cycle helps the AI understand your testing preferences and generate more relevant test cases for your Lambda functions. | App developer |

### Direct API invocation (optional)
<a name="direct-api-invocation-optional"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Invoke AgentCore API directly. | For automation and integration, invoke the AgentCore backend directly using API calls with Cognito authentication.<br />Get a Cognito token:<br />`TOKEN=$(agentcore identity get-cognito-inbound-token)`<br />Invoke test generation:<pre>agentcore invoke --bearer-token "$TOKEN" '{"action": "generate_test_cases", "function_name": "your-lambda-function", "num_test_cases": 10,"custom_instructions": "Focus on authentication scenarios", "target_filter": "validate_user","ignore_patterns": ["tests/", "*.test.js"] }'</pre><br />Or using curl:<pre>curl -X POST "$AGENTCORE_ENDPOINT" \ -H "Authorization: Bearer $TOKEN" \ -H "Content-Type: application/json" \ -d '{ "action": "generate_test_cases", "function_name": "your-lambda-function", "num_test_cases": 10}'</pre> | App developer |

### Monitor and optimize
<a name="monitor-and-optimize"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Monitor DynamoDB patterns and track costs. | 1. Query the DynamoDB table to review accepted patterns and understand what the system has learned:<pre>aws dynamodb query \<br />  --table-name $DYNAMODB_TABLE \<br />  --key-condition-expression "function_target = :ft AND begins_with(pattern_sk, :prefix)" \<br />  --expression-attribute-values '{":ft":{"S":"my-function#GLOBAL"},":prefix":{"S":"FEEDBACK#accepted"}}'<br /></pre><br />Replace `my-function` with your actual Lambda function name to view patterns specific to that function.<br />2. Track resource consumption to optimize costs:**AWS Cost Explorer**: Monitor overall spending on Bedrock, DynamoDB, and Lambda services**Amazon Bedrock**: Review token usage and API call metrics in the Bedrock console**DynamoDB**: Check request metrics, consumed capacity, and storage usage.**AgentCore:** Monitor agent runtime metrics and invocation counts in CloudWatch<br />3. Use CloudWatch Logs to diagnose issues and monitor system behavior:**AgentCore logs:** <pre>aws logs tail /aws/bedrock-agentcore/runtimes/lambda_test_generator --follow</pre>**Application errors**: Review application-level errors and exceptions**Bedrock API responses**: Analyze AI model responses and token consumption**DynamoDB operations**: Monitor read/write patterns and throttling eventsRegular monitoring helps identify cost optimization opportunities and ensures the system continues to learn effectively. The TTL configuration on your DynamoDB table automatically cleans up old patterns, helping manage storage costs over time. | AWS administrator |

### Cleanup
<a name="cleanup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete deployed resources. | To remove all deployed resources:<br />Delete the AgentCore agent:<pre>agentcore destroy</pre><br />Delete the CloudFormation stack (deletes DynamoDB table, Cognito User Pool, and IAM role):<pre>aws cloudformation delete-stack <br />\ --stack-name lambda-test-generator-infra <br />\ --region us-east-1</pre> | AWS administrator |

## Troubleshooting
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| "Access Denied" error when fetching Lambda code | + Verify IAM permissions include `lambda:GetFunction` and `lambda:GetFunctionConfiguration` for the target Lambda function<br />+ Check your AWS CLI credentials<pre>aws sts get-caller-identity</pre> |
| "DynamoDB write errors" | + Verify the table name in your `.env` file matches the deployed table name<br />+ Check CloudFormation outputs:<pre>aws cloudformation describe-stacks --stack-name lambda-test-generator-infra --query 'Stacks[0].Outputs[?OutputKey=DynamoDBTableName].OutputValue' --output text</pre><br />+ Or verify directly:<pre>aws dynamodb describe-table --table-name $DYNAMODB_TABLE</pre> |
| No test cases generated | **Possible causes and solutions:**+ **Lambda function code is not accessible**: Check IAM permissions for Lambda access<br />+ **Lambda deployment package contains only compiled code**: `.class`, `.dll` files without source files cannot be analyzed<br />+ **All files filtered out by ignore patterns**: Review and adjust your ignore patterns<br />+ **Custom instructions are too restrictive**: Simplify or remove custom instructions<br />+ Verify the Lambda function exists:<pre>aws lambda get-function --function-name <name></pre> |
| Java/C\# Lambda shows "No source code found" | Java and C\# Lambdas require source files in the deployment package:<br />**Java (Maven):**1. Add source inclusion configuration to `pom.xml` (see `docs/JAVA_SETUP.md`)<br />2. Rebuild and redeploy your Lambda function<br />**C\# (.NET):**1. Include `.cs` files in build configuration (see `docs/CSHARP_SETUP.md`)<br />2. Rebuild and redeploy your Lambda function |
| DynamoDB write errors | + Check DynamoDB permissions and table status:+ Verify IAM policy includes `dynamodb:PutItem` and `dynamodb:BatchWriteItem`<br />+ Check table status: <pre>aws dynamodb describe-table --table-name $DYNAMODB_TABLE</pre><br />The table name includes the stack name suffix. Use the value from your CloudFormation outputs or .env file.+ Enable CloudWatch Logs for DynamoDB to see detailed error messages |
| Slow test generation | Optimize generation speed:1. **Use target filter** to focus on specific functions (50-70% faster)<br />2. **Add ignore patterns** to exclude test files, dependencies, and irrelevant code<br />3. **Reduce code size** by filtering out unnecessary files before analysis |
| AgentCore: "Agent not found" | Verify agent is deployed:<pre>agentcore status<br /><br />agentcore configure list</pre> |
| AgentCore: "Permission denied" at runtime | Verify execution role has correct policies:<pre>aws iam list-role-policies --role-name agentcore-exec-lambda-test-generator-infra</pre> |
| Cognito: "Invalid username or password" | Verify your credentials are correct. You can create a new user using the Streamlit UI's "Create Account" flow, or via the AWS CLI:<pre>aws cognito-idp admin-create-user --user-pool-id <POOL_ID> --username <username> --temporary-password '<password>' --region us-east-1</pre><pre>aws cognito-idp admin-set-user-password --user-pool-id <POOL_ID> --username <username> --password '<password>' --permanent --region us-east-1</pre> |
| "Bedrock Guardrail not configured" warning in logs | Verify `BEDROCK_GUARDRAIL_ID` and `BEDROCK_GUARDRAIL_VERSION` environment variables are set in the AgentCore deployment. <br />Check CloudFormation outputs: <pre>aws cloudformation describe-stacks --stack-name lambda-test-generator-infra --query 'Stacks[0].Outputs[?OutputKey==`BedrockGuardrailId`].OutputValue' --output text</pre> |
| "Rate limit exceeded" error | The system limits to 5 requests per 60 seconds per user. Wait the indicated time before retrying. For production use with higher throughput needs, adjust `RATE_LIMIT_MAX_REQUESTS` and `RATE_LIMIT_WINDOW` constants in main.py. |

## Related resources
<a name="automate-lambda-test-event-generation-using-bedrock-agentcore-resources"></a>

**AWS documentation**
+  [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/)
+  [Amazon Bedrock API Reference – InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
+ [ Amazon Bedrock AgentCore Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
+ [ AWS Lambda Developer Guide – Testing Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html)
+  [Amazon DynamoDB Developer Guide – Best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
+  [DynamoDB Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html)
+  [AWS CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation)
+ [ Amazon Cognito Developer Guide](https://docs.aws.amazon.com/cognito/)
+ [Infrastructure as code with CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [Amazon Bedrock Guardrails User Guide](https://aws.amazon.com/bedrock/guardrails/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
