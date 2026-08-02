---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe.html
---

# Document institutional knowledge from voice inputs by using Amazon Bedrock and Amazon Transcribe
<a name="document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe"></a>

*Praveen Kumar Jeyarajan, Jundong Qiao, Rajiv Upadhyay, and Megan Wu, Amazon Web Services*

## Summary
<a name="document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe-summary"></a>

Capturing institutional knowledge is paramount for ensuring organizational success and resilience. Institutional knowledge represents the collective wisdom, insights, and experiences accumulated by employees over time, often tacit in nature and passed down informally. This wealth of information encompasses unique approaches, best practices, and solutions to intricate problems that might not be documented elsewhere. By formalizing and documenting this knowledge, companies can preserve institutional memory, foster innovation, enhance decision-making processes, and accelerate learning curves for new employees. Additionally, it promotes collaboration, empowers individuals, and cultivates a culture of continuous improvement. Ultimately, harnessing institutional knowledge helps companies use their most valuable asset—the collective intelligence of their workforce—to navigate challenges, drive growth, and maintain competitive advantage in dynamic business environments.

This pattern explains how to capture institutional knowledge through voice recordings from senior employees. It uses [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) and [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) for systematic documentation and verification. By documenting this informal knowledge, you can preserve it and share it with subsequent cohorts of employees. This endeavor supports operational excellence and improves the effectiveness of training programs through the incorporation of practical knowledge acquired through direct experience.

## Prerequisites and limitations
<a name="document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Docker, [installed](https://docs.docker.com/engine/install/)
+ AWS Cloud Development Kit (AWS CDK) version 2.114.1 or later, [installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_tools) and [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_bootstrap) to the `us-east-1` or `us-west-2` AWS Regions
+ AWS CDK Toolkit version 2.114.1 or later, [installed](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ Python version 3.12 or later, [installed](https://www.python.org/downloads/)
+ Permissions to create Amazon Transcribe, Amazon Bedrock, Amazon Simple Storage Service (Amazon S3), and AWS Lambda resources

**Limitations**
+ This solution is deployed to a single AWS account.
+ This solution can be deployed only in AWS Regions where Amazon Bedrock and Amazon Transcribe are available. For information about availability, see the documentation for [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-regions.html) and [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html#tsc-regions).
+ The audio files must be in a format that Amazon Transcribe supports. For a list of supported formats, see [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) in the Transcribe documentation.

**Product versions**
+ AWS SDK for Python (Boto3) version 1.34.57 or later
+ LangChain version 0.1.12 or later

## Architecture
<a name="document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe-architecture"></a>

The architecture represents a serverless workflow on AWS. [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) orchestrates Lambda functions for audio processing, text analysis, and document generation. The following diagram shows the Step Functions workflow, also known as a *state machine*.

![Architecture diagram of Step Functions state machine generating a document](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f1e0106d-b046-4adc-9718-c299efb7b436/images/e90298ca-1b7f-4c3e-97bd-311a9d5a4997.png)

Each step in the state machine is handled by a distinct Lambda function. The following are the steps in the document generation process:

1. The `preprocess` Lambda function validates the input passed to Step Functions and lists all of the audio files present in the provided Amazon S3 URI folder path. Downstream Lambda functions in the workflow use the file list to validate, summarize, and generate the document.

1. The `transcribe` Lambda function uses Amazon Transcribe to convert audio files into text transcripts. This Lambda function is responsible for initiating the transcription process and accurately transforming speech into text, which is then stored for subsequent processing.

1. The `validate` Lambda function analyzes the text transcripts, determining the relevance of the responses to the initial questions. By using a large language model (LLM) through Amazon Bedrock, it identifies and separates on-topic answers from off-topic responses.

1. The `summarize` Lambda function uses Amazon Bedrock to generate a coherent and concise summary of the on-topic answers.

1. The `generate` Lambda function assembles the summaries into a well-structured document. It can format the document according to predefined templates and include any additional necessary content or data.

1. If any of the Lambda functions fail, you receive an email notification through Amazon Simple Notification Service (Amazon SNS).

Throughout this process, AWS Step Functions makes sure that each Lambda function is initiated in the correct sequence. This state machine has the capacity for parallel processing to enhance efficiency. An Amazon S3 bucket acts as the central storage repository, supporting the workflow by managing the various media and document formats involved.

## Tools
<a name="document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe-tools"></a>

**AWS services**
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) is an automatic speech recognition service that uses machine learning models to convert audio to text.

**Other tools**
+ [LangChain](https://python.langchain.com/docs/get_started/introduction/) is a framework for developing applications that are powered by large language models (LLMs).

**Code repository**

The code for this pattern is available in the GitHub [genai-knowledge-capture](https://github.com/aws-samples/genai-knowledge-capture) repository.

The code repository contains the following files and folders:
+ `assets` folder – The static assets for the solution, such as the architecture diagram and the public dataset
+ `code/lambdas` folder – The Python code for all Lambda functions
  + `code/lambdas/generate` folder - The Python code that generates a document from the summarized data in the S3 bucket
  + `code/lambdas/preprocess` folder - The Python code that processes the inputs for the Step Functions state machine
  + `code/lambdas/summarize` folder - The Python code that summarizes the transcribed data by using Amazon Bedrock service
  + `code/lambdas/transcribe` folder - The Python code that converts speech data (audio file) into text by using Amazon Transcribe
  + `code/lambdas/validate` folder - The Python code that validates whether all answers pertain to the same topic
+ `code/code_stack.py` – The AWS CDK construct Python file that is used to create AWS resources
+ `app.py` – The AWS CDK app Python file that is used to deploy AWS resources in the target AWS account
+ `requirements.txt` – The list of all Python dependencies that must be installed for the AWS CDK
+ `cdk.json` – The input file to provide values that are required to create resources

## Best practices
<a name="document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe-best-practices"></a>

The code example provided is for proof-of-concept (PoC) or pilot purposes only. If you want to take the solution to production, use the following best practices:
+ Enable [Amazon S3 access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html)
+ Enable [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

## Epics
<a name="document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe-epics"></a>

### Set up AWS credentials on your local workstation
<a name="set-up-aws-credentials-on-your-local-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Export variables for the account and AWS Region. | To provide AWS credentials for the AWS CDK by using environment variables, run the following commands.<pre>export CDK_DEFAULT_ACCOUNT=<12-digit AWS account number><br />export CDK_DEFAULT_REGION=<Region></pre> | AWS DevOps, DevOps engineer |
| Set up the AWS CLI named profile. | To set up the AWS CLI named profile for the account, follow the instructions in [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). | AWS DevOps, DevOps engineer |

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repo to your local workstation. | To clone the [genai-knowledge-capture](https://github.com/aws-samples/genai-knowledge-capture) repository, run the following command in your terminal.<pre>git clone https://github.com/aws-samples/genai-knowledge-capture</pre> | AWS DevOps, DevOps engineer |
| (Optional) Replace the audio files. | To customize the sample application to incorporate your own data, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe.html) | AWS DevOps, DevOps engineer |
| Set up the Python virtual environment. | To set up the Python virtual environment, run the following commands.<pre>cd genai-knowledge-capture<br />python3 -m venv .venv<br />source .venv/bin/activate<br />pip install -r requirements.txt</pre> | AWS DevOps, DevOps engineer |
| Synthesize the AWS CDK code. | To convert the code to an AWS CloudFormation stack configuration, run the following command.<pre>cdk synth</pre> | AWS DevOps, DevOps engineer |

### Configure and deploy the solution
<a name="configure-and-deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provision foundation model access. | Enable access to the Anthropic Claude 3 Sonnet model for your AWS account. For instructions, see [Add model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-add) in the Bedrock documentation. | AWS DevOps |
| Deploy resources in the account. | To deploy resources in the AWS account by using the AWS CDK, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe.html) | AWS DevOps, DevOps engineer |
| Subscribe to the Amazon SNS topic. | To subscribe to the Amazon SNS topic for notification, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe.html) | General AWS |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the state machine. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe.html) | App developer, General AWS |

### Clean up all AWS resources in the solution
<a name="clean-up-all-aws-resources-in-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the AWS resources. | After you test the solution, clean up the resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe.html) | AWS DevOps, DevOps engineer |

## Related resources
<a name="document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe-resources"></a>

**AWS documentation**
+ Amazon Bedrock resources:
  + [Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
  + [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)
+ AWS CDK resources:
  + [Get started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
  + [Working with the AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
  + [Troubleshooting common AWS CDK issues](https://docs.aws.amazon.com/cdk/v2/guide/troubleshooting.html)
  + [Toolkit commands](https://docs.aws.amazon.com/cdk/v2/guide/cli.html#cli-commands)
+ AWS Step Functions resources:
  + [Getting started with AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started-with-sfn.html)
  + [Troubleshooting](https://docs.aws.amazon.com/step-functions/latest/dg/troubleshooting.html)
+ [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
+ [Generative AI Application Builder on AWS](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/solution-overview.html)

**Other resources**
+ [LangChain documentation](https://python.langchain.com/docs/get_started/introduction)
