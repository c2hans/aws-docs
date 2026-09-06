---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_MigrationOptions.html
---

# MigrationOptions
<a name="API_MigrationOptions"></a>

The configuration options for a saved objects migration job.

## Contents
<a name="API_MigrationOptions_Contents"></a>

 ** source **   <a name="opensearchservice-Type-MigrationOptions-source"></a>
The data source from which to export saved objects.
Type: [MigrationSource](API_MigrationSource.md) object
Required: Yes

 ** workspace **   <a name="opensearchservice-Type-MigrationOptions-workspace"></a>
The target workspace configuration for importing saved objects. You can specify an existing workspace or request creation of a new workspace.
Type: [MigrationWorkspace](API_MigrationWorkspace.md) object
Required: Yes

 ** conflictResolution **   <a name="opensearchservice-Type-MigrationOptions-conflictResolution"></a>
The strategy for resolving conflicts when saved objects already exist in the target workspace. Valid values are `CREATE_NEW_COPIES`, which creates new objects with unique IDs, and `overwrite`, which replaces existing objects.
Type: String
Required: No

 ** exportOptions **   <a name="opensearchservice-Type-MigrationOptions-exportOptions"></a>
Options to filter the scope of saved objects to export from the source.
Type: [ExportOptions](API_ExportOptions.md) object
Required: No

## See Also
<a name="API_MigrationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/MigrationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/MigrationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/MigrationOptions)
