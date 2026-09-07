---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions.html
---

# Dynamically generate an IAM policy with IAM Access Analyzer by using Step Functions
<a name="dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions"></a>

*Thomas Scott, Koen van Blijderveen, Adil El Kanabi, and Rafal Pawlaszek, Amazon Web Services*

## Summary
<a name="dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions-summary"></a>

*Least-privilege* is the security best practice of granting the minimum permissions required to perform a task. Implementing least-privilege access in an already active Amazon Web Services (AWS) account can be challenging because you don’t want to unintentionally block users from performing their job duties by changing their permissions. Before you can implement AWS Identity and Access Management (IAM) policy changes, you need to understand the actions and resources the account users are performing.

This pattern is designed to help you apply the principle of least-privilege access, without blocking or slowing down team productivity. It describes how to use IAM Access Analyzer and AWS Step Functions to dynamically generate an up-to-date IAM policy for your role, based on the actions that are currently being performed in the account. The new policy is designed to permit the current activity but remove any unnecessary, elevated privileges. You can customize the generated policy by defining allow and deny rules, and the solution integrates your custom rules.

This pattern includes options for implementing the solution with AWS Cloud Development Kit (AWS CDK) or HashiCorp CDK for Terraform (CDKTF). You can then associate the new policy to the role by using a continuous integration and continuous delivery (CI/CD) pipeline. If you have a multi-account architecture, you can deploy this solution in any account where you want to generate updated IAM policies for the roles, increasing the security of your entire AWS Cloud environment.

## Prerequisites and limitations
<a name="dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions-prereqs"></a>

**Prerequisites**
+ An active AWS account with a AWS CloudTrail trail enabled.
+ IAM permissions for the following:
  + Create and deploy Step Functions workflows. For more information, see [Actions, resources, and condition keys for AWS Step Functions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsstepfunctions.html) (Step Functions documentation).
  + Create AWS Lambda functions. For more information, see [Execution role and user permissions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-permissions) (Lambda documentation).
  + Create IAM roles. For more information, see [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) (IAM documentation).
+ npm installed. For more information, see [Downloading and installing Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (npm documentation).
+ If you are deploying this solution with AWS CDK (Option 1):
  + AWS CDK Toolkit, installed and configured. For more information, see [Install the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install) (AWS CDK documentation).
+ If you are deploying this solution with CDKTF (Option 2):
  + CDKTF, installed and configured. For more information, see [Install CDK for Terraform](https://learn.hashicorp.com/tutorials/terraform/cdktf-install?in=terraform/cdktf) (CDKTF documentation).
  + Terraform, installed and configured. For more information, see [Get Started](https://learn.hashicorp.com/collections/terraform/aws-get-started?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS) (Terraform documentation).
+ AWS Command Line Interface (AWS CLI) locally installed and configured for your AWS account. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (AWS CLI documentation).

**Limitations**
+ This pattern does not apply the new IAM policy to the role. At the end of this solution, the new IAM policy is stored in an AWS CodeCommit repository. You can use a CI/CD pipeline to apply policies to the roles in your account.

## Architecture
<a name="dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions-architecture"></a>

**Target architecture **

![The Step Functions workflow generating a new policy and storing it in CodeCommit.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/cb9ee0c9-3fe0-43d9-9dd2-1aedb705c78f/images/eb13a5db-f803-40b1-9a8c-4ef13d584cd4.png)

1. A regularly scheduled Amazon EventBridge event rule starts a Step Functions workflow. You define this regeneration schedule as part of setting up this solution.

1. In the Step Functions workflow, a Lambda function generates the date ranges to use when analyzing account activity in the CloudTrail logs.

1. The next workflow step calls the IAM Access Analyzer API to start generating the policy.

1. Using the Amazon Resource Name (ARN) of the role you specify during set up, IAM Access Analyzer analyzes the CloudTrail logs for activity within the specified date rate. Based on the activity, IAM Access Analyzer generates an IAM policy that permits only the actions and services used by the role during the specified date range. When this step is complete, this step generates a job ID.

1. The next workflow step checks for the job ID every 30 seconds. When the job ID is detected, this step uses the job ID to call the IAM Access Analyzer API and retrieve the new IAM policy. IAM Access Analyzer returns the policy as a JSON file.

1. The next workflow step puts the **<IAM role name>/policy.json** file in an Amazon Simple Storage Service (Amazon S3) bucket. You define this S3 bucket as part of setting up this solution.

1. An Amazon S3 event notification starts a Lambda function.

1. The Lambda function retrieves the policy from the S3 bucket, integrates the custom rules you define in the **allow.json** and **deny.json** files, and then pushes the updated policy to CodeCommit. You define the CodeCommit repository, branch, and folder path as part of setting up this solution.

## Tools
<a name="dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) is a command line cloud development kit that helps you interact with your AWS Cloud Development Kit (AWS CDK) app.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them. This pattern uses [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html), a feature of IAM, to analyze your CloudTrail logs to identify actions and services that have been used by an IAM entity (user or role) and then generate an IAM policy that is based on that activity.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications. In this pattern, you use [AWS SDK service integrations](https://docs.aws.amazon.com/step-functions/latest/dg/supported-services-awssdk.html) in Step Functions to call service API actions from your workflow.

**Other tools**
+ [CDK for Terraform (CDKTF)](https://learn.hashicorp.com/collections/terraform/cdktf) helps you define infrastructure as code (IaC) by using common programming languages, such as Python and Typescript.
+ [Lerna](https://lerna.js.org/docs/introduction) is a build system for managing and publishing multiple JavaScript or TypeScript packages from the same repository.
+ [Node.js](https://nodejs.org) is an event-driven JavaScript runtime environment designed for building scalable network applications.
+ [npm](https://docs.npmjs.com/about-npm) is a software registry that runs in a Node.js environment and is used to share or borrow packages and manage deployment of private packages.

**Code repository**

The code for this pattern is available in the GitHub [Automated IAM Access Analyzer Role Policy Generator](https://github.com/aws-samples/automated-iam-access-analyzer) repository.

## Epics
<a name="dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions-epics"></a>

### Prepare for deployment
<a name="prepare-for-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repo. | The following command clones the [Automated IAM Access Analyzer Role Policy Generator](https://github.com/aws-samples/automated-iam-access-analyzer) (GitHub) repository.<pre>git clone https://github.com/aws-samples/automated-iam-access-analyzer.git</pre> | App developer |
| Install Lerna. | The following command installs Lerna.<pre>npm i -g lerna</pre> | App developer |
| Set up the dependencies. | The following command installs the dependencies for the repository.<pre>cd automated-iam-access-analyzer/<br />npm install && npm run bootstrap</pre> | App developer |
| Build the code. | The following command tests, builds, and prepares the zip packages of the Lambda functions.<pre>npm run test:code<br />npm run build:code<br />npm run pack:code</pre> | App developer |
| Build the constructs. | The following command builds the infrastructure synthesizing applications, for both AWS CDK and CDKTF.<pre>npm run build:infra</pre> |  |
| Configure any custom permissions. | In the **repo** folder of the cloned repository, edit the **allow.json** and **deny.json** files to define any custom permissions for the role. If the **allow.json** and **deny.json** files contain the same permission, the deny permission is applied. | AWS administrator, App developer |

### Option 1 – Deploy the solution using AWS CDK
<a name="option-1-deploy-the-solution-using-cdk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the AWS CDK stack. | The following command deploys the infrastructure through AWS CloudFormation. Define the following parameters:+ `<NAME_OF_ROLE>` – The ARN of the IAM role for which you are creating a new policy.<br />+ `<TRAIL_ARN>` – The ARN of the CloudTrail trail in which the role activity is stored.<br />+ `<CRON_EXPRESSION_TO_RUN_SOLUTION>` – The Cron expression that defines the regeneration schedule for the policy. The Step Functions workflow runs on this schedule.<br />+ `<TRAIL_LOOKBACK>` – The period, in days, to look back in the trail when evaluating the role permissions.<pre>cd infra/cdk<br />cdk deploy —-parameters roleArn=<NAME_OF_ROLE> \<br />—-parameters trailArn=<TRAIL_ARN> \<br />--parameters schedule=<CRON_EXPRESSION_TO_RUN_SOLUTION> \<br />[ --parameters trailLookBack=<TRAIL_LOOKBACK> ]</pre>The square brackets denote optional parameters. | App developer |
| (Optional) Wait for the new policy. | If the trail does not contain a reasonable amount of historical activity for the role, wait until you are confident that there is enough logged activity for IAM Access Analyzer to generate an accurate policy. If the role has been active in the account for a sufficient period of time, this waiting period might not be necessary. | AWS administrator |
| Manually review the generated policy. | In your CodeCommit repository, review the generated **<ROLE\_ARN>.json** file to confirm that the allow and deny permissions are appropriate for the role. | AWS administrator |

### Option 2 – Deploy the solution using CDKTF
<a name="option-2-ndash-deploy-the-solution-using-cdktf"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Synthesize the Terraform template. | The following command synthesizes the Terraform template.<pre>lerna exec cdktf synth --scope @aiaa/tfm</pre> | App developer |
| Deploy the Terraform template. | The following command navigates to the directory that contains the CDKTF-defined infrastructure.<pre>cd infra/cdktf</pre><br />The following command deploys the infrastructure in the target AWS account. Define the following parameters:+ `<account_ID>` – The ID of the target account.<br />+ `<region>` - The target AWS Region.<br />+ `<selected_role_ARN>` – The ARN of the IAM role for which you are creating a new policy.<br />+ `<trail_ARN>` – The ARN of the CloudTrail trail in which the role activity is stored.<br />+ `<schedule_expression>` – The Cron expression that defines the regeneration schedule for the policy. The Step Functions workflow runs on this schedule.<br />+ `<trail_look_back>` – The period, in days, to look back in the trail when evaluating the role permissions.<pre>TF_VAR_accountId=<account_ID> \<br /> TF_VAR_region=<region> \<br /> TF_VAR_roleArns=<selected_role_ARN> \<br /> TF_VAR_trailArn=<trail_ARN> \<br /> TF_VAR_schedule=<schedule_expression> \<br /> [ TF_VAR_trailLookBack=<trail_look_back> ] \ cdktf deploy</pre>The square brackets denote optional parameters. | App developer |
| (Optional) Wait for the new policy. | If the trail does not contain a reasonable amount of historical activity for the role, wait until you are confident that there is enough logged activity for IAM Access Analyzer to generate an accurate policy. If the role has been active in the account for a sufficient period of time, this waiting period might not be necessary. | AWS administrator |
| Manually review the generated policy. | In your CodeCommit repository, review the generated **<ROLE\_ARN>.json** file to confirm that the allow and deny permissions are appropriate for the role. | AWS administrator |

## Related resources
<a name="dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions-resources"></a>

**AWS resources**
+ [IAM Access Analyzer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/access-analyzer.html)
+ [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
+ [Least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

**Other resources**
+ [CDK for Terraform](https://www.terraform.io/cdktf) (Terraform website)
