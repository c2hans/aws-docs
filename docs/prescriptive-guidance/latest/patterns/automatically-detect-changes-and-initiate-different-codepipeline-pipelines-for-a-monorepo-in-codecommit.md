---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit.html
---

# Automatically detect changes and initiate different CodePipeline pipelines for a monorepo in CodeCommit
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit"></a>

*Helton Ribeiro, Petrus Batalha, and Ricardo Morais, Amazon Web Services*

## Summary
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit-summary"></a>

**Notice**: AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

This pattern helps you automatically detect changes to the source code of a monorepo-based application in AWS CodeCommit and then initiate a pipeline in AWS CodePipeline that runs the continuous integration and continuous delivery (CI/CD) automation for each microservice. This approach means that each microservice in your monorepo-based application can have a dedicated CI/CD pipeline, which ensures better visibility, easier sharing of code, and improved collaboration, standardization, and discoverability.

The solution described in this pattern doesn't perform any dependency analysis among the microservices inside the monorepo. It only detects changes in the source code and initiates the matching CI/CD pipeline.

The pattern uses AWS Cloud9 as the integrated development environment (IDE) and AWS Cloud Development Kit (AWS CDK) to define an infrastructure by using two CloudFormation stacks: `MonoRepoStack` and `PipelinesStack`. The `MonoRepoStack` stack creates the monorepo in AWS CodeCommit and the AWS Lambda function that initiates the CI/CD pipelines. The `PipelinesStack` stack defines your pipeline infrastructure.

**Important**
This pattern’s workflow is a proof of concept (PoC). We recommend that you use it only in a test environment. If you want to use this pattern’s approach in a production environment, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the AWS Identity and Access Management (IAM) documentation and make the required changes to your IAM roles and AWS services.

## Prerequisites and limitations
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI), installed and configured. For more information, see [Installing, updating, and uninstalling the AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)in the AWS CLI documentation.
+ Python 3 and `pip`, installed on your local machine. For more information, see the [Python documentation](https://www.python.org/).
+ AWS CDK, installed and configured. For more information, see [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) in the AWS CDK documentation.
+ An AWS Cloud9 IDE, installed and configured. For more information, see [Setting up AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/setting-up.html) in the AWS Cloud9 documentation.
+ The GitHub [AWS CodeCommit monorepo multi-pipeline triggers](https://github.com/aws-samples/monorepo-multi-pipeline-trigger) repository, cloned on your local machine.
+ An existing directory containing application code that you want to build and deploy with CodePipeline.
+ Familiarity and experience with DevOps best practices on the AWS Cloud. To increase your familiarity with DevOps, you can use the pattern [Build a loosely coupled architecture with microservices using DevOps practices and AWS Cloud9](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-loosely-coupled-architecture-with-microservices-using-devops-practices-and-aws-cloud9.html) on the AWS Prescriptive Guidance website.

## Architecture
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit-architecture"></a>

The following diagram shows how to use the AWS CDK to define an infrastructure with two AWS CloudFormation stacks: `MonoRepoStack` and `PipelinesStack`.

![Workflow to use the AWS CDK to define an infrastructure with two CloudFormation stacks.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a3397158-a208-4033-844e-969af13ae8b6/images/b0bb1094-b598-4b3d-ab8b-ad9b0eb45f38.png)

The diagram shows the following workflow:

1. The bootstrap process uses the AWS CDK to create the AWS CloudFormation stacks `MonoRepoStack` and `PipelinesStack`.

1. The `MonoRepoStack` stack creates the CodeCommit repository for your application and the `monorepo-event-handler` Lambda function that is initiated after each commit.

1. The `PipelinesStack` stack creates the pipelines in CodePipeline that are initiated by the Lambda function. Each microservice must have a defined infrastructure pipeline.

1. The pipeline for `microservice-n` is initiated by the Lambda function and starts its isolated CI/CD stages that are based on the source code in CodeCommit.

1. The pipeline for `microservice-1` is initiated by the Lambda function and starts its isolated CI/CD stages that are based on the source code in CodeCommit.

The following diagram shows the deployment of the AWS CloudFormation stacks `MonoRepoStack` and `PipelinesStack` in an account.

![Deployment of the CloudFormation stacks MonoRepoStack and PipelinesStack in an AWS account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a3397158-a208-4033-844e-969af13ae8b6/images/39e60e49-dea2-486d-8a2c-6cae438f69b4.png)

1. A user changes code in one of the application’s microservices.

1. The user pushes the changes from a local repository to a CodeCommit repository.

1. The push activity initiates the Lambda function that receives all pushes to the CodeCommit repository.

1. The Lambda function reads a parameter in Parameter Store, a capability of AWS Systems Manager, to retrieve the most recent commit ID. The parameter has the naming format: `/MonoRepoTrigger/{repository}/{branch_name}/LastCommit`. If the parameter isn’t found, the Lambda function reads the last commit ID from the CodeCommit repository and saves the returned value in Parameter Store.

1. After identifying the commit ID and the changed files, the Lambda function identifies the pipelines for each microservice directory and initiates the required CodePipeline pipeline.

## Tools
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit-tools"></a>
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework for defining cloud infrastructure in code and provisioning it through CloudFormation.
+ [Python ](https://www.python.org/)is a programming language that lets you work quickly and integrate systems more effectively.

**Code **

The source code and templates for this pattern are available in the GitHub [AWS CodeCommit monorepo multi-pipeline triggers](https://github.com/aws-samples/monorepo-multi-pipeline-trigger) repository.

## Best practices
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit-best-practices"></a>
+ This sample architecture doesn't include a monitoring solution for the deployed infrastructure. If you want to deploy this solution in a production environment, we recommend that you enable monitoring. For more information, see [Monitor your serverless applications with CloudWatch Application Insights](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/monitor-app-insights.html) in the AWS Serverless Application Model (AWS SAM) documentation.
+ When you edit the sample code provided by this pattern, follow the [best practices for developing and deploying cloud infrastructure](https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html) in the AWS CDK documentation.
+ When you define your microservice pipelines, review the [security best practices](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-best-practices.html) in the AWS CodePipeline documentation.
+ You can also check your AWS CDK code for best practices by using the [cdk-nag](https://github.com/cdklabs/cdk-nag) utility. This tool uses a set of rules, grouped by packs, to evaluate your code. The available packs are:
  + [AWS Solutions Library](https://github.com/cdklabs/cdk-nag/blob/main/RULES.md#awssolutions)
  + [Health Insurance Portability and Accountability Act (HIPAA) security](https://github.com/cdklabs/cdk-nag/blob/main/RULES.md#hipaa-security)
  + [National Institute of Standards and Technology (NIST) 800-53 rev 4](https://github.com/cdklabs/cdk-nag/blob/main/RULES.md#nist-800-53-rev-4)
  + [NIST 800-53 rev 5](https://github.com/cdklabs/cdk-nag/blob/main/RULES.md#nist-800-53-rev-5)
  + [Payment Card Industry Data Security Standard (PCI DSS) 3.2.1](https://github.com/cdklabs/cdk-nag/blob/main/RULES.md#pci-dss-321)

## Epics
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual Python envionment. | In your AWS Cloud9 IDE, create a virtual Python environment and install the required dependencies by running the following command:<br />`make install` | Developer |
| Bootstrap the AWS account and AWS Region for the AWS CDK. | Bootstrap the required AWS account and Region by running the following command:<br />`make bootstrap account-id=<your-AWS-account-ID> region=<required-region>` | Developer |

### Add a new pipeline for a microservice
<a name="add-a-new-pipeline-for-a-microservice"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Add your sample code to your application directory. | Add the directory that contains your sample application code to the `monorepo-sample` directory in the cloned GitHub [AWS CodeCommit monorepo multi-pipeline triggers](https://github.com/aws-samples/monorepo-multi-pipeline-trigger) repository. | Developer |
| Edit the `monorepo-main.json` file. | Add the directory name of your application’s code and the pipeline's name to the `monorepo-main.json` file in the cloned repository . | Developer |
| Create the pipeline. | In the `Pipelines` directory for the repository, add the pipeline `class` for your application. The directory contains two sample files, `pipeline_hotsite.py` and `pipeline_demo.py`. Each file has three stages: source, build, and deploy.<br />You can copy one of the files and makes changes to it according to your application’s requirements.  | Developer |
| Edit the `monorepo_config.py` file. | In `service_map`, add the directory name for your application and the class that you created for the pipeline.<br />For example, the following code shows a pipeline definition in the `Pipelines` directory that uses a file named `pipeline_mysample.py`  with a `MySamplePipeline` class:<pre>...<br /># Pipeline definition imports<br />from pipelines.pipeline_demo import DemoPipeline<br />from pipelines.pipeline_hotsite import HotsitePipeline<br />from pipelines.pipeline_mysample import MySamplePipeline<br /><br />### Add your pipeline configuration here<br />service_map: Dict[str, ServicePipeline]  = {<br />    # folder-name -> pipeline-class<br />    'demo': DemoPipeline(),<br />    'hotsite': HotsitePipeline(),<br />    'mysample': MySamplePipeline()<br />}</pre> | Developer |

### Deploy the MonoRepoStack stack
<a name="deploy-the-monorepostack-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the AWS CloudFormation stack. | Deploy the AWS CloudFormation `MonoRepoStack` stack with default parameter values in the root directory of the cloned repository by running the `make deploy-core` command.<br />You can change the repository’s name by running the `make deploy-core monorepo-name=<repo_name>` command.You can simultaneously deploy both pipelines by using the `make deploy monorepo-name=<repo_name>` command. | Developer |
| Validate the CodeCommit repository. | Validate that your resources were created by running the `aws codecommit get-repository --repository-name <repo_name>` command. Because the CloudFormation stack creates the CodeCommit repository where the monorepo is stored, don’t run the `cdk destroy MonoRepoStack `command if you have started to push modifications into it. | Developer |
| Validate the CloudFormation stack results. | Validate that the CloudFormation `MonoRepoStack` stack is correctly created and configured by running the following command:<pre>aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --query 'StackSummaries[?StackName == 'MonoRepoStack']'</pre> | Developer |

### Deploy the PipelinesStack stack
<a name="deploy-the-pipelinesstack-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation stack. | The AWS CloudFormation `PipelinesStack` stack must be deployed after you deploy the `MonoRepoStack` stack. The stack increases in size when new microservices are added to the monorepo’s code base and is redeployed when a new microservice is onboarded.<br />Deploy the PipelinesStack stack by running the `make deploy-pipelines` command.You can also deploy simultaneously deploy both pipelines by running the `make deploy monorepo-name=<repo_name>` command.<br />The following sample output shows how the `PipelinesStacks` deployment prints the URLs for the microservices at the end of the implementation:<pre>Outputs:<br />PipelinesStack.demourl = .cloudfront.net<br />PipelinesStack.hotsiteurl = .cloudfront.net</pre> | Developer |
| Validate the AWS CloudFormation stack results. | Validate that the AWS CloudFormation `PipelinesStacks` stack is correctly created and configured by running the following command:<pre>aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --query 'StackSummaries[?StackName == 'PipelinesStack']'</pre> | Developer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete your AWS CloudFormation stacks. | Run the `make destroy` command. | Developer |
| Delete the S3 buckets for your pipelines. | 1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and open the [Amazon Simple Storage Service (Amazon S3) console](https://console.aws.amazon.com/s3/).<br />2. Delete the S3 buckets that are associated with your pipelines and use the following name: `pipelinesstack-codepipeline*` | Developer |

## Troubleshooting
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| I encountered AWS CDK issues. | See [Troubleshooting common AWS CDK issues](https://docs.aws.amazon.com/cdk/v2/guide/troubleshooting.html) in the AWS CDK documentation. |
| I pushed my microservice code, but the microservice pipeline didn't run. | **Setup validation**<br />*Verify branch configuration:*+ Make sure that you are pushing your code to the correct branch. This pipeline is configured to run only when changes are made to the `main` branch. Pushes to other branches don’t initiate the pipeline unless they are configured specifically.<br />+ After you push your code, check if the commit is visible in AWS CodeCommit to make sure that the push was successful and that the connection between your local environment and the repository is intact. Refresh your credentials if there are issues pushing code.<br />*Validate configuration files:*+ Confirm that the `service_map` variable in `monorepo_config.py` accurately reflects the current directory structure of your microservices. This variable plays a crucial role in mapping your code push to the respective pipeline.<br />+ Make sure that `monorepo-main.json` is updated to include the new mapping for your microservice. This file is essential for the pipeline to recognize and correctly handle changes to your microservice.<br />**Troubleshooting on the console**<br />*AWS CodePipeline checks:*+ On the [AWS Management Console](https://console.aws.amazon.com/), confirm that you're in the AWS Region where your pipeline is hosted. Open the [CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home) and check if the pipeline that corresponds to your microservice has been initiated.<br />**Error analysis**: If the pipeline was initiated but failed, review any error messages or logs provided by CodePipeline to understand what went wrong.<br />*AWS Lambda troubleshooting:*+ On the [AWS Lambda console](https://console.aws.amazon.com/lambda/home), open the `monorepo-event-handler` Lambda function. Verify that the function was initiated in response to the code push.<br />**Log analysis**: Examine the Lambda function's logs for any issues. The logs can provide detailed insights into what happened when the function ran and help identify whether the function processed the event as expected. |
| I need to redeploy all my microservices.  | There are two approaches to force the redeployment of all microservices. Choose the option that fits your requirements.<br />**Approach 1: Delete a parameter in Parameter Store**<br />This method involves deleting a specific parameter within Systems Manager Parameter Store that tracks the last commit ID used for deployment. When you remove this parameter, the system is forced to redeploy all microservices upon the next trigger, because it perceives it as a fresh state.<br />Steps:1. Locate the specific Parameter Store entry that holds the commit ID or a related deployment marker for your monorepo. The parameter name follows the format: `"/MonoRepoTrigger/{repository}/{branch_name}/LastCommit"`<br />2. Consider backing up the parameter value if it's critical or if you wish to maintain a record of the deployment state before resetting it.<br />3. Use the AWS Management Console, AWS CLI, or SDKs to delete the identified parameter. This action resets the deployment marker.<br />4. After deletion, the next push to the repository should cause the system to deploy all microservices, because it looks for the latest commit to consider for deployment.<br />Pros:+ Simple and quick to implement with minimal steps.<br />+ Doesn’t require making arbitrary code changes to initiate deployments.<br />Cons:+ Less granular control over the deployment process.<br />+ Potentially risky if the Parameter Store is used for managing other critical configurations.<br />**Approach 2: Push a commit in each monorepo subfolder**<br />This method involves making a minor change and pushing it in each microservice subfolder within the monorepo to initiate their individual pipelines.<br />Steps:1. List all the microservices within the monorepo that need redeployment.<br />2. For each microservice, make a minimal, non-impactful change in its subfolder. This might be updating a `README` file, adding a comment in a configuration file, or any change that doesn’t affect the service's functionality.<br />3. Commit these changes with a clear message (such as "Initiate redeployment of microservices") and push them to the repository. Make sure that you push the changes to the branch that initiates the deployment.<br />4. Monitor the pipelines for each microservice to confirm that they are initiated and complete successfully.<br />Pros:+ Provides granular control over which microservices are redeployed.<br />+ Safer because it doesn’t involve deleting configuration parameters that might be used for other purposes.<br />Cons:+ More time-consuming, especially with a large number of microservices.<br />+ Requires making unnecessary code changes that could clutter the commit history. |

## Related resources
<a name="automatically-detect-changes-and-initiate-different-codepipeline-pipelines-for-a-monorepo-in-codecommit-resources"></a>
+ [Continuous integration and delivery (CI/CD) using CDK Pipelines](https://docs.aws.amazon.com/cdk/latest/guide/cdk_pipeline.html) (AWS CDK documentation)
+ [aws-cdk/pipelines module](https://docs.aws.amazon.com/cdk/api/latest/docs/pipelines-readme.html) (AWS CDK API reference)
