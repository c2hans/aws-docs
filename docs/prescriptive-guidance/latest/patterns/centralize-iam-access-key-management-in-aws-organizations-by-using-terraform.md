---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html
---

# Centralize IAM access key management in AWS Organizations by using Terraform
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform"></a>

*Pradip kumar Pandey and Pratap Kumar Nanda, Amazon Web Services*

## Summary
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-summary"></a>

Enforcing security rules for keys and passwords is an** **essential task for every organization. One  important rule is to rotate AWS Identity and Access Management (IAM) keys at regular intervals to enforce security. AWS access keys are generally created and configured locally whenever teams want to access AWS from the AWS Command Line Interface** **(AWS CLI) or from applications outside AWS. To maintain strong security across the organization, old security keys must be changed or deleted after the requirement has been met or at regular intervals. The process of managing key rotations across multiple accounts in an organization is time-consuming and tedious. This pattern helps you automate the rotation process by using Account Factory for Terraform (AFT) and AWS services.

The pattern provides these benefits:
+ Manages your access key IDs and secret access keys across all the accounts in your organization from a central location.
+ Automatically rotates the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.
+ Enforces renewal if user credentials are compromised.

The pattern uses Terraform to deploy AWS Lambda functions, Amazon EventBridge rules, and IAM roles. An EventBridge rule runs at regular intervals and calls a Lambda function that lists all user access keys based on when they were created. Additional Lambda functions create a new access key ID and secret access key, if the previous key is older than the rotation period you define (for example, 45 days), and notify a security administrator by using Amazon Simple Notification Service (Amazon SNS) and Amazon Simple Email Service (Amazon SES). Secrets are created in AWS Secrets Manager for that user, the old secret access key is stored in Secrets Manager, and permissions for accessing the old key are configured. To ensure that the old access key is no longer used, it is disabled after an inactive period (for example, 60 days, which would be  15 days after the keys were rotated in our example). After an inactive buffer period (for example, 90 days, or 45 days after the keys were rotated in our example), the old access keys are deleted from AWS Secrets Manager. For a detailed architecture and workflow, see the [Architecture](#centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-architecture) section.

## Prerequisites and limitations
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-prereqs"></a>
+ A landing zone for your organization that’s built by using [AWS Control Tower ](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)(version 3.1 or later)
+  [Account Factory for Terraform (AFT)](https://catalog.workshops.aws/control-tower/en-US/customization/aft) configured with three accounts:
  + [Organization management account](https://catalog.workshops.aws/control-tower/en-US/customization/aft/repositories/global-customizations) manages the entire organization from a central location.
  + [AFT management account](https://catalog.workshops.aws/control-tower/en-US/customization/aft/repositories/account-customizations)  hosts the Terraform pipeline and deploys the infrastructure into the deployment account.
  + [Deployment account](https://catalog.workshops.aws/control-tower/en-US/customization/aft/repositories/provisioning-customizations) deploys this complete solution and manages IAM keys from a central location.
+ Terraform version 0.15.0 or later  for provisioning the infrastructure in the deployment account.
+ An email address that’s configured in [Amazon Simple Email Service (Amazon SES)](https://aws.amazon.com/ses/).
+ (Recommended) To enhance security, deploy this solution inside a [private subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) (deployment account) within a [virtual private cloud (VPC)](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest). You can provide the details of the VPC and subnet when you customize the variables (see *Customize parameters for the code pipeline* in the [Epics](#centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-epics) section).

## Architecture
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-architecture"></a>

**AFT repositories**

This pattern uses Account Factory for Terraform (AFT) to create all required AWS resources and the code pipeline to deploy the resources in a deployment account. The code pipeline runs in two repositories:
+ **Global customization** contains Terraform code that will run across all accounts registered with AFT.
+ **Account customizations** contains Terraform code that will run in the deployment account.

**Resource details**

AWS CodePipeline jobs create the following resources in the deployment account:
+ AWS EventBridge rule and configured rule
+ `account-inventory` Lambda function
+ `IAM-access-key-rotation` Lambda function
+ `Notification` Lambda function
+ Amazon Simple Storage Service (Amazon S3) bucket that contains an email template
+ Required IAM policy

**Architecture**

![Architecture for centralizing IAM access key management in AWS Organizations](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0217275c-cb4c-4bdf-b105-ad9abfd4fded/images/844512f0-67b3-4d41-aaaa-fbd9e341c438.png)

The diagram illustrates the following:

1. An EventBridge rule calls the `account-inventory` Lambda function every 24 hours.

1. The `account-inventory` Lambda function queries AWS Organizations for a list of all AWS account IDs, account names, and account emails.

1. The `account-inventory` Lambda function initiates an `IAM-access-key-auto-rotation` Lambda function for each AWS account and passes the metadata to it for additional processing.

1. The `IAM-access-key-auto-rotation` Lambda function uses an assumed IAM role to access the AWS account. The Lambda script runs an audit against all users and their IAM access keys in the account.

1. The IAM key rotation threshold (rotation period) is configured as an environment variable when the `IAM-access-key-auto-rotation` Lambda function is deployed. If the rotation period is modified, the `IAM-access-key-auto-rotation` Lambda function is redeployed with an updated environment variable. You can configure parameters to set the rotation period, the inactive period for old keys, and the inactive buffer after which old keys will be deleted (see *Customize parameters for the code pipeline* in the [Epics](#centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-epics) section).

1. The `IAM-access-key-auto-rotation` Lambda function validates the age of the access key based on its configuration. If the IAM access key's age hasn’t exceeded the rotation period you defined, the Lambda function takes no further action.

1. If the IAM access key's age has exceeded the rotation period you defined, the `IAM-access-key-auto-rotation` Lambda function creates a new key and rotates the existing key.

1. The Lambda function saves the old key in Secrets Manager and limits permissions to the user whose access keys deviated from security standards. The Lambda function also creates a resource-based policy that allows only the specified IAM principal to access and retrieve the secret.

1. The `IAM-access-key-rotation` Lambda function calls the `Notification` Lambda function.

1. The `Notification` Lambda function queries the S3 bucket for an email template and dynamically generates email messages with the relevant activity metadata.

1. The `Notification` Lambda function calls Amazon SES for further action.

1.  Amazon SES sends email to the account owner's email address with the relevant information.

## Tools
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-tools"></a>

**AWS services**
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them. This patern requires IAM roles and permissions.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) helps you send and receive emails by using your own email addresses and domains.

**Other tools**
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The instructions and code for this pattern are available in the GitHub [IAM access key rotation](https://github.com/aws-samples/centralized-iam-key-management-aws-organizations-terraform.git) repository. You can deploy the code in the AWS Control Tower central deployment account to manage key rotation from a central location.

## Best practices
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-best-practices"></a>
+ For IAM, see [security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.
+ For key rotation, see [guidelines for updating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials) in the IAM documentation.

## Epics
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-epics"></a>

### Set up source files
<a name="set-up-source-files"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html) | DevOps engineer |

### Configure accounts
<a name="configure-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the bootstrapping account. | As part of the [AFT bootstrapping](https://catalog.workshops.aws/control-tower/en-US/customization/aft/deploy) process, you should have a folder called `aft-bootstrap` on your local machine.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html) | DevOps engineer |
| Configure global customizations. | As part of the [AFT folder](https://catalog.workshops.aws/control-tower/en-US/customization/aft/repositories/global-customizations) setup, you should have a folder called `aft-global-customizations` on your local machine.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html) | DevOps engineer |
| Configure account customizations. | As part of the [AFT folder setup](https://catalog.workshops.aws/control-tower/en-US/customization/aft/repositories/account-customizations), you have be a folder called `aft-account-customizations` on your local machine.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html) | DevOps engineer |

### Customize parameters for the code pipeline
<a name="customize-parameters-for-the-code-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Customize non-Terraform code pipeline parameters for all accounts. | Create a file called `input.auto.tfvars` in the `aft-global-customizations/terraform/` folder and provide the required input data. See [the file in the GitHub repository](https://github.com/aws-samples/centralized-iam-key-management-aws-organizations-terraform/blob/main/global-account-customization/input.auto.tfvars) for default values. | DevOps engineer |
| Customize code pipeline parameters for the deployment account. | Create a file called `input.auto.tfvars` in the `aft-account-customizations/<AccountName>/terraform/` folder and push the code to AWS CodeCommit. Pushing code to AWS CodeCommit automatically initiates the code pipeline.<br />Specify values for parameters based on your organization’s requirements, including the following (see [the file in the Github repository](https://github.com/aws-samples/centralized-iam-key-management-aws-organizations-terraform/blob/main/account-customization/input.auto.tfvars) for default values): [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html) | DevOps engineer |

### Validate key rotation
<a name="validate-key-rotation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the solution. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html) | DevOps engineer |

### Extend the solution
<a name="extend-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Customize the email notification date. | If you want to send email notifications on a specific day before you disable the access key, you can update the `IAM-access-key-auto-rotation` Lambda function with those changes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html) | DevOps engineer |

## Troubleshooting
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The `account-inventory` Lambda job fails with `AccessDenied` while listing accounts. | If you encounter this issue, you must validate permissions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-iam-access-key-management-in-aws-organizations-by-using-terraform.html) |

## Related resources
<a name="centralize-iam-access-key-management-in-aws-organizations-by-using-terraform-resources"></a>
+ [Terraform Recommended Practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) (Terraform documentation)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation)
+ [Best practices for key rotation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials) (IAM documentation)
