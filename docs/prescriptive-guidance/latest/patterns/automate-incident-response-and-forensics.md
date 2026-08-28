---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-incident-response-and-forensics.html
---

# Automate incident response and forensics
<a name="automate-incident-response-and-forensics"></a>

*Lucas Kauffman and Tomek Jakubowski, Amazon Web Services*

## Summary
<a name="automate-incident-response-and-forensics-summary"></a>

This pattern deploys a set of processes that use AWS Lambda functions to provide the following:
+ A way to initiate the incident-response process with minimum knowledge
+ Automated, repeatable processes that are aligned with the *AWS Security Incident Response Guide*
+ Separation of accounts to operate the automation steps, store artifacts, and create forensic environments

The Automated Incident Response and Forensics framework follows a standard digital forensic process consisting of the following phases:

1. Containment

1. Acquisition

1. Examination

1. Analysis

You can perform investigations on static data (for example, acquired memory or disk images) and on dynamic data that is live but on separated systems.

For more details, see the [Additional information](#automate-incident-response-and-forensics-additional) section.

## Prerequisites and limitations
<a name="automate-incident-response-and-forensics-prereqs"></a>

**Prerequisites **
+ Two AWS accounts:
  + Security account, which can be an existing account, but is preferably new
  + Forensics account, preferably new
+ AWS Organizations set up
+ In the Organizations member accounts:
  + The Amazon Elastic Compute Cloud (Amazon EC2) role must have Get and List access to Amazon Simple Storage Service (Amazon S3) and be accessible by AWS Systems Manager. We recommend using the `AmazonSSMManagedInstanceCore` AWS managed role. Note that this role will automatically be attached to the Amazon EC2 instance when incident response is initiated. After the response has finished, AWS Identity and Access Management (IAM) will remove all rights to the instance.
  + Virtual private cloud (VPC) endpoints in the AWS member account and in the Incident Response and Analysis VPCs. Those endpoints are: S3 Gateway, EC2 Messages, SSM, and SSM Messages.
+ AWS Command Line Interface (AWS CLI) installed on the Amazon EC2 instances. If the Amazon EC2 instances don’t have AWS CLI installed, internet access will be required for the disk snapshot and memory acquisition to work. In this case, the scripts will reach out to the internet to download the AWS CLI installation files and will install them on the instances.

**Limitations **
+ This framework does not intend to generate artifacts that can be considered as electronic evidence, submissible in court.
+ Currently, this pattern supports only Linux based instances running on x86 architecture.

## Architecture
<a name="automate-incident-response-and-forensics-architecture"></a>

**Target architecture **

In addition to the member account, the target environment consists of two main accounts: a Security account and a Forensics account. Two accounts are used for the following reasons:
+ To separate them from any other customer accounts to reduce blast radius in case of a failed forensic analysis
+ To help ensure the isolation and protection of the integrity of the artifacts being analyzed
+ To keep the investigation confidential
+ To avoid situations where the threat actors might have used all the resources immediately available to your compromised AWS account by hitting service quotas and so preventing you from instantiating an Amazon EC2 instance to perform investigations.

Also, having separate Security and Forensics accounts allows for creating separate roles—a Responder for acquiring evidence and an Investigator for analyzing it. Each role would have access to its separate account.

The following diagram shows only the interaction between the accounts. Details of each account are shown in subsequent diagrams, and a complete diagram is attached.

![Interaction between member, security, and forensics accounts and users, the internet, and Slack.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7fc94597-d82d-4f6d-9c8b-5e0060010c53/images/6ed33293-d198-4458-9e38-74f6d20629c9.png)

The following diagram shows the member account.

![Member account with AWS KMS key, IAM roles, Lambda functions, endpoints, VPC with two EC2 instances.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7fc94597-d82d-4f6d-9c8b-5e0060010c53/images/464fcefa-1418-4c9e-9902-5050a76ba9b9.png)

1. An event is sent to the Slack Amazon Simple Notification Service (Amazon SNS) topic.

The following diagram shows the Security account.

![Security account with EC2DdCopyInstance in the incident response VPC and with LiME memory modules.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7fc94597-d82d-4f6d-9c8b-5e0060010c53/images/89dda7a1-972a-403e-abf8-98fc422422b2.png)

2. The Amazon SNS topic in the Security account initiates Forensics events.

The following diagram shows the Forensics account.

![Forensics account with forensics and victim EC2 instances, an Analysis VPC, and a Maintenance VPC.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7fc94597-d82d-4f6d-9c8b-5e0060010c53/images/da3bcfcc-cdca-4875-ada5-6131e8b666bc.png)

The Security account is where the two main AWS Step Functions workflows are created for memory and disk image acquisition. After the workflows are running, they access the member account that has the Amazon EC2 instances involved in an incident, and they initiate a set of Lambda functions that will gather a memory dump or a disk dump. Those artifacts are then stored in the Forensics account.

The Forensics account will hold the artifacts gathered by the Step Functions workflow in the Analysis artifacts Amazon S3 bucket. The Forensics account will also have an Amazon EC2 Image Builder pipeline that builds an Amazon Machine Image (AMI) of a Forensics instance. Currently, the image is based on SANS SIFT Workstation.

The build process uses the Maintenance VPC, which has connectivity to the internet. The image can be later used for spinning up the Amazon EC2 instance for analysis of the gathered artifacts in the Analysis VPC.

The Analysis VPC does not have internet connectivity. By default, the pattern creates three private analysis subnets. You can create up to 200 subnets, which is the quota for the number of subnets in a VPC, but the VPC endpoints need to have those subnets added for AWS Systems Manager Session Manager to automate running commands in them.

From a best-practices perspective, we recommend using AWS CloudTrail and AWS Config to do the following:
+ Track changes made in your Forensics account
+ Monitor access and integrity of the artifacts that are stored and analyzed

**Workflow**

The following diagram shows the key steps of a workflow that includes the process and decision tree from when an instance is compromised until it is analyzed and contained.

1. Has the `SecurityIncidentStatus`tag been set with the value Analyze? If yes, do the following:

   1. Attach the correct IAM profiles for AWS Systems Manager and Amazon S3.

   1. Send an Amazon SNS message to the Amazon SNS queue in Slack.

   1. Send an Amazon SNS message to the` SecurityIncident` queue.

   1. Invoke the Memory and Disk Acquisition state machine.

1. Have memory and disk been acquired? If no, there is an error.

1. Tag the Amazon EC2 instance with the `Contain` tag.

1. Attach the IAM role and security group to fully isolate the instance.

![Workflow steps listed previously.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7fc94597-d82d-4f6d-9c8b-5e0060010c53/images/b319bd9b-8cb4-4048-b5c8-6e39e72908b0.png)

**Automation and scale**

The intent of this pattern is to provide a scalable solution to perform incident response and forensics across several accounts within a single AWS Organizations organization.

## Tools
<a name="automate-incident-response-and-forensics-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool for interacting with AWS services through commands in your command-line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/index.html) helps you create and control cryptographic keys to protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. It also helps you check your AWS environment against security industry standards and best practices.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.

**Code **

For the code and specific implementation and usage guidance, see the GitHub [Automated Incident Response and Forensics Framework](https://github.com/awslabs/aws-automated-incident-response-and-forensics) repository.

## Epics
<a name="automate-incident-response-and-forensics-epics"></a>

### Deploy the CloudFormation templates
<a name="deploy-the-cfnshort-templates"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy CloudFormation templates. | The CloudFormation templates are marked 1 through 7 with the first word of the script name indicating in which account the template needs to be deployed. Note that the order of launching the CloudFormation templates is important.+ `1-forensic-AnalysisVPCnS3Buckets.yaml`: Deployed in the forensics account. It creates the Amazon S3 buckets and the Analysis VPC, and it activates CloudTrail.<br />+ `2-forensic-MaintenanceVPCnEC2ImageBuilderPipeline.yaml`: Deploys the maintenance VPC and image builder pipeline based on SANS SIFT.<br />+ `3-security_IR-Disk_Mem_automation.yaml`: Deploys the functions in the security account that enable disk and memory acquisition.<br />+ `4-security_LiME_Volatility_Factory.yaml`: Initiates a build function to start creating the memory modules based on the given AMI IDs. Note that AMI IDs are different across AWS Regions. Whenever you need new memory modules, you can rerun this script with the new AMI IDs. Consider integrating this with your golden image AMI builder pipelines (if used in your environment).<br />+ `5-member-IR-automation.yaml`: Creates the member incident-response automation function, which initiates the incident-response process. It allows sharing Amazon Elastic Block Store (Amazon EBS) volumes across accounts, automated posting to Slack channels during the incident-response process, initiating the forensics process, and isolating the instances after the process finishes.<br />+ `6-forensic-artifact-s3-policies.yaml`: After all the scripts have been deployed this script fixes the permissions required for all the cross-account interactions.<br />+ `7-security-IR-vpc.yaml`: Configures a VPC used for incident response volume processing.<br />To initiate the incident response framework for a specific Amazon EC2 instance, create a tag with the key `SecurityIncidentStatus` and the value `Analyze`. This will initiate the member Lambda function that will automatically start isolation and memory as well as disk acquisition. | AWS administrator |
| Operate the framework. | The Lambda function will also retag the asset at the end (or on failure) with `Contain`. This initiates the containment, which fully isolates the instance with a no INBOUND/OUTBOUND security group and with an IAM role that disallows all access.<br />Follow the steps in the [GitHub repository](https://github.com/awslabs/aws-automated-incident-response-and-forensics#operating-the-incident-response-framework). | AWS administrator |

### Deploy custom Security Hub CSPM actions
<a name="deploy-custom-ash-actions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the custom Security Hub CSPM actions by using a CloudFormation template. | To create a custom action so that you can use the dropdown list from Security Hub CSPM, deploy the `Modules/SecurityHub Custom Actions/SecurityHubCustomActions.yaml` CloudFormation template. Then modify the `IRAutomation` role in each of the member accounts to allow the Lambda function that runs the action to assume the `IRAutomation` role. For more information, see the [GitHub repository](https://github.com/awslabs/aws-automated-incident-response-and-forensics#securityhub-actions). | AWS administrator |

## Related resources
<a name="automate-incident-response-and-forensics-resources"></a>
+ [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)

## Additional information
<a name="automate-incident-response-and-forensics-additional"></a>

By using this environment, a Security Operations Center (SOC) team can improve their security incident response process through the following:
+ Having the ability to perform forensics in a segregated environment to avoid accidental compromise of production resources
+ Having a standardized, repeatable, automated process to do containment and analysis.
+ Giving any account owner or administrator the ability to initiate the incident-response process with the minimal knowledge of how to use tags
+ Having a standardized, clean environment for performing incident analysis and forensics without the noise of a larger environment
+ Having the ability to create multiple analysis environments in parallel
+ Focusing SOC resources on incident response instead of on maintenance and documentation of a cloud forensics environment
+ Moving away from a manual process toward an automated one to achieve scalability
+ Using CloudFormation templates for consistency and to avoid repeatable tasks

Additionally, you avoid using persistent infrastructure, and you pay for resources when you need them.

## Attachments
<a name="attachments-7fc94597-d82d-4f6d-9c8b-5e0060010c53"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/7fc94597-d82d-4f6d-9c8b-5e0060010c53/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
