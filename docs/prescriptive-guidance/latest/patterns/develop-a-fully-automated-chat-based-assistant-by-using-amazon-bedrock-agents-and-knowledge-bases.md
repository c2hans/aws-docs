---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases.html
---

# Develop a fully automated chat-based assistant by using Amazon Bedrock agents and knowledge bases
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases"></a>

*Jundong Qiao, Shuai Cao, Noah Hamilton, Kiowa Jackson, Praveen Kumar Jeyarajan, and Kara Yang, Amazon Web Services*

## Summary
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-summary"></a>

Many organizations face challenges when creating a chat-based assistant that is capable of orchestrating diverse data sources to offer comprehensive answers. This pattern presents a solution for developing a chat-based assistant that is capable of answering queries from both documentation and databases, with a straightforward deployment.

Starting with [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), this fully managed generative artificial intelligence (AI) service provides a wide array of advanced foundation models (FMs). This facilitates the efficient creation of generative AI applications with a strong focus on privacy and security. In the context of documentation retrieval, the [Retrieval Augmented Generation (RAG)](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html) is a pivotal feature. It uses [knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) to augment FM prompts with contextually relevant information from external sources. An [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) index serves as the vector database behind the knowledge bases for Amazon Bedrock. This integration is enhanced through careful prompt engineering to minimize inaccuracies and make sure that responses are anchored in factual documentation. For database queries, the FMs of Amazon Bedrock transform textual inquiries into structured SQL queries, incorporating specific parameters. This enables the precise retrieval of data from databases managed by [AWS Glue databases](https://docs.aws.amazon.com/glue/latest/dg/define-database.html). [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is used for these queries.

For handling more intricate queries, achieving comprehensive answers demands information sourced from both documentation and databases. [Agents for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) is a generative AI feature that helps you build autonomous agents that can understand complex tasks and break them down into simpler tasks for orchestration. The combination of insights retrieved from the simplified tasks, facilitated by Amazon Bedrock autonomous agents, enhances the synthesis of information, leading to more thorough and exhaustive answers. This pattern demonstrates how to build a chat-based assistant by using Amazon Bedrock and the related generative AI services and features within an automated solution.

## Prerequisites and limitations
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Docker, [installed](https://docs.docker.com/engine/install/)
+ AWS Cloud Development Kit (AWS CDK), [installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_tools) and [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_bootstrap) to the `us-east-1` or `us-west-2` AWS Regions
+ AWS CDK Toolkit version 2.114.1 or later, [installed](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ Python version 3.11 or later, [installed](https://www.python.org/downloads/)
+ In Amazon Bedrock, [enable access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) to Claude 2, Claude 2.1, Claude Instant, and Titan Embeddings G1 – Text

**Limitations**
+ This solution is deployed to a single AWS account.
+ This solution can be deployed only in AWS Regions where Amazon Bedrock and Amazon OpenSearch Serverless are supported. For more information, see the documentation for [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-regions.html) and [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html#serverless-regions).

**Product versions**
+ Llama-index version 0.10.6 or later
+ Sqlalchemy version 2.0.23 or later
+ Opensearch-py version 2.4.2 or later
+ Requests\_aws4auth version 1.2.3 or later
+ AWS SDK for Python (Boto3) version 1.34.57 or later

## Architecture
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-architecture"></a>

**Target technology stack **

The [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is an open source software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. The AWS CDK stack used in this pattern deploys the following AWS resources:
+ AWS Key Management Service (AWS KMS)
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Glue Data Catalog, for the AWS Glue database component
+ AWS Lambda
+ AWS Identity and Access Management (IAM)
+ Amazon OpenSearch Serverless
+ Amazon Elastic Container Registry (Amazon ECR)
+ Amazon Elastic Container Service (Amazon ECS)
+ AWS Fargate
+ Amazon Virtual Private Cloud (Amazon VPC)
+ [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

**Target architecture **

![Architecture diagram using an Amazon Bedrock knowledge base and agent](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/15372718-3a5d-4918-9cfa-422c455f288d/images/ff19152e-0bb6-4758-a6dd-4f6140e55113.png)

The diagram shows a comprehensive AWS cloud-native setup within a single AWS Region, using multiple AWS services. The primary interface for the chat-based assistant is a [Streamlit](https://docs.streamlit.io/) application hosted on an Amazon ECS cluster. An [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) manages accessibility. Queries made through this interface activate the `Invocation` Lambda function, which then interfaces with agents for Amazon Bedrock. This agent responds to user inquiries by either consulting the knowledge bases for Amazon Bedrock or by invoking an `Agent executor` Lambda function. This function triggers a set of actions associated with the agent, following a predefined API schema. The knowledge bases for Amazon Bedrock use an OpenSearch Serverless index as their vector database foundation. Additionally, the `Agent executor` function generates SQL queries that are executed against the AWS Glue database through Amazon Athena.

## Tools
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon Simple Storage Service (Amazon S3) by using standard SQL.
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.
+ [Elastic Load Balancing ](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses in one or more Availability Zones.
+ [AWS Glue](https://docs.aws.amazon.com/glue/) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams. This pattern uses an AWS Glue crawler and an AWS Glue Data Catalog table.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) is an on-demand serverless configuration for Amazon OpenSearch Service. In this pattern, an OpenSearch Serverless index serves as a vector database for the knowledge bases for Amazon Bedrock.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [Streamlit](https://docs.streamlit.io/) is an open source Python framework to create data applications.

**Code repository**

The code for this pattern is available in the GitHub [genai-bedrock-agent-chatbot](https://github.com/awslabs/genai-bedrock-agent-chatbot/) repository. The code repository contains the following files and folders:
+ `assets` folder – The static assets, such as the architecture diagram and the public dataset.
+ `code/lambdas/action-lambda` folder – The Python code for the Lambda function that acts as an action for the Amazon Bedrock agent.
+ `code/lambdas/create-index-lambda` folder – The Python code for the Lambda function that creates the OpenSearch Serverless index.
+ `code/lambdas/invoke-lambda` folder – The Python code for the Lambda function that invokes the Amazon Bedrock agent, which is called directly from the Streamlit application.
+ `code/lambdas/update-lambda` folder – The Python code for the Lambda function that updates or deletes resources after the AWS resources are deployed through the AWS CDK.
+ `code/layers/boto3_layer` folder – The AWS CDK stack that creates a Boto3 layer that is shared across all Lambda functions.
+ `code/layers/opensearch_layer` folder – The AWS CDK stack that creates an OpenSearch Serverless layer that installs all dependencies to create the index.
+ `code/streamlit-app` folder – The Python code that is run as the container image in Amazon ECS.
+ `code/code_stack.py` – The AWS CDK construct Python files that create AWS resources.
+ `app.py` – The AWS CDK stack Python files that deploy AWS resources in the target AWS account.
+ `requirements.txt` – The list of all Python dependencies that must be installed for the AWS CDK.
+ `cdk.json` – The input file to provide the values that are required to create resources. Also, in the `context/config` fields, you can customize the solution accordingly. For more information about customization, see the [Additional information](#develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-additional) section.

## Best practices
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-best-practices"></a>
+ The code example provided here is for proof-of-concept (PoC) or pilot purposes only. If you want to take the code to production, be sure to use the following best practices:
  + Enable [Amazon S3 access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html)
  + Enable [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+ Set up monitoring and alerting for the Lambda functions. For more information, see [Monitoring and troubleshooting Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html). For best practices, see the [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

## Epics
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-epics"></a>

### Set up AWS credentials on your local workstation
<a name="set-up-aws-credentials-on-your-local-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Export variables for the account and Region. | To provide AWS credentials for the AWS CDK by using environment variables, run the following commands.<pre>export CDK_DEFAULT_ACCOUNT=<12-digit AWS account number><br />export CDK_DEFAULT_REGION=<Region></pre> | AWS DevOps, DevOps engineer |
| Set up the AWS CLI named profile. | To set up the AWS CLI named profile for the account, follow the instructions in [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). | AWS DevOps, DevOps engineer |

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repo to your local workstation. | To clone the repository, run the following command in your terminal.<pre>git clone https://github.com/awslabs/genai-bedrock-agent-chatbot.git</pre> | DevOps engineer, AWS DevOps |
| Set up the Python virtual environment. | To set up the Python virtual environment, run the following commands.<pre>cd genai-bedrock-agent-chatbot<br />python3 -m venv .venv<br />source .venv/bin/activate</pre><br />To set up the required dependencies, run the following command.<pre>pip3 install -r requirements.txt</pre> | DevOps engineer, AWS DevOps |
| Set up the AWS CDK environment. | To convert the code to an AWS CloudFormation template, run the command `cdk synth`. | AWS DevOps, DevOps engineer |

### Configure and deploy the application
<a name="configure-and-deploy-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy resources in the account. | To deploy resources in the AWS account by using the AWS CDK, do the following:1. In the root of the cloned repository, in the `cdk.json` file, provide inputs for the logging parameters. Example values are `INFO`, `DEBUG`, `WARN`, and `ERROR`.<br />These values define log-level messages for the Lambda functions and the Streamlit application.<br />2. The `cdk.json` file in the root of the cloned repository contains the AWS CloudFormation stack name used for deployment. The default stack name is `chatbot-stack`. The default Amazon Bedrock agent name is `ChatbotBedrockAgent`, and the default Amazon Bedrock agent alias is `Chatbot_Agent`.<br />3. To deploy resources, run the command `cdk deploy`. The `cdk deploy` command uses layer-3 constructs to create multiple Lambda functions for copying documents and CSV dataset files to S3 buckets. It also deploys the Amazon Bedrock agent, knowledge bases, and `Action group` Lambda function for the Amazon Bedrock agent.<br />4. Sign in to the AWS Management Console, and then open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />5. Confirm that the stack deployed successfully. For instructions, see [Reviewing your stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-review.html).<br />After successful deployment, you can access the chat-based assistant application by using the URL provided on the **Outputs** tab in the CloudFormation console. | DevOps engineer, AWS DevOps |

### Clean up all AWS resources in the solution
<a name="clean-up-all-aws-resources-in-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the AWS resources. | After you test the solution, to clean up the resources, run the command `cdk destroy`. | AWS DevOps, DevOps engineer |

## Related resources
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-resources"></a>

**AWS documentation**
+ Amazon Bedrock resources:
  + [Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
  + [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)
  + [Agents for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
  + [Knowledge bases for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
+ [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
+ AWS CDK resources:
  + [Get started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
  + [Troubleshooting common AWS CDK issues](https://docs.aws.amazon.com/cdk/v2/guide/troubleshooting.html)
  + [Working with the AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
+ [Generative AI Application Builder on AWS](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/solution-overview.html)

**Other AWS resources**
+ [Vector Engine for Amazon OpenSearch Serverless](https://aws.amazon.com/opensearch-service/serverless-vector-engine/)

**Other resources**
+ [LlamaIndex documentation](https://docs.llamaindex.ai/en/stable/)
+ [Streamlit documentation](https://docs.streamlit.io/)

## Additional information
<a name="develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-additional"></a>

**Customize the chat-based assistant with your own data**

To integrate your custom data for deploying the solution, follow these structured guidelines. These steps are designed to ensure a seamless and efficient integration process, enabling you to deploy the solution effectively with your bespoke data.

*For knowledge base data integration*

**Data preparation**

1. Locate the `assets/knowledgebase_data_source/` directory.

1. Place your dataset within this folder.

**Configuration adjustments**

1. Open the `cdk.json` file.

1. Navigate to the `context/configure/paths/knowledgebase_file_name` field, and then update it accordingly.

1. Navigate to the `bedrock_instructions/knowledgebase_instruction` field, and then update it to accurately reflect the nuances and context of your new dataset.

*For structural data integration*

**Data organization**

1. Within the `assets/data_query_data_source/` directory, create a subdirectory, such as `tabular_data`.

1. Put your structured dataset (acceptable formats include CSV, JSON, ORC, and Parquet) into this newly created subfolder.

1. If you are connecting to an existing database, update the function `create_sql_engine()` in `code/lambda/action-lambda/build_query_engine.py` to connect to your database.

**Configuration and code updates**

1. In the `cdk.json` file, update the `context/configure/paths/athena_table_data_prefix` field to align with the new data path.

1. Revise `code/lambda/action-lambda/dynamic_examples.csv` by incorporating new text-to-SQL examples that correspond with your dataset.

1. Revise `code/lambda/action-lambda/prompt_templates.py` to mirror the attributes of your structured dataset.

1. In the `cdk.json` file, update the `context/configure/bedrock_instructions/action_group_description` field to explain the purpose and functionality of the `Action group` Lambda function.

1. In the `assets/agent_api_schema/artifacts_schema.json` file, explain the new functionalities of your `Action group` Lambda function.

*General update*

In the `cdk.json` file, in the `context/configure/bedrock_instructions/agent_instruction` section, provide a comprehensive description of the Amazon Bedrock agent's intended functionality and design purpose, taking into account the newly integrated data.
