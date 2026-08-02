---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-codeguru-reviews-for-aws-cdk-python-applications.html
---

# Automate Amazon CodeGuru reviews for AWS CDK Python applications by using GitHub Actions
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications"></a>

*Vanitha Dontireddy and Sarat Chandra Pothula, Amazon Web Services*

## Summary
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications-summary"></a>

Note: As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html) in the CodeGuru Reviewer documentation.

This pattern showcases the integration of Amazon CodeGuru automated code reviews for AWS Cloud Development Kit (AWS CDK) Python applications, orchestrated through GitHub Actions. The solution deploys a serverless architecture defined in AWS CDK Python. By automating expert code analysis within the development pipeline, this approach can do the following for AWS CDK Python projects:
+ Enhance code quality.
+ Streamline workflows.
+ Maximize the benefits of serverless computing.

## Prerequisites and limitations
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI) version 2.9.11 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
+ An active GitHub account and a GitHub repository with read and write workflow permissions and creation of pull requests (PR) by GitHub Actions to ensure the PR workflow operates correctly.
+ An OpenID Connect (OIDC) role in GitHub Actions to deploy the solution in the AWS account. To create the role, use the [AWS CDK construct](https://github.com/aws-samples/github-actions-oidc-cdk-construct).

**Limitations**
+ Amazon CodeGuru Profiler [supports applications](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html#what-is-language-support) written in all Java virtual machine (JVM) languages (such as Scala and Kotlin) and runtimes and Python 3.6 or later.
+ Amazon CodeGuru Reviewer [supports associations](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-repositories.html) with Java and Python code repositories only from the following source providers: AWS CodeCommit, Bitbucket, GitHub, GitHub Enterprise Cloud, and GitHub Enterprise Server. In addition, Amazon Simple Storage Service (Amazon S3) repositories are only supported through GitHub Actions.
+ There isn’t an automated way to print the findings during the continuous integration and continuous deployment (CI/CD) pipeline. Instead, this pattern uses GitHub Actions as an alternative method to handle and display the findings.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications-architecture"></a>

The following diagram shows the architecture for this solution.

![Workflow to integrate CodeGuru code review for AWS CDK Python applications using GitHub Actions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c5395e3e-ff2a-41cf-bd64-c73cc928b60b/images/18f880a2-9bc3-4d71-a598-bb83b68ee383.png)

As shown in the diagram, when a developer creates a pull request (PR) for review, GitHub Actions triggers the following steps:

1. IAM role assumption – The pipeline uses the IAM role that’s specified in GitHub Secrets to perform deployment tasks.

1. Code analysis
   + CodeGuru Reviewer analyzes the code stored in the Amazon S3 bucket. It identifies defects and provides recommendations for fixes and optimizations.
   + CodeGuru Security scans for policy violations and vulnerabilities.

1. Findings review
   + The pipeline prints a link to the findings dashboard in the console output.
   + If critical findings are detected, the pipeline fails immediately.
   + For high, normal, or low severity findings, the pipeline continues to the next step.

1. PR approval
   + A reviewer must manually approve the PR.
   + If the PR is denied, the pipeline fails and halts further deployment steps.

1. CDK deployment – Upon PR approval, the CDK deployment process begins. It sets up the following AWS services and resources:
   + CodeGuru Profiler
   + AWS Lambda function
   + Amazon Simple Queue Service (Amazon SQS) queue

1. Profiling data generation – To generate sufficient profiling data for CodeGuru Profiler:
   + The pipeline invokes the Lambda function multiple times by sending messages to the Amazon SQS queue periodically.

## Tools
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) is a command line cloud development kit that helps you interact with your AWS CDK app.
+ [Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html) collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance.
+ [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html) uses program analysis and machine learning to detect potential defects that are difficult for developers to find. Then, CodeGuru Profiler offers suggestions for improving your Java and Python code.
+ Amazon CodeGuru Security is a static application security tool that uses machine learning to detect security policy violations and vulnerabilities. It provides suggestions for addressing security risks and generates metrics so you can track the security posture of your applications.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart) is a continuous integration and continuous delivery (CI/CD) platform that’s tightly integrated with GitHub repositories. You can use GitHub Actions to automate your build, test, and deployment pipeline.

**Code repository**

The code for this pattern is available in the GitHub [amazon-codeguru-suite-cdk-python](https://github.com/aws-samples/amazon-codeguru-suite-cdk-python) repository.

## Best practices
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications-best-practices"></a>
+ Adhere to the [Best practices for developing and deploying cloud infrastructure with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html).
+ Follow [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) when using AWS services in GitHub Actions workflows, including:
  + Do not store credentials in your repository code.
  + [Assume an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles) to receive temporary credentials, and use temporary credentials when possible.
  + [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) to the IAM role used in GitHub Actions workflows. Grant only the permissions that are required to perform the actions in your GitHub Actions workflows.
  + [Monitor the activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#remove-credentials) of the IAM role that’s used in GitHub Actions workflows.
  + Periodically rotate any long-term credentials that you use.

## Epics
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up AWS credentials. | To export the variables that define the AWS account and AWS Region where you’re deploying the stack, run the following commands:<pre>export CDK_DEFAULT_ACCOUNT=<12-digit AWS account number></pre><pre>export CDK_DEFAULT_REGION=<AWS Region></pre><br />The AWS credentials for the AWS CDK are provided through environment variables. | AWS DevOps, DevOps engineer |
| Clone the repository. | To clone the repository on your local machine, run the following command:<pre>git clone https://github.com/aws-samples/amazon-codeguru-suite-cdk-python.git</pre> | AWS DevOps, DevOps engineer |
| Install the CDK Toolkit. | To confirm that the CDK Toolkit is installed and to check the version, run the following command: <pre>cdk --version</pre><br />If the CDK Toolkit version is earlier than 2.27.0, enter the following command to update it to version 2.27.0:<pre>npm install -g aws-cdk@2.27.0</pre><br />If the CDK Toolkit is *not* installed, run the following command to install it:<pre>npm install -g aws-cdk@2.27.0 --force</pre> | AWS DevOps, DevOps engineer |
| Install the required dependencies. | To install the required project dependencies, run the following command:<pre>python -m pip install --upgrade pip<br />pip install -r requirements.txt</pre> | AWS DevOps, DevOps engineer |
| Bootstrap the CDK environment. | To [bootstrap](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) an AWS CDK environment, run the following commands:<pre>npm install<br />npm run cdk bootstrap "aws://${ACCOUNT_NUMBER}/${AWS_REGION}"</pre><br />After you successfully bootstrap the environment, the following output should be displayed:<pre>⏳  Bootstrapping environment aws://{account}/{region}...<br />✅  Environment aws://{account}/{region} bootstrapped</pre> | AWS DevOps, DevOps engineer |

### Deploy the CDK app
<a name="deploy-the-cdk-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Synthesize the AWS CDK app. | To synthesize an AWS CDK app, run the following command:<pre>cdk synth</pre><br />For more information about this command, see [cdk synthesize](https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-synth.html) in the AWS CDK documentation. | AWS DevOps, DevOps engineer |
| Deploy the resources. | To deploy the resources, run the following command:<pre>cdk deploy --require-approval never</pre>The `--require-approval never` flag means that the CDK will approve and execute all changes automatically. This includes changes that the CDK would normally flag as needing manual review (such as IAM policy changes or removal of resources). Make sure that your CDK code and CI/CD pipeline are well-tested and secure before you use the `--require-approval never` flag in production environments. | AWS DevOps, DevOps engineer |

### Create GitHub secrets and personal access token
<a name="create-github-secrets-and-personal-access-token"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the required secrets in GitHub. | To allow GitHub Actions workflows to access AWS resources securely without exposing sensitive information in your repository's code, create secrets. To create the secrets in GitHub for `ROLE_TO_ASSUME`, `CodeGuruReviewArtifactBucketName`, and `AWS_ACCOUNT_ID`, follow the instructions in [Creating secrets for a repository](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) in the GitHub Actions documentation.<br />Following is more information about the variables:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-codeguru-reviews-for-aws-cdk-python-applications.html) | AWS DevOps, DevOps engineer |
| Create a GitHub personal access token. | To set up a secure way for your GitHub Actions workflows to authenticate and interact with GitHub, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-codeguru-reviews-for-aws-cdk-python-applications.html) | AWS DevOps, DevOps engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up resources. | To clean up your AWS CDK Python app, run the following command:<pre>cdk destroy --all</pre> | DevOps engineer |

## Troubleshooting
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Display link to the dashboard findings. | There is no way to print the findings during the CI/CD pipeline. Instead, this pattern uses GitHub Actions as an alternative method to handle and display the findings. |

## Related resources
<a name="automate-amazon-codeguru-reviews-for-aws-cdk-python-applications-resources"></a>

**AWS resources**
+ [AWS Cloud Development Kit](https://aws.amazon.com/cdk/)
+ [Amazon CodeGuru Documentation](https://docs.aws.amazon.com/codeguru/)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [AWS Identity and Access Management](https://aws.amazon.com/iam/)
+ [Amazon Simple Queue Service](https://aws.amazon.com/sqs/)
+ [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

**GitHub documentation**
+ [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
+ [GitHub Actions](https://github.com/features/actions)
+ [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
+ [Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow)
