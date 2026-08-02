---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html
---

# Copy Amazon ECR container images across AWS accounts and AWS Regions
<a name="copy-ecr-container-images-across-accounts-regions"></a>

*Faisal Shahdad, Amazon Web Services*

## Summary
<a name="copy-ecr-container-images-across-accounts-regions-summary"></a>

This pattern shows you how to use a serverless approach to replicate tagged images from existing Amazon Elastic Container Registry (Amazon ECR) repositories to other AWS accounts and AWS Regions. The solution uses AWS Step Functions to manage the replication workflow and AWS Lambda functions to copy large container images.

Amazon ECR uses native [cross-Region](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-settings-examples.html#registry-settings-examples-crr-single) and [cross-account](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-settings-examples.html#registry-settings-examples-crossaccount) replication features that replicate container images across Regions and accounts. But these features replicate images only from the moment replication is turned on. There is no mechanism to replicate existing images in different Regions and accounts.

This pattern helps artificial intelligence (AI) teams distribute containerized machine learning (ML) models, frameworks (for example, PyTorch, TensorFlow, and Hugging Face), and dependencies to other accounts and Regions. This can help you overcome service limits and optimize GPU compute resources. You can also selectively replicate Amazon ECR repositories from specific source accounts and Regions. For more information, see [Cross-Region replication in Amazon ECR has landed](https://aws.amazon.com/blogs/containers/cross-region-replication-in-amazon-ecr-has-landed/).

## Prerequisites and limitations
<a name="copy-ecr-container-images-across-accounts-regions-prereqs"></a>

**Prerequisites**
+ Two or more active AWS accounts (one source account and one destination account, minimally)
+ Appropriate AWS Identity and Access Management (IAM) permissions in all accounts
+ Docker for building the Lambda container image
+ AWS Command Line Interface (AWS CLI) configured for all accounts

**Limitations**
+ **Untagged image exclusion –** The solution copies only container images that have explicit tags. It skips untagged images that exist with `SHA256` digests.
+ **Lambda execution timeout constraints –** AWS Lambda is limited to a maximum 15-minute execution timeout, which may be insufficient to copy large container images or repositories.
+ **Manual container image management –** The `crane-app.py` Python code requires rebuilding and redeploying the Lambda container image.
+ **Limited parallel processing capacity –** The `MaxConcurrency` state setting limits how many repositories you can copy at the same time. However, you can modify this setting in the source account’s AWS CloudFormation template. Note that higher concurrency values can cause you to exceed service rate limits and account-level Lambda execution quotas.

## Architecture
<a name="copy-ecr-container-images-across-accounts-regions-architecture"></a>

**Target stack**

The pattern has four main components:
+ **Source account infrastructure –** CloudFormation template that creates the orchestration components
+ **Destination account infrastructure –** CloudFormation template that creates cross-account access roles
+ **Lambda function –** Python-based function that uses Crane for efficient image copying
+ **Container image –** Docker container that packages the Lambda function with required tools

**Target architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/787185e7-664b-4ed8-b30f-1d9507f13377/images/cc7d9823-3dc8-4090-a203-910b1ac4447c.png)

**Step Functions workflow**

The Step Functions state machine orchestrates the following, as shown in the following diagram:
+ `PopulateRepositoryList`** –** Scans Amazon ECR repositories and populates Amazon DynamoDB
+ `GetRepositoryList`** –** Retrieves unique repository list from DynamoDB
+ `DeduplicateRepositories`** –** Ensures that there is no duplicate processing
+ `CopyRepositories`** –** Handles parallel copying of repositories
+ `NotifySuccess`/`NotifyFailure`** –** Amazon Simple Notification Service (Amazon SNS) notifications based on execution outcome

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/787185e7-664b-4ed8-b30f-1d9507f13377/images/1b740084-ba2b-4956-aa12-ebbf52be5e7d.png)

## Tools
<a name="copy-ecr-container-images-across-accounts-regions-tools"></a>

**Amazon tools**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine Lambda functions and other AWS services to build business-critical applications.

**Other tools**
+ [Crane](https://michaelsauter.github.io/crane/index.html) is a Docker orchestration tool. It’s similar to Docker Compose but has additional features.
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating system level to deliver software in containers.

**Code repository**
+ The code for this pattern is available in the GitHub [sample-ecr-copy repository](https://github.com/aws-samples/sample-ecr-copy). You can use the CloudFormation template from the repository to create the underlying resources.

## Best practices
<a name="copy-ecr-container-images-across-accounts-regions-best-practices"></a>

Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="copy-ecr-container-images-across-accounts-regions-epics"></a>

### Prepare your environment
<a name="prepare-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure AWS CLI profiles. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | DevOps engineer, Data engineer, ML engineer |
| Gather required information. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | DevOps engineer, Data engineer, ML engineer |
| Clone the repository. | Clone the pattern’s repository to your local workstation:<pre>git clone https://github.com/aws-samples/sample-ecr-copy</pre> | DevOps engineer, Data engineer, ML engineer |

### Deploy infrastructure for the destination account
<a name="deploy-infrastructure-for-the-destination-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the template. | Validate the CloudFormation template:<pre>aws cloudformation validate-template \<br />  --template-body file://"Destination Account cf_template.yml" \<br />  --profile destination-account</pre> | DevOps engineer, ML engineer, Data engineer |
| Deploy the destination infrastructure. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | Data engineer, ML engineer, DevOps engineer |
| Verify the deployment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | DevOps engineer, ML engineer, Data engineer |

### Build and deploy the Lambda container image
<a name="build-and-deploy-the-lam-container-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the container build. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | Data engineer, ML engineer, DevOps engineer |
| Build the container image. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | Data engineer, ML engineer, DevOps engineer |
| Create a repository and upload the image. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | Data engineer, ML engineer, DevOps engineer |
| Verify the image. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | Data engineer, ML engineer, DevOps engineer |

### Deploy the source account infrastructure
<a name="deploy-the-source-account-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare deployment parameters. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | Data engineer, DevOps engineer, ML engineer |
| Validate the source template. | Validate the source CloudFormation template:<pre>aws cloudformation validate-template \<br />  --template-body file://"Source Account Cf template.yml" \<br />  --profile source-account</pre> | Data engineer, ML engineer, DevOps engineer |
| Deploy the source infrastructure. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | Data engineer, ML engineer, DevOps engineer |
| Verify the deployment and collect outputs. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | DevOps engineer, ML engineer, Data engineer |
| Confirm your email subscription. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | Data engineer, ML engineer, DevOps engineer |

### Run and monitor the copy process
<a name="run-and-monitor-the-copy-process"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run and monitor the copy process. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | DevOps engineer, ML engineer, Data engineer |
| Run the step function. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | DevOps engineer, ML engineer, Data engineer |
| Monitor progress. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | DevOps engineer, ML engineer, Data engineer |
| Check the results. | Wait for the process to complete (updated every 30 seconds):<pre>while true; do<br />  STATUS=$(aws stepfunctions describe-execution \<br />    --execution-arn $EXECUTION_ARN \<br />    --profile source-account \<br />    --region $SOURCE_REGION \<br />    --query 'status' \<br />    --output text)<br />  <br />  echo "Current status: $STATUS"<br />  <br />  if [[ "$STATUS" == "SUCCEEDED" || "$STATUS" == "FAILED" || "$STATUS" == "TIMED_OUT" || "$STATUS" == "ABORTED" ]]; then<br />    break<br />  fi<br />  <br />  sleep 30<br />done<br /><br />echo "Final execution status: $STATUS"</pre> | DevOps engineer, ML engineer, Data engineer |
| Verify the images. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) | DevOps engineer, Data engineer, ML engineer |

## Troubleshooting
<a name="copy-ecr-container-images-across-accounts-regions-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Step functions fail to run. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-ecr-container-images-across-accounts-regions.html) |

## Related resources
<a name="copy-ecr-container-images-across-accounts-regions-resources"></a>
+ [Crane documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md)
+ [What is Amazon Elastic Container Registry?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
+ [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ [What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

## Additional information
<a name="copy-ecr-container-images-across-accounts-regions-additional"></a>

**Configuration parameters**

|
|
| Parameter | Description | Example |
| --- |--- |--- |
| `SourceAccountId` | Source AWS account ID | `11111111111` |
| `DestinationAccountId` | Destination AWS account ID | `22222222222` |
| `DestinationRegion` | Target AWS Region | `us-east-2` |
| `SourceRegion` | Source AWS Region | `us-east-1` |
| `NotificationEmail` | Email for notifications | `abc@xyz.com` |
| `RepositoryList` | Repositories to copy | `repo1,repo2,repo3` |
| `LambdaImageUri` | Lambda container image URI | `${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/ecr-copy-lambda:latest` |
