---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html
---

# Automatically build CI/CD pipelines and Amazon ECS clusters for microservices using AWS CDK
<a name="automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk"></a>

*Varsha Raju, Amazon Web Services*

## Summary
<a name="automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk-summary"></a>

This pattern describes how to automatically create the continuous integration and continuous delivery (CI/CD) pipelines and underlying infrastructure for building and deploying microservices on Amazon Elastic Container Service (Amazon ECS). You can use this approach if you want to set up proof-of-concept CI/CD pipelines to show your organization the benefits of CI/CD, microservices, and DevOps. You can also use this approach to create initial CI/CD pipelines that you can then customize or change according to your organization’s requirements.

The pattern’s approach creates a production environment and non-production environment that each have a virtual private cloud (VPC) and an Amazon ECS cluster configured to run in two Availability Zones. These environments are shared by all your microservices and you then create a CI/CD pipeline for each microservice. These CI/CD pipelines pull changes from a source repository in AWS CodeCommit, automatically build the changes, and then deploy them into your production and non-production environments. When a pipeline successfully completes all of its stages, you can use URLs to access the microservice in the production and non-production environments.

## Prerequisites and limitations
<a name="automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk-prereqs"></a>

**Prerequisites **
+ An active Amazon Web Services (AWS) account.
+ An existing Amazon Simple Storage Service (Amazon S3) bucket that contains the `starter-code.zip` file (attached).
+ AWS Cloud Development Kit (AWS CDK), installed and configured in your account. For more information about this, see [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) in the AWS CDK documentation.
+ Python 3 and `pip`, installed and configured. For more information about this, see the [Python documentation](https://www.python.org/).
+ Familiarity with AWS CDK, AWS CodePipeline, AWS CodeBuild, CodeCommit, Amazon Elastic Container Registry (Amazon ECR), Amazon ECS, and AWS Fargate.
+ Familiarity with Docker.
+ An understanding of CI/CD and DevOps.

**Limitations**
+ General AWS account limits apply. For more information about this, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in the AWS General Reference documentation.

**Product versions**
+ The code was tested using Node.js version 16.13.0 and AWS CDK version 1.132.0.

## Architecture
<a name="automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk-architecture"></a>

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/05ac2cad-408e-433f-8150-0a2b71f63cfd/images/6fa3dbef-88de-4b3f-ae41-dfa90256a058.png)

The diagram shows the following workflow:

1. An application developer commits code to a CodeCommit repository.

1. A pipeline is initiated.

1. CodeBuild builds and pushes the Docker image to an Amazon ECR repository

1. CodePipeline deploys a new image to an existing Fargate service in a non-production Amazon ECS cluster.

1. Amazon ECS pulls the image from the Amazon ECR repository into a non-production Fargate service.

1. Testing is performed using a non-production URL.

1. The release manager approves the production deployment.

1. CodePipeline deploys the new image to an existing Fargate service in a production Amazon ECS cluster

1. Amazon ECS pulls the image from the Amazon ECR repository into the production Fargate service.

1. Production users access your feature by using a production URL.

**Technology stack  **
+ AWS CDK
+ CodeBuild
+ CodeCommit
+ CodePipeline
+ Amazon ECR
+ Amazon ECS
+ Amazon VPC

**Automation and scale**

You can use this pattern’s approach to create pipelines for microservices deployed in a shared AWS CloudFormation stack. The automation can create more than one Amazon ECS cluster in each VPC and also create pipelines for microservices deployed in a shared Amazon ECS cluster. However, this requires that you provide new resource information as inputs to the pipeline stack.

## Tools
<a name="automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk-tools"></a>
+ [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) – AWS Cloud Development Kit (AWS CDK) is a software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.
+ [AWS CodeBuild ](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)– AWS CodeBuild is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) – AWS CodeCommit is a version control service that enables you to privately store and manage Git repositories in the AWS Cloud. CodeCommit eliminates the need for you to manage your own source control system or worry about scaling its infrastructure.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)  – AWS CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software. You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.
+ [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) – Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast container management service that is used for running, stopping, and managing containers on a cluster. You can run your tasks and services on a serverless infrastructure that is managed by AWS Fargate. Alternatively, for more control over your infrastructure, you can run your tasks and services on a cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances that you manage.
+ [Docker](https://www.docker.com/) – Docker helps developers to pack, ship, and run any application as a lightweight, portable, and self-sufficient container.

**Code **

The code for this pattern is available in the `cicdstarter.zip` and `starter-code.zip` files (attached).

## Epics
<a name="automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the working directory for AWS CDK.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html) | AWS DevOps, Cloud infrastructure |

### Create the shared infrastructure
<a name="create-the-shared-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the shared infrastructure. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html) | AWS DevOps, Cloud infrastructure |
| Monitor the AWS CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html) | AWS DevOps, Cloud infrastructure |
| Test the AWS CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html)Make sure that you record the IDs for the two VPCs and the security group IDs for the default security groups in both VPCs. | AWS DevOps, Cloud infrastructure |

### Create a CI/CD pipeline for a microservice
<a name="create-a-ci-cd-pipeline-for-a-microservice"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the infrastructure for the microservice. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html)You can also provide the values for both commands by using the `cdk.json` file in the directory. | AWS DevOps, Cloud infrastructure |
| Monitor the AWS CloudFormation stack. | Open the AWS CloudFormation console and monitor the progress of the `myservice1-cicd-stack` stack. Eventually, the status changes to `CREATE_COMPLETE`*.* | AWS DevOps, Cloud infrastructure |
| Test the AWS CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html) |  |
| Use the pipeline. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html) | AWS DevOps, Cloud infrastructure |
| Repeat this epic for each microservice. | Repeat the tasks in this epic to create a CI/CD pipeline for each of your microservices. | AWS DevOps, Cloud infrastructure |

## Related resources
<a name="automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk-resources"></a>
+ [Using Python with AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)
+ [AWS CDK Python reference](https://docs.aws.amazon.com/cdk/api/latest/python/index.html)
+ [Creating an AWS Fargate service using the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/ecs_example.html)

## Additional information
<a name="automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk-additional"></a>

**`cdk synth` command**

```
cdk synth --context aws_account=<aws_account_number> --context aws_region=<aws_region> --context vpc_nonprod_id=<id_of_non_production VPC> --context vpc_prod_id=<id_of_production_VPC> --context ecssg_nonprod_id=< default_security_group_id_of_non-production_VPC> --context ecssg_prod_id=<default_security_group_id_of_production_VPC> --context code_commit_s3_bucket_for_code=<S3 bucket name> --context code_commit_s3_object_key_for_code=<Object_key_of_starter_code> --context microservice_name=<name_of_microservice>
```

**`cdk deploy `command**

```
cdk deploy --context aws_account=<aws_account_number> --context aws_region=<aws_region> --context vpc_nonprod_id=<id_of_non_production_VPC> --context vpc_prod_id=<id_of_production_VPC> --context ecssg_nonprod_id=< default_security_group_id_of_non-production_VPC> --context ecssg_prod_id=<default_security_group_id_of_production_VPC> --context code_commit_s3_bucket_for_code=<S3 bucket name> --context code_commit_s3_object_key_for_code=<Object_key_of_starter_code> --context microservice_name=<name_of_microservice>
```

## Attachments
<a name="attachments-05ac2cad-408e-433f-8150-0a2b71f63cfd"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/05ac2cad-408e-433f-8150-0a2b71f63cfd/attachments/attachment.zip)
