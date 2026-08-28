---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/audit-trails.html
---

# Audit trails
<a name="audit-trails"></a>

The audit trail (or audit log) provides a security-relevant chronological record of events in your AWS account. It includes events for Amazon RDS, which provide documentary evidence of the sequence of activities that have affected your database or your cloud environment. In Amazon RDS for MySQL or MariaDB, using the audit trail involves:
+ Monitoring the DB instance audit log
+ Monitoring Amazon RDS API calls in AWS CloudTrail

For an Amazon RDS DB instance, the objectives of auditing typically include:
+ Enabling accountability for the following:
  + Modifications performed on the parameter or security configuration
  + Actions performed in a database schema, table, or row, or actions that affect specific content
+ Intrusion detection and investigation
+ Suspicious activity detection and investigation
+ Detection of authorization problems; for example, to identify abuse of access rights by regular or privileged users

The database audit trail tries to answer these typical questions: *Who viewed or modified sensitive data inside your database? When did this happen? Where did a specific user access the data from? Did privileged users abuse their unlimited access rights?*

Both MySQL and MariaDB implement the DB instance audit trail feature by using the MariaDB Audit Plugin. This plugin records database activity such as users logging on to the database and queries running against the database. The record of database activity is stored in a log file. To access the audit log, the DB instance must use a custom option group with the `MARIADB_AUDIT_PLUGIN` option. For more information, see [MariaDB Audit Plugin support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.AuditPlugin.html) for MySQL in the Amazon RDS documentation. The records in the audit log are stored in a specific format, as defined by the plugin. You can find more details about the audit log format in the [MariaDB Server documentation](https://mariadb.com/kb/en/mariadb-audit-plugin-log-format/).

The AWS Cloud audit trail for your AWS account is provided by the [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) service. CloudTrail captures API calls for Amazon RDS as events. All Amazon RDS actions are logged. CloudTrail provides a record of actions in Amazon RDS performed by a user, role, or another AWS service. Events include actions taken in the AWS Management Console, AWS CLI, and AWS SDKs and APIs.

## Example
<a name="example"></a>

In a typical audit scenario, you might need to combine AWS CloudTrail trails with the database audit log and Amazon RDS events monitoring. For example, you might have a scenario where the database parameters of your Amazon RDS DB instance (for example, database-1) have been modified and your task is to identify who did the modification, what was changed, and when the change happened.

To accomplish the task, follow these steps:

1. List the Amazon RDS events that happened to the database instance `database-1` and determine whether there is an event in the category configuration change that has the message `Finished updating DB parameter group`.

   ```
   $ aws rds describe-events --source-identifier database-1 --source-type db-instance
   {
       "Events": [
           {
               "SourceIdentifier": "database-1",
               "SourceType": "db-instance",
               "Message": "Finished updating DB parameter group",
               "EventCategories": [
                   "configuration change"
               ],
               "Date": "2022-12-01T09:22:40.413000+00:00",
               "SourceArn": "arn:aws:rds:eu-west-3:111122223333:db:database-1"
           }
       ]
   }
   ```

1. Identify which DB parameter group the DB instance is using:

   ```
   $ aws rds describe-db-instances --db-instance-identifier database-1 --query 'DBInstances[*].[DBInstanceIdentifier,Engine,DBParameterGroups]'
   [
       [
           "database-1",
           "mariadb",
           [
               {
                   "DBParameterGroupName": "mariadb10-6-test",
                   "ParameterApplyStatus": "pending-reboot"
               }
           ]
       ]
   ]
   ```

1. [Use the AWS CLI to search for CloudTrail events ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-cli.html)in the Region where `database-1` is deployed, in the time period around the Amazon RDS event discovered in step 1, and where `EventName=ModifyDBParameterGroup`.

   ```
   $ aws cloudtrail --region eu-west-3 lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ModifyDBParameterGroup --start-time "2022-12-01, 09:00 AM" --end-time "2022-12-01, 09:30 AM"

   {
       "eventVersion": "1.08",
       "userIdentity": {
           "accountId": "111122223333",
           "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
           "sessionContext": {
               "sessionIssuer": {
                   "type": "Role",
                   "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                   "arn": "arn:aws:iam::111122223333:role/Role1",
                   "accountId": "111122223333",
                   "userName": "User1"
               }
           }
       },
       "eventTime": "2022-12-01T09:18:19Z",
       "eventSource": "rds.amazonaws.com",
       "eventName": "ModifyDBParameterGroup",
       "awsRegion": "eu-west-3",
       "sourceIPAddress": "AWS Internal",
       "userAgent": "AWS Internal",
       "requestParameters": {
           "parameters": [
               {
                   "isModifiable": false,
                   "applyMethod": "pending-reboot",
                   "parameterName": "innodb_log_buffer_size",
                   "parameterValue": "8388612"
               },
               {
                   "isModifiable": false,
                   "applyMethod": "pending-reboot",
                   "parameterName": "innodb_write_io_threads",
                   "parameterValue": "8"
               }
           ],
           "dBParameterGroupName": "mariadb10-6-test"
       },
       "responseElements": {
           "dBParameterGroupName": "mariadb10-6-test"
       },
       "requestID": "fdf19353-de72-4d3d-bf29-751f375b6378",
       "eventID": "0bba7484-0e46-4e71-93a8-bd01ca8386fe",
       "eventType": "AwsApiCall",
       "managementEvent": true,
       "recipientAccountId": "111122223333",
       "eventCategory": "Management",
       "sessionCredentialFromConsole": "true"
   }
   ```

The CloudTrail event reveals that *User1 with role Role1* from AWS account 111122223333 modified the DB parameter group `mariadb10-6-test`, which was used by the DB instance `database-1` on *2022-12-01 at 09:18:19 h*. Two parameters were modified and set to the following values:
+ `innodb_log_buffer_size = 8388612`
+ `innodb_write_io_threads = 8`

## Additional CloudTrail and CloudWatch Logs features
<a name="additional-cloud-trail-and-cloud-watch-logs-features"></a>

You can troubleshoot operational and security incidents over the past 90 days by viewing **Event history** on the CloudTrail console. To extend the retention period and take advantage of additional query capabilities, you can use [AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html). With AWS CloudTrail Lake, you can keep event data in an event data store for up to seven years. Additionally, the service supports complex SQL queries that offer a deeper and more customizable view of events than the views provided by simple key-value lookups in **Event history**.

To monitor your audit trails, set alarms, and get notifications when specific activity occurs, you need to [configure CloudTrail to send its trail records to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html). After the trail records are stored as CloudWatch logs, you can define metric filters to evaluate log events to match terms, phrases, or values, and assign metrics to metric filters. Furthermore, you can create CloudWatch alarms that are generated according to thresholds and time periods that you specify. For example, you can configure alarms that send notifications to responsible teams, so they can take the appropriate action. You can also configure CloudWatch to automatically perform an action in response to an alarm.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
