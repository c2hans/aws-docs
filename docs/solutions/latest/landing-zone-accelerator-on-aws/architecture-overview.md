---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

 **AWS architecture diagram showing Management, Log Archive, and Audit accounts with various services and their interactions.**

![lza arch diagram](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/lza-arch-diagram.png)

1. You use AWS CloudFormation to install the solution into your environment. Your environment must meet [prerequisites](prerequisites.md) before deploying the solution. The provided CloudFormation template deploys an [AWS CodePipeline](https://aws.amazon.com/codepipeline/) that contains the Landing Zone Accelerator on AWS installation engine.

1. The **Installer** pipeline (`AWSAccelerator-InstallerStack`) functions separately from the **Core** pipeline. This way, you can update to future versions of the solution with a single parameter through the AWS CloudFormation console.

1. An [AWS CodeBuild](https://aws.amazon.com/codebuild/) project functions as an orchestration engine to build and run the solution’s AWS CDK application that deploys the Core pipeline (`AWSAccelerator-PipelineStack`) and its associated dependencies.

1. The solution deploys [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) topics that you can subscribe to for alerts on Core pipeline events, which can increase observability of your Core pipeline operations. Additionally, the solution deploys two [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) customer-managed keys to manage encryption at rest of Installer and Core pipeline dependencies.

1. The Core pipeline validates and synthesizes inputs and deploys additional CloudFormation stacks with AWS CDK. An [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket (`aws-accelerator-config`) stores the configuration files that the solution uses. These configuration files are the primary mechanism for configuring and managing the solution.

1. An AWS CodeBuild project compiles and validates the solution’s AWS CDK application configuration.

1. Multiple AWS CodeBuild deployment stages deploy the resources that were defined in the solution configuration files to your multi-account environment. An optional manual review stage can be included, allowing you to view all the changes that these stages will apply.

1. The solution deploys resources that monitor AWS Control Tower lifecycle events to detect potential drift against a known good state (in other words, when the actual configuration of an infrastructure resource differs from its expected configuration). The solution also deploys resources that can automate the enrollment of new AWS accounts into your multi-account environment. When using AWS Control Tower with this solution, ensure that accounts and organizational units (OUs) within your AWS Control Tower environment are properly enrolled. You can manage this through the AWS Control Tower console.
**Note**
We provide guidance in [For AWS Organizations based installation (without AWS Control Tower)](prerequisites.md#for-aws-organizations-based-installation-without-aws-control-tower) later in this document if you wish not to use AWS Control Tower.

1. The solution deploys centralized logging resources in the **Log Archive** account in your multi-account environment. This includes [Amazon Kinesis](https://aws.amazon.com/kinesis/) resources to stream and ingest logs, AWS KMS keys to facilitate encryption at rest, and [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) buckets as log storage destinations.

1. The solution provisions the audit account with resources to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) log groups to the centralized logging infrastructure in the LogArchive account.

**Note**
Initial deployment includes, at a minimum, account creation, drift detection, key management, and centralized logging infrastructure. These mandatory components are part of the core feature set of the solution and are described further in [Architecture details](architecture-details.md). Remaining infrastructure that the solution deploys depends on the content of the user-defined configuration files.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
