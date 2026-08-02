---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergOrphanFileDeletionConfiguration.html
---

# IcebergOrphanFileDeletionConfiguration
<a name="API_IcebergOrphanFileDeletionConfiguration"></a>

The configuration for an Iceberg orphan file deletion optimizer.

## Contents
<a name="API_IcebergOrphanFileDeletionConfiguration_Contents"></a>

 ** location **   <a name="Glue-Type-IcebergOrphanFileDeletionConfiguration-location"></a>
Specifies a directory in which to look for files (defaults to the table's location). You may choose a sub-directory rather than the top-level table location.
Type: String
Required: No

 ** orphanFileRetentionPeriodInDays **   <a name="Glue-Type-IcebergOrphanFileDeletionConfiguration-orphanFileRetentionPeriodInDays"></a>
The number of days that orphan files should be retained before file deletion. If an input is not provided, the default value 3 will be used.
Type: Integer
Required: No

 ** runRateInHours **   <a name="Glue-Type-IcebergOrphanFileDeletionConfiguration-runRateInHours"></a>
The interval in hours between orphan file deletion job runs. This parameter controls how frequently the orphan file deletion optimizer will run to clean up orphan files. The value must be between 3 and 168 hours (7 days). If an input is not provided, the default value 24 will be used.
Type: Integer
Required: No

## See Also
<a name="API_IcebergOrphanFileDeletionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergOrphanFileDeletionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergOrphanFileDeletionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergOrphanFileDeletionConfiguration)
