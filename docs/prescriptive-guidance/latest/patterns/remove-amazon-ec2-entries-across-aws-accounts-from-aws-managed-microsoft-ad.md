---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html
---

# Remove Amazon EC2 entries across AWS accounts from AWS Managed Microsoft AD by using AWS Lambda automation
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad"></a>

*Dr. Rahul Sharad Gaikwad and Tamilselvan P, Amazon Web Services*

## Summary
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad-summary"></a>

Active Directory (AD) is a Microsoft scripting tool that manages domain information and user interactions with network services. It’s widely used among managed services providers (MSPs) to manage employee credentials and access permissions. Because AD attackers can use inactive accounts to try and hack into an organization, it’s important to find inactive accounts and disable them on a routine maintenance schedule. With AWS Directory Service for Microsoft Active Directory, you can run Microsoft Active Directory as a managed service. This pattern can help you to configure AWS Lambda automation to quickly find and remove inactive accounts.

If the following scenarios apply to your organization, this pattern can assist you:
+ **Centralized AD management** – If your organization has multiple AWS accounts, each with its own AD deployment, it can be challenging to manage user accounts and access permissions consistently across all accounts. With an across-accounts AD cleanup solution, you can disable or remove inactive accounts from all AD instances in a centralized manner.
+ **AD restructuring or migration** – If your organization plans to restructure or migrate its AD deployment, an across-accounts AD cleanup solution can help you prepare the environment. The solution can help you remove unnecessary or inactive accounts, simplify the migration process, and reduce potential conflicts or issues.

When you use this pattern, you can get the following benefits:
+ Improve database and server performance, and fix vulnerabilities in your security from inactive accounts.
+ If your AD server is hosted in the cloud, removing inactive accounts can also reduce storage costs while improving performance. Your monthly bills might decrease because bandwidth charges and compute resources can both drop.
+ Keep potential attackers at bay with a clean Active Directory.

## Prerequisites and limitations
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad-prereqs"></a>

**Prerequisites**
+ An active parent AWS account and one or multiple child accounts. In this pattern, a *parent account* is where Active Directory is created. *Child accounts* host Windows servers and are joined through the parent account Active Directory.
+ Git [installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and configured on a local workstation.
+ Terraform [installed](https://learn.hashicorp.com/tutorials/terraform/install-cli) and configured on a local workstation.
+ AWS Managed Microsoft AD directory configured in the parent account and shared to all child accounts. For more details, see [Tutorial: Sharing your AWS Managed Microsoft AD directory for seamless EC2 domain-join](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.html) in the *AWS Directory Service Administration Guide*.
+ A virtual private cloud (VPC) peering connection or AWS Transit Gateway connection available between the VPC of AWS Directory Service (parent account) and the VPC of the Amazon Elastic Compute Cloud (Amazon EC2) instances (child accounts). For more details, see [Configure a VPC peering connection between the directory owner and the directory consumer account](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step1_setup_networking.html#step1_configure_owner_account_vpc) in the *AWS Directory Service Administration Guide*.
+ A Windows machine configured with the `EC2WindowsUserdata` script on all the parent and child accounts. The script file is available in the root of this pattern’s [code repository](https://github.com/aws-samples/aws-lambda-ad-cleanup-terraform-samples/tree/main/multiple-account-cleanup).
+ A cross-account AWS Identity and Access Management (IAM) role available on each child account that’s configured with a trust policy to allow the use of an AWS Lambda function from the parent account. For more information, see [Sending and receiving events between AWS accounts in Amazon EventBridge](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html) in the *Amazon EventBridge User Guide*.
+ The following secrets values available in AWS Systems Manager Parameter Store of the parent account:
  + `domainJoinUser` – Username of the directory service
  + `domainJoinPassword` – Password of the directory service

  For more information about secrets, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.

**Limitations**
+ Creating a resource in a child account isn’t automated with Terraform. You must create the following resources manually by using the AWS Management Console:
  + Amazon EventBridge rule to send the Amazon EC2 termination events to the parent account
  + Amazon EC2 cross-account role creation in the child account with trust policy
  + VPC peering or Transit Gateway connection
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ [Terraform version 1.1.9 or later](https://developer.hashicorp.com/terraform/install)
+ [Terraform AWS Provider version 3.0 or higher](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/version-3-upgrade)

## Architecture
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad-architecture"></a>

The following diagram displays the high-level architecture of the solution.

![Process to use Lambda automation to remove EC2 entries from across AWS accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c397d873-e10d-44b6-8352-5f1380ab94ca/images/bd6c80a7-e490-47db-bd47-165314e1ea8a.png)

The architecture diagram illustrates the following process:

1. In child accounts, the EventBridge rule collects all the Amazon EC2 termination events. The rule sends those events to EventBridge which is present in the parent account.

1. From the parent account, EventBridge collects all the events and contains the rule to trigger the Lambda function `ADcleanup-Lambda`.

1. The parent account receives any termination events from the parent or child account and triggers the Lambda function.

1. The Lambda function makes the call to Amazon EC2 Auto Scaling groups using the Python boto module and gets the random instance ID. The instance ID is used to execute Systems Manager commands.

1. The Lambda function makes another call to Amazon EC2 using the boto module. The Lambda function gets the private IP addresses of the running Windows servers and stores the addresses in a temporary variable. In steps 5.1 and 5.2, the running Windows EC2 instances are collected from child accounts.

1. The Lambda function makes another call to Systems Manager to get the computer information that is connected to AWS Directory Service.

1. An AWS Systems Manager document helps to execute the PowerShell command on Amazon EC2 Windows servers to get the private IP addresses of the computers which are connected to AD. (The Systems Manager document uses the instance ID that was obtained in step 4.)

1. The AD domain username and passwords are stored in the AWS Systems Manager Parameter Store. AWS Lambda and Systems Manager make a call to Parameter Store and get the username and password values to use to connect to AD.

1. Using the Systems Manager document, the PowerShell script is executed on the Amazon EC2 Windows server using the instance id obtained earlier in step 4.

1. Amazon EC2 connects to AWS Directory Service by using PowerShell commands and remove the computers that are not in use or inactive.

## Tools
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad-tools"></a>

**AWS services**
+ [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) provides multiple ways to use Microsoft Active Directory (AD) with other AWS services such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS) for SQL Server, and Amazon FSx for Windows File Server.
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them. With IAM, you can specify who or what can access services and resources in AWS, centrally manage fine-grained permissions, and analyze access to refine permissions across AWS.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.
+ [AWS Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) define the actions that Systems Manager performs on your managed instances. Systems Manager includes more than 100 pre-configured documents that you can use by specifying parameters at runtime.
+ [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) is a capability of AWS Systems Manager and provides secure, hierarchical storage for configuration data management and secrets management.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.
+ [PowerShell](https://learn.microsoft.com/en-us/powershell/) is a Microsoft automation and configuration management program that runs on Windows, Linux, and macOS.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [aws-lambda-ad-cleanup-terraform-samples](https://github.com/aws-samples/aws-lambda-ad-cleanup-terraform-samples/tree/main/multiple-account-cleanup) repository.

## Best practices
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad-best-practices"></a>
+ **Automatically join domains. **When you launch a Windows instance that’s to be part of an Directory Service domain, join the domain during the instance creation process instead of manually adding the instance later. To automatically join a domain, select the correct directory from the **Domain join directory** dropdown list when launching a new instance. For more details, see [Seamlessly join an Amazon EC2 Windows instance to your AWS Managed Microsoft AD Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html) in the *Directory Service Administration Guide*.
+ **Delete unused accounts. **It’s common to find accounts in AD that have never been used. Like disabled or inactive accounts that remain in the system, neglected unused accounts can slow down your AD system or make your organization vulnerable to data breaches.
+ **Automate Active Directory cleanups. **To help mitigate security risks and prevent obsolete accounts from impacting AD performance, conduct AD cleanups should at regular intervals. You can accomplish most AD management and cleanup tasks by writing scripts. Example tasks include removing disabled and inactive accounts, deleting empty and inactive groups, and locating expired user accounts and passwords.

## Epics
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad-epics"></a>

### Set up child accounts
<a name="set-up-child-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a cross-account role in the child account. | To create a cross-account role in a child account, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html) | DevOps engineer |
| Create an event rule in the child account. | To create an EventBridge rule for each child account, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html)<br />For more details, see [Creating rules that react to events in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the* Amazon EventBridge User Guide*. | DevOps engineer |
| Create an EC2 instance and join to AD. | To create an EC2 instance for Windows, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html) | DevOps engineer |

### Set up the local workstation
<a name="set-up-the-local-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a project folder and add the files. | To clone the repository and create a project folder, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html) | DevOps engineer |
| Build the `adcleanup.zip` file. | To compress the `lambda_function.py` file, run the following command:<br />`zip -r adcleanup.zip lambda_function.py` | DevOps engineer |

### Provision the target architecture using the Terraform configuration
<a name="provision-the-target-architecture-using-the-terraform-configuration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provide values for the Terraform variables. | For the child account, provide values for the following `arn` variables as string types in the `terraform.tfvars` file:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html) | DevOps engineer |
| Initialize the Terraform configuration. | To initialize your working directory that contains the Terraform files, run the following command:<br />`terraform init` | DevOps engineer |
| Preview changes. | You can preview the changes that Terraform will make to the infrastructure before your infrastructure is deployed. To validate that Terraform will make the changes as required, run the following command:<br />`terraform plan —-var-file=examples/terraform.tfvars` | DevOps engineer |
| Execute the proposed actions. | To verify that the results from the `terraform plan` command are as expected, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html) | DevOps engineer |

### Verify the deployment
<a name="verify-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Execute and test the Lambda function. | To verify that the deployment occurred successfully, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html)<br />The execution results show the output of the function. | DevOps engineer |
| View results of EventBridge rule execution from parent account. | To view the results of the EventBridge rule that’s based on Amazon EC2 termination events from the parent account, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html)<br />In the CloudWatch console, the **Log groups** page shows the results of the Lambda function. | DevOps engineer |
| View results of EventBridge rule execution from the child account. | To view the results of the EventBridge rule that’s based on Amazon EC2 termination events from the child account, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad.html)<br />In the CloudWatch console, the **Log groups** page shows the results of the Lambda function. | DevOps engineer |

### Clean up infrastructure after use
<a name="clean-up-infrastructure-after-use"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up the infrastructure. | To clean up the infrastructure that you created, use the following command:<br />`terraform destroy`<br />To confirm the `destroy` command, type `yes`. | DevOps engineer |
| Verify after cleanup. | Verify that the resources are successfully removed. | DevOps engineer |

## Troubleshooting
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Connection issue between AWS Directory Service (parent account) and Amazon EC2 instance (child account) – You are unable to join the child account’s computers to AD even though VPC peering is available. | Add routing in the VPCs. For instructions, see [Configure a VPC peering connection between the directory owner and the directory consumer account](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step1_setup_networking.html#step1_configure_owner_account_vpc) in the AWS Directory Service documentation. |

## Related resources
<a name="remove-amazon-ec2-entries-across-aws-accounts-from-aws-managed-microsoft-ad-resources"></a>

**AWS documentation**
+ [Amazon EventBridge and AWS Identity and Access Management](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-iam.html)
+ [Configure instance permissions required for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html)
+ [Identity and access management for Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_auth_access.html)
+ [Identity-based IAM policies for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-identity-based.html)
+ [Manually join an Amazon EC2 Windows instance to your AWS Managed Microsoft AD Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_windows_instance.html)
+ [Remove Amazon EC2 entries in the same AWS account from AWS Managed Microsoft AD by using AWS Lambda automation](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad.html)

**Other resources**
+ [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) (Terraform documentation)
+ [Backend Configuration](https://developer.hashicorp.com/terraform/language/backend) (Terraform documentation)
+ [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) (Terraform documentation)
+ [Python boto module](https://pypi.org/project/boto/) (Python Package Index repository)
+ [Terraform binary download](https://www.terraform.io/downloads) (Terraform documentation)
