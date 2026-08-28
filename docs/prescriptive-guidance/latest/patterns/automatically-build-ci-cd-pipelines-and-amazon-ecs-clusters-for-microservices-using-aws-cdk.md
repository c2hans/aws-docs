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
| Set up the working directory for AWS CDK.  | 1. Create a directory named `cicdproject` on your local machine.<br />2. Download the `cicdstarter.zip` file (attached) into the `cicdproject` directory and unzip it. This creates a folder named `cicdstarter`.<br />3. Run the `cd <user-home>/cicdproject/cicdstarter` command. <br />4. Set up the Python virtual environment by running the `python3 -m venv .venv` command.<br />5. Run the `source ./.venv/bin/activate` command.<br />6. Configure your AWS environment by running the `aws configure` command or by using the following environment variables: `AWS_ACCESS_KEY_ID``AWS_SECRET_ACCESS_KEY` `AWS_DEFAULT_REGION` | AWS DevOps, Cloud infrastructure |

### Create the shared infrastructure
<a name="create-the-shared-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the shared infrastructure. | 1. In your working directory, run the `cd cicdvpcecs` command. <br />2. Run the `pip3 install -r requirements.txt` command to install all required Python dependencies<br />3. Run the `cdk bootstrap command` to set the AWS environment for the AWS CDK. <br />4. Run the `cdk synth --context aws_account=<aws_account_ID> --context aws_region=<aws-region>` command. <br />5. Run the `cdk deploy --context aws_account=<aws_account_ID> --context aws_region=<aws-region>` command.<br />6. The AWS CloudFormation stack creates the following infrastructure:A non-production VPC named `cicd-vpc-ecs/cicd-vpc-nonprod`A production VPC named `cicd-vpc-ecs/cicd-vpc-prod`A non-production Amazon ECS cluster named `cicd-ecs-nonprod`A production Amazon ECS cluster named `cicd-ecs-prod` | AWS DevOps, Cloud infrastructure |
| Monitor the AWS CloudFormation stack. | 1. Sign in to the AWS Management Console, open the AWS CloudFormation console, and then choose the `cicd-vpc-ecs` stack from the list. <br />2. In the stack details pane, choose the **Events** tab and monitor the progress of your stack creation. | AWS DevOps, Cloud infrastructure |
| Test the AWS CloudFormation stack. | 1. After the `cicd-vpc-ecs` AWS CloudFormation stack is created, ensure that the `cicd-vpc-ecs/cicd-vpc-nonprod` and `cicd-vpc-ecs/cicd-vpc-prod` VPCs are created. <br />2. Ensure that the `cicd-ecs-nonprod` and `cicd-ecs-prod` Amazon ECS clusters are created.Make sure that you record the IDs for the two VPCs and the security group IDs for the default security groups in both VPCs. | AWS DevOps, Cloud infrastructure |

### Create a CI/CD pipeline for a microservice
<a name="create-a-ci-cd-pipeline-for-a-microservice"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the infrastructure for the microservice. | 1. Name your microservice. For example, this pattern uses `myservice1` as the microservice's name.<br />2. In your working directory run the `cd <working-directory>/cdkpipeline` command.<br />3. Run the `pip3 install -r requirements.txt` command.<br />4. Run the full `cdk synth` command that is available in the *Additional information* section of this pattern.<br />5. Run the full `cdk deploy` command that is available in the *Additional information* section of this pattern.You can also provide the values for both commands by using the `cdk.json` file in the directory. | AWS DevOps, Cloud infrastructure |
| Monitor the AWS CloudFormation stack. | Open the AWS CloudFormation console and monitor the progress of the `myservice1-cicd-stack` stack. Eventually, the status changes to `CREATE_COMPLETE`*.* | AWS DevOps, Cloud infrastructure |
| Test the AWS CloudFormation stack. | 1. On the AWS CodeCommit console, verify that a repository named `myservice1` exists and contains the starter code.<br />2. On the AWS CodeBuild console, verify that a build project named `myservice1` exists.<br />3. On the Amazon ECR console, verify that an Amazon ECR repository named `myservice1` exists.<br />4. On the Amazon ECS console, verify that a Fargate service named `myservice1` exists in both a non-production and production Amazon ECS cluster.<br />5. On the Amazon Elastic Compute Cloud (Amazon EC2) console, verify that the non-production and production Application Load Balancers are created. Record the DNS names of the ALBs.<br />6. On the AWS CodePipeline console, verify that a pipeline named `myservice1` exists. It must have `Source`, `Build`, `Deploy-NonProd`, and `Deploy-Prod` stages. The pipeline should also have an `in progress` status.<br />7. Monitor the pipeline until all stages are complete. <br />8. Manually approve it for production.<br />9. In a browser window, enter the DNS names of the ALBs.<br />10. The application should display `Hello World` in the non-production and production URLs.  |  |
| Use the pipeline. | 1. Open the CodeCommit repository that you created earlier and open the `index.js` file. <br />2. Replace `Hello World` with `Hello CI/CD`.<br />3. Save and commit the changes to the main branch.<br />4. Verify that the pipeline initiates and that the change goes through the `Build`, `Deploy-NonProd`, and `Deploy-Prod `stages. <br />5. Manually approve the production.<br />6. Both production and non-production URLs should now display `Hello CICD`*.* | AWS DevOps, Cloud infrastructure |
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
