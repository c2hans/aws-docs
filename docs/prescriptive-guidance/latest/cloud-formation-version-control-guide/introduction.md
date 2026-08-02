---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-formation-version-control-guide/introduction.html
---

# Version-controlled AWS CloudFormation deployments using commit ID tagging
<a name="introduction"></a>

*Neeti Mishra, Amazon Web Services*

Many organizations that use AWS CloudFormation to define and provision cloud resources face challenges with version tracking and environment consistency. Without a structured versioning strategy, teams struggle to trace which infrastructure code is deployed to which environment, making rollbacks difficult and compliance audits time-consuming. This guide describes an approach that combines Git commit ID-based tagging with version-to-environment mapping by using AWS CodePipeline and AWS CodeBuild. This approach helps teams improve deployment traceability, maintain environment consistency, and control infrastructure changes across development, staging, and production environments.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for DevOps engineers, cloud infrastructure engineers, and platform teams who manage CloudFormation deployments across multiple environments. Readers should have experience with:
+ CloudFormation template authoring
+ Git version control
+ Continuous integration and continuous delivery (CI/CD) pipeline concepts
+ AWS Identity and Access Management (IAM) role configuration
+ Python scripting

## Objectives
<a name="objectives"></a>

After reading this guide, you will be able to:
+ Implement semantic versioning for CloudFormation templates by using Git tags
+ Configure version-to-environment mapping for controlled deployments
+ Set up automated deployment pipelines by using AWS CodePipeline and AWS CodeBuild
+ Manage cross-account deployments with appropriate IAM roles
+ Maintain audit trails for infrastructure changes

Some AWS services aren't available in all AWS Regions. For Region availability, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the AWS documentation, and choose the link for the service.

## Prerequisites
<a name="prerequisites"></a>

For this walkthrough, you should have the following:
+ An active [AWS account](https://aws.amazon.com/resources/create-account/)
+ A Git repository that supports [webhooks](https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks) and can connect to a webhook URL through the internet- [Github connection](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html)
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to work with your account
+ Python
+ Basic knowledge of CloudFormation template and version control
+ Set up [AWS CodePipeline](https://aws.amazon.com/codepipeline/) and establish a connection with a source control provider. Specifically, we are using [GitHub](https://docs.github.com/en/get-started) as our source repository to showcase our solution
+ Download and install [Visual Studio Code](https://code.visualstudio.com/docs/setup/setup-overview)
