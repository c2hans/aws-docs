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
| Create an hdbuserstore key. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge.html) | AWS administrator, SAP HANA Administrator |

### Install AWS Backint Agent
<a name="install-aws-backint-agent"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS Backint Agent. | Follow the instructions in [Install and configure AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-installing-configuring.html) in the AWS Backint Agent documentation. | AWS administrator, SAP HANA administrator |

### Create the Systems Manager Command document
<a name="create-the-systems-manager-command-document"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Systems Manager Command document. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge.html) | AWS administrator, SAP HANA administrator |

### Schedule backups on a regular frequency
<a name="schedule-backups-on-a-regular-frequency"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Schedule regular backups using Amazon EventBridge. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge.html)You can verify backup success from the S3 bucket path.  <pre> s3:/<your_bucket_name>/<target folder>/<SID>/usr/sap/<SID>/SYS/global/hdb/backint/DB_<SID>/</pre><br />You can also verify backups from the SAP HANA backup catalog. | AWS administrator, SAP HANA administrator |

## Related resources
<a name="automatically-back-up-sap-hana-databases-using-systems-manager-and-eventbridge-resources"></a>
+ [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-sap-hana.html)
+ [Install and configure AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-installing-configuring.html)
