---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-the-aws-fargate-waitcondition-hook-construct.html
---

# Coordinate resource dependency and task execution by using the AWS Fargate WaitCondition hook construct
<a name="use-the-aws-fargate-waitcondition-hook-construct"></a>

*Stan Fan, Amazon Web Services*

## Summary
<a name="use-the-aws-fargate-waitcondition-hook-construct-summary"></a>

This pattern describes the WaitCondition hook (`waitcondition-hook-for-aws-fargate-task`) npm package, which is a cloud-native solution designed for orchestrating [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) tasks in Amazon Elastic Container Service (Amazon ECS) clusters.

The WaitCondition hook is an AWS Cloud Development Kit (AWS CDK) construct that’s specifically tailored for integration with AWS CloudFormation. The WaitCondition hook provides the following key capabilities:
+ Acts as a wait condition mechanism, pausing CloudFormation stack execution until a specified Fargate task completes, which helps with orderly deployments and resource provisioning.
+ Supports TypeScript and Python, making it ideal for AWS CDK projects.
+ Allows developers and architects to orchestrate deployments by coordinating task completion and resource management for containerized applications on AWS.
+ Enables running Fargate tasks with one or multiple containers embedded in a CloudFormation lifecycle. and can handle task failures and roll back the CloudFormation stack after a task failure.
+ Provides flexibility to add dependencies between resources and the Fargate task execution results, enabling custom tasks or invoking other endpoints. For instance, you can pause a CloudFormation stack and wait for a database migration (done by a Fargate task) and provision other resources that might depend on the success of the database migration.

## Prerequisites and limitations
<a name="use-the-aws-fargate-waitcondition-hook-construct-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Cloud Development Kit (AWS CDK) Command Line Interface (CLI) installed on a local workstation. For more information, see [AWS CDK CLI reference](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) in the AWS CDK documentation.
+ Node package manager (npm), installed on a local workstation and configured for the [AWS CDK in TypeScript](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-typescript.html). For more information, see [Downloading and installing Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) in the npm documentation.
+ Yarn installed on a local workstation. For more information, see [Installation](https://yarnpkg.com/getting-started/install) in the Yarn documentation.

**Limitations**
+ This solution is deployed to a single AWS account.
+ The expected return code of the container is `0` for success. Any other return code indicates failure, and the CloudFormation stack will roll back.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="use-the-aws-fargate-waitcondition-hook-construct-architecture"></a>

The following diagram shows the construct architecture.

![AWS Step Functions workflow of waitcondition-hook-for-aws-fargate-task construct.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e58680e3-f89f-422f-b0e1-e85605ae8bf9/images/598020df-908c-4486-9844-c05af759c18a.png)

The diagram shows the workflow of `waitcondition-hook-for-aws-fargate-task`:

1. `WaitCondition` and `WaitConditionHandler` are provisioned to listen to the response from the AWS Lambda functions.

1. Depending on the result of the task, either the `CallbackFunction` or the `ErrorHandlerFunction` is triggered by the finish of the Fargate task.

1. The Lambda function sends a SUCCEED or FAILURE signal to `WaitConditionHandler`.

1. `WaitConditionHandler` continues to provision the resources if the execution result of the Fargate task succeeds, or rolls back the stack if the task failed.

The following diagram shows an example of a workflow to perform a database migration.

![Workflow of Amazon RDS database migration using WaitCondition hook construct.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e58680e3-f89f-422f-b0e1-e85605ae8bf9/images/3b83fc2a-80bb-4ba9-9637-782060493cf0.png)

The example workflow uses the `waitcondition-hook-for-aws-fargate-task` construct to perform a database migration, as follows:

1. An Amazon Relational Database Service (Amazon RDS) instance is provisioned.

1. The `waitcondition-hook-for-aws-fargate-task` construct runs the database migration task and pauses the stack as an Amazon Elastic Compute Cloud (Amazon EC2) instance.

1. If the migration task finishes successfully, it sends a Succeed signal to CloudFormation. Otherwise, it sends a Fail signal to CloudFormation and rolls back the stack.

## Tools
<a name="use-the-aws-fargate-waitcondition-hook-construct-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a software development framework that helps you define cloud infrastructure in code and provision it through CloudFormation.
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.
+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) helps you run containers without needing to manage servers or Amazon EC2 instances. It’s used in conjunction with Amazon ECS.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you would operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**
+ [npm](https://docs.npmjs.com/about-npm) is a software registry that runs in a Node.js environment and is used to share or borrow packages and manage deployment of private packages.
+ [Yarn](https://yarnpkg.com/) is an open source package manager that you can use to manage dependencies in JavaScript projects. Yarn can assist you with installing, updating, configuring, and removing packages dependencies.

**Code repository**

The code for this pattern is available in the GitHub [waitcondition-hook-for-aws-fargate-task](https://github.com/aws-samples/waitcondition-hook-for-aws-fargate-task) repository.

## Best practices
<a name="use-the-aws-fargate-waitcondition-hook-construct-best-practices"></a>
+ When building your AWS CDK app, follow the [Best practices for developing and deploying cloud infrastructure with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html) in the AWS CDK v2 documentation.
+ For the AWS Fargate task, follow the [Best practices for Amazon ECS container images](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/application.html) in the Amazon ECS documentation.

## Epics
<a name="use-the-aws-fargate-waitcondition-hook-construct-epics"></a>

### Set up the AWS CDK
<a name="set-up-the-cdk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the AWS CDK. | To install the AWS CDK on your local machine or other environment, run the following command: <pre>npm install -g aws-cdk@latest</pre> | Cloud architect, App developer |
| Bootstrap the AWS CDK. | [Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) is the process of preparing an [environment](https://docs.aws.amazon.com/cdk/v2/guide/environments.html) for deployment. To bootstrap your AWS CDK toolkit for the target AWS account and AWS Region, run the following command:<pre>cdk bootstrap aws://ACCOUNT-NUMBER-1/REGION-1 </pre><br />This command creates a CloudFormation stack named `CDKToolkit`.  | Cloud architect |

### Run the WaitCondition hook for AWS Fargate tasks construct
<a name="run-the-waitcondition-hook-for-fargatelong-tasks-construct"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the CDK project. | Create a CDK project using the language that you prefer. This pattern uses TypeScript. To create a CDK project using TypeScript, run the following command: <br />`cdk init app —language typescript` | Cloud architect |
| Install the package. | Execute `npm install` on the root path of your CDK project. After the CDK library has been installed, run the following command to install `waitcondition-hook-for-aws-fargate-task`: <br />`yarn add waitcondition-hook-for-aws-fargate-task` | Cloud architect |
| Build your CDK application and Amazon ECS components. | Build your CDK project. An Amazon ECS task definition resource is required. For information about creating a task definition, see [Amazon ECS task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) in the Amazon ECS documentation.<br />The following example uses this construct:<pre>import * as cdk from 'aws-cdk-lib';<br />import { Vpc } from 'aws-cdk-lib/aws-ec2';<br />import * as ecr from 'aws-cdk-lib/aws-ecr';<br />import * as ecs from 'aws-cdk-lib/aws-ecs';<br />import { Construct } from 'constructs';<br />import { FargateRunner } from 'waitcondition-hook-for-aws-fargate-task';<br />import { Queue } from 'aws-cdk-lib/aws-sqs';<br /><br />export class FargateRunnerStack extends cdk.Stack {<br />    constructor(scope: Construct, id: string, props?: cdk.StackProps) {<br />        super(scope, id, props);<br />        // Define the VPC<br />        const vpc = new Vpc(this, 'MyVpc')<br />        // Define the Fargate Task<br />        const taskDefinition = new ecs.FargateTaskDefinition(this, 'MyTask', {});<br />        // Import exiting ecr repo<br />        const repo = ecr.Repository.fromRepositoryName(this, 'MyRepo', 'RepoName');<br />        // Add a container to the task<br />        taskDefinition.addContainer('MyContainer', {<br />            image: ecs.ContainerImage.fromEcrRepository(repo),<br />        });<br />        // Create the Fargate runner<br />        const myFargateRunner = new FargateRunner(this, 'MyRunner', {<br />            fargateTaskDef: taskDefinition,<br />            timeout: `${60 * 5}`,<br />            vpc: vpc,<br />        });<br />        // Create the SQS queue<br />        const myQueue = new Queue(this, 'MyQueue', {});<br />        // Add dependency<br />        myQueue.node.addDependency(myFargateRunner);<br />    }<br />}</pre> | Cloud architect |
| Synth and launch the CDK application. | 1. To generate the assets and CloudFormation template, run the following command in your CDK root path:<br />`cdk synth` <br />2. After the `synth` command is successful, run the following command to deploy the resources:<br />`cdk deploy` The `waitcondition-hook-for-aws-fargate-task` construct runs the Fargate task.  | Cloud architect |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up resources. | To clean up the resources provisioned from the previous step, run the following command:<pre>cdk destroy </pre> | Cloud architect |

## Troubleshooting
<a name="use-the-aws-fargate-waitcondition-hook-construct-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| General CloudFormation stack failure | To help troubleshoot general CloudFormation stack failures, add the `--no-rollback` flag as shown in the following example: <pre>cdk deploy --no-rollback</pre><br />This command will pause the CloudFormation stack from rolling back, which gives you resources to troubleshoot. For more information, see [Choose how to handle failures when provisioning resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-failure-options.html) in the CloudFormation documentation. |
| AWS Step Functions failure | An AWS Step Functions state machine might fail to execute for different reasons. With `—disable-rollback` configured, use the following steps to troubleshoot:1. Sign in to the AWS Management Console, enter **Step Functions** in the **Search** field, and then choose the Step Functions service.<br />2. In the left navigation pane, choose **State machines** and then select the state machine that is provisioned by the CloudFormation stack.<br />3. In **Executions**, choose the name of the execution that failed unexpectedly.<br />4. In the **Event** view, choose the failed step.<br />For more information, see [Troubleshooting issues in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/troubleshooting.html) and [Viewing execution details in the Step Functions console](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-view-execution-details.html#exec-details-intf-step-details) in the AWS Step Functions documentation. |
| AWS Lambda function failure | This construct provisions two Lambda functions: `CallbackFunction` and `ErrorhandlerFunction`. They can fail for various reasons such as unhandled exceptions. Use the following steps to troubleshoot: 1. Sign in to the AWS Management Console, enter **CloudWatch** in the **Search** field, and then choose the CloudWatch service.<br />2. In the left navigation pane, choose **Log groups**. <br />3. In the **Search** field, enter the name of the Lambda function.<br />4. Choose the log group name that’s associated with the Lambda function.<br />5. To go to the Lambda function execution result, choose the latest log stream. <br />For more information, see [Troubleshooting issues in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-troubleshooting.html) in the AWS Lambda documentation. |

## Related resources
<a name="use-the-aws-fargate-waitcondition-hook-construct-resources"></a>

**AWS documentation**
+ [AWS CDK Construct API Reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html)
+ [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
+ [Learn how to create and use Amazon ECS resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html)
+ [Learn how to get started with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started-with-sfn.html)
+ [What is AWS CDK?](https://docs.aws.amazon.com/cdk/v2/guide/home.html)

**Other resources**
+ [Waitcondition Hook for AWS Fargate task](https://pypi.org/project/waitcondition-hook-for-aws-fargate-task/) (npm)
+ [waitcondition-hook-for-aws-fargate-task 1.0.6](https://pypi.org/project/waitcondition-hook-for-aws-fargate-task/) (pypi.org)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
