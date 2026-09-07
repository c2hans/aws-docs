---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-third-party-git-source-repositories-in-aws-codepipeline.html
---

# Use third-party Git source repositories in AWS CodePipeline
<a name="use-third-party-git-source-repositories-in-aws-codepipeline"></a>

*Kirankumar Chandrashekar, Amazon Web Services*

## Summary
<a name="use-third-party-git-source-repositories-in-aws-codepipeline-summary"></a>

This pattern describes how to use AWS CodePipeline with third-party Git source repositories.

[AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html) is a continuous delivery service that automates tasks for building, testing, and deploying your software. The service currently supports Git repositories managed by GitHub, [AWS CodeCommit](https://aws.amazon.com/codecommit), and Atlassian Bitbucket. However, some enterprises use third-party Git repositories that are integrated with their single sign-on (SSO) service and Microsoft Active Directory for authentication. You can use these third-party Git repositories as sources for CodePipeline by creating custom actions and webhooks.

A webhook is an HTTP notification that detects events in another tool, such as a GitHub repository, and connects those external events to a pipeline. When you create a webhook in CodePipeline, the service returns a URL that you can use in your Git repository webhook. If you push code to a specific branch of the Git repository, the Git webhook initiates the CodePipeline webhook through this URL, and sets the source stage of the pipeline to **In Progress**. When the pipeline is in this state, a job worker polls CodePipeline for the custom job, runs the job, and sends a success or failure status to CodePipeline. In this case, because the pipeline is in the source stage, the job worker gets the contents of the Git repository, zips the contents, and uploads it to the Amazon Simple Storage Service (Amazon S3) bucket where artifacts for the pipeline are stored, using the object key provided by the polled job. You can also associate a transition for the custom action with an event in Amazon CloudWatch, and initiate the job worker based on the event. This setup enables you to use third-party Git repositories that the service doesn't natively support as sources for CodePipeline.

## Prerequisites and limitations
<a name="use-third-party-git-source-repositories-in-aws-codepipeline-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ A Git repository that supports webhooks and can connect to a CodePipeline webhook URL through the internet
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to work with the AWS account

## Architecture
<a name="use-third-party-git-source-repositories-in-aws-codepipeline-architecture"></a>

The pattern involves these steps:

1. The user commits code to a Git repository.

1. The Git webhook is called.

1. The CodePipeline webhook is called.

1. The pipeline is set to **In Progress**, and the source stage is set to the **In Progress** state.

1. The source stage action initiates a CloudWatch Events rule, indicating that it was started.

1. The CloudWatch event initiates a Lambda function.

1. The Lambda function gets the details of the custom action job.

1. The Lambda function initiates AWS CodeBuild and passes it all the job-related information.

1. CodeBuild gets the public SSH key or user credentials for HTTPS Git access from Secrets Manager.

1. CodeBuild clones the Git repository for a specific branch.

1. CodeBuild zips the archive and uploads it to the S3 bucket that serves as the CodePipeline artifact store.

![Workflow that uses third-party Git source repos as sources for AWS CodePipeline.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/84284bec-b39d-466a-9fd9-994be2c953df/images/85555dab-7317-40f5-86a7-ccb8987c5bf3.png)

## Tools
<a name="use-third-party-git-source-repositories-in-aws-codepipeline-tools"></a>
+ [AWS CodePipeline](https://aws.amazon.com/codepipeline/) – AWS CodePipeline is a fully managed [continuous delivery](https://aws.amazon.com/devops/continuous-delivery/) service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deployment phases of your release process for each code change, based on the release model you define. This enables you to rapidly and reliably deliver features and updates. You can integrate AWS CodePipeline with third-party services such as GitHub or with your own custom plugin.
+ [AWS Lambda](https://aws.amazon.com/lambda/) – AWS Lambda lets you run code without provisioning or managing servers. With Lambda, you can run code for virtually any type of application or backend service with no administration necessary. You upload your code and Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically initiate from other AWS services or call it directly from any web or mobile app.
+ [AWS CodeBuild](https://aws.amazon.com/codebuild/) – AWS CodeBuild is a fully managed [continuous integration](https://aws.amazon.com/devops/continuous-integration/) service that compiles source code, runs tests, and produces software packages that are ready to deploy. With CodeBuild, you don't need to provision, manage, and scale your own build servers. CodeBuild scales continuously and processes multiple builds concurrently, so your builds are not left waiting in a queue. You can get started quickly by using prepackaged build environments, or you can create custom build environments that use your own build tools.
+ [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) – AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Users and applications retrieve secrets by calling Secrets Manager APIs, without having to hardcode sensitive information in plain text. Secrets Manager offers secret rotation with built-in integration for Amazon Relational Database Service (Amazon RDS), Amazon Redshift, and Amazon DocumentDB. The service can be extended to support other types of secrets, including API keys and OAuth tokens. In addition, Secrets Manager lets you control access to secrets by using fine-grained permissions, and audit secret rotation centrally for resources in the AWS Cloud, third-party services, and on-premises environments.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) – Amazon CloudWatch is a monitoring and observation service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides you with data and actionable insights to monitor your applications, respond to systemwide performance changes, optimize resource utilization, and get a unified view of operational health. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, providing you with a unified view of AWS resources, applications, and services that run on AWS and on-premises servers. You can use CloudWatch to detect anomalous behavior in your environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep your applications running smoothly.
+ [Amazon S3](https://aws.amazon.com/s3/) – Amazon Simple Storage Service (Amazon S3) is an object storage service that lets you store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features to help you organize your data and configure finely tuned access controls to meet your specific business, organizational, and compliance requirements.

## Epics
<a name="use-third-party-git-source-repositories-in-aws-codepipeline-epics"></a>

### Create a custom action in CodePipeline
<a name="create-a-custom-action-in-codepipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a custom action using AWS CLI or AWS CloudFormation. | This step involves creating a custom source action that can be used in the source stage of a pipeline in your AWS account in a particular region. You must use AWS CLI or AWS CloudFormation (not the console) to create the custom source action. For more information about the commands and steps described in this and other epics, see the "Related resources" section at the end of this pattern. In AWS CLI, use the create-custom-action-type command. Use --configuration-properties to provide all the parameters required for the job worker to process when it polls CodePipeline for a job. Make sure to note the values provided to the --provider and --action-version options, so that you can use the same values when creating the pipeline with this custom source stage. You can also create the custom source action in AWS CloudFormation by using the resource type AWS::CodePipeline::CustomActionType. | General AWS |

### Set up authentication
<a name="set-up-authentication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SSH key pair. | Create a Secure Shell (SSH) key pair. For instructions, see the GitHub documentation. | Systems/DevOps engineer |
| Create a secret in AWS Secrets Manager. | Copy the contents of the private key from the SSH key pair and create a secret in AWS Secrets Manager. This secret is used for authentication when accessing the Git repository. | General AWS |
| Add the public key to the Git repository. | Add the public key from the SSH key pair to the Git repository account settings, for authentication against the private key. | Systems/DevOps engineer |

### Create a pipeline and webhook
<a name="create-a-pipeline-and-webhook"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a pipeline that includes the custom source action. | Create a pipeline in CodePipeline. When you configure the source stage, choose the custom source action that you created previously. You can do this in the AWS CodePipeline console or in AWS CLI. CodePipeline prompts you for the configuration properties that you set on the custom action. This information is required for the job worker to process the job for the custom action. Follow the wizard and create the next stage for the pipeline. | General AWS |
| Create a CodePipeline webhook. | Create a webhook for the pipeline you created with the custom source action. You must use AWS CLI or AWS CloudFormation (not the console) to create the webhook. In AWS CLI, run the put-webhook command and provide the appropriate values for the webhook options. Make a note of the webhook URL that the command returns. If you're using AWS CloudFormation to create the webhook, use the resource type AWS::CodePipeline::Webhook. Make sure to output the webhook URL from the created resource, and make a note of it. | General AWS |
| Create a Lambda function and CodeBuild project. | In this step, you use Lambda and CodeBuild to create a job worker that will poll CodePipeline for job requests for the custom action, run the job, and return the status result to CodePipeline. Create a Lambda function that is initiated by an Amazon CloudWatch Events rule when the custom source action stage of the pipeline transitions to "In Progress." When the Lambda function is initiated, it should get the custom action job details by polling for jobs. You can use the PollForJobs API to return this information. After the polled job information is obtained, the Lambda function should return an acknowledgment, and then process the information with the data it obtains from the configuration properties for the custom action. When the worker is ready to talk to the Git repository, you might initiate a CodeBuild project, because it's convenient to handle Git tasks by using the SSH client. | General AWS, code developer |

### Create an event in CloudWatch
<a name="create-an-event-in-cloudwatch"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudWatch Events rule. | Create a CloudWatch Events rule that initiates the Lambda function as a target whenever the pipeline's custom action stage transitions to "In Progress." | General AWS |

## Related resources
<a name="use-third-party-git-source-repositories-in-aws-codepipeline-resources"></a>

**Creating a custom action in CodePipeline**
+ [Create and add a custom action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html)
+ [AWS::CodePipeline::CustomActionType resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html)

**Setting up authentication**
+ [Creating and Managing Secrets with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets.html)

**Creating a pipeline and webhook**
+ [Create a Pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html)
+ [put-webhook command reference](https://docs.aws.amazon.com/cli/latest/reference/codepipeline/put-webhook.html)
+ [AWS::CodePipeline::Webhook resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html)
+ [PollForJobs API reference](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PollForJobs.html)
+ [Create and Add a Custom Action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html)
+ [Create a build project in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project.html)

**Creating an event**
+ [Detect and react to changes in pipeline state with Amazon CloudWatch Events](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html)

**Additional references**
+ [Working with pipelines in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines.html)
+ [AWS Lambda developer guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
