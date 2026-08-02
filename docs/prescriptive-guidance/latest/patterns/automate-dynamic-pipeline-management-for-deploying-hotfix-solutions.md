---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html
---

# Automate dynamic pipeline management for deploying hotfix solutions in Gitflow environments by using AWS Service Catalog and AWS CodePipeline
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions"></a>

*Balaji Vedagiri, Faisal Shahdad, Shanmugam Shanker, and Vivek Thangamuthu, Amazon Web Services*

## Summary
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-summary"></a>

**Note**
AWS CodeCommit is no longer available to new customers. Existing customers of AWS CodeCommit can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider)

This pattern addresses a scenario of managing a dynamic hotfix pipeline that’s dedicated solely to deploying hotfix solutions to a production environment securely. The solution is implemented and managed by using an AWS Service Catalog portfolio and product. An Amazon EventBridge rule is used for event automation. Restrictions are enforced by using Service Catalog portfolio constraints and AWS Identity and Access Management (IAM) roles for developers. Only an AWS Lambda function is allowed to launch the Service Catalog product, triggered by the EventBridge rule. This pattern is designed for environments with a specific Gitflow setup, which is described in [Additional information](#automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-additional).

Typically, a hotfix is deployed to address critical or security issues reported in a live environment, such as Production. Hotfixes should be deployed directly to Staging and Production environments only. The Staging and Production pipelines are used extensively for regular development requests. These pipelines can’t be used to deploy hotfixes because there are ongoing features in quality assurance that can’t be promoted to Production. To release hotfixes, this pattern describes a dynamic, short-lived pipeline with the following security features:
+ **Automatic creation** – A hotfix pipeline is automatically created whenever a hotfix branch is created in an AWS CodeCommit repository.
+ **Access restrictions** – Developers don’t have access to create this pipeline outside of the hotfix process.
+ **Controlled stage** – The pipeline has a controlled stage with a special access token, ensuring that a pull request (PR) can only be created once.
+ **Approval stages** – Approval stages are included in the pipeline to get necessary approvals from relevant stakeholders.
+ **Automatic deletion** – The hotfix pipeline is automatically deleted whenever a `hotfix` branch is deleted in the CodeCommit repository after it’s merged with a PR.

## Prerequisites and limitations
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-prereqs"></a>

**Prerequisites**
+ Three active AWS accounts are required as follows:
  + Tools account - For continuous integration and continuous delivery (CI/CD) setup.
  + Stage account - For user acceptance testing.
  + Production account - For a business end user.
  + (Optional) Add an AWS account to act as a QA account. This account is required if you want both a main pipeline setup, including QA, and a hotfix pipeline solution for testing.
+ An AWS CloudFormation stack with an optional condition to deploy in the QA account using the main pipeline, if needed. The pattern can still be tested without the main pipeline setup by creating and deleting a `hotfix` branch.
+ An Amazon Simple Storage Service (Amazon S3) bucket to store the CloudFormation templates that are used to create Service Catalog products.
+ Create PR approval rules for the CodeCommit repository in accordance with the compliance requirements (after creating the repository).
+ Restrict the IAM permissions of developers and team leads to deny the execution of the [prcreation-lambda](https://github.com/aws-samples/dynamic_hotfix_codepipeline/blob/main/pre-requisites/lambdasetup.yaml#L55) Lambda function because it should be invoked only from the pipeline.

**Limitations**
+ The CloudFormation provider is used in the deploy stage, and the application is deployed using a CloudFormation change set. If you want to use a different deployment option, modify the CodePipeline stack as required.
+ This pattern uses AWS CodeBuild and other configuration files to deploy a sample microservice. If you have a different workload type (for example, serverless workloads), you must update all relevant configurations.
+ This pattern deploys the application in a single AWS Region (for example, US East (N. Virginia) us-east-1) across AWS accounts. To deploy across multiple Regions, change the Region reference in commands and stacks.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-architecture"></a>

The diagrams in this section provide workflows for a create lifecycle event and for a delete lifecycle event.

![Workflow to create a lifecycle event.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/64311acc-8c0f-4734-aa1b-74345d86c752/images/3939f77c-4221-4c23-a3a1-3e8a294b2b32.png)

The preceding diagram for creating a lifecycle event shows the following:

1. The developer creates a `hotfix-*` branch in the CodeCommit repository to develop a hotfix-related solution.

1. The `hotfix-*` branch creation event is captured through the EventBridge rule. The event details include the repository name and branch name.

1. The EventBridge rule invokes the AWS Lambda function `hotfix-lambda-function`. The EventBridge rule passes the event information to the Lambda function as input.

1. The Lambda function processes the input to retrieve the repository name and branch name. It launches the Service Catalog product with values retrieved from the processed input.

1. The Service Catalog product includes a pipeline setup that will deploy the solution to the Stage and Production environments. The pipeline block includes source, build, and deploy stages. Also, there is a manual approval stage to promote the deployment for the Production environment.

1. The source stage retrieves the code from the repository and `hotfix-*` branch that was created in the first step. The code is passed to the build stage through an Amazon S3 bucket for artifacts. In the build stage, a container image is created that includes the hotfix that is developed in the `hotfix-*` branch and pushed into Amazon Elastic Container Registry (Amazon ECR).

1. The deploy stage to the stage environment updates Amazon Elastic Container Service (Amazon ECS) with the latest container image that includes the hotfix. The hotfix is deployed by creating and executing a CloudFormation change set.

1. The `prcreation-lambda` Lambda function is invoked after successful deployment in the Stage environment. This Lambda function creates a PR from the `hotfix-*` branch to the `develop` and `main` branches of the repository. The Lambda function ensures that the fix developed in the `hotfix-*` branch is backmerged and included in subsequent deployments.

1. A manual approval stage helps to ensure that the necessary stakeholders review the fix and give approval to deploy in Production.

1. The deploy stage to the production environment updates Amazon ECS with the latest container image that includes the hotfix. The hotfix is deployed by creating and executing a CloudFormation change set.

![Workflow to delete a lifecycle event.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/64311acc-8c0f-4734-aa1b-74345d86c752/images/192aa897-bd9b-4a9f-804e-340371612b3b.png)

The preceding diagram for deleting a lifecycle event shows the following:

1. The developer deletes the `hotfix-*` branch after successful deployment of the hotfix to the production environment.

1. The `hotfix-*` branch deletion event is captured through an EventBridge rule. The event details include the repository name and branch name.

1. The EventBridge rule invokes the Lambda function. The EventBridge rule passes the event information to the Lambda function as input.

1. The Lambda function processes the input to retrieve the repository name and branch name. The Lambda function determines the respective Service Catalog product from the passed input and then terminates the product.

1. The Service Catalog provisioned product termination deletes the pipeline and relevant resources that were created earlier in that product.

**Automation and scale**
+ The pattern includes an EventBridge rule and a Lambda function, which can handle multiple hotfix branch creation requests in parallel. The Lambda function provisions the Service Catalog product for the matching event rule.
+ The pipeline setup is handled by using the Service Catalog product, which provides version control capabilities. The solution also scales automatically to handle multiple hotfix developments for the same application in parallel.
+ The [prcreation-lambda](https://github.com/aws-samples/dynamic_hotfix_codepipeline/blob/main/pre-requisites/lambdasetup.yaml#L55) function ensures that these hotfix changes are also merged back into the `main` and the `develop` branches through an automatic pull request creation. This approach is essential to keep the `main` and the `develop` branches up to date with all fixes and avoid potential code regressions. This process helps to maintain consistency across branches and prevent code regressions by ensuring that all long-lived branches have the latest fixes.

## Tools
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system. AWS CodeCommit is no longer available to new customers. Existing customers of AWS CodeCommit can continue to use the service as normal. For more information, see [How to migrate your AWS CodeCommit repository to another Git provider](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/).
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) helps you centrally manage catalogs of IT services that are approved for AWS. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [CloudFormation Linter (cfn-lint)](https://github.com/aws-cloudformation/cfn-lint) is a linter that checks CloudFormation YAML or JSON templates against the [CloudFormation resource specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html). It also performs other checks, such as checking for valid values for resource properties and adherence to best practices.
+ [cfn-nag](https://github.com/stelligent/cfn_nag) is an open source tool that that identifies potential security issues in CloudFormation templates by searching for patterns.
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers. This pattern uses Docker to build and test container images locally.
+ [Git](https://git-scm.com/docs) is an open-source, distributed version control system.

**Code repository**

The code for this pattern is available in the GitHub [dynamic\_hotfix\_codepipeline](https://github.com/aws-samples/dynamic_hotfix_codepipeline) repository.

## Best practices
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-best-practices"></a>

Review and adjust IAM roles and service control policies (SCP) in your environment to ensure that they restrict access appropriately. This is crucial to prevent any actions that could override the security measures included in this pattern. Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-epics"></a>

### Set up the work environment
<a name="set-up-the-work-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the sample [repository](https://github.com/aws-samples/dynamic_hotfix_codepipeline) into a new directory in your work location, run the following command:<pre>git clone git@github.com:aws-samples/dynamic_hotfix_codepipeline.git</pre> | AWS DevOps |
| Export environment variables for CloudFormation stack deployment. | Define the following environment variables that will be used as input to the CloudFormation stacks later in this pattern.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html)<pre>export BucketStartName=<BucketName></pre>[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html)<pre>export ProdAccount=<prodaccountnumber><br />export StageAccount=<stage/preprodaccountnumber><br />export QAAccount=<qaccountnumber><br />export ToolsAccount=<toolsaccountnumber><br />export DepRegion=<region></pre> | AWS DevOps |

### Set up prerequisites required in AWS accounts
<a name="set-up-prerequisites-required-in-aws-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create resources required for CI/CD in the tools account. | To deploy the CloudFormation stack in the tools account, use the following commands. (Remove the `QAAccount` parameter if you’re not using the QA account for setup.)<pre>#InToolsAccount<br />aws cloudformation deploy \<br />    --template-file pre-requisites/pre-reqs.yaml \<br />    --stack-name prereqs \<br />    --parameter-overrides BucketStartName=${BucketStartName} \<br />    ApplicationName=${ApplicationName} ProdAccount=${ProdAccount} \<br />    StageAccount=${StageAccount} ToolsAccount=${ToolsAccount} \<br />    QAAccount=${QAAccount} \<br />    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --region ${DepRegion}</pre><br />Make a note of the resources that the CodeCommit repository and Amazon ECR created from the preceding stack. These parameters are necessary to set up the `main` branch of the pipeline in upcoming steps. | AWS DevOps |
| Create resources required for CI/CD in the workload accounts. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html) | AWS DevOps |
| Update the S3 artifact bucket policy to allow access for workload accounts. | To update the CloudFormation stack prerequisites in the tools account, use the following commands to add all required permissions for the Stage and Production workload accounts. (Remove the `QAAccount` parameter if you’re not using it for setup.)<pre>#InToolsAccount<br />aws cloudformation deploy \<br />    --template-file pre-requisites/pre-reqs.yaml \<br />    --stack-name prereqs \<br />    --parameter-overrides BucketStartName=${BucketStartName} \<br />    ApplicationName=${ApplicationName} ProdAccount=${ProdAccount} \<br />    StageAccount=${StageAccount} ToolsAccount=${ToolsAccount} \<br />    QAAccount=${QAAccount} PutPolicy=true \<br />    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --region ${DepRegion}</pre> | AWS DevOps |

### Set up Lambda function and Service Catalog resources in tools account
<a name="set-up-lam-function-and-sc-resources-in-tools-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the Service Catalog portfolio and products. | To set up the Service Catalog portfolio and products, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html) | AWS DevOps |
| Set up Lambda functions. | This solution uses the following Lambda functions to manage hotfix workflows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html)<br />To enable the Lambda functions to provision and terminate Service Catalog products when `hotfix `branches are created or deleted through the associated EventBridge rule, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html) | AWS DevOps |

### Create pipeline for main branch and deploy application in workload accounts
<a name="create-pipeline-for-main-branch-and-deploy-application-in-workload-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up pipeline for `main` branch. | To set up the pipeline for the main branch, run the following command in the tools account. Replace the parameters for `MainProductId` and `MainProductArtifactId` with values from `servicecatalogsetup` stack outputs.<pre>#InToolsAccount<br />aws servicecatalog provision-product \<br />    --product-id <MainProductId> \<br />    --provisioning-artifact-id <MainProductArtifactId> \<br />    --provisioned-product-name "${ApplicationName}-main-pipeline" \<br />    --provisioning-parameters Key=CodeCommitRepoName,Value="${ApplicationName}-repository" Key=ECRRepository,Value="${ApplicationName}-app" \<br />    --region=${DepRegion}</pre> | AWS DevOps |
| Deploy application using the `main` branch. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html) | AWS DevOps |

### Create the pipeline for a hotfix-\* branch and deploy the hotfix
<a name="create-the-pipeline-for-a-hotfix--branch-and-deploy-the-hotfix"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a `hotfix-*` branch and commit changes. | To create a pipeline for the `hotfix-*` branch and deploy the hotfix to the workload accounts, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html) | AWS DevOps |
| Delete the `hotfix-check1` branch. | To delete the `hotfix-check1` branch created earlier, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html) | AWS DevOps |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up the deployed resources. | To clean up the resources that were deployed earlier, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-dynamic-pipeline-management-for-deploying-hotfix-solutions.html)<pre>##In Tools Account##<br />aws cloudformation delete-stack --stack-name servicecatalogsetup --region ${DepRegion}<br />aws cloudformation delete-stack --stack-name prlambdasetup --region ${DepRegion}<br />aws cloudformation delete-stack --stack-name prereqs --region ${DepRegion}</pre><pre>##In Workload Accounts##<br />aws cloudformation delete-stack --stack-name inframainstack --region ${DepRegion}</pre><br />For more information, see [Deleting provisioned products](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-delete.html) in the Service Catalog documentation. | AWS DevOps |

## Troubleshooting
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Changes that you committed to the CodeCommit repository aren’t getting deployed. | Check the CodeBuild logs for errors in the Docker build action. For more information, see the [CodeBuild documentation](https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting.html). |
| The Service Catalog product isn't being provisioned. | Review the related CloudFormation stacks for failed events. For more information, see the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html). |

## Related resources
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-resources"></a>
+ [Basic Git commands](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-basic-git.html)
+ [Configure an IAM policy to limit pushes and merges to a branch](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-conditional-branch.html#how-to-conditional-branch-create-policy)
+ [Connect to an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-connect.html)
+ [Granting access to users](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html)
+ [Pushing a Docker image to an Amazon ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)
+ [Troubleshooting AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting.html)
+ [What is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)

## Additional information
<a name="automate-dynamic-pipeline-management-for-deploying-hotfix-solutions-additional"></a>

This pattern is designed for environments with a Gitflow setup that is adopted for the development workflow in the CI/CD process. The pipelines follow the deployment cycle that starts from development and moves through quality assurance (QA), stage, and production environments. The CI/CD setup includes two git branches with promotional deployments to environments as follows:
+ The `develop` branch deploys to the development environment.
+ The `main` branch deploys to the QA, stage, and production environments.

In this setup, it’s a challenge to apply a hotfix or a security patch faster than the usual deployment cycle while the active development of new features is ongoing. A dedicated process is necessary to address hotfix or security requests, ensuring that live environments remain properly functioning and secure.

However, you can use other available options without requiring a dedicated deployment process if:
+ The CI/CD process is well-equipped with automated testing, such as functional and end-to-end tests, which eliminate the need for manual testing and prevent delays in deployments to production. However, if automated testing isn’t well integrated into the CI/CD process, pushing a small fix to the production environment can become complex and cumbersome for developers. This is because there might be new features waiting in the QA environment for approval and sign-off. A hotfix or security fix can’t be pushed into production in a straightforward manner simultaneously.
+ Development teams continuously deploy new features into the production environment, integrating hotfixes or security patches into the scheduled deployment of each new feature. In other words, the next feature update to the production environment comprises two components: The addition of a new feature and the inclusion of the hotfix or security patch. However, if the deployment cycle isn’t continuous, there can be multiple new features already awaiting approval in the QA environment. Managing different versions and ensuring the correct changes are reapplied can then become complex and error-prone.

**Note**
If you’re using [version 2](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types.html#:~:text=V2%20type%20pipelines%20have%20the%20same%20structure) of AWS CodePipeline with proper triggers set up on the `hotfix` branch, you still require a dedicated process to address unscheduled requests. In version 2, you can set up triggers for either push or pull requests. The execution will either be queued or executed immediately, depending on the previous state of the pipeline. However, with a dedicated pipeline, the fixes are applied immediately to the production environment, ensuring that urgent issues are resolved without delay.
