---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/overview.html
---

# Overview
<a name="overview"></a>

Terraform providers are plugins that allow Terraform to interact with different APIs. The Terraform AWS Provider is the official plugin for managing AWS infrastructure as code (IaC) with Terraform. It translates Terraform syntax into AWS API calls to create, read, update, and delete AWS resources.

TheAWS Provider handles authentication, translating Terraform syntax to AWS API calls, and provisioning resources in AWS. You use a Terraform `provider` code block to configure the provider plugin that Terraform uses to interact with the AWS API. You can configure multiple AWS Provider blocks to manage resources across different AWS accounts and Regions.

Here's an example Terraform configuration that uses multiple AWS Provider blocks with aliases to manage an Amazon Relational Database Service (Amazon RDS) database that has a replica in a different Region and account. The primary and secondary providers assume different AWS Identity and Access Management (IAM) roles:

```
# Configure the primary AWS Provider
provider "aws" {
  region = "us-west-1"
  alias  = "primary"
}

# Configure a secondary AWS Provider for the replica Region and account
provider "aws" {
  region      = "us-east-1"
  alias       = "replica"
  assume_role {
    role_arn     = "arn:aws:iam::<replica-account-id>:role/<role-name>"
    session_name = "terraform-session"
  }
}

# Primary Amazon RDS database
resource "aws_db_instance" "primary" {
  provider = aws.primary

  # ... RDS instance configuration
}

# Read replica in a different Region and account
resource "aws_db_instance" "read_replica" {
  provider = aws.replica

  # ... RDS read replica configuration
  replicate_source_db = aws_db_instance.primary.id
}
```

In this example:
+ The first `provider` block configures the primary AWS Provider in the `us-west-1` Region with the alias `primary`.
+ The second `provider` block configures a secondary AWS Provider in the `us-east-1` Region with the alias `replica`. This provider is used to create a read replica of the primary database in a different Region and account. The `assume_role` block is used to assume an IAM role in the replica account. The `role_arn` specifies the Amazon Resource Name (ARN) of the IAM role to assume, and `session_name` is a unique identifier for the Terraform session.
+ The `aws_db_instance.primary` resource creates the primary Amazon RDS database by using the `primary` provider in the `us-west-1` Region.
+ The `aws_db_instance.read_replica` resource creates a read replica of the primary database in the `us-east-1` Region by using the `replica` provider. The `replicate_source_db` attribute references the ID of the `primary` database.

## Objectives
<a name="objectives"></a>

This guide helps you gain operational knowledge on the Terraform AWS Provider and addresses the following business goals that you can achieve by following IaC best practices around security, reliability, compliance, and developer productivity.
+ Improve infrastructure code quality and consistency across Terraform projects.
+ Accelerate developer onboarding and ability to contribute to infrastructure code.
+ Increase business agility through faster infrastructure changes.
+ Reduce errors and downtime related to infrastructure changes.
+ Optimize infrastructure costs by following IaC best practices.
+ Strengthen your overall security posture through best practice implementation.

## Target audience
<a name="target-audience"></a>

The target audience for this guide includes technical leads and managers who oversee teams that use Terraform for IaC on AWS.

Other potential readers include infrastructure engineers, DevOps engineers, solutions architects, and developers who actively use Terraform to manage AWS infrastructure.

Following these best practices will save time and help unlock the benefits of IaC for these roles.
