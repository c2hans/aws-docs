---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge.html
---

# Automatically back up SAP HANA databases using Systems Manager and EventBridge
<a name="automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge"></a>

*Ambarish Satarkar and Gaurav Rath, Amazon Web Services*

## Summary
<a name="automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge-summary"></a>

This pattern describes how to automate SAP HANA database backups using AWS Systems Manager, Amazon EventBridge, Amazon Simple Storage Service (Amazon S3), and AWS Backint Agent for SAP HANA.

This pattern provides a shell script-based approach using the `BACKUP DATA` command and removes the need to maintain scripts and job configurations for each operating system (OS) instance across numerous systems.

|
|
| Note: As of April 2023, AWS Backup announced support for SAP HANA databases on Amazon Elastic Compute Cloud (Amazon EC2). For more information, see [SAP HANA databases on Amazon EC2 instances backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-saphana.html).Based on your organization’s needs, you can use the AWS Backup service to automatically back up your SAP HANA databases or you can use this pattern. |
| --- |

## Prerequisites and limitations
<a name="automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge-prereqs"></a>

**Prerequisites **
+ An existing SAP HANA instance with a supported release in running state on a managed Amazon Elastic Compute Cloud (Amazon EC2) instance that is configured for Systems Manager
+ Systems Manager Agent (SSM Agent) 2.3.274.0 or later installed
+ An S3 bucket that doesn’t have public access enabled
+ An `hdbuserstore` key named `SYSTEM`
+ An AWS Identity and Access Management (IAM) role for the Automation runbook to run on schedule
+ `AmazonSSMManagedInstanceCore` and `ssm:StartAutomationExecution` policies are attached to Systems Manager Automation service role.

**Limitations **
+ AWS Backint Agent for SAP HANA doesn't support deduplication.
+ AWS Backint Agent for SAP HANA doesn't support data compression.

**Product versions**

AWS Backint Agent is supported on the following operating systems:
+ SUSE Linux Enterprise Server
+ SUSE Linux Enterprise Server for SAP
+ Red Hat Enterprise Linux for SAP

AWS Backint Agent supports the following databases:
+ SAP HANA 1.0 SP12 (single node and multiple nodes)
+ SAP HANA 2.0 and later (single node and multiple nodes)

## Architecture
<a name="automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge-architecture"></a>

**Target technology stack**
+ AWS Backint Agent
+ Amazon S3
+ AWS Systems Manager
+ Amazon EventBridge
+ SAP HANA

**Target architecture**

The following diagram shows the installation scripts that install AWS Backint Agent, the S3 bucket, and Systems Manager and EventBridge, which use a Command document to schedule regular backups.

![Workflow for scheduling regular backups.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0aa22a27-d100-483d-95f9-c3101f40402c/images/201d2b9a-b88e-4432-82cd-240b81da981e.png)

**Automation and scale**
+ Multiple AWS Backint Agents can be installed by using a Systems Manager Automation runbook.
+ Each run of the Systems Manager runbook can scale to *n* number of SAP HANA instances, based on target selection.
+ EventBridge can automate SAP HANA backups.

## Tools
<a name="automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge-tools"></a>
+ [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-sap-hana.html) is a standalone application that integrates with your existing workflows to back up your SAP HANA database to an S3 bucket that you specify in the configuration file. AWS Backint Agent supports full, incremental, and differential backups of SAP HANA databases. It runs on an SAP HANA database server, where backups and catalogs are transferred from the SAP HANA database to the AWS Backint Agent.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that you can use to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your applications, software as a service (SaaS) applications, and AWS services to targets such as AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other accounts.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is an object storage service. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources.

**Code**

The code for this pattern is available in the [aws-backint-automated-backup](https://github.com/aws-samples/aws-backint-automated-backup) GitHub repository.

## Epics
<a name="automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge-epics"></a>

### Create an hdbuserstore key SYSTEM
<a name="create-an-hdbuserstore-key-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an hdbuserstore key. | 1. Navigate to `/usr/sap/<SID>/HDB<Inst No>/exe`.<br />2. Run the following command, with `XX` as the SAP HANA database instance number.<pre>hdbuserstore -i set SYSTEM <hostname>:3XX13@SYSTEMDB SYSTEM </pre><br />For example,  for an SAP HANA host `saphanadb` with instance number `00`, run the following command.<pre>hdbuserstore -i set SYSTEM saphanadb:30013@SYSTEMDB SYSTEM</pre> | AWS administrator, SAP HANA Administrator |

### Install AWS Backint Agent
<a name="install-aws-backint-agent"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS Backint Agent. | Follow the instructions in [Install and configure AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-installing-configuring.html) in the AWS Backint Agent documentation. | AWS administrator, SAP HANA administrator |

### Create the Systems Manager Command document
<a name="create-the-systems-manager-command-document"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Systems Manager Command document. | 1. Sign in to the AWS Management Console and open the AWS Systems Manager Console.<br />2. Choose **Documents,** and choose **Owned by me**.<br />3. Confirm that you are in the same AWS Region as your SAP HANA database.<br />4. Choose **Create document**,** Command or session** to create your document. <br />5. Use a unique and descriptive name, with no spaces (for example, **SAP HANA-Backup**).<br />6. Make sure that **Document type** is set to **Command document**. <br />7. Under the **Content** header, there is some sample code. Make sure that you choose the **JSON** code type, and replace the code with the code from the `HDB_Backup_SSM_Document.json` file from the [GitHub repository](https://github.com/aws-samples/aws-backint-automated-backup).<br />8. Choose **Create document**.<br />9. Check your document in the **Owned by me **section. | AWS administrator, SAP HANA administrator |

### Schedule backups on a regular frequency
<a name="schedule-backups-on-a-regular-frequency"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Schedule regular backups using Amazon EventBridge. | 1. Open the Amazon EventBridge** **console, choose **Rules**, and choose **Create rule**.<br />2. On the **Define rule detail** screen, enter a unique name and description for your rule, and use the default event bus.<br />3. Under **Rule type**, choose **Schedule**, and choose **Next**.<br />4. On then **Define schedule** screen, choose the appropriate schedule pattern and cron or rate expression based on the required frequency.<br />5. On the **Select targets** screen, for **Target type**, choose **AWS service**. Under **Select a target**, choose **Systems Manager Run Command**.<br />6. Choose the document that you created earlier.<br />7. Under **Target key** and **Target value**, provide the instance ID. You can use tag names and tag values to add multiple instances.<br />8. Under **Configure automation parameters**, choose **Constant** for incremental or differential backups. If you want full backup, choose **No Parameters**.<br />9. Choose whether to create a new role or to use an existing role. If you use an existing role, make sure that it has the policies required to invoke the target.<br />10. Keep the default additional settings, and choose **Next**.<br />11. The **Configure tags** screen is optional. Choose **next**.<br />12. On the **Review and create** screen, review the rule settings, and choose **Create**. The rule should be successfully created.You can verify backup success from the S3 bucket path.  <pre> s3:/<your_bucket_name>/<target folder>/<SID>/usr/sap/<SID>/SYS/global/hdb/backint/DB_<SID>/</pre><br />You can also verify backups from the SAP HANA backup catalog. | AWS administrator, SAP HANA administrator |

## Related resources
<a name="automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge-resources"></a>
+ [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-sap-hana.html)
+ [Install and configure AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-installing-configuring.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
