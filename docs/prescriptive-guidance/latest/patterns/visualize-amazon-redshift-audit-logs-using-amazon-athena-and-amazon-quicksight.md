---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/visualize-amazon-redshift-audit-logs-using-amazon-athena-and-amazon-quicksight.html
---

# Visualize Amazon Redshift audit logs using Amazon Athena and Amazon QuickSight
<a name="visualize-amazon-redshift-audit-logs-using-amazon-athena-and-amazon-quicksight"></a>

*Sanket Sirsikar and Gopal Krishna Bhatia, Amazon Web Services*

## Summary
<a name="visualize-amazon-redshift-audit-logs-using-amazon-athena-and-amazon-quicksight-summary"></a>

Security is an integral part of database operations on the Amazon Web Services (AWS) Cloud. Your organization should ensure that it monitors database user activities and connections to detect potential security incidents and risks. This pattern helps you monitor your databases for security and troubleshooting purposes, which is a process known as database auditing.

 This pattern provides a SQL script that automates the creation of an Amazon Athena table and views for a reporting dashboard in Amazon QuickSight that helps you audit Amazon Redshift logs. This ensures that users responsible for monitoring database activities have convenient access to data security features.

## Prerequisites and limitations
<a name="visualize-amazon-redshift-audit-logs-using-amazon-athena-and-amazon-quicksight-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing Amazon Redshift cluster. For more information about this, see [Create an Amazon Redshift cluster](https://docs.aws.amazon.com/redshift/latest/dg/tutorial-loading-data-launch-cluster.html) in the Amazon Redshift documentation.
+ Access to an existing Athena workgroup. For more information, see [How workgroups work](https://docs.aws.amazon.com/athena/latest/ug/user-created-workgroups.html) in the Amazon Athena documentation.
+ An existing Amazon Simple Storage Service (Amazon S3) source bucket with the required AWS Identity and Access Management (IAM) permissions. For more information, see [Bucket permissions for Amazon Redshift audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-bucket-permissions) from [Database audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html) in the Amazon Redshift documentation.

## Architecture
<a name="visualize-amazon-redshift-audit-logs-using-amazon-athena-and-amazon-quicksight-architecture"></a>

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/90e69009-001e-4ced-bef0-3c361f93ae87/images/9fde7f01-17ab-4207-8a59-a12daf85a382.png)

**Technology stack  **
+ Athena
+ Amazon Redshift
+ Amazon S3
+ QuickSight

## Tools
<a name="visualize-amazon-redshift-audit-logs-using-amazon-athena-and-amazon-quicksight-tools"></a>
+ [Amazon Athena ](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)– Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.
+ [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) – QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service.
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) – Amazon Redshift is an enterprise-level, petabyte scale, fully managed data warehousing service.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is storage for the internet.

## Epics
<a name="visualize-amazon-redshift-audit-logs-using-amazon-athena-and-amazon-quicksight-epics"></a>

### Configure the Amazon Redshift cluster
<a name="configure-the-amazon-redshift-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Enable audit logging for the Amazon Redshift cluster. | 1. Sign in to the AWS Management Console, open the Amazon Redshift console, choose **CLUSTERS**, and then choose the cluster that you want to enable logging for.<br />2. Choose the **Properties** tab and then enable auditing by following the instructions from [Configuring auditing using the console](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing-console.html) in the Amazon Redshift documentation. | DBA, Data engineer |
| Enable logging in the Amazon Redshift cluster parameter group. | You can enable auditing of connection logs, user logs, and user activity logs at the same time by using the AWS Management Console, the Amazon Redshift API reference, or AWS Command Line Interface (AWS CLI).  <br />For auditing of user activity logs, you must enable the `enable_user_activity_logging` database parameter. If you only enable the audit logging feature but not the associated parameter, the database audit logs the logging information for the connection and user logs but not for the user activity logs. The `enable_user_activity_logging` parameter is not enabled by default, but you can enable it by changing it from `false` to `true`.You need to create a new cluster parameter group with the `user_activity_logging` parameter enabled and attach it to your Amazon Redshift cluster. For more information about this, see [Modifying a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html#modify-cluster) in the Amazon Redshift documentation.<br />For more information about this task, see [Amazon Redshift parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) and [Configuring auditing using the console](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing-console.html) in the Amazon Redshift documentation. | DBA, Data engineer |
| Configure S3 bucket permissions for Amazon Redshift cluster logging. | When you enable logging, Amazon Redshift collects logging information and uploads it to log files stored in an S3 bucket. You can use an existing S3 bucket or create a new bucket.Make sure that Amazon Redshift has the required IAM permissions to access the S3 bucket. For more information about this, see [Bucket permissions for Amazon Redshift audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-bucket-permissions) from [Database audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html) in the Amazon Redshift documentation. | DBA, Data engineer |

### Create the Athena table and views
<a name="create-the-athena-table-and-views"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Athena table and views to query Amazon Redshift audit log data from the S3 bucket. | Open the Amazon Athena console and use the data definition language (DDL) query from the `AuditLogging.sql` SQL script (attached) to create the table and views for user activity logs, user logs, and connection logs.<br />For more information and instructions, see the [Create tables and run queries](https://athena-in-action.workshop.aws/30-basics/301-create-tables.html) tutorial from the Amazon Athena Workshop. | Data engineer |

### Set up log monitoring in the QuickSight dashboard
<a name="set-up-log-monitoring-in-the-quicksight-dashboard"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a QuickSight dashboard using Athena as the data source. | Open the Amazon QuickSight console and create a QuickSight dashboard by following the instructions in the [Visualize with QuickSight using Athena](https://athena-in-action.workshop.aws/30-basics/307-quicksight.html) tutorial from the Amazon Athena Workshop. | DBA, Data engineer |

## Related resources
<a name="visualize-amazon-redshift-audit-logs-using-amazon-athena-and-amazon-quicksight-resources"></a>
+ [Create tables and run queries in Athena](https://athena-in-action.workshop.aws/30-basics/301-create-tables.html)
+ [Visualize with QuickSight using Athena](https://athena-in-action.workshop.aws/30-basics/307-quicksight.html)

## Attachments
<a name="attachments-90e69009-001e-4ced-bef0-3c361f93ae87"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/90e69009-001e-4ced-bef0-3c361f93ae87/attachments/attachment.zip)
