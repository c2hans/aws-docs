---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad.html
---

# Remove Amazon EC2 entries in the same AWS account from AWS Managed Microsoft AD by using AWS Lambda automation
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad"></a>

*Dr. Rahul Sharad Gaikwad and Tamilselvan P, Amazon Web Services*

## Summary
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-summary"></a>

Active Directory (AD) is a Microsoft scripting tool that manages domain information and user interactions with network services. It’s widely used among managed services providers (MSPs) to manage employee credentials and access permissions. Because AD attackers can use inactive accounts to try and hack into an organization, it’s important to find inactive accounts and disable them on a routine maintenance schedule. With AWS Directory Service for Microsoft Active Directory, you can run Microsoft Active Directory as a managed service.

This pattern can help you to configure AWS Lambda automation to quickly find and remove inactive accounts. When you use this pattern, you can get the following benefits:
+ Improve database and server performance, and fix vulnerabilities in your security from inactive accounts.
+ If your AD server is hosted in the cloud, removing inactive accounts can also reduce storage costs while improving performance. Your monthly bills might decrease because bandwidth charges and compute resources can both drop.
+ Keep potential attackers at bay with a clean Active Directory.

## Prerequisites and limitations
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Git [installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and configured on a local workstation.
+ Terraform [installed](https://learn.hashicorp.com/tutorials/terraform/install-cli) and configured on a local workstation.
+ Windows computer with Active Directory modules (`ActiveDirectory`).
+ A directory in AWS Managed Microsoft AD and credentials stored in a [parameter in AWS Systems Manager Parameter Store.](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-create-console.html)
+ AWS Identity and Access Management (IAM) role with permissions to the AWS services listed in [Tools](#remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-tools)*. * For more information about IAM, see [Related resources](#remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-resources).

**Limitations**
+ This pattern doesn’t support cross-account setup.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ [Terraform version 1.1.9 or later](https://developer.hashicorp.com/terraform/install)
+ [Terraform AWS Provider version 3.0 or higher](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/version-3-upgrade)

## Architecture
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Process to use Lambda automation to remove EC2 entries from Managed Microsoft AD.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6b50dcc5-4f4b-4eea-85a7-04cebc9f7454/images/b7fc5962-bfb8-4f5a-968e-7487b1d48c4f.png)

The diagram shows the following workflow:

1. Amazon EventBridge triggers the AWS Lambda function based on a cron expression. (For this pattern, the cron expression schedule is once per day.)

1. The required IAM role and policy are created and attached to AWS Lambda through Terraform.

1. The AWS Lambda function is executed and calls to Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling Groups by using the Python boto module. The Lambda function gets the random instance id. The instance id is used to execute AWS Systems Manager commands.

1. AWS Lambda makes another call to Amazon EC2 using the boto module and gets the private IP addresses of the running Windows servers and stores the addresses in a temporary variable.

1. AWS Lambda makes another call to Systems Manager to get the computer information that is connected to Directory Service.

1. An AWS Systems Manager document helps to execute the PowerShell script on Amazon EC2 Windows servers to get the private IP addresses of the computers which are connected with AD.

1. The AD domain username and passwords are stored in the AWS Systems Manager Parameter Store. AWS Lambda and Systems Manager make a call to Parameter Store and get the username and password values to use to connect AD.

1. Using the Systems Manager document, the PowerShell script is executed on the Amazon EC2 Windows server using the instance id obtained earlier in step 3.

1. Amazon EC2 connects Directory Service by using PowerShell commands and removes the computers which are not in use or inactive.

## Tools
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-tools"></a>

**AWS services**
+ [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) provides multiple ways to use Microsoft Active Directory (AD) with other AWS services such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS) for SQL Server, and Amazon FSx for Windows File Server.
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWSresources by controlling who is authenticated and authorized to use them. With IAM, you can specify who or what can access services and resources in AWS, centrally manage fine-grained permissions, and analyze access to refine permissions across AWS.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.
+ [AWS Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) define the actions that Systems Manager performs on your managed instances. Systems Manager includes more than 100 pre-configured documents that you can use by specifying parameters at runtime.
+ [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) is a capability of AWS Systems Manager and provides secure, hierarchical storage for configuration data management and secrets management.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an open source infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.
+ [PowerShell](https://learn.microsoft.com/en-us/powershell/) is a Microsoft automation and configuration management program that runs on Windows, Linux, and macOS.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**C****ode repository**

The code for this pattern is available in the GitHub [Custom AD Cleanup Automation solution](https://github.com/aws-samples/aws-lambda-ad-cleanup-terraform-samples/) repository.

## Best practices
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-best-practices"></a>
+ **Automatically join domains. **When you launch a Windows instance that’s to be part of an Directory Service domain, join the domain during the instance creation process instead of manually adding the instance later. To automatically join a domain, select the correct directory from the **Domain join directory** dropdown list when launching a new instance. For more details, see [Seamlessly join an Amazon EC2 Windows instance to your AWS Managed Microsoft AD Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html) in the *Directory Service Administration Guide*.
+ **Delete unused accounts. **It’s common to find accounts in AD that have never been used. Like disabled or inactive accounts that remain in the system, neglected unused accounts can slow down your AD system or make your organization vulnerable to data breaches.
+ **Automate Active Directory cleanups. **To help mitigate security risks and prevent obsolete accounts from impacting AD performance, conduct AD cleanups should at regular intervals. You can accomplish most AD management and cleanup tasks by writing scripts. Example tasks include removing disabled and inactive accounts, deleting empty and inactive groups, and locating expired user accounts and passwords.

## Epics
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a project folder, and add the files. | To clone the repository and create a project folder, do the following: 1. Open this pattern’s [GitHub repository](https://github.com/aws-samples/aws-lambda-ad-cleanup-terraform-samples/).<br />2. Choose the **Code **button to see the options to clone in the **Clone **dropdown.<br />3. On the **HTTPS** tab, copy the URL provided in **Clone using the web URL**.<br />4. Create a folder on your machine, and name it with your project name.<br />5. Open a terminal in your local machine, and navigate to this folder.<br />6. To clone the git repository, use the following command.<br />`git clone <repository-URL>.git`<br />7. After the repository has been cloned, use the following command to go to the cloned directory. <br />`cd <directory name>`<br />8. In the cloned repository, open this project in an integrated development environment (IDE) of your choice. | DevOps engineer |

### Provision the target architecture by using the Terraform configuration
<a name="provision-the-target-architecture-by-using-the-terraform-configuration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initialize the Terraform configuration. | To initialize your working directory that contains the Terraform files, run the following command.<br />`terraform init` | DevOps engineer |
| Preview changes. | You can preview the changes that Terraform will make to the infrastructure before your infrastructure is deployed. To validate that Terraform will make the changes as required, run the following command.<br />`terraform plan` | DevOps engineer |
| Execute the proposed actions. | To verify that the results from the `terraform plan` command are as expected, do the following:1. Run the following command.<br />`terraform apply`<br />2. Sign in to the AWS Management Console, and verify that the resources are present. | DevOps engineer |
| Clean up the infrastructure. | To clean up the infrastructure that you created, use the following command.<br />`terraform destroy`<br />To confirm the destroy command, type `yes`. | DevOps engineer |

### Verify the deployment
<a name="verify-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Execute and test the Lambda function. | To verify that the deployment occurred successfully, do the following:1. Sign in to the AWS Management Console and open the console. Open the **Functions **page, and select the function name that begins with **ADcleanup-Lambda-\***. <br />2. On the function overview page, choose **Test **on the **Code **tab in the **Code source** section.<br />3. To save the test event, provide a name for the event and choose **Save**. Then to test the event, choose **Test **again.<br />The execution results show the output of the function. | DevOps engineer |
| View the results of the Lambda function. | In this pattern, an EventBridge rule executes the Lambda function once per day. To view the results of the Lambda function, do the following:1. Sign in to the AWS Management Console and open the AWS Lambda console. Open the **Functions** page and select the function name that begins with **ADcleanup-Lambda-\***.<br />2. Choose the **Monitor** tab and choose **View CloudWatch logs**.<br />In the CloudWatch console, the **Log groups** page shows the results of the Lambda function. | DevOps engineer |

### Clean up infrastructure after use
<a name="clean-up-infrastructure-after-use"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up infrastructure. | To clean up the infrastructure that you created, use the following command.<br />`terraform destroy`<br />To confirm the destroy command, type `yes`. | DevOps engineer |
| Verify after cleanup. | Verify that the resources are successfully removed. | DevOps engineer |

## Troubleshooting
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| If you try to remove the AD computer, you get an "Access Denied" message. The AD computer can’t be removed because, by default, the action tries to remove two private IP addresses which are connected as a part of the AD services. | To avoid this error, use the following Python operation to ignore the first two computers when you list the differences between an AD computer output and the output of your machine running Windows.<pre>Difference = Difference[2:]</pre> |
| When Lambda executes a PowerShell script on a Windows server, it expects Active Directory modules to be available by default. If the modules are not available, a Lambda function creates an error that states "Get-AdComputer is not installed on instance". | To avoid this error, install the required modules by using the user data of the EC2 instances. Use the [EC2WindowsUserdata](https://github.com/aws-samples/aws-lambda-ad-cleanup-terraform-samples/blob/main/EC2WindowsUserdata) script that’s in this pattern’s GitHub repository. |

## Related resources
<a name="remove-amazon-ec2-entries-in-the-same-aws-account-from-aws-managed-microsoft-ad-resources"></a>

**AWS documentation**
+ [Amazon EventBridge and AWS Identity and Access Management](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-iam.html)
+ [Configure instance permissions required for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html)
+ [Identity and access management for Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_auth_access.html)
+ [Manually join an Amazon EC2 Windows instance to your AWS Managed Microsoft AD Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_windows_instance.html)
+ [Working with identity-based IAM policies in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-identity-based.html)

**Other resources**
+ [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) (Terraform documentation)
+ [Backend Configuration](https://developer.hashicorp.com/terraform/language/backend) (Terraform documentation)
+ [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) (Terraform documentation)
+ [Python boto module](https://pypi.org/project/boto/) (Python Package Index repository)
+ [Terraform binary download](https://www.terraform.io/downloads) (Terraform documentation)
