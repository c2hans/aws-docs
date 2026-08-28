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
| Configure AWS CLI profiles. | 1. Configure the source account profile:<pre>aws configure --profile source-account<br /># Enter: Access Key ID, Secret Access Key, Default region, Output format (json)</pre><br />2. Configure the destination account profile:<pre>aws configure --profile destination-account <br /># Enter: Access Key ID, Secret Access Key, Default region, Output format (json) </pre><br />3. Verify the configurations:<pre>aws sts get-caller-identity --profile source-account <br />aws sts get-caller-identity --profile destination-account</pre> | DevOps engineer, Data engineer, ML engineer |
| Gather required information. | 1. Get the source account ID:<pre>export SOURCE_ACCOUNT_ID=$(aws sts get-caller-identity --profile source-account --query Account --output text)<br />echo "Source Account ID: $SOURCE_ACCOUNT_ID"</pre><br />2. Get the destination account ID:<pre>export DEST_ACCOUNT_ID=$(aws sts get-caller-identity --profile destination-account --query Account --output text)<br />echo "Destination Account ID: $DEST_ACCOUNT_ID"</pre><br />3. Set the AWS Regions. Modify this command for your Region:<pre>export SOURCE_REGION="us-east-1"<br />export DEST_REGION="us-east-2"</pre><br />4. List the existing Amazon ECR repositories in the source account:<pre>aws ecr describe-repositories --profile source-account --region $SOURCE_REGION --query 'repositories[].repositoryName' --output table</pre> | DevOps engineer, Data engineer, ML engineer |
| Clone the repository. | Clone the pattern’s repository to your local workstation:<pre>git clone https://github.com/aws-samples/sample-ecr-copy</pre> | DevOps engineer, Data engineer, ML engineer |

### Deploy infrastructure for the destination account
<a name="deploy-infrastructure-for-the-destination-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the template. | Validate the CloudFormation template:<pre>aws cloudformation validate-template \<br />  --template-body file://"Destination Account cf_template.yml" \<br />  --profile destination-account</pre> | DevOps engineer, ML engineer, Data engineer |
| Deploy the destination infrastructure. | 1. Deploy the destination account stack:<pre>aws cloudformation deploy \<br />  --template-file "Destination Account cf_template.yml" \<br />  --stack-name ecr-copy-destination \<br />  --parameter-overrides \<br />    SourceAccountId=$SOURCE_ACCOUNT_ID \<br />    SourceRoleName=ECRContainerLambdaRole \<br />  --capabilities CAPABILITY_NAMED_IAM \<br />  --profile destination-account \<br />  --region $DEST_REGION<br /></pre><br />2. Wait for the stack to complete:<pre>aws cloudformation wait stack-create-complete \<br />  --stack-name ecr-copy-destination \<br />  --profile destination-account \<br />  --region $DEST_REGION</pre> | Data engineer, ML engineer, DevOps engineer |
| Verify the deployment. | 1. Get stack outputs:<pre>aws cloudformation describe-stacks \<br />  --stack-name ecr-copy-destination \<br />  --profile destination-account \<br />  --region $DEST_REGION \<br />  --query 'Stacks[0].Outputs' \<br />  --output table</pre><br />2. Store the cross-account IAM role:<pre>export CROSS_ACCOUNT_ROLE_ARN=$(aws cloudformation describe-stacks \<br />  --stack-name ecr-copy-destination \<br />  --profile destination-account \<br />  --region $DEST_REGION \<br />  --query 'Stacks[0].Outputs[?OutputKey==`CrossAccountRoleArn`].OutputValue' \<br />  --output text)<br /><br />echo "Cross-Account Role ARN: $CROSS_ACCOUNT_ROLE_ARN"</pre> | DevOps engineer, ML engineer, Data engineer |

### Build and deploy the Lambda container image
<a name="build-and-deploy-the-lam-container-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the container build. | 1. Verify that Docker is running:<pre>docker --version<br />docker info</pre><br />2. Ensure that `crane-app.py` and `Dockerfile` are in the current directory:<pre>ls -la crane-app.py Dockerfile</pre> | Data engineer, ML engineer, DevOps engineer |
| Build the container image. | 1. Build the Lambda container image:<pre>docker build -t ecr-copy-lambda . --no-cache</pre><br />2. Verify that the image was created:<pre>docker images ecr-copy-lambda</pre><br />3. (Optional) Test the container locally:<pre>docker run --rm --entrypoint python ecr-copy-lambda -c "import boto3; print('Container working')"</pre> | Data engineer, ML engineer, DevOps engineer |
| Create a repository and upload the image. | 1. Create an Amazon ECR repository in the source account:<pre>aws ecr create-repository \<br />  --repository-name ecr-copy-lambda \<br />  --profile source-account \<br />  --region $SOURCE_REGION</pre><br />2. Get an Amazon ECR login token and authenticate Docker:<pre>aws ecr get-login-password \<br />  --profile source-account \<br />  --region $SOURCE_REGION | \<br />  docker login --username AWS --password-stdin \<br />  $SOURCE_ACCOUNT_ID.dkr.ecr.$SOURCE_REGION.amazonaws.com</pre><br />3. Tag the image for Amazon ECR:<pre>docker tag ecr-copy-lambda:latest \<br />  $SOURCE_ACCOUNT_ID.dkr.ecr.$SOURCE_REGION.amazonaws.com/ecr-copy-lambda:latest</pre><br />4. Upload the image to Amazon ECR:<pre>docker push $SOURCE_ACCOUNT_ID.dkr.ecr.$SOURCE_REGION.amazonaws.com/ecr-copy-lambda:latest</pre><br />5. Store the image URI for later use:<pre>export LAMBDA_IMAGE_URI="$SOURCE_ACCOUNT_ID.dkr.ecr.$SOURCE_REGION.amazonaws.com/ecr-copy-lambda:latest"<br />echo "Lambda Image URI: $LAMBDA_IMAGE_URI"</pre> | Data engineer, ML engineer, DevOps engineer |
| Verify the image. | 1. List the images in the repository:<pre>aws ecr list-images \<br />  --repository-name ecr-copy-lambda \<br />  --profile source-account \<br />  --region $SOURCE_REGION</pre><br />2. Get the image details:<pre>aws ecr describe-images \<br />  --repository-name ecr-copy-lambda \<br />  --profile source-account \<br />  --region $SOURCE_REGION</pre> | Data engineer, ML engineer, DevOps engineer |

### Deploy the source account infrastructure
<a name="deploy-the-source-account-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare deployment parameters. | 1. Set the notification email:<pre>export NOTIFICATION_EMAIL="your-email@company.com"</pre><br />2. Define the repositories to copy (comma-separated):<pre>export REPOSITORY_LIST="app-frontend,app-backend,database-migrations"</pre><br />3. Set the environment:<pre>export ENVIRONMENT="dev"<br /><br />echo "Deployment Parameters:"<br />echo "Source Account: $SOURCE_ACCOUNT_ID"<br />echo "Destination Account: $DEST_ACCOUNT_ID"<br />echo "Source Region: $SOURCE_REGION"<br />echo "Destination Region: $DEST_REGION"<br />echo "Lambda Image: $LAMBDA_IMAGE_URI"<br />echo "Notification Email: $NOTIFICATION_EMAIL"<br />echo "Repositories: $REPOSITORY_LIST"</pre> | Data engineer, DevOps engineer, ML engineer |
| Validate the source template. | Validate the source CloudFormation template:<pre>aws cloudformation validate-template \<br />  --template-body file://"Source Account Cf template.yml" \<br />  --profile source-account</pre> | Data engineer, ML engineer, DevOps engineer |
| Deploy the source infrastructure. | 1. Deploy the source account stack:<pre>aws cloudformation deploy \<br />  --template-file "Source Account Cf template.yml" \<br />  --stack-name ecr-copy-source \<br />  --parameter-overrides \<br />    SourceAccountId=$SOURCE_ACCOUNT_ID \<br />    DestinationAccountId=$DEST_ACCOUNT_ID \<br />    DestinationRegion=$DEST_REGION \<br />    SourceRegion=$SOURCE_REGION \<br />    NotificationEmail=$NOTIFICATION_EMAIL \<br />    RepositoryList="$REPOSITORY_LIST" \<br />    LambdaImageUri=$LAMBDA_IMAGE_URI \<br />    Environment=$ENVIRONMENT \<br />  --capabilities CAPABILITY_NAMED_IAM \<br />  --profile source-account \<br />  --region $SOURCE_REGION</pre><br />2. Wait for the stack to complete (this might take up to 10 minutes):<pre>aws cloudformation wait stack-create-complete \<br />  --stack-name ecr-copy-source \<br />  --profile source-account \<br />  --region $SOURCE_REGION</pre> | Data engineer, ML engineer, DevOps engineer |
| Verify the deployment and collect outputs. | 1. Get the stack outputs:<pre>aws cloudformation describe-stacks \<br />  --stack-name ecr-copy-source \<br />  --profile source-account \<br />  --region $SOURCE_REGION \<br />  --query 'Stacks[0].Outputs' \<br />  --output table</pre><br />2. Store the Amazon Resource Names (ARNs) for the state machine and SNS topic:<pre>export STATE_MACHINE_ARN=$(aws cloudformation describe-stacks \<br />  --stack-name ecr-copy-source \<br />  --profile source-account \<br />  --region $SOURCE_REGION \<br />  --query 'Stacks[0].Outputs[?OutputKey==`StateMachineArn`].OutputValue' \<br />  --output text)<br /><br />export SNS_TOPIC_ARN=$(aws cloudformation describe-stacks \<br />  --stack-name ecr-copy-source \<br />  --profile source-account \<br />  --region $SOURCE_REGION \<br />  --query 'Stacks[0].Outputs[?OutputKey==`SNSTopicArn`].OutputValue' \<br />  --output text)<br /><br />echo "State Machine ARN: $STATE_MACHINE_ARN"<br />echo "SNS Topic ARN: $SNS_TOPIC_ARN"</pre> | DevOps engineer, ML engineer, Data engineer |
| Confirm your email subscription. | 1. Check your email for confirmation of your SNS subscription.<br />2. Choose the confirmation link in the email.<br />3. Verify the subscription status.<pre>aws sns list-subscriptions-by-topic \<br />  --topic-arn $SNS_TOPIC_ARN \<br />  --profile source-account \<br />  --region $SOURCE_REGION</pre> | Data engineer, ML engineer, DevOps engineer |

### Run and monitor the copy process
<a name="run-and-monitor-the-copy-process"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run and monitor the copy process. | 1. Sign in to the AWS Management Console, and open the [Step Functions ](https://console.aws.amazon.com/states/home)[console](https://console.aws.amazon.com/states/home).<br />2. Locate the state machine.<br />3. Choose **Start execution**.<br />When it finishes, results are displayed on the **Execution input and output** tab.<br />4. (Optional) If you want to continue running Step Functions by using the AWS CLI, follow the remaining steps in this epic. | DevOps engineer, ML engineer, Data engineer |
| Run the step function. | 1. Generate a unique name:<pre>export EXECUTION_NAME="ecr-copy-$(date +%Y%m%d-%H%M%S)"</pre><br />2. Run the step function.<pre>export EXECUTION_ARN=$(aws stepfunctions start-execution \<br />  --state-machine-arn $STATE_MACHINE_ARN \<br />  --name $EXECUTION_NAME \<br />  --profile source-account \<br />  --region $SOURCE_REGION \<br />  --query 'executionArn' \<br />  --output text)<br /><br />echo "Execution started: $EXECUTION_ARN"<br />echo "Execution Name: $EXECUTION_NAME"</pre> | DevOps engineer, ML engineer, Data engineer |
| Monitor progress. | 1. Check the status:<pre><br />aws stepfunctions describe-execution \<br />  --execution-arn $EXECUTION_ARN \<br />  --profile source-account \<br />  --region $SOURCE_REGION \<br />  --query '{Status:status,StartDate:startDate,StopDate:stopDate}' \<br />  --output table</pre><br />2. Get the history:<pre><br />aws stepfunctions get-execution-history \<br />  --execution-arn $EXECUTION_ARN \<br />  --profile source-account \<br />  --region $SOURCE_REGION \<br />  --query 'events[?type==`TaskStateEntered` || type==`TaskSucceeded` || type==`TaskFailed`].{Type:type,Timestamp:timestamp,Details:stateEnteredEventDetails.name}' \<br />  --output table</pre> | DevOps engineer, ML engineer, Data engineer |
| Check the results. | Wait for the process to complete (updated every 30 seconds):<pre>while true; do<br />  STATUS=$(aws stepfunctions describe-execution \<br />    --execution-arn $EXECUTION_ARN \<br />    --profile source-account \<br />    --region $SOURCE_REGION \<br />    --query 'status' \<br />    --output text)<br />  <br />  echo "Current status: $STATUS"<br />  <br />  if [[ "$STATUS" == "SUCCEEDED" || "$STATUS" == "FAILED" || "$STATUS" == "TIMED_OUT" || "$STATUS" == "ABORTED" ]]; then<br />    break<br />  fi<br />  <br />  sleep 30<br />done<br /><br />echo "Final execution status: $STATUS"</pre> | DevOps engineer, ML engineer, Data engineer |
| Verify the images. | 1. List the repositories in the destination account:<pre>aws ecr describe-repositories \<br />  --profile destination-account \<br />  --region $DEST_REGION \<br />  --query 'repositories[].repositoryName' \<br />  --output table</pre><br />2. Check the repository images:<pre>for repo in $(echo $REPOSITORY_LIST | tr ',' ' '); do<br />  echo "\nImages in repository: $repo"<br />  aws ecr list-images \<br />    --repository-name $repo \<br />    --profile destination-account \<br />    --region $DEST_REGION \<br />    --query 'imageIds[].imageTag' \<br />    --output table 2>/dev/null || echo "Repository $repo not found or no images"<br />done</pre> | DevOps engineer, Data engineer, ML engineer |

## Troubleshooting
<a name="copy-ecr-container-images-across-accounts-regions-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Step functions fail to run. | 1. To retrieve detailed failure events from the history, run the following AWS CLI command:<pre>if [[ "$STATUS" == "FAILED" ]]; then<br />  echo "Getting failure details..."<br />  aws stepfunctions get-execution-history \<br />    --execution-arn $EXECUTION_ARN \<br />    --profile source-account \<br />    --region $SOURCE_REGION \<br />    --query 'events[?type==`TaskFailed`]' \<br />    --output json<br />fi<br /></pre><br />2. To retrieve logs for failed Lambda functions, run the following AWS CLI command:<pre># Check Lambda function logs<br />echo "\nLambda function logs:"<br />aws logs describe-log-groups \<br />  --log-group-name-prefix "/aws/lambda/ecr-copy-source" \<br />  --profile source-account \<br />  --region $SOURCE_REGION \<br />  --query 'logGroups[].logGroupName' \<br />  --output table</pre> |

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
