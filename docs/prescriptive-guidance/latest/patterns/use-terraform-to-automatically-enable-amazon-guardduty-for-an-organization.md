---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization.html
---

# Use Terraform to automatically enable Amazon GuardDuty for an organization
<a name="use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization"></a>

*Aarthi Kannan, Amazon Web Services*

## Summary
<a name="use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-summary"></a>

Amazon GuardDuty continuously monitors your Amazon Web Services (AWS) accounts and uses threat intelligence to identify unexpected and potentially malicious activity within your AWS environment. Manually enabling GuardDuty for multiple accounts or organizations, across multiple AWS Regions, or through the AWS Management Console can be cumbersome. You can automate the process by using an infrastructure as code (IaC) tool, such as Terraform, which can provision and manage multi-account, multi-Region services and resources in the cloud.

AWS recommends using AWS Organizations to set up and manage multiple accounts in GuardDuty. This pattern adheres to that recommendation. One benefit of this approach is that, when new accounts are created or added to the organization, GuardDuty will be auto-enabled in these accounts for all supported Regions, without the need for manual intervention.

This pattern demonstrates how to use HashiCorp Terraform to enable Amazon GuardDuty for three or more Amazon Web Services (AWS) accounts in an organization. The sample code provided with this pattern does the following:
+ Enables GuardDuty for all AWS accounts that are current members of the target organization in AWS Organizations
+ Turns on the *Auto-Enable* feature in GuardDuty, which automatically enables GuardDuty for any accounts that are added to the target organization in the future
+ Allows you select the Regions where you want to enable GuardDuty
+ Uses the organization’s security account as the GuardDuty delegated administrator
+ Creates an Amazon Simple Storage Service (Amazon S3) bucket in the logging account and configures GuardDuty to publish the aggregated findings from all accounts in this bucket
+ Assigns a life-cycle policy that transitions findings from the S3 bucket to Amazon S3 Glacier Flexible Retrieval storage after 365 days, by default

You can manually run this sample code, or you can integrate it into your continuous integration and continuous delivery (CI/CD) pipeline.

**Target audience**

This pattern is recommended for users who have experience with Terraform, Python, GuardDuty, and AWS Organizations.

## Prerequisites and limitations
<a name="use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An organization is set up in AWS Organizations, and it contains at least the following three accounts:
  + **A management account** – This is the account from which you deploy the Terraform code, either standalone or as part of the CI/CD pipeline. The Terraform state is also stored in this account.
  + **A security account** – This account is used as the GuardDuty delegated administrator. For more information, see [Important considerations for GuardDuty delegated administrators](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html#delegated_admin_important) (GuardDuty documentation).
  + **A logging account** – This account contains the S3 bucket where GuardDuty publishes the aggregated findings from all member accounts.

  For more information about how to set up the organization with the required configuration, see [Create an account structure](https://www.wellarchitectedlabs.com/cost/100_labs/100_1_aws_account_setup/2_account_structure/) (AWS Well-Architected Labs).
+ An Amazon S3 bucket and an Amazon DynamoDB table that serve as a remote backend to store Terraform’s state in the management account. For more information on using remote backends for the Terraform state, see [S3 Backends](https://www.terraform.io/language/settings/backends/s3) (Terraform documentation). For a code sample that sets up remote state management with an S3 backend, see [remote-state-s3-backend](https://registry.terraform.io/modules/nozaq/remote-state-s3-backend/aws/latest) (Terraform Registry). Note the following requirements:
  + The S3 bucket and DynamoDB table must be in the same Region.
  + When creating the DynamoDB table, the partition key must be `LockID` (case-sensitive), and the partition key type must be **String**. All other table settings must be at their default values. For more information, see [About primary keys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey) and [Create a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html) (DynamoDB documentation).
+ An S3 bucket that will be used to store access logs for the S3 bucket in which GuardDuty will publish findings. For more information, see [Enabling Amazon S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html) (Amazon S3 documentation). If you’re deploying to an AWS Control Tower landing zone, you can reuse the S3 bucket in the **log archive** account for this purpose.
+ Terraform version 0.14.6 or later is installed and configured. For more information, see [Get Started – AWS](https://learn.hashicorp.com/collections/terraform/aws-get-started) (Terraform documentation).
+ Python version 3.9.6 or later is installed and configured. For more information, see [Source releases](https://www.python.org/downloads/source/) (Python website).
+ AWS SDK for Python (Boto3) is installed. For more information, see [Installation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation) (Boto3 documentation).
+ jq is installed and configured. For more information, see [Download jq](https://stedolan.github.io/jq/download/) (jq documentation).

**Limitations**
+ This pattern supports macOS and Amazon Linux 2 operating systems. This pattern has not been tested for use in Windows operating systems.
**Note**
Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/).
+ GuardDuty must not already be enabled in any of the accounts, in any of the target Regions.
+ The IaC solution in this pattern does not deploy the prerequisites.
+ This pattern is designed for an AWS landing zone that adheres to the following best practices:
  + The landing zone was created by using AWS Control Tower.
  + Separate AWS accounts are used for security and logging.

**Product versions**
+ Terraform version 0.14.6 or later. The sample code has been tested for version 1.2.8.
+ Python version 3.9.6 or later.

## Architecture
<a name="use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-architecture"></a>

This section gives a high-level overview of this solution and the architecture established by the sample code. The following diagram shows the resources deployed across the various accounts in the organization, within a single AWS Region.

![Architecture diagram showing resources in management, security, logging, and member accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c9b68627-b68e-47a6-9933-d0f36ea10ae2/images/86193749-eef9-4d63-8a7f-daa0cd03fbfe.png)

1. Terraform creates the **GuardDutyTerraformOrgRole** AWS Identity and Access Management (IAM) role in the security account and the logging account.

1. Terraform creates an S3 bucket in the default AWS Region in the logging account. This bucket is used as the publishing destination to aggregate all GuardDuty findings across all Regions and from all accounts in the organization. Terraform also creates an AWS Key Management Service (AWS KMS) key in the security account that is used to encrypt the findings in the S3 bucket and configures automatic archiving of findings from the S3 bucket into S3 Glacier Flexible Retrieval storage.

1. From the management account, Terraform designates the security account as the delegated administrator for GuardDuty. This means that the security account now manages the GuardDuty service for all member accounts, including the management account. Individual member accounts cannot suspend or disable GuardDuty by themselves.

1. Terraform creates the GuardDuty detector in the security account, for the GuardDuty delegated administrator.

1. If it is not already enabled, Terraform enables S3 protection in GuardDuty. For more information, see [Amazon S3 protection in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html) (GuardDuty documentation).

1. Terraform enrolls all current, active member accounts in the organization as GuardDuty members.

1. Terraform configures the GuardDuty delegated administrator to publish the aggregated findings from all member accounts to the S3 bucket in the logging account.

1. Terraform repeats steps 3 through 7 for each AWS Region you choose.

**Automation and scale**

The sample code provided is modularized so that you can integrate it into your CI/CD pipeline for automated deployment.

## Tools
<a name="use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-tools"></a>

**AWS services**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyzes and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to protect your data.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.

**Other tools and services**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is a command-line interface application that helps you use code to provision and manage cloud infrastructure and resources.
+ [Python](https://www.python.org/) is a general-purpose programming language.
+ [jq](https://stedolan.github.io/jq/download/) is a command-line processor that helps you work with JSON files.

**Code repository**

The code for this pattern is available on GitHub, in the [amazon-guardduty-for-aws-organizations-with-terraform](https://github.com/aws-samples/amazon-guardduty-for-aws-organizations-with-terraform) repository.

## Epics
<a name="use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-epics"></a>

### Enable GuardDuty in the organization
<a name="enable-guardduty-in-the-organization"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | In a Bash shell, run the following command. In *Clone the repository* in the [Additional information](#use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-additional) section, you can copy the full command containing the URL of the GitHub repository. This clones the [amazon-guardduty-for-aws-organizations-with-terraform](https://github.com/aws-samples/amazon-guardduty-for-aws-organizations-with-terraform) repository from GitHub.<pre>git clone <github-repository-url></pre> | DevOps engineer |
| Edit the Terraform configuration file. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization.html) | DevOps engineer, General AWS, Terraform, Python |
| Generate CloudFormation templates for new IAM roles.  | This pattern includes an IaC solution to create two CloudFormation templates. These templates create two IAM roles that Terraform uses during the setup process. These templates adhere to the security best practice of [least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization.html) | DevOps engineer, General AWS |
| Create the IAM roles. | Following the instructions in [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (CloudFormation documentation), do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization.html) | DevOps engineer, General AWS |
| Assume the IAM role in the management account. | As a security best practice, we recommend that you assume the new **management-account-role** IAM role before proceeding. In the AWS Command Line Interface (AWS CLI), enter the command in *Assume the management account IAM role* in the [Additional Information](#use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-additional) section. | DevOps engineer, General AWS |
| Run the setup script. | In the repository `root` folder, run the following command to start the setup script.<pre>bash scripts/full-setup.sh</pre><br />The **full-setup.sh** script performs the following actions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization.html) | DevOps engineer, Python |

### (Optional) Disable GuardDuty in the organization
<a name="optional-disable-guardduty-in-the-organization"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the clean-up script. | If you used this pattern to enable GuardDuty for the organization and want to disable GuardDuty, in the repository `root` folder, run the following command to start the **cleanup-gd.sh** script.<pre>bash scripts/cleanup-gd.sh</pre><br />This script disables GuardDuty in the target organization, removes any deployed resources, and restores the organization to its previous state before using Terraform to enable GuardDuty.This script does not remove the Terraform state files or lock files from the local and remote backends. If you need to do so, you must perform these actions manually. Also, this script does not delete the imported organization or the accounts managed by it. Trusted access for GuardDuty isn’t disabled as part of the clean-up script. | DevOps engineer, General AWS, Terraform, Python |
| Remove IAM roles. | Delete the stacks that were created with the **role-to-assume-for-role-creation.yaml** and **management-account-role.yaml** CloudFormation templates. For more information, see [Deleting a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) (CloudFormation documentation). | DevOps engineer, General AWS |

## Related resources
<a name="use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-resources"></a>

*AWS documentation*
+ [Managing multiple accounts](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html) (GuardDuty documentation)
+ [Granting least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) (IAM documentation)

*AWS marketing*
+ [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
+ [AWS Organizations](https://aws.amazon.com/organizations/)

*Other resources*
+ [Terraform](https://www.terraform.io/)
+ [Terraform CLI Documentation](https://www.terraform.io/cli)

## Additional information
<a name="use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization-additional"></a>

**Clone the repository**

Run the following command to clone the GitHub repository.

```
git clone https://github.com/aws-samples/amazon-guardduty-for-aws-organizations-with-terraform
```

**Assume the management account IAM role**

To assume the IAM role in the management account, run the following command. Replace `<IAM role ARN>` with the ARN of the IAM role.

```
export ROLE_CREDENTIALS=$(aws sts assume-role --role-arn <IAM role ARN> --role-session-name AWSCLI-Session --output json)
export AWS_ACCESS_KEY_ID=$(echo $ROLE_CREDENTIALS | jq .Credentials.AccessKeyId | sed 's/"//g')
export AWS_SECRET_ACCESS_KEY=$(echo $ROLE_CREDENTIALS | jq .Credentials.SecretAccessKey | sed 's/"//g')
export AWS_SESSION_TOKEN=$(echo $ROLE_CREDENTIALS | jq .Credentials.SessionToken | sed 's/"//g')
```
