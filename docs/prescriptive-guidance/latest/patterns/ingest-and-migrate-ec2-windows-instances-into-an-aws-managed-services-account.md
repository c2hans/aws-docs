---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ingest-and-migrate-ec2-windows-instances-into-an-aws-managed-services-account.html
---

# Ingest and migrate EC2 Windows instances into an AWS Managed Services account
<a name="ingest-and-migrate-ec2-windows-instances-into-an-aws-managed-services-account"></a>

*Anil Kunapareddy and Venkatramana Chintha, Amazon Web Services*

## Summary
<a name="ingest-and-migrate-ec2-windows-instances-into-an-aws-managed-services-account-summary"></a>

This pattern explains the step-by-step process of migrating and ingesting Amazon Elastic Compute Cloud (Amazon EC2) Windows instances into an Amazon Web Services (AWS) Managed Services (AMS) account. AMS can help you manage the instance more efficiently and securely. AMS provides operational flexibility, enhances security and compliance, and helps you optimize capacity and reduce costs.

This pattern starts with an EC2 Windows instance that you have migrated to a staging subnet in your AMS account. A variety of migration services and tools are available to perform this task, such as AWS Application Migration Service.

To make a change to your AMS-managed environment, you create and submit a request for change (RFC) for a particular operation or action. Using an AMS workload ingest (WIGS) RFC, you ingest the instance into the AMS account and create a custom Amazon Machine Image (AMI). You then create the AMS-managed EC2 instance by submitting another RFC to create an EC2 stack. For more information, see [AMS Workload Ingest](https://docs.aws.amazon.com/managedservices/latest/appguide/ams-workload-ingest.html) in the AMS documentation.

## Prerequisites and limitations
<a name="ingest-and-migrate-ec2-windows-instances-into-an-aws-managed-services-account-prereqs"></a>

**Prerequisites**
+ An active, AMS-managed AWS account
+ An existing landing zone
+ Permissions to make changes in the AMS-managed VPC
+ An Amazon EC2 Windows instance in a staging subnet in your AMS account
+ Completion of the [general prerequisites](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-instance-prereqs.html) for migrating workloads using AMS WIGS
+ Completion of the [Windows prerequisites](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-prereqs-win.html) for migrating workloads using AMS WIGS

**Limitations**
+ This pattern is for EC2 instances operating Windows Server. This pattern doesn’t apply to instances running other operating systems, such as Linux.

## Architecture
<a name="ingest-and-migrate-ec2-windows-instances-into-an-aws-managed-services-account-architecture"></a>

**Source technology stack**

Amazon EC2 Windows instance in a staging subnet in your AMS account

**Target technology stack**

Amazon EC2 Windows instance managed by AWS Managed Services (AMS)

**Target architecture**

![Process to migrate and ingest Amazon EC2 Windows instances into an AWS Managed Services account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/393c21cb-b6c6-4446-b597-b62e29fdb7f8/images/0b2fa855-7460-49f8-9e7f-3485e6ce1745.png)

## Tools
<a name="ingest-and-migrate-ec2-windows-instances-into-an-aws-managed-services-account-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can use Amazon EC2 to launch as many or as few virtual servers as you need, and you can scale out or scale in.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Managed Services (AMS)](https://docs.aws.amazon.com/managedservices/?id=docs_gateway) helps you operate more efficiently and securely by providing ongoing management of your AWS infrastructure, including monitoring, incident management, security guidance, patch support, and backup for AWS workloads.

**Other services**
+ [PowerShell](https://learn.microsoft.com/en-us/powershell/) is a Microsoft automation and configuration management program that runs on Windows, Linux, and macOS.

## Epics
<a name="ingest-and-migrate-ec2-windows-instances-into-an-aws-managed-services-account-epics"></a>

### Configure settings on the instance
<a name="configure-settings-on-the-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Change the DNS Client settings. | 1. On the source EC2 instance, open Command Prompt as an administrator, type `gpedit.msc`, and then press **Enter**.<br />2. In the Local Group Policy Editor, navigate to **Computer Configuration**, **Administrative Templates**,**Network**, **DNS Client**.<br />3. For **Primary DNS suffix**, choose **Not configured**.<br />4. For **Primary DNS suffix devolution**, choose **Not configured**.  | Migration engineer |
| Change the Windows Update settings. | 1. In the Local Group Policy Editor, navigate to **Computer Configuration**, **Administrative Templates**, **Windows Components**, **Windows Update**.<br />2. For **Specify intranet Microsoft update service location**, choose **Not configured**.<br />3. For **Configure Automatic Updates**, choose **Not configured**.<br />4. For **Automatic Updates detection frequency**, choose **Not configured**.<br />5. Close the Local Group Policy Editor. | Migration engineer |
| Enable the firewall. | 1. On the source EC2 instance, open Command Prompt as an administrator, type `services.msc`, and then press **Enter**.<br />2. In Windows Services, enable **Firewall**.<br />3. Close Windows Services. | Migration engineer |

### Prepare the instance for AMS WIGS
<a name="prepare-the-instance-for-ams-wigs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up and prepare the instance. | 1. Using a bastion host and local credentials, create a Remote Desktop Protocol (RDP) connection to the EC2 instance in the staging subnet.<br />2. Remove all legacy software, antivirus software, and backup solutions that aren’t required in AMS.  | Migration engineer |
| Repair the sppnp.dll file. | 1. Go to `C:\Windows\System32\sppnp.dll`.<br />2. Rename `sppnp.dll` to` sppnp_old.dll`.<br />3. Using PowerShell and administrator credentials, enter the following commands:<pre>dism /online /cleanup-image /restorehealth<br />sfc /scannnow</pre><br />4. Restart the EC2 Windows instance. | Migration engineer |
| Run the pre-WIG validation script. | 1. Download the Windows WIGS Pre-ingestion Validation zip file (`windows-prewings-valication.zip`) from [Migrating workloads: Windows pre-ingestion validation](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-instance-win-validation.html) in the AMS documentation.<br />2. Run the Windows pre-WIG validation script and verify the results.<br />3. If the validation fails, fix the issue, and rerun the validation script until the validation succeeds. | Migration engineer |
| Create the failsafe AMI. | After the pre-WIG validation passes, create a pre-ingestion AMI as follows:1. Choose **Deployment**, **Advanced stack components**, **AMI**, **Create**.<br />2. During creation, add a tag `Key=Name, Value=APPLICATION-ID_IngestReady`.<br />3. Wait until AMI is created before proceeding.<br />For more information, see [AMI \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-ami-create.html) in the AMS documentation. | Migration engineer |

### Ingest and validate the instance
<a name="ingest-and-validate-the-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Submit the RFC to create the workload ingest stack. | Submit a request for change (RFC) to start the AMS WIGS. For instructions, see [Workload Ingest Stack: Creating](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-workload-ingest-col.html) in the AMS documentation. This starts the workload ingestion and installs all the software required by AMS, including backup tools, Amazon EC2 management software, and antivirus software. | Migration engineer |
| Validate successful migration. | After the workload ingestion is complete, you can see the AMS-managed instance and AMS-ingested AMI.1. Log in to the AMS-managed instance with domain credentials.<br />2. Validate the domain joining as follows:In Windows Explorer, right-click **This PC**, and then choose **Properties**.In the Device Specification section, confirm that the domain appears in the **Full device name**.<br />3. Validate the source and target disk drives. | Migration engineer |

### Launch the instance in the target AMS account
<a name="launch-the-instance-in-the-target-ams-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Submit the RFC to create an EC2 stack. | 1. Using the AMS-ingested AMI of the Windows instance, prepare an RFC for an EC2 stack according to the instructions in [Create EC2 stack instance](https://docs.aws.amazon.com/managedservices/latest/ctexguide/ex-ec2-create-col.html) in AMS documentation. In the EC2 stack RFC, provide all the parameters, including the server name, tags, target VPC, target subnet, instance type, target security groups, ingestion AMI, and role.<br />2. Submit the RFC for the EC2 stack, and then wait for the instance to be successfully created. | Migration engineer |

## Related resources
<a name="ingest-and-migrate-ec2-windows-instances-into-an-aws-managed-services-account-resources"></a>

**AWS Prescriptive Guidance**
+ [Automate pre-workload ingestion activities for AWS Managed Services on Windows](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-pre-workload-ingestion-activities-for-aws-managed-services-on-windows.html)
+ [Automatically create an RFC in AMS using Python](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-create-an-rfc-in-ams-using-python.html?did=pg_card&trk=pg_card)

**AMS documentation**
+ [AMS Workload Ingest](https://docs.aws.amazon.com/managedservices/latest/appguide/ams-workload-ingest.html)
+ [How Migration Changes Your Resource](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-changes.html)
+ [Migrating Workloads: Standard Process](https://docs.aws.amazon.com/managedservices/latest/appguide/mp-migrate-stack-process.html)

**Marketing resources**
+ [AWS Managed Services](https://aws.amazon.com/managed-services/)
+ [AWS Managed Services FAQs](https://aws.amazon.com/managed-services/faqs/)
+ [AWS Managed Services Resources](https://aws.amazon.com/managed-services/resources/)
+ [AWS Managed Services Features](https://aws.amazon.com/managed-services/features/)
