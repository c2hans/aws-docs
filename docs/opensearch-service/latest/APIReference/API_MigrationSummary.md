---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_MigrationSummary.html
---

# MigrationSummary
<a name="API_MigrationSummary"></a>

A summary of a migration job, including its status and progress.

## Contents
<a name="API_MigrationSummary_Contents"></a>

 ** applicationId **   <a name="opensearchservice-Type-MigrationSummary-applicationId"></a>
The unique identifier of the OpenSearch application associated with the migration.
Type: String
Pattern: `[a-z0-9]{3,30}`
Required: No

 ** createdAt **   <a name="opensearchservice-Type-MigrationSummary-createdAt"></a>
The date and time when the migration job was created.
Type: Timestamp
Required: No

 ** error **   <a name="opensearchservice-Type-MigrationSummary-error"></a>
Error details if the migration failed or completed with errors.
Type: [MigrationError](API_MigrationError.md) object
Required: No

 ** exportedCount **   <a name="opensearchservice-Type-MigrationSummary-exportedCount"></a>
The number of saved objects exported from the source data source.
Type: Integer
Required: No

 ** importedCount **   <a name="opensearchservice-Type-MigrationSummary-importedCount"></a>
The number of saved objects successfully imported into the target workspace.
Type: Integer
Required: No

 ** migrationId **   <a name="opensearchservice-Type-MigrationSummary-migrationId"></a>
The unique identifier of the migration job.
Type: String
Required: No

 ** source **   <a name="opensearchservice-Type-MigrationSummary-source"></a>
The source configuration for the migration.
Type: [MigrationSource](API_MigrationSource.md) object
Required: No

 ** status **   <a name="opensearchservice-Type-MigrationSummary-status"></a>
The current status of the migration job.
Type: String
Required: No

 ** updatedAt **   <a name="opensearchservice-Type-MigrationSummary-updatedAt"></a>
The date and time when the migration job was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_MigrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/MigrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/MigrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/MigrationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
