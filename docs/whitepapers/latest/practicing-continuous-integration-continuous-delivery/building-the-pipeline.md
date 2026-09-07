---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/building-the-pipeline.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Building the pipeline
<a name="building-the-pipeline"></a>

 This section discusses building the pipeline. Start by establishing a pipeline with just the components needed for CI and then transition later to a continuous delivery pipeline with more components and stages. This section also discusses how you can consider using AWS Lambda functions and manual approvals for large projects, plan for multiple teams, branches, and AWS Regions.

## Starting with a minimum viable pipeline for continuous integration
<a name="starting-with-a-minimum-viable-pipeline-for-continuous-integration"></a>

 Your organization’s journey toward continuous delivery begins with a minimum viable pipeline (MVP). As discussed in [Implementing continuous integration and continuous delivery](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/implementing-continuous-integration-and-continuous-delivery.html), teams can start with a very simple process, such as implementing a pipeline that performs a code style check or a single unit test without deployment.

 A key component is a continuous delivery orchestration tool. To help you build this pipeline, Amazon provides you with services such as [Amazon CodeCatalyst](https://aws.amazon.com/codecatalyst/).

 Amazon CodeCatalyst [workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-concepts.html) are continuous integration and continuous delivery (CI/CD) pipelines that enable you to easily build, test and deploy applications. CodeCatalyst Workflows help you reliably deliver high-quality application updates frequently, quickly and securely. CodeCatalyst uses a visual editor or YAML to quickly assemble and configure actions to compose workflows that automate your CI/CD pipeline, test reporting and other manual processes. You can get started with a new project from scratch or by using a blueprint from a library of blueprints for popular cloud architecture and application types. if you use a blueprint, a default workflow will be created from the main branch of your repository, that you can then customize. To create a new workflow, once you launch a new project in Amazon CodeCatalyst, navigate to CI/CD > Workflows and create a new workflow.

![Screenshot showing create workflow.](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/create-workflow.png)

 The following is an example of a workflow that includes actions to build, test and deploy backend and frontend code.

![Screenshot showing an example workflow.](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/example-workflow.png)

 Amazon CodeCatalyst supports many purpose [build actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-actions-types.html) developed by AWS as well as third parties such as GitHub Actions. To deploy an application or resource through CodeCatalyst, you can specify a deploy action inside the workflow. A *deploy action* is a workflow building block that defines what you want to deploy, where you want to deploy it, and how you want to deploy it (for example, using a blue/green scheme). Using deploy actions within a workflow, allows for traceability, automatic rollbacks, and monitoring of your deployment as it progresses through the various stages of your workflow and deployment.

 AWS CodePipeline is a CI/CD service that can be used through the AWS Management Console for fast and reliable application and infrastructure updates. AWS CodePipeline builds, tests, and deploys your code every time there is a code change, based on the release process models you define. This enables you to rapidly and reliably deliver features and updates. You can easily build out an end-to-end solution by using our pre-built plugins for popular third-party services like GitHub or by integrating your own custom plugins into any stage of your release process. With AWS CodePipeline, you only pay for what you use. There are no upfront fees or long-term commitments.

The steps of AWS CodePipeline map directly to the [source, build, staging, and production CI/CD stages](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/testing-stages-in-continuous-integration-and-continuous-delivery.html). While continuous delivery is desirable, you could start out with a simple two-step pipeline that checks the source repository and performs a build action:

![Screenshot of AWS CodePipeline — source and build stages](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/source-and-build.png)

 For AWS CodePipeline, the source stage can accept inputs from GitHub, AWS CodeCommit, Atlassian Bitbucket, and Amazon Simple Storage Service (Amazon S3). Automating the build process is a critical first step for implementing continuous delivery and moving toward continuous deployment. Eliminating human involvement in producing build artifacts removes the burden from your team, minimizes errors introduced by manual packaging, and allows you to start packaging consumable artifacts more often.

 AWS CodePipeline works seamlessly with AWS CodeBuild, a fully managed build service, to make it easier to set up a build step within your pipeline that packages your code and runs unit tests. With AWS CodeBuild, you don’t need to provision, manage, or scale your own build servers. AWS CodeBuild scales continuously and processes multiple builds concurrently so your builds are not left waiting in a queue. AWS CodePipeline also integrates with build servers such as Jenkins, Solano CI, and TeamCity.

 For example, in the following build stage, three actions (unit testing, code style checks, and code metrics collection) run in parallel. Using AWS CodeBuild, these steps can be added as new projects without any further effort in building or installing build servers to handle the load.

![Screenshot of AWS CodePipeline — build functionality](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/build-functionality.png)

 The source and build stages shown in the figure *AWS CodePipeline — source and build stages*, along with supporting processes and automation, support your team’s transition toward a Continuous Integration. At this level of maturity, developers need to regularly pay attention to build and test results. They need to grow and maintain a healthy unit test base as well. This, in turn, bolsters the entire team’s confidence in the CI/CD pipeline and furthers its adoption.

![Screenshot showing AWS CodePipeline stages](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/stages.png)

## Continuous delivery pipeline
<a name="continuous-delivery-pipeline"></a>

 After the continuous integration pipeline has been implemented and supporting processes have been established, your teams can start transitioning toward the continuous delivery pipeline. This transition requires teams to automate both building and deploying applications.

 A continuous delivery pipeline is characterized by the presence of staging and production steps, where the production step is performed after a manual approval.

 In the same manner as the continuous integration pipeline was built, your teams can gradually start building a continuous delivery pipeline by writing their deployment scripts.

 Depending on the needs of an application, some of the deployment steps can be abstracted by existing AWS services. For example, AWS CodePipeline directly integrates with AWS CodeDeploy, a service that automates code deployments to Amazon EC2 instances and instances running on-premises.

 AWS has detailed [documentation](https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started-w.html#getting-started-w-create-deployment) on how to implement and integrate AWS CodeDeploy with your infrastructure and pipeline. If you are using Amazon CodeCatalyst, reference the [documentation](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy.html) for deploying using workflows. You can add a deploy action (for example, Deploy to Amazon ECS) to your workflow that defines what you want to deploy, where you want to deploy it, and how you want to deploy it (for example, using a blue/green scheme).

 After your team successfully automates the deployment of the application, deployment stages can be expanded with various tests. For example you can add other out-of-the-box integrations with services like Ghost Inspector, Runscope, and others as shown in the following figure.

![Screenshot showing AWS CodePipeline—code tests in deployment stages](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/code-tests.png)

## Adding Lambda actions
<a name="adding-lambda-actions"></a>

 AWS CodePipeline support [integration with AWS Lambda](https://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-lambda-integration.html). This integration enables implementing a broad set of tasks, such as creating custom resources in your environment, integrating with third-party systems (such as Slack), and performing checks on your newly deployed environment.

 Lambda functions can be used in CI/CD pipelines to do many tasks based on your needs. Some examples include:
+  Roll out changes to your environment by applying or updating an AWS CloudFormation template.
+  Create resources on demand in one stage of a pipeline using AWS CloudFormation and delete them in another stage.
+  Deploy to Amazon Elastic Container Service (ECS) Docker instances.
+  Back up resources before building or deploying by creating an AMI snapshot.
+  Add integration with third-party products to your pipeline, such as posting messages to an Internet Relay Chat (IRC) client.

## Manual approvals
<a name="manual-approvals"></a>

 Add an approval action to a stage in a pipeline at the point where you want the pipeline processing to stop so that someone with the required AWS Identity and Access Management (IAM) permissions can approve or reject the action.

 If the action is approved, the pipeline processing resumes. If the action is rejected—or if no one approves or rejects the action within seven days of the pipeline reaching the action and stopping—the result is the same as an action failing, and the pipeline processing does not continue.

![Screenshot showing AWS CodeDeploy—manual approvals](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/manual-approvals.png)

## Deploying infrastructure code changes in a CI/CD pipeline
<a name="deploying-infrastructure-code-changes-in-a-cicd-pipeline"></a>

 AWS CodePipeline lets you select AWS CloudFormation as a deployment action in any stage of your pipeline. You can then choose the specific action you would like AWS CloudFormation to perform, such as creating or deleting stacks and creating or executing [change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#d0e3952).

 A [stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#d0e3929) is an AWS CloudFormation concept and represents a group of related AWS resources. While there are many ways of provisioning infrastructure as code (IaC), AWS CloudFormation is a comprehensive tool recommended by AWS as a scalable, complete solution that can describe the most comprehensive set of AWS resources as code. AWS recommends using AWS CloudFormation in an AWS CodePipeline project to [track infrastructure changes and tests](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline.html).

## CI/CD for serverless applications
<a name="cicd-for-serverless-applications"></a>

 Amazon CodeCatalyst makes building CI/CD pipelines or workflows easy for serverless applications. You can use one of the serverless [blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/custom-blueprints.html) from the library of blueprints to kickstart a project within minutes. You can also use AWS CodePipeline, AWS CodeBuild, and AWS CloudFormation to build CI/CD pipelines for serverless applications. Serverless applications integrate managed services such as [Amazon Cognito](https://aws.amazon.com/cognito), Amazon S3, and Amazon DynamoDB with event-driven service, and AWS Lambda to deploy applications in a manner which doesn’t require managing servers. If you are a serverless application developer, you can use the combination of AWS CodePipeline, AWS CodeBuild, and AWS CloudFormation to automate the building, testing, and deployment of serverless applications that are expressed in templates built with the AWS Serverless Application Model. For more information, refer to the AWS Lambda documentation for [Rolling deployments for Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-rolling-deployments.html).

 You can also create secure CI/CD pipelines that follow your organization’s best practices with [CDK Pipelines](https://docs.aws.amazon.com/cdk/v2/guide/cdk_pipeline.html) or AWS Serverless Application Model Pipelines (AWS SAM Pipelines). AWS SAM Pipelines are a new feature of AWS SAM CLI that give you access to benefits of CI/CD in minutes, such as accelerating deployment frequency, shortening lead time for changes, and reducing deployment errors. AWS SAM Pipelines come with a set of default pipeline templates for AWS CodeBuild/CodePipeline that follow AWS deployment best practices. For more information and to view the tutorial, refer to the blog [Introducing AWS SAM Pipelines](https://aws.amazon.com/blogs/compute/introducing-aws-sam-pipelines-automatically-generate-deployment-pipelines-for-serverless-applications/).
