---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DataMigrationSettings.html
---

# DataMigrationSettings
<a name="API_DataMigrationSettings"></a>

Options for configuring a data migration, including whether to enable CloudWatch logs, and the selection rules to use to include or exclude database objects from the migration.

## Contents
<a name="API_DataMigrationSettings_Contents"></a>

 ** CloudwatchLogsEnabled **   <a name="DMS-Type-DataMigrationSettings-CloudwatchLogsEnabled"></a>
Whether to enable CloudWatch logging for the data migration.
Type: Boolean
Required: No

 ** NumberOfJobs **   <a name="DMS-Type-DataMigrationSettings-NumberOfJobs"></a>
The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.
Type: Integer
Required: No

 ** SelectionRules **   <a name="DMS-Type-DataMigrationSettings-SelectionRules"></a>
A JSON-formatted string that defines what objects to include and exclude from the migration.
Type: String
Required: No

## See Also
<a name="API_DataMigrationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DataMigrationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DataMigrationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DataMigrationSettings)
