---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk.html
---

# Set up a CI/CD pipeline by using AWS CodePipeline and AWS CDK
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk"></a>

*Konstantin Zarudaev, Yasha Dabas, Lars Kinder, and Cizer Pereira, Amazon Web Services*

## Home
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk-summary"></a>

Automating your software build and release process with continuous integration and continuous delivery (CI/CD) supports repeatable builds and rapid delivery of new features to your users. You can quickly and easily test each code change, and you can catch and fix bugs before releasing your software. By running each change through your staging and release process, you can verify the quality of your application or infrastructure code. CI/CD embodies a culture, a set of operating principles, and a [collection of practices](https://aws.amazon.com/devops/#cicd) that help application development teams to deliver code changes more frequently and reliably. The implementation is also known as the *CI/CD pipeline*.

This pattern defines a reusable continuous integration and continuous delivery (CI/CD) pipeline on Amazon Web Services (AWS) with an AWS CodeCommit repository. The AWS CodePipeline pipeline is written using [AWS Cloud Development Kit (AWS CDK) v2](https://aws.amazon.com/cdk/).

Using CodePipeline, you can model the different stages of your software release process through the AWS Management Console interface, the AWS Command Line Interface (AWS CLI), AWS CloudFormation, or the AWS SDKs. This pattern demonstrates the implementation of CodePipeline and its components using AWS CDK. In addition to construct libraries, AWS CDK includes a toolkit (the CLI command `cdk`), which is the primary tool for interacting with your AWS CDK app. Among other functions, the toolkit provides the ability to convert one or more stacks to CloudFormation templates and deploy them to an AWS account.

The pipeline includes tests to validate the security of your third-party libraries, and it helps ensure expedited, automated release in the specified environments. You can increase the overall security of your applications by putting them through a validation process.

The intent of this pattern is to accelerate your use of CI/CD pipelines to deploy your code while ensuring the resources you deploy adhere to DevOps best practices. After you implement the [example code](https://github.com/aws-samples/aws-codepipeline-cicd), you will have an [AWS CodePipeline](https://aws.amazon.com/codepipeline/) with linting, testing, a security check, deployment, and post-deployment processes. This pattern also includes steps for Makefile. Using a Makefile, developers can reproduce CI/CD steps locally and increase the velocity of the development process.

## Prerequisites and limitations
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A basic understanding in the following:
  + AWS CDK
  + AWS CloudFormation
  + AWS CodePipeline
  + TypeScript

**Limitations**

This pattern uses [AWS CDK ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html)for TypeScript only. It doesn’t cover other languages supported by AWS CDK.

**Product versions**

Use the latest versions of the following tools:
+ AWS Command Line Interface (AWS CLI)
+ cfn\_nag
+ git-remote-codecommit
+ Node.js

## Architecture
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk-architecture"></a>

**Target technology stack**
+ AWS CDK
+ AWS CloudFormation
+ AWS CodeCommit
+ AWS CodePipeline

**Target architecture**

The pipeline is triggered by a change in the AWS CodeCommit repository (`SampleRepository`). In the beginning, CodePipeline builds artifacts, updates itself, and starts the deployment process. The resulting pipeline deploys a solution to three independent environments:
+ Dev – Three-step code check in the active development environment
+ Test – Integration and regression test environment
+ Prod – Production environment

The three steps included in the Dev stage are linting, security, and unit tests. These steps run in parallel to speed up the process. To ensure that the pipeline provides only working artifacts, it will be stop running whenever a step in the process fails. After a Dev stage deployment, the pipeline runs validation tests to verify the results. In the case of success, the pipeline will then deploy the artifacts to the Test environment, which contains post-deployment validation. The final step is to deploy the artifacts to the Prod environment.

The following diagram shows the workflow from the CodeCommit repository to the build and update processes performed by CodePipeline, the three Dev environment steps, and subsequent deployment and validation in each of the three environments.

![Dev environment includes linting, security and unit testing, all include deploy and validate.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d617e735-8624-4722-8a3d-073bcc356328/images/92504aac-03e3-4c95-b225-74505f8dd136.png)

## Tools
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions. In this pattern CloudFormation templates can be used to create a CodeCommit repository and a CodePipeline CI/CD pipeline.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) is a CI/CD service that helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.

**Other tools**
+ [cfn\_nag](https://github.com/stelligent/cfn_nag) is an open-source tool that looks for patterns in CloudFormation templates to identify potential security issues.
+ [git-remote-codecommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html) is a utility for pushing and pulling code from CodeCommit repositories by extending Git.
+ [Node.js](https://nodejs.org/en/docs/) is an event-driven JavaScript runtime environment designed for building scalable network applications.

**Code**

The code for this pattern is available in the GitHub [AWS CodePipeline with CI/CD practices](https://github.com/aws-samples/aws-codepipeline-cicd) repository.

## Best practices
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk-best-practices"></a>

Review resources, such as AWS Identity and Access Management (IAM) policies, to confirm that they align with your organizational best practices.

## Epics
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk-epics"></a>

### Install tools
<a name="install-tools"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install tools on macOS or Linux. | If you are using MacOS or Linux, you can install the tools by running the following command in your preferred terminal or using [Homebrew for Linux](https://docs.brew.sh/Homebrew-on-Linux).<pre>brew install<br />brew install git-remote-codecommit<br />brew install ruby brew-gem<br />brew-gem install cfn-nag</pre> | DevOps engineer |
| Set up AWS CLI. | To set up AWS CLI, use the instructions for your operating system:+ Windows: [Setup steps for HTTPS connections to AWS CodeCommit repositories on Windows with the AWS CLI credential helper](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-windows.html)<br />+ Linux, macOS, Unix: [Setup steps for HTTPS connections to AWS CodeCommit repositories on Linux, macOS, or Unix with the AWS CLI credential helper](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-unixes.html) | DevOps engineer |

### Set up the initial deployment
<a name="set-up-the-initial-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download or clone the code. | To get the code that is used by this pattern, do one of the following:+ Download the latest source code from [releases](https://github.com/aws-samples/aws-codepipeline-cicd/releases) in the GitHub repo, and unzip the downloaded file into a folder.<br />+ Clone the project by running the following command.<pre>git clone --depth 1 https://github.com/aws-samples/aws-codepipeline-cicd.git</pre><br />Remove the `.git` directory from the cloned repository.<pre>cd ./aws-codepipeline-cicd<br />rm -rf ./.git</pre><br />Later, you will use a newly created AWS CodeCommit repository as a remote origin. | DevOps engineer |
| Connect to the AWS account. | You can connect by using a temporary security token or landing zone authentication. To confirm that you are using the correct account and AWS Region, run the following commands.<pre>AWS_REGION="eu-west-1"<br />ACCOUNT_NUMBER=$(aws sts get-caller-identity --query Account --output text)<br />echo "${ACCOUNT_NUMBER}"</pre> | DevOps engineer |
| Bootstrap the environment. | To bootstrap an AWS CDK environment, run the following commands.<pre>npm install<br />npm run cdk bootstrap "aws://${ACCOUNT_NUMBER}/${AWS_REGION}"</pre><br />After you successfully bootstrap the environment, the following output should be displayed.<pre>⏳  Bootstrapping environment aws://{account}/{region}...<br />✅  Environment aws://{account}/{region} bootstrapped</pre><br />For more information about AWS CDK bootstrapping, see the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html). | DevOps engineer |
| Synthesize a template. | To synthesize an AWS CDK app, use the `cdk synth` command.<pre>npm run cdk synth</pre><br />You should see the following output.<pre>Successfully synthesized to <path-to-directory>/aws-codepipeline-cicd/cdk.out<br />Supply a stack id (CodePipeline, Dev-MainStack) to display its template.</pre> | DevOps engineer |
| Deploy the CodePipeline stack. | Now that you bootstrapped and synthesized the CloudFormation template, you can deploy it. The deployment will create the CodePipeline pipeline and a CodeCommit repository, which will be the source and trigger of the pipeline.<pre>npm run cdk -- deploy CodePipeline --require-approval never</pre><br />After you run the command, you should see a successful deployment of the CodePipeline stack and output information. The `CodePipeline.RepositoryName` gives you the name of the CodeCommit repository in the AWS account.<pre>CodePipeline: deploying...<br />CodePipeline: creating CloudFormation changeset...<br />✅  CodePipeline<br />Outputs:<br />CodePipeline.RepositoryName = SampleRepository<br />Stack ARN:<br />arn:aws:cloudformation:REGION:ACCOUNT-ID:stack/CodePipeline/STACK-ID</pre> | DevOps engineer |
| Set up the remote CodeCommit repository and branch. | After a successful deployment, CodePipeline will initiate the first run of the pipeline, which you can find in the [AWS CodePipeline console](https://eu-west-1.console.aws.amazon.com/codesuite/codepipeline/pipelines). Because AWS CDK and CodeCommit don’t initiate a default branch, this initial pipeline run will fail and return the following error message.<pre>The action failed because no branch named main was found in the selected AWS CodeCommit repository SampleRepository. Make sure you are using the correct branch name, and then try again. Error: null</pre><br />To fix this error, set up a remote origin as `SampleRepository`, and create the required `main` branch.<pre>RepoName=$(aws cloudformation describe-stacks --stack-name CodePipeline --query "Stacks[0].Outputs[?OutputKey=='RepositoryName'].OutputValue" --output text)<br />echo "${RepoName}"<br />#<br />git init<br />git branch -m master main<br />git remote add origin codecommit://${RepoName}<br />git add .<br />git commit -m "Initial commit"<br />git push -u origin main</pre> | DevOps engineer |

### Test the deployed CodePipeline pipeline
<a name="test-the-deployed-codepipeline-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Commit a change to activate the pipeline. | After a successful initial deployment, you should have a complete CI/CD pipeline with a `main` branch for `SampleRepository` as a source branch. As soon as you commit changes to the `main` branch, the pipeline will initiate and run the following sequence of actions:1. Get your code from the CodeCommit repository.<br />2. Build your code.<br />3. Update the pipeline itself (`UpdatePipeline`).<br />4. Run three parallel jobs for linting, security and unit test checks.<br />5. In the case of success, the pipeline will deploy the `Main` stack from `./lib/main-stack.ts` to the Dev environment.<br />6. Run a post-deployment check for deployed resources. You can follow all CodePipeline steps and results in the CodePipeline console.<br />7. In the case of success, the pipeline will repeat deployment and validation for the Test and Prod environments. | DevOps engineer |

### Test locally by using a Makefile
<a name="test-locally-by-using-a-makefile"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the development process by using a Makefile. | You can run the whole pipeline locally by using the `make` command, or you can run an individual step (for example, `make linting`).<br />To test using `make`, perform the following actions:+ Implement the local pipeline: `make`<br />+ Run only unit testing: `make unittest`<br />+ Deploy to the current account: `make deploy`<br />+ Clean up the environment: `make clean` | App developer, DevOps engineer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete AWS CDK app resources. | To clean up your AWS CDK app, run the following command.<pre>cdk destroy --all</pre><br />Be aware that the Amazon Simple Storage Service (Amazon S3) buckets that are created during bootstrapping aren't automatically deleted. They need a retention policy that allows deletion, or you need to delete them manually in your AWS account. | DevOps engineer |

## Troubleshooting
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The template isn’t working as expected. | If something goes wrong and template is not working, make sure that you have the following:+ The proper versions of the tools.<br />+ Access to the target AWS account (network connectivity).<br />+ Enough permissions to the target AWS account. |

## Related resources
<a name="set-up-a-ci-cd-pipeline-by-using-aws-codepipeline-and-aws-cdk-resources"></a>
+ [Get started with common tasks in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html)
+ [AWS CodePipeline documentation](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+ [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
