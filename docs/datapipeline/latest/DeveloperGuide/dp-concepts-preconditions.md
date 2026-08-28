---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-preconditions.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Preconditions
<a name="dp-concepts-preconditions"></a>

In AWS Data Pipeline, a precondition is a pipeline component containing conditional statements that must be true before an activity can run. For example, a precondition can check whether source data is present before a pipeline activity attempts to copy it. AWS Data Pipeline provides several pre-packaged preconditions that accommodate common scenarios, such as whether a database table exists, whether an Amazon S3 key is present, and so on. However, preconditions are extensible and allow you to run your own custom scripts to support endless combinations.

There are two types of preconditions: system-managed preconditions and user-managed preconditions. System-managed preconditions are run by the AWS Data Pipeline web service on your behalf and do not require a computational resource. User-managed preconditions only run on the computational resource that you specify using the `runsOn` or `workerGroup` fields. The `workerGroup` resource is derived from the activity that uses the precondition.

## System-Managed Preconditions
<a name="dp-concepts-system-preconditions"></a>

[DynamoDBDataExists](dp-dynamodbdataexists.md)
Checks whether data exists in a specific DynamoDB table.

[DynamoDBTableExists](dp-dynamodbtableexists.md)
Checks whether a DynamoDB table exists.

[S3KeyExists](dp-object-S3KeyExists.md)
Checks whether an Amazon S3 key exists.

[S3PrefixNotEmpty](dp-object-s3prefixnotempty.md)
Checks whether an Amazon S3 prefix is empty.

## User-Managed Preconditions
<a name="dp-concepts-user-preconditions"></a>

[Exists](dp-object-exists.md)
Checks whether a data node exists.

[ShellCommandPrecondition](dp-object-shellcommandprecondition.md)
Runs a custom Unix/Linux shell command as a precondition.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
