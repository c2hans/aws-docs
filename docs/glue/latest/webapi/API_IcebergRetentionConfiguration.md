---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergRetentionConfiguration.html
---

# IcebergRetentionConfiguration
<a name="API_IcebergRetentionConfiguration"></a>

The configuration for an Iceberg snapshot retention optimizer.

## Contents
<a name="API_IcebergRetentionConfiguration_Contents"></a>

 ** cleanExpiredFiles **   <a name="Glue-Type-IcebergRetentionConfiguration-cleanExpiredFiles"></a>
If set to false, snapshots are only deleted from table metadata, and the underlying data and metadata files are not deleted.
Type: Boolean
Required: No

 ** numberOfSnapshotsToRetain **   <a name="Glue-Type-IcebergRetentionConfiguration-numberOfSnapshotsToRetain"></a>
The number of Iceberg snapshots to retain within the retention period. If an input is not provided, the corresponding Iceberg table configuration field will be used or if not present, the default value 1 will be used.
Type: Integer
Required: No

 ** runRateInHours **   <a name="Glue-Type-IcebergRetentionConfiguration-runRateInHours"></a>
The interval in hours between retention job runs. This parameter controls how frequently the retention optimizer will run to clean up expired snapshots. The value must be between 3 and 168 hours (7 days). If an input is not provided, the default value 24 will be used.
Type: Integer
Required: No

 ** snapshotRetentionPeriodInDays **   <a name="Glue-Type-IcebergRetentionConfiguration-snapshotRetentionPeriodInDays"></a>
The number of days to retain the Iceberg snapshots. If an input is not provided, the corresponding Iceberg table configuration field will be used or if not present, the default value 5 will be used.
Type: Integer
Required: No

## See Also
<a name="API_IcebergRetentionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergRetentionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergRetentionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergRetentionConfiguration)
