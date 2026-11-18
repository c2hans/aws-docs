---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file.html
---

# Export AWS Backup reports from across an organization in AWS Organizations as a CSV file
<a name="export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file"></a>

*Aromal Raj Jayarajan, Prasobh S P, and Vishnu Unnikrishnan, Amazon Web Services*

## Summary
<a name="export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file-summary"></a>

This pattern shows how to export [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) job reports from across an organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) as a CSV file. The solution uses [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) to categorize AWS Backup job reports based on their status, which can help you configure status-based automations.

AWS Backup helps organizations centrally manage and automate data protection across AWS services, in the cloud, and on-premises. However, for AWS Backup jobs configured within AWS Organizations, consolidated reporting is available only in the AWS Management Console of each organization’s management account. Making this reporting available outside of the management account can reduce the effort required for auditing and expand the options for automations, notifications, and alerting.

AWS Backup Audit Manager can also create multi-account, multi-Region job reports as CSV files from the management account or from a delegated administrator account. For more information, see [Working with audit reports](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-reports.html) (AWS Backup documentation). Use this pattern if you need reports in the Amazon S3 bucket of a member account that is not the delegated administrator, one report file per job status, or a custom schedule.

## Prerequisites and limitations
<a name="export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An active [organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) in AWS Organizations that includes at least a management account and a member account (the reporting account)
+ The ID of your organization in AWS Organizations (for example, `o-a1b2c3d4e5`)
+ Permissions to create AWS CloudFormation stacks and named [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/) roles in both the management account and the reporting account
+ AWS Backup configured at the organization level in AWS Organizations (for more information, see [Automate centralized backup at scale across AWS services using AWS Backup](https://aws.amazon.com/blogs/storage/automate-centralized-backup-at-scale-across-aws-services-using-aws-backup/) on the AWS Blog)
+ AWS Backup cross-account monitoring turned on in the management account. In the AWS Backup console of the management account, choose **Settings**, and then in the **Cross-account monitoring** section, choose **Enable**. Without this setting, the report function receives an `AccessDeniedException` when it lists jobs for all accounts. For more information, see [Managing AWS Backup resources across multiple AWS accounts](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html) (AWS Backup documentation).
+ [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), installed and configured on your local machine

**Limitations**
+ The solution identifies AWS resources that are configured for AWS Backup jobs only. The report can’t identify AWS resources that aren’t configured for backup through AWS Backup.
+ Each report contains the AWS Backup jobs that were created on the current UTC day.
+ The IAM role in the management account trusts the Lambda execution role in the reporting account. If you delete and recreate the reporting stack, you must update the management stack afterward.

## Architecture
<a name="export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file-architecture"></a>

**Target technology stack**
+ AWS Backup
+ AWS CloudFormation
+ Amazon CloudWatch Logs
+ Amazon EventBridge
+ AWS Identity and Access Management (IAM)
+ AWS Key Management Service (AWS KMS)
+ AWS Lambda
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Security Token Service (AWS STS)

**Target architecture**

The following diagram shows an example workflow for exporting AWS Backup job reports from across an organization in AWS Organizations as a CSV file.

![Using EventBridge, Lambda, AWS STS, and IAM to export AWS Backup job reports from across an organization in CSV format.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/74955aad-cc6d-488b-aa34-ae43f50fec60/images/5c39c79f-e731-4ad0-b404-51ebe0976420.png)

The diagram shows the following workflow:

1. A scheduled EventBridge event rule invokes a Lambda function in the member (reporting) AWS account. By default, the rule runs once a day at 23:59 UTC.

1. The Lambda function uses AWS STS to assume an IAM role in the management account. That role trusts only the Lambda execution role in the reporting account, and only for principals in your organization.

1. The Lambda function then does the following:

   1. Requests the jobs for each job status from AWS Backup for the current UTC day

   1. Converts the response for each job status to a CSV file

   1. Uploads the results to an Amazon S3 bucket in the reporting account, into folders that it labels by creation date

## Tools
<a name="export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file-tools"></a>

**Tools**
+ [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a fully managed service that helps you centralize and automate data protection across AWS services, in the cloud, and on premises.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources, such as AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.

**Code**

The code for this pattern is available in the GitHub [aws-backup-report-generator](https://github.com/aws-samples/aws-backup-report-generator) repository.

## Best practices
<a name="export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file-best-practices"></a>
+ [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) (*Amazon S3 User Guide*)
+ [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) (*AWS Lambda Developer Guide*)
+ [Best practices for the management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html) (*AWS Organizations User Guide*)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (*IAM User Guide*)

## Epics
<a name="export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file-epics"></a>

### Deploy the solution components
<a name="deploy-the-solution-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository. | Clone the GitHub [aws-backup-report-generator](https://github.com/aws-samples/aws-backup-report-generator) repository by running the following command in a terminal window:<pre>git clone https://github.com/aws-samples/aws-backup-report-generator.git</pre><br />For more information, see [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) in the GitHub Docs. | AWS DevOps, DevOps engineer |
| Deploy the solution components in the member (reporting) AWS account. | Deploy this stack first. The role that you create in the management account in the next story trusts the Lambda role that this stack creates.1. In the member (reporting) account, sign in to the AWS Management Console and then open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. Choose **Create stack**, and then choose **With new resources (standard)**.<br />3. On the **Create stack** page, in the **Specify template** section, choose **Upload a template file**.<br />4. Choose **Choose file**. Then, navigate to the root folder of the cloned GitHub repository on your local workstation and choose `template-reporting.yml`.<br />5. Choose **Open**, and then choose **Next**.<br />6. On the **Specify stack details** page, for **Stack name**, enter a name for your CloudFormation stack.<br />7. For **ManagementAccountID**, enter the 12-digit AWS account ID of your organization’s management account in AWS Organizations.<br />8. For **ScheduleExpression**, keep the default value `cron(59 23 * * ? *)` to run the report once a day.<br />9. Choose **Next**.<br />10. On the **Configure stack options** page, choose **Next**.<br />11. On the **Review and create** page, select the check box to acknowledge that CloudFormation might create IAM resources with custom names, and then choose **Submit**.<br />The stack shows `CREATE_COMPLETE` status when the solution components are deployed in the member (reporting) account. | DevOps engineer, AWS DevOps |
| Deploy the solution components in the management account. | 1. In the management account, sign in to the AWS Management Console and then open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. Choose **Create stack**, and then choose **With new resources (standard)**.<br />3. On the **Create stack** page, in the **Specify template** section, choose **Upload a template file**.<br />4. Choose **Choose file**. Then, navigate to the root folder of the cloned GitHub repository on your local workstation and choose `template-management.yml`.<br />5. Choose **Open**, and then choose **Next**.<br />6. On the **Specify stack details** page, for **Stack name**, enter a name for your CloudFormation stack.<br />7. For **ReportingAccountID**, enter the 12-digit AWS account ID of the member (reporting) account.<br />8. For **OrganizationID**, enter the ID of your organization in AWS Organizations (for example, `o-a1b2c3d4e5`).<br />9. Choose **Next**.<br />10. On the **Configure stack options** page, choose **Next**.<br />11. On the **Review and create** page, select the check box to acknowledge that CloudFormation might create IAM resources with custom names, and then choose **Submit**.The stack shows `CREATE_COMPLETE` status when the solution components are deployed in the management account. | AWS DevOps, DevOps engineer |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the report on a shorter schedule. | By default, the report runs once a day at 23:59 UTC. To test sooner, update the stack in the member (reporting) account:1. In the member (reporting) account, open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/) and select the stack that you created.<br />2. Choose **Update**, choose **Use existing template**, and then choose **Next**.<br />3. For **ScheduleExpression**, enter `rate(5 minutes)`, and then choose **Next** until you reach **Submit**.<br />4. Wait at least 5 minutes.<br />When you finish testing, update the stack again and set **ScheduleExpression** back to `cron(59 23 * * ? *)`. | AWS DevOps, DevOps engineer |
| Check the Amazon S3 bucket for the generated report. | 1. In the member (reporting) account, sign in to the AWS Management Console and then open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. In the **Stacks** pane, select the name of the stack you created. Then, choose the **Resources** tab.<br />3. In the **Resources** pane, in the **Logical ID** column, find `BackupReportS3Bucket`. Then, open the associated Amazon S3 bucket in a new tab by selecting the link in the **Physical ID** column next to that logical ID.<br />4. Make sure that the bucket contains a report that’s generated in the following format: `BackupReports/<yyyy>/<mm>/<dd>/BackupReport-<BACKUP JOB STATUS>-<dd>-<Mon>-<yyyy>.csv`The solution creates a file only for the job statuses that have at least one job on that day. | AWS DevOps, DevOps engineer |

### Clean up your resources
<a name="clean-up-your-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the solution components from the management account. | 1. In the management account, sign in to the AWS Management Console and then open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. In the **Stacks** pane, select the checkbox next to the name of the stack you created. Then, choose **Delete**. | AWS DevOps, DevOps engineer |
| Delete the solution components from the member (reporting) account. | 1. In the member (reporting) account, open the solution’s Amazon S3 bucket. For instructions, see steps 1-3 in the **Check the Amazon S3 bucket for the generated report** story of the **Test the solution** section of this pattern.<br />2. Delete the contents of the bucket and empty the bucket. Because versioning is turned on, choose to delete all object versions. For instructions, see [Emptying a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html) in the Amazon S3 User Guide.<br />3. In the member (reporting) account, open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />4. In the **Stacks** pane, select the checkbox next to the name of the stack you created. Then, choose **Delete**. | AWS DevOps, DevOps engineer |

## Related resources
<a name="export-aws-backup-reports-from-across-an-organization-in-aws-organizations-as-a-csv-file-resources"></a>
+ [Tutorial: Using AWS Lambda with scheduled events ](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-tutorial.html)(AWS Lambda documentation)
+ [Creating scheduled events to run AWS Lambda functions](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/scheduled-events-invoking-lambda-example.html) (AWS SDK for JavaScript documentation)
+ [IAM tutorial: Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) (IAM documentation)
+ [AWS Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) (AWS Organizations documentation)
+ [Creating report plans using the AWS Backup console](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-console.html) (AWS Backup documentation)
+ [Create an audit report](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-audit-report.html) (AWS Backup documentation)
+ [Creating on-demand reports](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-on-demand-reports.html) (AWS Backup documentation)
+ [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) (AWS Backup documentation)
+ [Automate centralized backup at scale across AWS services using AWS Backup](https://aws.amazon.com/blogs/storage/automate-centralized-backup-at-scale-across-aws-services-using-aws-backup/) (AWS blog post)
+ [Working with audit reports](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-reports.html) (AWS Backup documentation)
+ [Managing AWS Backup resources across multiple AWS accounts](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html) (AWS Backup documentation)
+ [IAM role trust policies and the aws:PrincipalOrgID condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgid) (IAM documentation)
