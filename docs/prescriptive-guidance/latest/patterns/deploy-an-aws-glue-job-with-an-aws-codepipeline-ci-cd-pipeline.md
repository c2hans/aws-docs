---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline.html
---

# Deploy an AWS Glue job with an AWS CodePipeline CI/CD pipeline
<a name="deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline"></a>

*Bruno Klein and Luis Henrique Massao Yamada, Amazon Web Services*

## Summary
<a name="deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline-summary"></a>

This pattern demonstrates how you can integrate AWS CodeCommit and AWS CodePipeline with AWS Glue, and use AWS Lambda to launch jobs as soon as a developer pushes their changes to a remote AWS CodeCommit repository.

When a developer submits a change to an extract, transform, and load (ETL) repository and pushes the changes to AWS CodeCommit, a new pipeline is invoked. The pipeline initiates a Lambda function that launches an AWS Glue job with these changes. The AWS Glue job performs the ETL task.

This solution is helpful in the situation where businesses, developers, and data engineers want to launch jobs as soon as changes are committed and pushed to the target repositories. It helps achieve a higher level of automation and reproducibility, therefore avoiding errors during the job launch and lifecycle.

## Prerequisites and limitations
<a name="deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ [Git](https://git-scm.com/) installed on the local machine
+ [Amazon Cloud Development Kit (Amazon CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) installed on the local machine
+ [Python](https://www.python.org/) installed on the local machine
+ The code in the *Attachments *section

**Limitations**
+ The pipeline is finished as soon as the AWS Glue job is successfully launched. It does not wait for the conclusion of the job.
+ The code provided in the attachment is intended for demo purposes only.

## Architecture
<a name="deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline-architecture"></a>

**Target technology stack  **
+ AWS Glue
+ AWS Lambda
+ AWS CodePipeline
+ AWS CodeCommit

**Target architecture **

![Using Lambda to launch a Glue job as soon as a developer pushes changes to a CodeCommit repo.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/99a67388-5939-4267-8324-b6ca8bfa7962/images/917c9041-b94d-4e95-a3c4-9a1115ead228.png)

The process consists of these steps:

1. The developer or data engineer makes a modification in the ETL code, commits, and pushes the change to AWS CodeCommit.

1. The push initiates the pipeline.

1. The pipeline initiates a Lambda function, which calls `codecommit:GetFile` on the repository and uploads the file to Amazon Simple Storage Service (Amazon S3).

1. The Lambda function launches a new AWS Glue job with the ETL code.

1. The Lambda function finishes the pipeline.

**Automation and scale**

The sample attachment demonstrates how you can integrate AWS Glue with AWS CodePipeline. It provides a baseline example that you can customize or extend for your own use. For details, see the *Epics *section.

## Tools
<a name="deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline-tools"></a>
+ [AWS CodePipeline](https://aws.amazon.com/codepipeline/) – AWS CodePipeline is a fully managed [continuous delivery](https://aws.amazon.com/devops/continuous-delivery/) service that helps you automate your release pipelines for fast and reliable application and infrastructure updates.
+ [AWS CodeCommit](https://aws.amazon.com/codecommit/) – AWS CodeCommit is a fully managed [source control](https://aws.amazon.com/devops/source-control/) service that hosts secure, Git-based repositories.
+ [AWS Lambda](https://aws.amazon.com/lambda/) – AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers.
+ [AWS Glue](https://aws.amazon.com/glue) – AWS Glue is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
+ [Git client](https://git-scm.com/downloads) – Git provides GUI tools, or you can use the command line or a desktop tool to check out the required artifacts from GitHub.
+ [AWS CDK](https://aws.amazon.com/cdk/) – The AWS CDK is an open source software development framework that helps you define your cloud application resources by using familiar programming languages.

## Epics
<a name="deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline-epics"></a>

### Deploy the sample code
<a name="deploy-the-sample-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the AWS CLI. | Configure the AWS Command Line Interface (AWS CLI) to target and authenticate with your current AWS account. For instructions, see the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html). | Developer, DevOps engineer |
| Extract the sample project files. | Extract the files from the attachment to create a folder that contains the sample project files. | Developer, DevOps engineer |
| Deploy the sample code. | After you extract the files, run the following commands from the extract location to create a baseline example:<pre>cdk bootstrap<br />cdk deploy<br />git init<br />git remote add origin <code-commit-repository-url><br />git stage .<br />git commit -m "adds sample code"<br />git push --set-upstream origin main</pre><br />After the last command, you can monitor the status of the pipeline and the AWS Glue job. | Developer, DevOps engineer |
| Customize the code. | Customize the code for the etl.py file in accordance with your business requirements. You can revise the ETL code, modify the pipeline stages, or extend the solution. | Data engineer |

## Related resources
<a name="deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline-resources"></a>
+ [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
+ [Adding jobs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-job.html)
+ [Source action integrations in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations-action-type.html#integrations-source)
+ [Invoke an AWS Lambda function in a pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html)
+ [AWS Glue programming](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming.html)
+ [AWS CodeCommit GetFile API](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetFile.html)

## Attachments
<a name="attachments-99a67388-5939-4267-8324-b6ca8bfa7962"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/99a67388-5939-4267-8324-b6ca8bfa7962/attachments/attachment.zip)
