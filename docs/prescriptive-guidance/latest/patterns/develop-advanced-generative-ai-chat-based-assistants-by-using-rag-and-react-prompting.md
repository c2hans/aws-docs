---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting.html
---

# Develop advanced generative AI chat-based assistants by using RAG and ReAct prompting
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting"></a>

*Praveen Kumar Jeyarajan, Shuai Cao, Noah Hamilton, Kiowa Jackson, Jundong Qiao, and Kara Yang, Amazon Web Services*

## Summary
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-summary"></a>

A typical corporation has 70 percent of its data trapped in siloed systems. You can use generative AI-powered chat-based assistants to unlock insights and relationships between these data silos through natural language interactions. To get the most out of generative AI, the outputs must be trustworthy, accurate, and inclusive of the available corporate data. Successful chat-based assistants depend on the following:
+ Generative AI models (such as Anthropic Claude 2)
+ Data source vectorization
+ Advanced reasoning techniques, such as the [ReAct framework](https://www.promptingguide.ai/techniques/react), for prompting the model

This pattern provides data-retrieval approaches from data sources such as Amazon Simple Storage Service (Amazon S3) buckets, AWS Glue, and Amazon Relational Database Service (Amazon RDS). Value is gained from that data by interleaving [Retrieval Augmented Generation (RAG)](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) with chain-of-thought methods. The results support complex chat-based assistant conversations that draw on the entirety of your corporation's stored data.

This pattern uses Amazon SageMaker manuals and pricing data tables as an example to explore the capabilities of a generative AI chat-based assistant. You will build a chat-based assistant that helps customers evaluate the SageMaker service by answering questions about pricing and the service's capabilities. The solution uses a Streamlit library for building the frontend application and the LangChain framework for developing the application backend powered by a large language model (LLM).

Inquiries to the chat-based assistant are met with an initial intent classification for routing to one of three possible workflows. The most sophisticated workflow combines general advisory guidance with complex pricing analysis. You can adapt the pattern to suit enterprise, corporate, and industrial use cases.

## Prerequisites and limitations
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-prereqs"></a>

**Prerequisites**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured
+ [AWS Cloud Development Kit (AWS CDK) Toolkit 2.114.1 or later](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and configured
+ Basic familiarity with Python and AWS CDK
+ [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
+ [Docker](https://docs.docker.com/get-docker/) installed
+ [Python 3.11 or later](https://www.python.org/downloads/) installed and configured (for more information, see the [Tools](#develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-tools) section)
+ An [active AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) bootstrapped by using [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)
+ Amazon Titan and Anthropic Claude [model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#add-model-access) enabled in the Amazon Bedrock service
+ [AWS security credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html), including `AWS_ACCESS_KEY_ID`, correctly configured in your terminal environment

**Limitations**
+ LangChain doesn't support every LLM for streaming. The Anthropic Claude models are supported, but models from AI21 Labs are not.
+ This solution is deployed to a single AWS account.
+ This solution can be deployed only in AWS Regions where Amazon Bedrock and Amazon Kendra are available. For information about availability, see the documentation for [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html#bedrock-regions) and [Amazon Kendra](https://docs.aws.amazon.com/general/latest/gr/kendra.html).

**Product versions**
+ Python version 3.11 or later
+ Streamlit version 1.30.0 or later
+ Streamlit-chat version 0.1.1 or later
+ LangChain version 0.1.12 or later
+ AWS CDK version 2.132.1 or later

## Architecture
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-architecture"></a>

**Target technology stack**
+ Amazon Athena
+ Amazon Bedrock
+ Amazon Elastic Container Service (Amazon ECS)
+ AWS Glue
+ AWS Lambda
+ Amazon S3
+ Amazon Kendra
+ Elastic Load Balancing

**Target architecture**

The AWS CDK code will deploy all the resources that are required to set up the chat-based assistant application in an AWS account. The chat-based assistant application shown in the following diagram is designed to answer SageMaker related queries from users. Users connect through an Application Load Balancer to a VPC that contains an Amazon ECS cluster hosting the Streamlit application. An orchestration Lambda function connects to the application. S3 bucket data sources provide data to the Lambda function through Amazon Kendra and AWS Glue. The Lambda function connects to Amazon Bedrock for answering queries (questions) from chat-based assistant users.

![Architecture diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b4df6405-76ab-4493-a722-15ceca067254/images/4e5856cf-9489-41f8-a411-e3b8d8a50748.png)

1. The orchestration Lambda function sends the LLM prompt request to the Amazon Bedrock model (Claude 2).

1. Amazon Bedrock sends the LLM response back to the orchestration Lambda function.

**Logic flow within the orchestration Lambda function**

When users ask a question through the Streamlit application, it invokes the orchestration Lambda function directly. The following diagram shows the logic flow when the Lambda function is invoked.

![Architecture diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b4df6405-76ab-4493-a722-15ceca067254/images/70ae4736-06a6-4d3a-903a-edc5c10d78a0.png)

+ Step 1 – The input `query` (question) is classified into one of the three intents:
  + General SageMaker guidance questions
  + General SageMaker pricing (training/inference) questions
  + Complex questions related to SageMaker and pricing
+ Step 2 – The input `query` initiates one of the three services:
  + `RAG Retrieval service`, which retrieves relevant context from the [Amazon Kendra](https://aws.amazon.com/kendra/) vector database and calls the LLM through [Amazon Bedrock](https://aws.amazon.com/bedrock/) to summarize the retrieved context as the response.
  + `Database Query service`, which uses- the LLM, database metadata, and sample rows from relevant tables to convert the input `query` into a SQL query. Database Query service runs the SQL query against the SageMaker pricing database through [Amazon Athena](https://aws.amazon.com/athena/) and summarizes the query results as the response.
  + `In-context ReACT Agent service`, which breaks down the input `query` into multiple steps before providing a response. The agent uses `RAG Retrieval service` and `Database Query service` as tools to retrieve relevant information during the reasoning process. After the reasoning and actions processes are complete, the agent generates the final answer as the response.
+ Step 3 – The response from the orchestration Lambda function is sent to the Streamlit application as output.

## Tools
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon Simple Storage Service (Amazon S3) by using standard SQL.
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.
+ [AWS Glue](https://docs.aws.amazon.com/glue/) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams. This pattern uses an AWS Glue crawler and an AWS Glue Data Catalog table.
+ [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) is an intelligent search service that uses natural language processing and advanced machine learning algorithms to return specific answers to search questions from your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses in one or more Availability Zones.

**Code repository**

The code for this pattern is available in the GitHub [genai-bedrock-chatbot](https://github.com/awslabs/genai-bedrock-chatbot) repository.

The code repository contains the following files and folders:
+ `assets` folder – The static assets the architecture diagram and the public dataset
+ `code/lambda-container` folder – The Python code that is run in the Lambda function
+ `code/streamlit-app` folder – The Python code that is run as the container image in Amazon ECS
+ `tests` folder – The Python files that are run to unit test the AWS CDK constructs
+ `code/code_stack.py` – The AWS CDK construct Python files used to create AWS resources
+ `app.py` – The AWS CDK stack Python files used to deploy AWS resources in the target AWS account
+ `requirements.txt` – The list of all Python dependencies that must be installed for AWS CDK
+ `requirements-dev.txt` – The list of all Python dependencies that must be installed for AWS CDK to run the unit-test suite
+ `cdk.json` – The input file to provide values required to spin up resources

|
|
| Note: The AWS CDK code uses [L3 (layer 3) constructs](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) and [AWS Identity and Access Management (IAM) policies managed by AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) for deploying the solution. |
| --- |

## Best practices
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-best-practices"></a>
+ The code example provided here is for a proof-of-concept (PoC) or pilot demo only. If you want to take the code to Production, be sure to use the following best practices:
  + [Amazon S3 access logging is enabled](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html).
  + [VPC Flow Logs is enabled](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html).
  + The [Amazon Kendra Enterprise Edition index](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/amazon-kendra.html) is enabled.
+ Set up monitoring and alerting for the Lambda function. For more information, see [Monitoring and troubleshooting Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html). For general best practices when working with Lambda functions, see the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

## Epics
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-epics"></a>

### Set up AWS credentials on your local machine
<a name="set-up-aws-credentials-on-your-local-machine"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Export variables for the account and AWS Region where the stack will be deployed. | To provide AWS credentials for AWS CDK by using environment variables, run the following commands.<pre>export CDK_DEFAULT_ACCOUNT=<12 Digit AWS Account Number><br />export CDK_DEFAULT_REGION=<region></pre> | DevOps engineer, AWS DevOps |
| Set up the AWS CLI profile. | To set up the AWS CLI profile for the account, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/keys-profiles-credentials.html). | DevOps engineer, AWS DevOps |

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repo on your local machine. | To clone the repository, run the following command in your terminal.<pre>git clone https://github.com/awslabs/genai-bedrock-chatbot.git</pre> | DevOps engineer, AWS DevOps |
| Set up the Python virtual environment and install required dependencies. | To set up the Python virtual environment, run the following commands.<pre>cd genai-bedrock-chatbot<br />python3 -m venv .venv<br />source .venv/bin/activate</pre><br />To set up the required dependencies, run the following command.<pre>pip3 install -r requirements.txt</pre> | DevOps engineer, AWS DevOps |
| Set up the AWS CDK environment and synthesize the AWS CDK code. | 1. To set up the AWS CDK environment in your AWS account, run the following command.<pre>cdk bootstrap aws://ACCOUNT-NUMBER/REGION</pre><br />2. To convert the code to an AWS CloudFormation stack configuration, run the command `cdk synth`. | DevOps engineer, AWS DevOps |

### Configure and deploy the chat-based assistant application
<a name="configure-and-deploy-the-chat-based-assistant-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provision Claude model access. | To enable Anthropic Claude model access for your AWS account, follow the instructions in the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#add-model-access). | AWS DevOps |
| Deploy resources in the account. | To deploy resources in the AWS account by using the AWS CDK, do the following:1. In the root of the cloned repository, in the `cdk.json` file, provide inputs for the `logging` parameters. Example values are `INFO`, `DEBUG`, `WARN`, and `ERROR`.<br />These values define log-level messages for the Lambda function and the Streamlit application.<br />2. The `app.py` file in the root of the cloned repository contains the AWS CloudFormation stack name used for deployment. The default stack name is `chatbot-stack`.<br />3. To deploy resources, run the command `cdk deploy`.<br />The `cdk deploy` command uses L3 constructs to create multiple Lambda functions for copying documents and CSV dataset files to S3 buckets.<br />4. After the command is complete, sign in to the AWS Management Console, open the CloudFormation console, and [review that the stack deployed successfully](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-review.html).<br />Upon successful deployment, you can access the chat-based assistant application by using the URL provided in the CloudFormation **Outputs** section. | AWS DevOps, DevOps engineer |
| Run the AWS Glue crawler and create the Data Catalog table. | An [AWS Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) is used to keep the data schema dynamic. The solution creates and updates partitions in the [AWS Glue Data Catalog table](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html) by running the crawler on demand. After the CSV dataset files are copied into the S3 bucket, run the AWS Glue crawler and create the Data Catalog table schema for testing:1. Navigate to the AWS Glue console.<br />2. In the navigation pane, under **Data Catalog**, choose **Crawlers**.<br />3. Select the crawler with suffix `sagemaker-pricing-crawler`.<br />4. Run the crawler.<br />5. After the crawler runs successfully, it creates an AWS Glue Data Catalog table.The AWS CDK code configures the AWS Glue crawler to run on demand, but you can also [schedule](https://docs.aws.amazon.com/glue/latest/dg/schedule-crawler.html) it to run periodically. | DevOps engineer, AWS DevOps |
| Initiate document indexing. | After the files are copied into the S3 bucket, use Amazon Kendra to crawl and index them:1. Navigate to the Amazon Kendra console.<br />2. Select the index with the suffix `chatbot-index`.<br />3. In the navigation pane, choose **Data sources**, and select the data source connector with the suffix `chatbot-index`.<br />4. Choose **Sync Now** to initiate the indexing process.The AWS CDK code configures the Amazon Kendra index sync to run on demand, but you can also run periodically by using the [Schedule parameter](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html#cron). | AWS DevOps, DevOps engineer |

### Clean up all AWS resources in the solution
<a name="clean-up-all-aws-resources-in-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the AWS resources. | After you test the solution, clean up the resources:1. To remove AWS resources deployed by the solution, run the command `cdk destroy`.<br />2. Delete all objects from the two S3 buckets, and then remove the buckets.<br />For more information, see [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html). | DevOps engineer, AWS DevOps |

## Troubleshooting
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS CDK returns errors. | For help with AWS CDK issues, see [Troubleshooting common AWS CDK issues](https://docs.aws.amazon.com/cdk/v2/guide/troubleshooting.html). |

## Related resources
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-resources"></a>
+ Amazon Bedrock:
  + [Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
  + [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)
+ [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
+ [Get started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
+ [Working with the AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
+ [Generative AI Application Builder on AWS](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/solution-overview.html)
+ [LangChain documentation](https://python.langchain.com/docs/get_started/introduction)
+ [Streamlit documentation](https://docs.streamlit.io/)

## Additional information
<a name="develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting-additional"></a>

**AWS CDK commands**

When working with AWS CDK, keep in mind the following useful commands:
+ Lists all stacks in the app

  ```
  cdk ls
  ```
+ Emits the synthesized AWS CloudFormation template

  ```
  cdk synth
  ```
+ Deploys the stack to your default AWS account and Region

  ```
  cdk deploy
  ```
+ Compares the deployed stack with the current state

  ```
  cdk diff
  ```
+ Opens the AWS CDK documentation

  ```
  cdk docs
  ```
+ Deletes the CloudFormation stack and removes AWS deployed resources

  ```
  cdk destroy
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
