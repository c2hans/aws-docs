---
source_url: https://docs.aws.amazon.com/migrationhub/latest/ug/API_MigrationTaskUpdate.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# MigrationTaskUpdate
<a name="API_MigrationTaskUpdate"></a>

A migration-task progress update.

## Contents
<a name="API_MigrationTaskUpdate_Contents"></a>

 ** MigrationTaskState **   <a name="migrationhub-Type-MigrationTaskUpdate-MigrationTaskState"></a>
Task object encapsulating task information.
Type: [Task](API_Task.md) object
Required: No

 ** UpdateDateTime **   <a name="migrationhub-Type-MigrationTaskUpdate-UpdateDateTime"></a>
The timestamp for the update.
Type: Timestamp
Required: No

 ** UpdateType **   <a name="migrationhub-Type-MigrationTaskUpdate-UpdateType"></a>
The type of the update.
Type: String
Valid Values: `MIGRATION_TASK_STATE_UPDATED`
Required: No

## See Also
<a name="API_MigrationTaskUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWSMigrationHub-2017-05-31/MigrationTaskUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/MigrationTaskUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/MigrationTaskUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
