---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html
---

# Manage blue/green deployments of microservices to multiple accounts and Regions by using AWS code services and AWS KMS multi-Region keys
<a name="manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys"></a>

*Balaji Vedagiri, Vanitha Dontireddy, Ashish Kumar, Faisal Shahdad, Vivek Thangamuthu, and Anand Krishna Varanasi, Amazon Web Services*

## Summary
<a name="manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys-summary"></a>

This pattern describes how to deploy a global microservices application from a central AWS account to multiple workload accounts and Regions in accordance with a blue/green deployment strategy. The pattern supports the following:
+ Software is developed in a central account, whereas workloads and applications are spread across multiple accounts and AWS Regions.
+ A single AWS Key Management System (AWS KMS) multi-Region key is used for encryption and decryption to cover disaster recovery.
+ The KMS key is Region-specific and has to be maintained or created in three different Regions for pipeline artifacts. A KMS multi-Region key helps retain the same key ID across Regions.
+ The Git workflow branching model is implemented with two branches (development and main) and code is merged by using pull requests (PRs). The AWS Lambda function that is deployed from this stack creates a PR from the development branch to the main branch. The PR merge to the main branch initiates an AWS CodePipeline pipeline, which orchestrates the continuous integration and continuous delivery (CI/CD) flow and deploys the stacks across accounts.

This pattern  provides a sample infrastructure as code (IaC) setup through AWS CloudFormation stacks to demonstrate this use case. The blue/green deployment of microservices is implemented by using AWS CodeDeploy.

## Prerequisites and limitations
<a name="manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys-prereqs"></a>

**Prerequisites**
+ Four active AWS accounts:
  + A tools account to manage the code pipeline and maintain the AWS CodeCommit repository.
  + Three workload (test) accounts for deploying the microservices workload.
+ This pattern uses the following Regions. If  you want to use other Regions, you must make the appropriate modifications to the AWS CodeDeploy and AWS KMS multi-Region stacks.
  + Tools (AWS CodeCommit) account: `ap-south-1`
  + Workload (test) account 1: `ap-south-1`
  + Workload (test) account 2: `eu-central-1`
  + Workload (test) account 3: `us-east-1`
+ Three Amazon Simple Storage Service (Amazon S3) buckets for the deployment Regions in each workload account. (These are called `S3BUCKETNAMETESTACCOUNT1`, `S3BUCKETNAMETESTACCOUNT2 `and `S3BUCKETNAMETESTACCOUNT3 `later in this pattern.)

  For example, you can create these buckets in specific accounts and Regions with unique bucket names as follows (replace *xxxx* with a random number):

  ```
  ##In Test Account 1
  aws s3 mb s3://ecs-codepipeline-xxxx-ap-south-1 --region ap-south-1
  ##In Test Account 2
  aws s3 mb s3://ecs-codepipeline-xxxx-eu-central-1 --region eu-central-1
  ##In Test Account 3
  aws s3 mb s3://ecs-codepipeline-xxxx-us-east-1 --region us-east-1

  #Example
  ##In Test Account 1
  aws s3 mb s3://ecs-codepipeline-18903-ap-south-1 --region ap-south-1
  ##In Test Account 2
  aws s3 mb s3://ecs-codepipeline-18903-eu-central-1 --region eu-central-1
  ##In Test Account 3
  aws s3 mb s3://ecs-codepipeline-18903-us-east-1 --region us-east-1
  ```

**Limitations**

The pattern uses AWS CodeBuild and other configuration files to deploy a sample microservice. If you have a different workload type (for example, serverless), you must update all relevant configurations.

## Architecture
<a name="manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys-architecture"></a>

**Target technology stack **
+ AWS CloudFormation
+ AWS CodeCommit
+ AWS CodeBuild
+ AWS CodeDeploy
+ AWS CodePipeline

**Target architecture **

![Target architecture for deploying microservices to multiple accounts and Regions](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a144c977-6823-4b08-a215-fae779b3ce7c/images/eedfabdb-f266-4190-b271-5caf7ac9b47b.png)

**Automation and scale**

The setup is automated by using AWS CloudFormation stack templates (IaC). It can be easily scaled for multiple environments and accounts.

## Tools
<a name="manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) automates deployments to Amazon Elastic Compute Cloud (Amazon EC2) or on-premises instances, AWS Lambda functions, or Amazon Elastic Container Service (Amazon ECS) services.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Additional tools**
+ [Git](https://git-scm.com/docs) is an open-source, distributed version control system that works with the AWS CodeCommit repository.
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers. This pattern uses Docker to build and test container images locally.
+ [cfn-lint](https://github.com/aws-cloudformation/cfn-lint) and [cfn-nag](https://github.com/stelligent/cfn_nag) are open-source tools that help you review CloudFormation stacks for any errors and security issues.

**Code repository**

The code for this pattern is available in the GitHub [Global Blue/Green deployments in multiple regions and accounts](https://github.com/aws-samples/ecs-blue-green-global-deployment-with-multiregion-cmk-codepipeline) repository.

## Epics
<a name="manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys-epics"></a>

### Set up environment variables
<a name="set-up-environment-variables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Export environment variables for CloudFormation stack deployment. | Define environment variables that will be used as input to the CloudFormation stacks later in this pattern.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) | AWS DevOps |

### Package and deploy the CloudFormation stacks for the infrastructure
<a name="package-and-deploy-the-cloudformation-stacks-for-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Clone the [sample repository](https://github.com/aws-samples/ecs-blue-green-global-deployment-with-multiregion-cmk-codepipeline) into a new repository in your work location:<pre>##In work location<br />git clone https://github.com/aws-samples/ecs-blue-green-global-deployment-with-multiregion-cmk-codepipeline.git</pre> | AWS DevOps |
| Package the Cloudformation resources. | In this step, you package the local artifacts that the CloudFormation templates reference to create the infrastructure resources required for services such as Amazon Virtual Private Cloud (Amazon VPC) and Application Load Balancer.<br />The templates are available in the `Infra` folder of the code repository.<pre>##In TestAccount1##<br />aws cloudformation package \<br />    --template-file mainInfraStack.yaml \<br />    --s3-bucket $S3BUCKETNAMETESTACCOUNT1 \<br />    --s3-prefix infraStack \<br />    --region $TESTACCOUNT1REGION \<br />    --output-template-file infrastructure_${TESTACCOUNT1}.template</pre><pre>##In TestAccount2##<br />aws cloudformation package \<br />    --template-file mainInfraStack.yaml \<br />    --s3-bucket $S3BUCKETNAMETESTACCOUNT2 \<br />    --s3-prefix infraStack \<br />    --region $TESTACCOUNT2REGION \<br />    --output-template-file infrastructure_${TESTACCOUNT2}.template</pre><pre>##In TestAccount3##<br />aws cloudformation package \<br />    --template-file mainInfraStack.yaml \<br />    --s3-bucket $S3BUCKETNAMETESTACCOUNT3 \<br />    --s3-prefix infraStack \<br />    --region $TESTACCOUNT3REGION \<br />    --output-template-file infrastructure_${TESTACCOUNT3}.template</pre> | AWS DevOps |
| Validate the package templates. | Validate the package templates:<pre>aws cloudformation validate-template \<br />    --template-body file://infrastructure_${TESTACCOUNT1}.template<br /><br />aws cloudformation validate-template \<br />    --template-body file://infrastructure_${TESTACCOUNT2}.template<br /><br />aws cloudformation validate-template \<br />    --template-body file://infrastructure_${TESTACCOUNT3}.template</pre> | AWS DevOps |
| Deploy the package files into the workload accounts, | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) | AWS DevOps |

### Push a sample image and scale Amazon ECS
<a name="push-a-sample-image-and-scale-amazon-ecs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Push a sample image to the Amazon ECR repository. | Push a sample (NGINX) image to the Amazon Elastic Container Registry (Amazon ECR) repository named `web` (as set in parameters). You can customize the image as required.<br />To log in and set the credentials for pushing an image to Amazon ECR, follow the instructions in the [Amazon ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html).<br />The commands are:<pre>  docker pull nginx<br />  docker images<br />  docker tag <imageid> aws_account_id.dkr.ecr.region.amazonaws.com/<web>:latest<br />  docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<web>:tag </pre> | AWS DevOps |
| Scale Amazon ECS and verify access. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) | AWS DevOps |

### Set up code services and resources
<a name="set-up-code-services-and-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CodeCommit repository in the tools account. | Create a CodeCommit repository in the tools account by using the `codecommit.yaml` template, which is in the `code` folder of the GitHub repository. You must create this repository only in the single Region where you plan to develop the code.<pre>aws cloudformation deploy --stack-name codecommitrepoStack --parameter-overrides  CodeCommitReponame=$CODECOMMITREPONAME \<br />ToolsAccount=$TOOLSACCOUNT --template-file codecommit.yaml  --region $TOOLSACCOUNTREGION \<br />--capabilities CAPABILITY_NAMED_IAM</pre> | AWS DevOps |
| Create an S3 bucket for managing artifacts generated by CodePipeline. | Create an S3 bucket for managing artifacts generated by CodePipeline by using the `pre-reqs-bucket.yaml` template, which is in the `code` folder of the GitHub repository. The stacks must be deployed in all three workload (test) and tools accounts and Regions.<pre>aws cloudformation deploy --stack-name pre-reqs-artifacts-bucket --parameter-overrides BucketStartName=$BUCKETSTARTNAME \<br />TestAccount1=$TESTACCOUNT1 TestAccount2=$TESTACCOUNT2 \<br />TestAccount3=$TESTACCOUNT3 CodeCommitAccount=$CODECOMMITACCOUNT ToolsAccount=$TOOLSACCOUNT \<br />--template-file pre-reqs_bucket.yaml --region $TESTACCOUNT1REGION --capabilities CAPABILITY_NAMED_IAM<br /><br />aws cloudformation deploy --stack-name pre-reqs-artifacts-bucket --parameter-overrides BucketStartName=$BUCKETSTARTNAME \<br />TestAccount1=$TESTACCOUNT1 TestAccount2=$TESTACCOUNT2 \<br />TestAccount3=$TESTACCOUNT3 CodeCommitAccount=$CODECOMMITACCOUNT ToolsAccount=$TOOLSACCOUNT \<br />--template-file pre-reqs_bucket.yaml --region $TESTACCOUNT2REGION --capabilities CAPABILITY_NAMED_IAM<br /><br />aws cloudformation deploy --stack-name pre-reqs-artifacts-bucket --parameter-overrides BucketStartName=$BUCKETSTARTNAME \<br />TestAccount1=$TESTACCOUNT1 TestAccount2=$TESTACCOUNT2 \<br />TestAccount3=$TESTACCOUNT3 CodeCommitAccount=$CODECOMMITACCOUNT ToolsAccount=$TOOLSACCOUNT \<br />--template-file pre-reqs_bucket.yaml --region $TESTACCOUNT3REGION --capabilities CAPABILITY_NAMED_IAM<br /><br />aws cloudformation deploy --stack-name pre-reqs-artifacts-bucket --parameter-overrides BucketStartName=$BUCKETSTARTNAME \<br />TestAccount1=$TESTACCOUNT1 TestAccount2=$TESTACCOUNT2 \<br />TestAccount3=$TESTACCOUNT3 CodeCommitAccount=$CODECOMMITACCOUNT ToolsAccount=$TOOLSACCOUNT \<br />--template-file pre-reqs_bucket.yaml --region $TOOLSACCOUNTREGION --capabilities CAPABILITY_NAMED_IAM</pre> | AWS DevOps |
| Set up a multi-Region KMS key. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) | AWS DevOps |
| Set up the CodeBuild project in the tools account. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) | AWS DevOps |
| Set up CodeDeploy in workload accounts. | Use the `codedeploy.yaml` template in the `code` folder of the GitHub repository to set up CodeDeploy in all three workload accounts. The output of `mainInfraStack` includes the Amazon Resource Names (ARNs) of the Amazon ECS cluster and Application Load Balancer listener.The values from the infrastructure stacks are exported already, so they are imported by the CodeDeploy stack templates.<pre>##WorkloadAccount1##<br />aws cloudformation deploy --stack-name ecscodedeploystack \<br />--parameter-overrides  ToolsAccount=$TOOLSACCOUNT mainInfrastackname=mainInfrastack \<br />--template-file codedeploy.yaml  --region $TESTACCOUNT1REGION --capabilities CAPABILITY_NAMED_IAM<br /><br />##WorkloadAccount2##<br />aws cloudformation deploy --stack-name ecscodedeploystack \<br />--parameter-overrides ToolsAccount=$TOOLSACCOUNT mainInfrastackname=mainInfrastack \<br />--template-file codedeploy.yaml  --region $TESTACCOUNT2REGION --capabilities CAPABILITY_NAMED_IAM<br /><br />##WorkloadAccount3##<br />aws cloudformation deploy --stack-name ecscodedeploystack \<br />--parameter-overrides ToolsAccount=$TOOLSACCOUNT mainInfrastackname=mainInfrastack \<br />--template-file codedeploy.yaml  --region $TESTACCOUNT3REGION --capabilities CAPABILITY_NAMED_IAM</pre> | AWS DevOps |

### Set up CodePipeline in the tools account
<a name="set-up-codepipeline-in-the-tools-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a code pipeline in the tools account. | In the tools account, run the command:<pre>aws cloudformation deploy --stack-name ecscodepipelinestack --parameter-overrides  \<br />TestAccount1=$TESTACCOUNT1 TestAccount1Region=$TESTACCOUNT1REGION \<br />TestAccount2=$TESTACCOUNT2 TestAccount2Region=$TESTACCOUNT2REGION \<br />TestAccount3=$TESTACCOUNT3 TestAccount3Region=$TESTACCOUNT3REGION \<br />CMKARNTools=$CMKTROOLSARN CMKARN1=$CMKARN1 CMKARN2=$CMKARN2 CMKARN3=$CMKARN3 \<br />CodeCommitRepoName=$CODECOMMITREPONAME BucketStartName=$BUCKETSTARTNAME \<br />--template-file codepipeline.yaml --capabilities CAPABILITY_NAMED_IAM</pre> | AWS DevOps |
| Provide access for CodePipeline and CodeBuild roles in the AWS KMS key policy and S3 bucket policy. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) | AWS DevOps |

### Call and test the pipeline
<a name="call-and-test-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Push changes to the CodeCommit repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) |  |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up all the deployed resources. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) |  |

## Troubleshooting
<a name="manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Changes that you committed to the repository aren’t getting deployed. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys.html) |

## Related resources
<a name="manage-blue-green-deployments-of-microservices-to-multiple-accounts-and-regions-by-using-aws-code-services-and-aws-kms-multi-region-keys-resources"></a>
+ [Pushing a Docker image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) (Amazon ECR documentation)
+ [Connect to an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-connect.html) (AWS CodeCommit documentation)
+ [Troubleshooting AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting.html) (AWS CodeBuild documentation)
