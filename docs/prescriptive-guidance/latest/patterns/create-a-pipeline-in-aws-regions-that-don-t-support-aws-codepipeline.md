---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline.html
---

# Create a pipeline in AWS Regions that don’t support AWS CodePipeline
<a name="create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline"></a>

*Anand Krishna Varanasi, Amazon Web Services*

## Summary
<a name="create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline-summary"></a>

AWS CodePipeline is a continuous delivery (CD) orchestration service that’s part of a set of DevOps tools from Amazon Web Services (AWS). It integrates with a large variety of sources (such as version control systems and storage solutions), continuous integration (CI) products and services from AWS and AWS Partners, and open-source products to provide an end-to-end workflow service for fast application and infrastructure deployments.

However, CodePipeline isn’t supported in all AWS Regions, and it’s useful to have an invisible orchestrator that connects AWS CI/CD services. This pattern describes how to implement an end-to-end workflow pipeline in AWS Regions where CodePipeline isn’t yet supported by using AWS CI/CD services such as AWS CodeCommit, AWS CodeBuild, and AWS CodeDeploy.

## Prerequisites and limitations
<a name="create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ AWS Cloud Development Kit (AWS CDK) CLI version 2.28 or later

## Architecture
<a name="create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline-architecture"></a>

The following diagram shows a pipeline that was created in a Region that doesn’t support CodePipeline, such as the Africa (Cape Town) Region. A developer pushes the CodeDeploy configuration files (also called *deployment lifecycle hook scripts*) to the Git repository that’s hosted by CodeCommit. (See the [GitHub repository](https://github.com/aws-samples/invisible-codepipeline-unsupported-regions) provided with this pattern.) An Amazon EventBridge rule automatically initiates CodeBuild.

The CodeDeploy configuration files are fetched from CodeCommit as part of the source stage of the pipeline and transferred to CodeBuild.

In the next phase, CodeBuild performs these tasks:

1. Downloads the application source code TAR file. You can configure the name of this file by using Parameter Store, a capability of AWS Systems Manager.

1. Downloads the CodeDeploy configuration files.

1. Creates a combined archive of application source code and CodeDeploy configuration files that are specific to the application type.

1. Initiates CodeDeploy deployment to an Amazon Elastic Compute Cloud (Amazon EC2) instance by using the combined archive.

![Pipeline creation in unsupported AWS Region](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e27750de-b597-424e-b5bf-4d58dc9b60cc/images/95fc815e-a762-4142-b0fd-2a716823e498.png)

## Tools
<a name="create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline-tools"></a>

**AWS services**
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) automates deployments to Amazon EC2 or on-premises instances, AWS Lambda functions, or Amazon Elastic Container Service (Amazon ECS) services.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.

**Code**

The code for this pattern is available in the GitHub [CodePipeline Unsupported Regions](https://github.com/aws-samples/invisible-codepipeline-unsupported-regions) repository.

## Epics
<a name="create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline-epics"></a>

### Set up your developer workstation
<a name="set-up-your-developer-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the AWS CDK CLI. | For instructions, see the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_prerequisites). | AWS DevOps |
| Install a Git client. | To create commits, you can use a Git client installed on your local computer, and then push your commits to the CodeCommit repository. To set up CodeCommit with your Git client, see the [CodeCommit documentation](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-commit.html). | AWS DevOps |
| Install npm. | Install the **npm **package manager. For more information, see the [npm documentation](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). | AWS DevOps |

### Set up the pipeline
<a name="set-up-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the code repository. | Clone the GitHub [CodePipeline Unsupported Regions](https://github.com/aws-samples/invisible-codepipeline-unsupported-regions) repository to your local machine by running the following command.<pre>git clone https://github.com/aws-samples/invisible-codepipeline-unsupported-regions</pre> | DevOps engineer |
| Set parameters in cdk.json. | Open the `cdk.json` file and provide values for the following parameters:<pre>"pipeline_account":"XXXXXXXXXXXX",<br />"pipeline_region":"us-west-2",<br />"repo_name": "app-dev-repo",<br />"ec2_tag_key": "test-vm",<br />"configName" : "cbdeployconfig",<br />"deploymentGroupName": "cbdeploygroup",<br />"applicationName" : "cbdeployapplication",<br />"projectName" : "CodeBuildProject"</pre><br />where:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline.html) | AWS DevOps |
| Set up the AWS CDK construct library. | In the cloned GitHub repository, use the following commands to install the AWS CDK construct library, build your application, and synthesize to generate the AWS CloudFormation template for the application.<pre>npm i aws-cdk-lib<br />npm run build<br />cdk synth</pre> | AWS DevOps |
| Deploy the sample AWS CDK application. | Deploy the code by running the following command in an unsupported Region (such as `af-south-1`).<pre>cdk deploy</pre> | AWS DevOps |

### Set up the CodeCommit repository for CodeDeploy
<a name="set-up-the-acc-repository-for-acd"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up CI/CD for the application. | Clone the CodeCommit repository that you specified in the `cdk.json` file (this is called `app-dev-repo` by default) to set up the CI/CD pipeline for the application.<pre>git clone https://git-codecommit.us-west-2.amazonaws.com/v1/repos/app-dev-repo</pre><br />where the repository name and Region depend on the values you provided in the `cdk.json` file. | AWS DevOps |

### Test the pipeline
<a name="test-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the pipeline with deployment instructions. | The `CodeDeploy_Files` folder of the GitHub [CodePipeline Unsupported Regions](https://github.com/aws-samples/invisible-codepipeline-unsupported-regions) repository includes sample files that instruct CodeDeploy to deploy the application. The `appspec.yml` file is a CodeDeploy configuration file that contains hooks to control the flow of application deployment. You can use the sample files `index.html`, `start_server.sh`, `stop_server.sh`, and `install_dependencies.sh` to update a website that’s hosted on Apache. These are examples—you can use the code in the GitHub repository to deploy any type of application. When the files are pushed to the CodeCommit repository, the invisible pipeline is initiated automatically. For deployment results, check the results of individual phases in the CodeBuild and CodeDeploy consoles. | AWS DevOps |

## Related resources
<a name="create-a-pipeline-in-aws-regions-that-don-t-support-aws-codepipeline-resources"></a>
+ [Getting started](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_prerequisites) (AWS CDK documentation)
+ [Introduction to the AWS Cloud Development Kit (AWS CDK)](https://catalog.us-east-1.prod.workshops.aws/workshops/5962a836-b214-4fbf-9462-fedba7edcc9b/en-US) (AWS Workshop Studio)
+ [AWS CDK Workshop](https://cdkworkshop.com/)
