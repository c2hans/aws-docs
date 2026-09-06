---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-attach-an-aws-managed-policy-for-systems-manager-to-ec2-instance-profiles-using-cloud-custodian-and-aws-cdk.html
---

# Automatically attach an AWS managed policy for Systems Manager to EC2 instance profiles using Cloud Custodian and AWS CDK
<a name="automatically-attach-an-aws-managed-policy-for-systems-manager-to-ec2-instance-profiles-using-cloud-custodian-and-aws-cdk"></a>

*Ali Asfour and Aaron Lennon, Amazon Web Services*

## Summary
<a name="automatically-attach-an-aws-managed-policy-for-systems-manager-to-ec2-instance-profiles-using-cloud-custodian-and-aws-cdk-summary"></a>

You can integrate Amazon Elastic Compute Cloud (Amazon EC2) instances with AWS Systems Manager to automate operational tasks and provide more visibility and control. To integrate with Systems Manager, EC2 instances must have an installed [AWS Systems Manager Agent (SSM Agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) and an `AmazonSSMManagedInstanceCore` AWS Identity and Access Management (IAM) policy attached to their instance profiles.

However, if you want to ensure that all EC2 instance profiles have the `AmazonSSMManagedInstanceCore` policy attached, you can face challenges updating new EC2 instances that don’t have instance profiles or EC2 instances that have an instance profile but don’t have the `AmazonSSMManagedInstanceCore` policy. It can also be difficult to add this policy across multiple Amazon Web Services (AWS) accounts and AWS Regions.

This pattern helps solve these challenges by deploying three [Cloud Custodian](https://cloudcustodian.io/) policies in your AWS accounts:
+ The first Cloud Custodian policy checks for existing EC2 instances that have an instance profile but don't have the `AmazonSSMManagedInstanceCore` policy. The `AmazonSSMManagedInstanceCore` policy is then attached.
+ The second Cloud Custodian policy checks for existing EC2 instances without an instance profile and adds a default instance profile that has the `AmazonSSMManagedInstanceCore` policy attached.
+ The third Cloud Custodian policy creates [AWS Lambda functions](https://cloudcustodian.io/docs/aws/lambda.html) in your accounts to monitor the creation of EC2 instances and instance profiles. This ensures that the `AmazonSSMManagedInstanceCore` policy is automatically attached when an EC2 instance is created.

This pattern uses [AWS DevOps](https://aws.amazon.com/devops/) tools to achieve a continuous, at-scale deployment of the Cloud Custodian policies to a multi-account environment, without provisioning a separate compute environment.

## Prerequisites and limitations
<a name="automatically-attach-an-aws-managed-policy-for-systems-manager-to-ec2-instance-profiles-using-cloud-custodian-and-aws-cdk-prereqs"></a>

**Prerequisites**
+ Two or more active AWS accounts. One account is the *security account* and the others are *member accounts*.
+ Permissions to provision AWS resources in the security account. This pattern uses [administrator permissions](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html), but you should grant permissions according to your organization’s requirements and policies.
+ Ability to assume an IAM role from the security account to member accounts and create the required IAM roles. For more information about this, see [Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) in the IAM documentation.
+
**Important**
AWS Command Line Interface (AWS CLI), installed and configured. For testing purposes, you can configure AWS CLI by using the `aws configure` command or setting environment variables. : This isn't recommended for production environments and we recommend that this account is only granted least privilege access. For more information about this, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the IAM documentation.
+ The `devops-cdk-cloudcustodian.zip` file (attached), downloaded to your local computer.
+ Familiarity with Python.
+ The required tools (Node.js, AWS Cloud Development Kit (AWS CDK), and Git), installed and configured. You can use the `install-prerequisites.sh` file in the `devops-cdk-cloudcustodian.zip` file to** **install these tools.** **Make sure you run this file with root privileges.

**Limitations**
+ Although this pattern can be used in a production environment, make sure that all IAM roles and policies meet your organization’s requirements and policies.

**Package versions**
+ Cloud Custodian version 0.9 or later
+ TypeScript version 3.9.7 or later
+ Node.js version 14.15.4 or later
+ `npm` version 7.6.1 or later
+ AWS CDK version 1.96.0 or later

## Architecture
<a name="automatically-attach-an-aws-managed-policy-for-systems-manager-to-ec2-instance-profiles-using-cloud-custodian-and-aws-cdk-architecture"></a>

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/169a7bde-789e-4ebd-b4ca-80eb28ac9927/images/8ec0b6b4-d4b0-42e5-833d-24d1e6098fd9.png)

The diagram shows the following workflow:

1. Cloud Custodian policies are pushed to an AWS CodeCommit repository in the security account. An Amazon CloudWatch Events rule automatically initiates the AWS CodePipeline pipeline.

1. The pipeline fetches the most recent code from CodeCommit and sends it to the continuous integration part of the continuous integration and continuous delivery (CI/CD) pipeline handled by AWS CodeBuild.

1. CodeBuild performs the complete DevSecOps actions, including policy syntax validation on the Cloud Custodian policies, and runs these policies in `--dryrun` mode to check which resources are identified.

1. If there are no errors, the next task alerts an administrator to review the changes and approve the deployment into the member accounts.

**Technology stack**
+ AWS CDK
+ CodeBuild
+ CodeCommit
+ CodePipeline
+ IAM
+ Cloud Custodian

**Automation and scale**

The AWS CDK pipelines module provisions a CI/CD pipeline that uses CodePipeline to orchestrate the building and testing of source code with CodeBuild, in addition to the deployment of AWS resources with AWS CloudFormation stacks. You can use this pattern for all member accounts and Regions in your organization. You can also extend the `Roles creation` stack to deploy other IAM roles in your member accounts.

## Tools
<a name="automatically-attach-an-aws-managed-policy-for-systems-manager-to-ec2-instance-profiles-using-cloud-custodian-and-aws-cdk-tools"></a>
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that enables you to interact with AWS services using commands in your command-line shell.
+ [AWS CodeBuild ](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)is a fully managed build service in the cloud.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that you can use to privately store and manage assets.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software.
+ [AWS Identity and Access Management  ](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)is a web service that helps you securely control access to AWS resources.
+ [Cloud Custodian](https://cloudcustodian.io/) is a tool that unifies the dozens of tools and scripts most organizations use for managing their public cloud accounts into one open-source tool.
+ [Node.js ](https://nodejs.org/en/)is a JavaScript runtime built on Google Chrome's V8 JavaScript engine.

**Code **

For a detailed list of modules, account functions, files, and deployment commands used in this pattern, see the `README` file in the `devops-cdk-cloudcustodian.zip` file (attached).

## Epics
<a name="automatically-attach-an-aws-managed-policy-for-systems-manager-to-ec2-instance-profiles-using-cloud-custodian-and-aws-cdk-epics"></a>

### Set up the pipeline with AWS CDK
<a name="set-up-the-pipeline-with-aws-cdk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the CodeCommit repository. | 1. Unzip the `devops-cdk-cloudcustodian.zip` file (attached) in the working directory on your local computer.<br />2. Sign in to the AWS Management Console for your security account,** **open the CodeCommit console, and then create a new `devops-cdk-cloudcustodian` repository.<br />3. Change into the project directory and set up the CodeCommit repository as the origin, commit the changes, and then push them to the origin branch by running the following commands:+ `cd devops-cdk-cloudcustodian` <br />+ `git init --initial-branch=main`<br />+ `git add . git commit -m 'initial commit' `<br />+ `git remote add origin https://git-codecommit.us-east-1.amazonaws.com/v1/devops-cdk-cloudcustodian `<br />+ `git push origin main`For more information about this, see [Creating a CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html) in the AWS CodeCommit documentation. | Developer |
| Install the required tools. | Use the `install-prerequisites.sh` file to install all the required tools on Amazon Linux. This doesn’t include AWS CLI because it comes pre-installed.<br />For more information about this, see the [Prerequisites](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_prerequisites) section of [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) in the AWS CDK documentation. | Developer |
| Install the required AWS CDK packages. | 1. Set up your virtual environment by running the following command in AWS CLI: `$ python3 -m venv .env`<br />2. Activate your virtual environment by running the following command: `$ source .env/bin/activate`<br />3. After the virtual environment is activated, install the required dependencies by running the following command: `$ pip install -r requirements.txt`<br />4. To add additional dependencies (for example, other AWS CDK libraries), add them to the `requirements.txt` file, and then run the following command: `pip install -r requirements.txt`The following packages are required by AWS CDK and are included in the `requirements.txt` file:+ `aws-cdk.aws-cloudwatch`<br />+ `aws-cdk.aws-codebuild`<br />+ `aws-cdk.aws-codecommit`<br />+ `aws-cdk.aws-codedeploy`<br />+ `aws-cdk.aws-codepipeline`<br />+ `aws-cdk.aws-codepipeline-actions`<br />+ `aws-cdk.aws-events`<br />+ `aws-cdk.aws-events-targets`<br />+ `aws-cdk.aws-iam`<br />+ `aws-cdk.aws-logs`<br />+ `aws-cdk.aws-s3`<br />+ `aws-cdk.aws-sns`<br />+ `aws-cdk.aws-sns-subscriptions`<br />+ `aws-cdk.aws-sqs`<br />+ `aws-cdk.core` | Developer |

### Configure your environment
<a name="configure-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the required variables. | Open the `vars.py` file in the root folder of your CodeCommit repository and update the following variables:+  Update `var_deploy_region = ‘us-east-1’` with the AWS Region where you want the pipeline to be deployed.<br />+  Update `var_codecommit_repo_name = "cdk-cloudcustodian"` with the name of your CodeCommit repository.<br />+  Update `var_codecommit_branch_name = "main"` with name of the CodeCommit branch.<br />+  Update `var_adminEmail=notifyadmin@email.com’` with the email address for the administrator that approves changes.<br />+ Update `var_slackWebHookUrl = https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`’ with the Slack webhook used to send Cloud Custodian notifications when changes are made.<br />+  Update `var_orgId = ‘o-yyyyyyyyyy’` with your organization ID.<br />+ Update `security_account = ‘123456789011’` with the AWS account ID for the account where the pipeline is deployed.<br />+ Update `member_accounts = [‘111111111111’,’111111111112’,’111111111113’]` with the member accounts where you want to bootstrap the AWS CDK stack and deploy the required IAM roles.<br />+ Set `cdk_bootstrap_member_accounts = True` to `True` if you want the pipeline to automatically bootstrap the AWS CDK to your member accounts.  If set to `True` this also requires the name of an existing IAM role in the member accounts that can be assumed from the security account. This IAM role must also have the required permissions to bootstrap the AWS CDK.<br />+ Update `cdk_bootstrap_role = ‘AWSControlTowerExecution’` with the existing IAM role in the member accounts that can be assumed from the security account. This role must also permission to bootstrap the AWS CDK. : This only applies if `cdk_bootstrap_member_accounts` is set to `True`. | Developer |
| Update the account.yml file with the member account information. | To run the [c7n-org Cloud Custodian](https://cloudcustodian.io/docs/tools/c7n-org.html) tool against multiple accounts, you must place the `accounts.yml` config file in the root of the repository. The following is a sample Cloud Custodian config file for AWS:<pre>accounts:<br />- account_id: '123123123123'<br />  name: account-1<br />  regions:<br />  - us-east-1<br />  - us-west-2<br />  role: arn:aws:iam::123123123123:role/CloudCustodian<br />  vars:<br />    charge_code: xyz<br />  tags:<br />  - type:prod<br />  - division:some division<br />  - partition:us<br />  - scope:pci</pre> | Developer |

### Bootstrap the AWS accounts
<a name="bootstrap-the-aws-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Boostrap the security account. | Bootstrap the `deploy_account` with the `cloudcustodian_stack` application by running the following command:<pre>cdk bootstrap -a 'python3 <br />cloudcustodian/cloudcustodian_stack.py</pre> | Developer |
| Option 1 - Automatically bootstrap the member accounts. | If the `cdk_bootstrap_member_accounts` variable is set to `True` in the `vars.py` file, the accounts specified in the `member_accounts` variable are automatically bootstrapped by the pipeline.<br />If required, you can update `*cdk_bootstrap_role*` with an IAM role that you can assume from the security account and that has the required permissions to bootstrap the AWS CDK.<br />New accounts added to the `member_accounts `variable are automatically bootstrapped by the pipeline so that the required roles can be deployed. | Developer |
| Option 2 - Manually bootstrap the member accounts.  | Although we don’t recommend using this approach, you can set the value of `cdk_bootstrap_member_accounts` to `False` and perform this step manually by running the following command:<pre>$ cdk bootstrap -a 'python3 cloudcustodian/member_account_roles_stack.py' \<br /><br />--trust {security_account_id} \<br /><br />--context assume-role-credentials:writeIamRoleName={role_name} \<br /><br />--context assume-role-credentials:readIamRoleName={role_name} \<br /><br />--mode=ForWriting \<br /><br />--context bootstrap=true \<br /><br />--cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess</pre>Make sure that you update the `{security_account_id}` and `{role_name}` values with the name of an IAM role that you can assume from the security account and that has the required permissions to bootstrap the AWS CDK.<br />You can also use other approaches to bootstrap the member accounts, for example, with AWS CloudFormation. For more information about this, see [Bootstrapping](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html) in the AWS CDK documentation. | Developer |

### Deploy the AWS CDK stacks
<a name="deploy-the-aws-cdk-stacks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the IAM roles in the member accounts. | Run the following command to deploy the `member_account_roles_stack` stack and create the IAM roles in the member accounts:<pre>cdk deploy --all -a 'python3 cloudcustodian/member_account_roles_stack.py' --require-approval never</pre> | Developer |
| Deploy the Cloud Custodian pipeline stack. | Run the following command to create the Cloud Custodian `cloudcustodian_stack.py` pipeline that is deployed into the security account:<pre>cdk deploy -a 'python3 cloudcustodian/cloudcustodian_stack.py'</pre> | Developer |

## Related resources
<a name="automatically-attach-an-aws-managed-policy-for-systems-manager-to-ec2-instance-profiles-using-cloud-custodian-and-aws-cdk-resources"></a>
+ [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)

## Attachments
<a name="attachments-169a7bde-789e-4ebd-b4ca-80eb28ac9927"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/169a7bde-789e-4ebd-b4ca-80eb28ac9927/attachments/attachment.zip)
