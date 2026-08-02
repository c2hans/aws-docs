---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/deployment-pipelines.html
---

# Deployment pipelines
<a name="deployment-pipelines"></a>

The AWS CloudFormation template deploys two CodePipeline pipelines, an installer and the core deployment pipeline, along with associated dependencies. This solution uses CodeBuild to build and deploy a series of CDK-based CloudFormation stacks that are responsible for deploying supported resources in the multi-account, multi-Region environment.

**Note**
AWS CloudFormation resources are created from AWS CDK constructs.

## Installer (`AWSAccelerator-InstallerStack`)
<a name="awsaccelerator-installerstack"></a>

This CloudFormation template deploys the following resources:
+ A CodePipeline (`AWSAccelerator-Installer`) that’s used to orchestrate the build and deployment of the `AWSAccelerator-PipelineStack` AWS CloudFormation template.
+ A CodeBuild project is used as an orchestration engine within the pipeline to build the Landing Zone Accelerator on AWS source code and then synthesize and deploy the `AWSAccelerator-PipelineStack` CloudFormation template.
+ An Amazon S3 bucket that’s used for pipeline artifact storage.
+ An AWS KMS key that’s used to activate encryption at-rest for applicable resources deployed in `AWSAccelerator-InstallerStack` and `AWSAccelerator-PipelineStack`.
+ Supporting [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) roles for CodePipeline and CodeBuild to perform their actions.

## Core (`AWSAccelerator-PipelineStack`)
<a name="awsaccelerator-pipelinestack"></a>

This AWS CloudFormation stack is deployed by the AWS CDK with the following resources:
+ A CodePipeline (`AWSAccelerator-Pipeline`) that’s used for input validation, synthesis, and deployment of additional CloudFormation stacks by using the AWS CDK. The pipeline contains several stages that are discussed in [Architecture details](architecture-details.md).
+ Two CodeBuild projects. The projects are used in the pipeline stages to:
  + Build the Landing Zone Accelerator on AWS source code.
  + Run AWS CDK toolkit commands across the pipeline stages.
+ An S3 bucket (`awsaccelerator-config`) that’s used to store the configuration files that are used by the `AWSAccelerator-Pipeline`. These configuration files are your primary mechanism for configuration and management of the entire Landing Zone Accelerator on AWS solution.
+ Two Amazon SNS topics are created and can be optionally subscribed to for AWS CodePipeline run notifications. No topic subscriptions are created by default. One Amazon SNS will notifies for all pipeline run events. The other notifies only on pipeline failure events.
+ An optional third SNS topic is created if the **EnableApprovalStage** is set to `Yes` in **AWSAccelerator-InstallerStack**. Email address(es) listed in the **ApprovalStageNotifyEmailList** will be automatically subscribed to this topic.
+ An AWS IAM service-linked role is created to allow [AWS CodeStar](https://aws.amazon.com/codestar/) notifications to publish CodePipeline pipeline run events to the Amazon SNS topics.
+ A CloudWatch alarm is created to alarm on pipeline processing failures.
+ An Amazon S3 bucket that’s used for pipeline artifact storage.
