---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts.html
---

# Monitor use of a shared Amazon Machine Image across multiple AWS accounts
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts"></a>

*Naveen Suthar and Sandeep Gawande, Amazon Web Services*

## Summary
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-summary"></a>

[Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) are used to create Amazon Elastic Compute Cloud (Amazon EC2) instances in your Amazon Web Services (AWS) environment. You can create AMIs in a separate, centralized AWS account, which is called a *creator account* in this pattern. You can then share the AMI across multiple AWS accounts that are in the same AWS Region, which are called *consumer accounts* in this pattern. Managing AMIs from a single account provides scalability and simplifies governance. In the consumer accounts, you can reference the shared AMI in Amazon EC2 Auto Scaling [launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html) and Amazon Elastic Kubernetes Service (Amazon EKS) [node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html).

When a shared AMI is [deprecated](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html), [deregistered](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html), or [unshared](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html), AWS services that refer to the AMI in the consumer accounts cannot use this AMI to launch new instances. Any auto scaling event or relaunch of the same instance fails. This can lead to issues in the production environment, such as application downtime or performance degradation. When AMI sharing and usage events occur in multiple AWS accounts, it can be difficult to monitor this activity.

This pattern helps you monitor shared AMI usage and status across accounts in the same Region. It uses serverless AWS services, such as Amazon EventBridge, Amazon DynamoDB, AWS Lambda, and Amazon Simple Email Service (Amazon SES). You provision the infrastructure as code (IaC) by using HashiCorp Terraform. This solution provides alerts when a service in a consumer account references a deregistered or unshared AMI.

## Prerequisites and limitations
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-prereqs"></a>

**Prerequisites**
+ Two or more active AWS accounts: one creator account and one or more consumer accounts
+ One or more AMIs that are shared from the creator account to a consumer account
+ Terraform CLI, [installed](https://developer.hashicorp.com/terraform/cli) (Terraform documentation)
+ Terraform AWS Provider, [configured](https://hashicorp.github.io/terraform-provider-aws/) (Terraform documentation)
+ (Optional, but recommended) Terraform backend, [configured](https://developer.hashicorp.com/terraform/language/backend) (Terraform documentation)
+ Git, [installed](https://github.com/git-guides/install-git)

**Limitations**
+ This pattern monitors AMIs that have been shared to specific accounts by using the account ID. This pattern does not monitor AMIs that have been shared to an organization by using the organization ID.
+ AMIs can only be shared to accounts that are within the same AWS Region. This pattern monitors AMIs within a single, target Region. To monitor use of AMIs in multiple Regions, you deploy this solution in each Region.
+ This pattern doesn't monitor any AMIs that were shared before this solution was deployed. If you want to monitor previously shared AMIs, you can unshare the AMI and then reshare it with the consumer accounts.

**Product versions**
+ Terraform version 1.2.0 or later
+ Terraform AWS Provider version 4.20 or later

## Architecture
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-architecture"></a>

**Target technology stack**

The following resources are provisioned as IaC through Terraform:
+ Amazon DynamoDB tables
+ Amazon EventBridge rules
+ AWS Identity and Access Management (IAM) role
+ AWS Lambda functions
+ Amazon SES

**Target architecture**

![Architecture for monitoring shared AMI use and alerting users if the AMI is unshared or deregistered](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2d709249-0c68-47d7-be5d-46e8a73071ed/images/8c48c4dd-d681-4c32-9ba8-8f5ad2d66f64.png)

The diagram shows the following workflow:

1. An AMI in the creator account is shared with a consumer account in the same AWS Region.

1. When the AMI is shared, an EventBridge rule in the creator account captures the `ModifyImageAttribute` event and initiates a Lambda function in the creator account.

1. The Lambda function stores data related to the AMI in a DynamoDB table in the creator account.

1. When an AWS service in the consumer account uses the shared AMI to launch an Amazon EC2 instance or when the shared AMI is associated with a launch template, an EventBridge rule in the consumer account captures use of the shared AMI.

1. The EventBridge rule initiates a Lambda function in the consumer account. The Lambda function does the following:

   1. The Lambda function updates the AMI-related data in a DynamoDB table in the consumer account.

   1. The Lambda function assumes an IAM role in the creator account and updates the Lambda table in the creator account. In the `Mapping` table, it creates an item that maps the instance ID or launch template ID to its respective AMI ID.

1. The AMI that is centrally managed in the creator account is deprecated, deregistered, or unshared.

1. The EventBridge rule in the creator account captures the `ModifyImageAttribute` or `DeregisterImage` event with the `remove` action and initiates the Lambda function.

1. The Lambda function checks the DynamoDB table to determine whether the AMI is used in any of the consumer accounts. If there are no instance IDs or launch template IDs associated with the AMI in the `Mapping` table, then the process is complete.

1. If any instance IDs or launch template IDs are associated with the AMI in the `Mapping` table, then the Lambda function uses Amazon SES to send an email notification to the configured subscribers.

## Tools
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-tools"></a>

**AWS services**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) helps you send and receive emails by using your own email addresses and domains.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [cross-account-ami-monitoring-terraform-samples](https://github.com/aws-samples/cross-account-ami-monitoring-terraform-samples) repository.

## Best practices
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-best-practices"></a>
+ Follow the [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).
+ Follow the [Best practices for building AMIs](https://docs.aws.amazon.com/marketplace/latest/userguide/best-practices-for-building-your-amis.html).
+ When creating the IAM role, follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPracticesAndUseCases.html) in the IAM documentation.
+ Set up monitoring and alerting for the AWS Lambda functions. For more information, see [Monitoring and troubleshooting Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html).

## Epics
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-epics"></a>

### Customize the Terraform configuration files
<a name="customize-the-terraform-configuration-files"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the AWS CLI named profiles. | For the creator account and each consumer account, create an AWS Command Line Interface (AWS CLI) named profile. For instructions, see [Set up the AWS CLI](https://aws.amazon.com/getting-started/guides/setup-environment/module-three/)  in the AWS Getting Started Resources Center. | DevOps engineer |
| Clone the repository. | Enter the following command. This clones the [cross-account-ami-monitoring-terraform-samples](https://github.com/aws-samples/cross-account-ami-monitoring-terraform-samples) repository from GitHub by using SSH.<pre>git clone git@github.com:aws-samples/cross-account-ami-monitoring-terraform-samples.git</pre> | DevOps engineer |
| Update the provider.tf file. | 1. Enter the following command to navigate into the `terraform` folder in the cloned repository.<pre>cd cross-account-ami-monitoring/terraform</pre><br />2. Open the `provider.tf` file.<br />3. Update the Terraform AWS Provider configurations for the creator account and consumer account as follows:For `alias`, enter a name for the provider configuration.For `region`, enter the target AWS Region where you want to deploy this solution.For `profile`, enter the AWS CLI named profile for accessing the account.<br />4. If you are configuring more than one consumer account, create a profile for each additional consumer account.<br />5. Save and close the `provider.tf` file.For more information about configuring the providers, see [Multiple provider configurations](https://developer.hashicorp.com/terraform/language/providers/configuration#alias-multiple-provider-configurations) in the Terraform documentation. | DevOps engineer |
| Update the terraform.tfvars file. | 1. Open the `terraform.tfvars` file.<br />2. In the `account_email_mapping` parameter, configure alerts for the creator account and consumer account as follows:For `account`, enter the account ID.For `email`, enter the email address where you want to send alerts. You can enter only one email address for each account.<br />3. If you are configuring more than one consumer account, enter an account and email address for each additional consumer account.<br />4. Save and close the `terraform.tfvars` file. | DevOps engineer |
| Update the main.tf file. | Complete these steps only if you are deploying this solution to more than one consumer account. If you are deploying this solution to only one consumer account, no modification of this file is necessary.1. Open the `main.tf` file.<br />2. For each additional consumer account, create a new module that is based off the `consumer_account_A` module in the template. For each consumer account, for `provider`, the value should match the alias you entered in the `provider.tf` file.<br />3. Save and close the `main.tf` file. | DevOps engineer |

### Deploy the solution by using Terraform
<a name="deploy-the-solution-by-using-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the solution. | In the Terraform CLI, enter the following commands to deploy the AWS resources in the creator and consumer accounts:1. Enter the following command to initialize Terraform.<pre>terraform init</pre><br />2. Enter the following command to validate the Terraform configurations.<pre>terraform validate</pre><br />3. Enter the following command to create a Terraform execution plan.<pre>terraform plan</pre><br />4. Review the configuration changes in the Terraform plan and confirm that you want to implement these changes.<br />5. Enter the following command to deploy the resources.<pre>terraform apply</pre> | DevOps engineer |
| Verify the email address identity. | When you deployed the Terraform plan, Terraform created an email address identity for each consumer account in Amazon SES. Before notifications can be sent to that email address, you must verify the email address. For instructions, see [Verifying an email address identity](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#just-verify-email-proc) in the Amazon SES documentation. | General AWS |

### Validate resource deployment
<a name="validate-resource-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate deployment in the creator account. | 1. Sign in to the creator account.<br />2. In the navigation bar, confirm that are viewing the target AWS Region. If you're in a different Region, choose the name of the currently displayed Region, and then choose the target Region.<br />3. Open the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).<br />4. In the navigation pane, choose **Tables**.<br />5. In the list of tables, validate that the `AmiShare` table is present.<br />6. Open the [Lambda console](https://console.aws.amazon.com/lambda).<br />7. In the navigation pane, choose **Functions**.<br />8. In the list of functions, validate that the `ami-share` function is present.<br />9. Open the [IAM console](https://console.aws.amazon.com/iamv2/).<br />10. In the navigation pane, choose **Roles**.<br />11. In the list of roles, validate that the `external-ddb-role` role is present.<br />12. Open the [EventBridge console](https://console.aws.amazon.com/events/).<br />13. In the navigation pane, choose **Rules**.<br />14. In the list of rules, validate that the `modify_image_attribute_event` rule is present.<br />15. Open the [Amazon SES console](https://console.aws.amazon.com/ses/).<br />16. In the navigation pane, choose **Verified Identities**.<br />17. In the list of identities, validate that an email address identity has been registered and verified for each consumer account. | DevOps engineer |
| Validate deployment in the consumer account. | 1. Sign in to the consumer account.<br />2. In the navigation bar, confirm that are viewing the target AWS Region. If you're in a different Region, choose the name of the currently displayed Region, and then choose the target Region.<br />3. Open the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).<br />4. In the navigation pane, choose **Tables**.<br />5. In the list of tables, validate that the `Mapping` table is present.<br />6. Open the [Lambda console](https://console.aws.amazon.com/lambda).<br />7. In the navigation pane, choose **Functions**.<br />8. In the list of functions, validate that the `ami-usage-function` and `ami-deregister-function` functions are present.<br />9. Open the [EventBridge console](https://console.aws.amazon.com/events/).<br />10. In the navigation pane, choose **Rules**.<br />11. In the list of rules, validate that the `ami_usage_events` and `ami_deregister_events` rules are present. | DevOps engineer |

### Validate monitoring
<a name="validate-monitoring"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AMI in the creator account. | 1. In the creator account, create a private AMI. For instructions, see [Create an AMI from an Amazon EC2 instance](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html).<br />2. Share the new AMI with one of the consumer accounts. For instructions, see [Share an AMI with specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html). | DevOps engineer |
| Use the AMI in the consumer account. | In the consumer account, use the shared AMI to create an Amazon EC2 instance or launch template. For instructions, see [How do I launch an Amazon EC2 instance from a custom AMI](https://repost.aws/knowledge-center/launch-instance-custom-ami) (AWS re:Post Knowledge Center) or [Create a launch template for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html) (Amazon EC2 Auto Scaling documentation). | DevOps engineer |
| Validate monitoring and alerting. | 1. Sign in to the creator account.<br />2. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/).<br />3. In the navigation pane, choose **AMIs**.<br />4. Select the AMI in the list, and then choose **Actions**,** Edit AMI permissions**.<br />5. In the **Shared accounts** section, select the consumer account, and then choose **Remove selected**.<br />6. Choose **Save changes**.<br />7. Validate that the target email address you defined for the consumer account receives a notification that the sharing was canceled for the AMI. | DevOps engineer |

### (Optional) Stop monitoring shared AMIs
<a name="optional-stop-monitoring-shared-amis"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the resources. | 1. Enter the following command to remove the resources deployed by this pattern and stop monitoring shared AMIs.<pre>terraform destroy</pre><br />2. Confirm the `destroy` command by entering `yes`. | DevOps engineer |

## Troubleshooting
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| I did not receive an email alert. | There could be multiple reasons why the Amazon SES email was not sent. Check the following:1. In the [Epics](#monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-epics) section, use the *Validate resource deployment* epic to confirm that the infrastructure was provisioned properly in all AWS accounts.<br />2. Validate the Lambda function events in Amazon CloudWatch Logs. For instructions, see [Using the CloudWatch console](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html#python-logging-cwconsole) in the Lambda documentation. Confirm that there are no permissions issues, such an explicit deny in any identity-based or resource-based policies. For more information, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the IAM documentation.<br />3. In Amazon SES, validate that the status of the email address identity is **Verified**. For more information, see [Verifying an email address identity](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#just-verify-email-proc). |

## Related resources
<a name="monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts-resources"></a>

**AWS documentation**
+ [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html) (Lambda documentation)
+ [Create an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ami.html) (Amazon EC2 documentation)
+ [Share an AMI with specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html) (Amazon EC2 documentation)
+ [Deregister your AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html) (Amazon EC2 documentation)

**Terraform documentation**
+ [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
+ [Terraform Backend Configuration](https://www.terraform.io/language/settings/backends/configuration)
+ [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
+ [Terraform binary download](https://developer.hashicorp.com/terraform/install)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
