---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html
---

# Validate Account Factory for Terraform (AFT) code locally
<a name="validate-account-factory-for-terraform-aft-code-locally"></a>

*Alexandru Pop and Michal Gorniak, Amazon Web Services*

## Summary
<a name="validate-account-factory-for-terraform-aft-code-locally-summary"></a>

This pattern shows how to locally test HashiCorp Terraform code that’s managed by AWS Control Tower Account Factory for Terraform (AFT). Terraform is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources. AFT sets up a Terraform pipeline that helps you provision and customize multiple AWS accounts in AWS Control Tower.

During code development, it can be helpful to test your Terraform infrastructure as code (IaC) locally, outside of the AFT pipeline. This pattern shows how to do the following:
+ Retrieve a local copy of the Terraform code that’s stored in the AWS CodeCommit repositories in your AFT management account.
+ Simulate the AFT pipeline locally by using the retrieved code.

This procedure can also be used to run Terraform commands that aren’t part of the normal AFT pipeline. For example, you can use this method to run commands such as `terraform validate`, `terraform plan`, `terraform destroy`, and `terraform import`.

## Prerequisites and limitations
<a name="validate-account-factory-for-terraform-aft-code-locally-prereqs"></a>

**Prerequisites **
+ An active AWS multi-account environment that uses [AWS Control Tower](https://aws.amazon.com/controltower)
+ A fully deployed of [AFT environment](https://docs.aws.amazon.com/controltower/latest/userguide/taf-account-provisioning.html)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [AWS CLI credential helper for AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-unixes.html), installed and configured
+ Python 3.x
+ [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), installed and configured on your local machine
+ `git-remote-commit` utility, [installed and configured](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html#setting-up-git-remote-codecommit-install)
+ [Terraform](https://learn.hashicorp.com/collections/terraform/aws-get-started?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS), installed and configured (the local Terraform package version must match the version that’s used in the AFT deployment)

**Limitations **
+ This pattern doesn’t cover the deployment steps required for AWS Control Tower, AFT, or any specific Terraform modules.
+ The output that’s generated locally during this procedure isn’t saved in the AFT pipeline runtime logs.

## Architecture
<a name="validate-account-factory-for-terraform-aft-code-locally-architecture"></a>

**Target technology stack  **
+ AFT infrastructure deployed within an AWS Control Tower deployment
+ Terraform
+ Git
+ AWS CLI version 2

**Automation and scale**

This pattern shows how to locally invoke Terraform code for AFT global account customizations in a single AFT-managed AWS account. After your Terraform code is validated, you can apply it to the remaining accounts in your multi-account environment. For more information, see [Re-invoke customizations](https://docs.aws.amazon.com/controltower/latest/userguide/aft-account-customization-options.html#aft-re-invoke-customizations) in the AWS Control Tower documentation.

You can also use a similar process to run AFT account customizations in a local terminal. To locally invoke Terraform code from AFT account customizations, clone the **aft-account-customizations** repository instead of **aft-global-account-customizations** repository from CodeCommit in your AFT management account.

## Tools
<a name="validate-account-factory-for-terraform-aft-code-locally-tools"></a>

**AWS services**
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following prescriptive best practices.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.

**Other services**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.
+ [Git](https://git-scm.com/docs) is an open-source, distributed version control system.

**Code **

The following is an example bash script that can be used to locally run Terraform code that’s managed by AFT. To use the script, follow the instructions in the [Epics](#validate-account-factory-for-terraform-aft-code-locally-epics) section of this pattern.

```
#! /bin/bash
# Version: 1.1 2022-06-24 Unsetting AWS_PROFILE since, when set, it interferes with script operation
#          1.0 2022-02-02 Initial Version
#
# Purpose: For use with AFT: This script runs the local copy of TF code as if it were running within AFT pipeline.
#        * Facilitates testing of what the AFT pipline will do
#           * Provides the ability to run terraform with custom arguments (like 'plan' or 'move') which are currently not supported within the pipeline.
#
# © 2021 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
# This AWS Content is provided subject to the terms of the AWS Customer Agreement
# available at http://aws.amazon.com/agreement or other written agreement between
# Customer and either Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.
#
# Note: Arguments to this script are passed directly to 'terraform' without parsing nor validation by this script.
#
# Prerequisites:
#    1. local copy of ct GIT repositories
#    2. local backend.tf and aft-providers.tf filled with data for the target account on which terraform is to be run
#       Hint: The contents of above files can be obtain from the logs of a previous execution of the AFT pipeline for the target account.
#    3. 'terraform' binary is available in local PATH
#    4. Recommended: .gitignore file containing 'backend.tf', 'aft_providers.tf' so the local copy of these files are not pushed back to git

readonly credentials=$(aws sts assume-role \
    --role-arn arn:aws:iam::$(aws sts get-caller-identity --query "Account" --output text ):role/AWSAFTAdmin \
    --role-session-name AWSAFT-Session \
    --query Credentials )

unset AWS_PROFILE
export AWS_ACCESS_KEY_ID=$(echo $credentials | jq -r '.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $credentials | jq -r '.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $credentials | jq -r '.SessionToken')
terraform "$@"
```

## Epics
<a name="validate-account-factory-for-terraform-aft-code-locally-epics"></a>

### Save the example code as a local file
<a name="save-the-example-code-as-a-local-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Save the example code as a local file. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html) | AWS administrator |
| Make the example code runnable. | Open a terminal window and authenticate into your AWS AFT management account by doing one of the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html)Your organization might also have a custom tool to provide authentication credentials to your AWS environment. | AWS administrator |
| Verify access to AFT management account in the correct AWS Region. | Make sure that you use the same terminal session with which you authenticated into your AFT management account.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html) | AWS administrator |
| Create a new, local directory to store the AFT repository code. | In the same terminal session, run the following commands:<pre>mkdir my_aft <br />cd my_aft</pre> | AWS administrator |
| Clone the remote AFT repository code. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html) | AWS administrator |

### Create the Terraform configuration files required for the AFT pipeline to run locally
<a name="create-the-terraform-configuration-files-required-for-the-aft-pipeline-to-run-locally"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Open a previously run AFT pipeline and copy the Terraform configuration files to a local folder. | The `backend.tf` and `aft-providers.tf` configuration files that are created in this epic are needed for the AFT pipeline to run locally. These files are created automatically within the cloud-based AFT pipeline, but must be created manually for the pipeline to run locally. Running the AFT pipeline locally requires one set of files that represent running the pipeline within a single AWS account.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html)**Example auto-generated backend.tf statement**<pre>## Autogenerated backend.tf ##<br />## Updated on: 2022-05-31 16:27:45 ##<br />terraform {<br />  required_version = ">= 0.15.0"<br />  backend "s3" {<br />    region         = "us-east-2"<br />    bucket         = "aft-backend-############-primary-region"<br />    key            = "############-aft-global-customizations/terraform.tfstate"<br />    dynamodb_table = "aft-backend-############"<br />    encrypt        = "true"<br />    kms_key_id     = "########-####-####-####-############"<br />    role_arn       = "arn:aws:iam::#############:role/AWSAFTExecution"<br />  }<br />}</pre>** **The `backend.tf` and `aft-providers.tf` files are tied to a specific AWS account, AFT deployment, and folder. These files are also different, depending on whether they’re in the **aft-global-customizations** and **aft-account-customizations** repository within the same AFT deployment. Make sure that you generate both files from the same runtime listing. | AWS administrator |

### Run the AFT pipeline locally by using the example bash script
<a name="run-the-aft-pipeline-locally-by-using-the-example-bash-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Implement the Terraform configuration changes that you want to validate. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html) | AWS administrator |
| Run the `ct_terraform.sh` script and review the output. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html)** **[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html) | AWS administrator |

### Push your local code changes back to the AFT repository
<a name="push-your-local-code-changes-back-to-the-aft-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add references to the `backend.tf` and `aft-providers.tf` files to a `.gitignore` file. | Add the `backend.tf`** **and `aft-providers.tf` files that you created to a `.gitignore` file by running the following commands:<pre>echo backend.tf >> .gitignore<br />echo aft-providers.tf >>.gitignore</pre>Moving the files to the `.gitignore`** **file ensures that they don’t get committed and pushed back to the remote AFT repository. | AWS administrator |
| Commit and push your code changes to the remote AFT repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/validate-account-factory-for-terraform-aft-code-locally.html)The code changes that you introduce by following this procedure up until this point are applied to one AWS account only. | AWS administrator |

### Roll out the changes to multiple accounts
<a name="roll-out-the-changes-to-multiple-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Roll out the changes to all of your accounts that are managed by AFT. | To roll out the changes to multiple AWS accounts that are managed by AFT, follow the instructions in [Re-invoke customizations](https://docs.aws.amazon.com/controltower/latest/userguide/aft-account-customization-options.html#aft-re-invoke-customizations) in the AWS Control Tower documentation. | AWS administrator |
