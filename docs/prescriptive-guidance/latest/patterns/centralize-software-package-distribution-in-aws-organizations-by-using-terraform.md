---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-software-package-distribution-in-aws-organizations-by-using-terraform.html
---

# Centralize software package distribution in AWS Organizations by using Terraform
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform"></a>

*Pradip kumar Pandey, Chintamani Aphale, T.V.R.L.Phani Kumar Dadi, Pratap Kumar Nanda, Aarti Rajput, and Mayuri Shinde, Amazon Web Services*

## Summary
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform-summary"></a>

Enterprises often maintain multiple AWS accounts that are spread across multiple AWS Regions in order to create a strong isolation barrier between workloads. To stay secure and compliant, their administration teams install agent-based tools such as [CrowdStrike](https://www.crowdstrike.com/falcon-platform/), [SentinelOne](https://www.sentinelone.com/platform/), or [TrendMicro](https://www.trendmicro.com/en_sg/business.html) tools for security scanning, and the [Amazon CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), [Datadog Agent](https://www.datadoghq.com/), or [AppDynamics agents](https://www.appdynamics.com/product/how-it-works/agents-and-controller) for monitoring. These teams often face challenges when they want to centrally automate software package management and distribution across this large landscape.

[Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html), a capability of [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html), automates the process of packaging and publishing software to managed Microsoft Windows and Linux instances across the cloud and on-premises servers through a single simplified interface. This pattern demonstrates how you can use Terraform to further simplify the process of managing the installation of software and to run scripts across a large number of instances and member accounts within AWS Organizations with minimal effort.

This solution works for Amazon, Linux, and Windows instances that are managed by Systems Manager.

## Prerequisites and limitations
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform-prereqs"></a>
+ A [Distributor package](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-create.html) that has the software to be installed
+ [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) version 0.15.0 or later
+ Amazon Elastic Compute Cloud (Amazon EC2) instances that are [managed by Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html) and have basic [permissions to access Amazon Simple Storage Service (Amazon S3](https://repost.aws/knowledge-center/ec2-instance-access-s3-bucket)) in the target account
+ A landing zone for your organization that’s set up by using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
+ (Optional) [Account Factory for Terraform (AFT)](https://catalog.workshops.aws/control-tower/en-US/customization/aft)

## Architecture
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform-architecture"></a>

**Resource details**

This pattern uses [Account Factory for Terraform (AFT) ](https://catalog.workshops.aws/control-tower/en-US/customization/aft)to create all required AWS resources and the code pipeline to deploy the resources in a deployment account. The code pipeline runs in two repositories:
+ **Global customization** contains Terraform code that will run across all accounts registered with AFT.
+ **Account customizations** contains Terraform code that will run in the deployment account.

You can also deploy this solution without using AFT, by running [Terraform](https://developer.hashicorp.com/terraform/intro) commands in the account customizations folder.

The Terraform code deploys the following resources:
+ AWS Identity and Access Management (IAM) role and policies
  + [SystemsManager-AutomationExecutionRole](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-multiple-accounts-regions.html) grants the user permissions to run automations in the target accounts.
  + [SystemsManager-AutomationAdministrationRole](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-multiple-accounts-regions.html) grants the user permissions to run automations in multiple accounts and organizational units (OUs).
+ Compressed files and manifest.json for the package
  + In Systems Manager, a [package](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-create.html) includes at least one .zip file of software or installable assets.
  + The JSON manifest includes pointers to your package code files.
+ S3 bucket
  + The distributed package that is shared across the organization is securely stored in an Amazon S3 bucket.
+ AWS Systems Manager documents (SSM documents)
  + `DistributeSoftwarePackage` contains the logic to distribute the software package to every target instance in the member accounts.
  + `AddSoftwarePackageToDistributor` contains the logic to package the installable software assets and add it to Automation, a capability of AWS Systems Manager.
+ Systems Manager association
  + A Systems Manager association is used to deploy the solution.

**Architecture and workflow**

![Architecture diagram for centralizing software package distribution in AWS Organizations](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/da584449-e12b-4878-a61d-00d8cea3d3d7/images/2718f2c4-f816-4e34-89b8-8182c128e6db.png)

The diagram illustrates the following steps:

1. To run the solution from a centralized account, you upload your packages or software along with deployment steps to an S3 bucket.

1. Your customized package becomes available in the Systems Manager console [Documents](https://ap-southeast-2.console.aws.amazon.com/systems-manager/documents?region=ap-southeast-2) section, in the **Owned by me **tab.

1. State Manager, a capability of Systems Manager, creates, schedules, and runs an association for the package across the organization. The association specifies that the software package must be installed and running on a managed node before it can be installed on the target node.

1. The association instructs Systems Manager to install the package on the target node.

1. For any subsequent installations or changes, users can run the same association periodically or manually from a single location to perform deployments across accounts.

1. In member accounts, Automation sends deployment commands to Distributor.

1. Distributor distributes software packages across instances.

This solution uses the management account within AWS Organizations, but you can also designate an account (delegated administrator) to manage this on behalf of the organization.

## Tools
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform-tools"></a>

**AWS services**
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. This pattern uses Amazon S3 to centralize and securely store the distributed package.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale. This pattern uses the following Systems Manager capabilities:
  + [Distributor ](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html)helps you package and publish software to Systems Manager managed instances.
  + [Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) simplifies common maintenance, deployment, and remediation tasks for many AWS services.
  + [Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) performs actions on your Systems Manager managed instances across your organization and accounts.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.

**Other tools**
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The instructions and code for this pattern are available in the GitHub [Centralized package distribution](https://github.com/aws-samples/aws-organization-centralised-package-distribution) repository.

## Best practices
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform-best-practices"></a>
+ To assign tags to an association, use the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) or the [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html). Adding tags to an association by using the Systems Manager console isn't supported. For more information, see [Tagging Systems Manager resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/tagging-resources.html) in the Systems Manager documentation.
+ To run an association by using a new version of a document shared from another account, set the document version to `default`.
+ To tag only the target node, use one tag key. If you want to target your nodes by using multiple tag keys, use the resource group option.

## Epics
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform-epics"></a>

### Configure source files and accounts
<a name="configure-source-files-and-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | 1. Clone the GitHub [Centralized package distribution](https://github.com/aws-samples/aws-organization-centralised-package-distribution) repository:<pre>git clone https://github.com/aws-samples/aws-organization-centralised-package-distribution</pre><br />2. The Terraform code repository requires two customization folders that are managed by AFT. Confirm that your local copy of the repository contains these folders:<pre>$ cd centralised-package-distribution<br />$ ls<br />global-customization<br />account-customization</pre> | DevOps engineer |
| Update global variables. | Update the following input parameters in the `global-customization/variables.tf` file. These variables apply to all accounts that are created and managed by AFT.+ `account_id`: The ID of the account where the Distributor solution will be deployed.<br />+ `aws_region`: The AWS Region where the association will be deployed. | DevOps engineer |
| Update account variables. | Update the following input parameters in the `account-customization/variables.tf` file. These variables apply only to specific accounts that are created and managed by AFT.+ `package_bucket_name`: The name of the S3 bucket that contains the package distribution file.<br />+ `package_name`: The name of the package distribution file.<br />+ `package_version`: The package version of the installer. | DevOps engineer |

### Customize parameters and deployment files
<a name="customize-parameters-and-deployment-files"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update input parameters for the State Manager association. | Update the following input parameters in the `account-customization/association.tf` file to define the state you want to maintain on your instances. You can use the default parameter values if they support your use case.+ `targetAccounts`: The organizational unit (OU) IDs within AWS Organizations that represent accounts with the target instances for distribution. OU IDs start with "ou".<br />+ `targetRegions`: The AWS Regions (for example, "us-east-1″ or "ap-southeast-2") where the target instances are running.<br />+ `action`:** **Specify whether to install or uninstall the package.<br />+ `installationType`:** **One of the following installation types:`uninstall`: The package is uninstalled.`reinstall`: The application is taken offline until the reinstallation process is complete. `In-place update`: The application is available while new or updated files are added to the installation.<br />+ `name`: The name of the package to install or uninstall.<br />+ `version`:** **The version of the package to install or uninstall. If no version of the package is installed, the system returns an error.<br />+ `bucketName`:** **The S3 bucket name the package has been deployed to. This bucket should consist of the packages and the manifest file only.<br />+ `bucketPrefix`:** **The S3 prefix where the package assets are stored.<br />+ `AutomationAssumeRole`: The Amazon Resource Name (ARN) of `SystemsManager-AutomationAdministrationRole`. | DevOps engineer |
| Prepare compressed files and the `manifest.json` file for the package. | This pattern provides sample PowerShell installable files (.msi for Windows and .rpm for Linux) with install and uninstall scripts in the `account-customization/package` folder.1. Replace the PowerShell installable files with your own files, or provide your installable file, install and uninstall scripts, and manifest file to create a package in the `account-customization` folder in your account.<br />2. Customize the default `manifest.json` file that Terraform generates in the `account-customization` folder according to your requirements. | DevOps engineer |

### Run Terraform commands to provision resources
<a name="run-terraform-commands-to-provision-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initialize the Terraform configuration. | To deploy the solution automatically with AFT, push the code to AWS CodeCommit:<pre>$ git add *<br />$ git commit -m "message"<br />$ git push</pre><br />You can also deploy this solution without using AFT by running a Terraform command from the `account-customization` folder. To initialize the working directory that contains the Terraform files, run:<pre>$ terraform init</pre> | DevOps engineer |
| Preview changes. | To preview the changes that Terraform will make to the infrastructre, run the command:<pre>$ terraform plan</pre><br />This command evaluates the Terraform configuration to determine the desired state of the resources that have been declared. It also compares the desired state with the actual infrastructure to provision within the workspace. | DevOps engineer |
| Apply changes. | Run the following command to implement the changes that you made to the `variables.tf` files:<pre>$ terraform apply</pre> | DevOps engineer |

### Validate resources
<a name="validate-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the creation of SSM documents. | 1. On the [Systems Manager console](https://console.aws.amazon.com/systems-manager/), in the left navigation pane, choose **Documents**.<br />2. Choose the **Owned by me** tab.You should see the `DistributeSoftwarePackage` and `AddSoftwarePackageToDistributor` packages. | DevOps engineer |
| Validate the successful deployment of automations. | 1. On the Systems Manager console, in the left navigation pane, choose **Automation**.<br />2. In the **Automation executions** list, you should see the most recent `DistributeSoftwarePackage` and `AddSoftwarePackageToDistributor` deployments.<br />3. Choose **Execution ID** to validate that they completed successfully. | DevOps engineer |
| Validate that the package deployed to the targeted member account instances. | 1. On the Systems Manager console, in the navigation pane, choose **Run Command**.<br />2. In **Command history**, you will see each invocation and its status.<br />3. Choose any **Command ID** to see the deployment history for each target instance.<br />4. Choose the **Instance ID** and check the **Output** section for the distribution. | DevOps engineer |

## Troubleshooting
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The State Manager association failed or is stuck in pending status. | See the [troubleshooting information](https://repost.aws/knowledge-center/ssm-state-manager-association-fail) in the AWS Knowledge Center. |
| A scheduled association failed to run. | Your schedule specification might be invalid. State Manager doesn't currently support specifying months in cron expressions for associations. Use [cron or rate expressions](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html) to confirm the schedule. |

## Related resources
<a name="centralize-software-package-distribution-in-aws-organizations-by-using-terraform-resources"></a>
+ [Centralized package distribution](https://github.com/aws-samples/aws-organization-centralised-package-distribution) (GitHub repository)
+ [Account Factory for Terraform (AFT)](https://catalog.workshops.aws/control-tower/en-US/customization/aft)
+ [Use cases and best practices](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-best-practices.html) (AWS Systems Manager documentation)
