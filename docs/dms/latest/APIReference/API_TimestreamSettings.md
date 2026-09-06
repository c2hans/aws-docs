---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_TimestreamSettings.html
---

# TimestreamSettings
<a name="API_TimestreamSettings"></a>

Provides information that defines an Amazon Timestream endpoint.

## Contents
<a name="API_TimestreamSettings_Contents"></a>

 ** DatabaseName **   <a name="DMS-Type-TimestreamSettings-DatabaseName"></a>
Database name for the endpoint.
Type: String
Required: Yes

 ** MagneticDuration **   <a name="DMS-Type-TimestreamSettings-MagneticDuration"></a>
Set this attribute to specify the default magnetic duration applied to the Amazon Timestream tables in days. This is the number of days that records remain in magnetic store before being discarded. For more information, see [Storage](https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html) in the [Amazon Timestream Developer Guide](https://docs.aws.amazon.com/timestream/latest/developerguide/).
Type: Integer
Required: Yes

 ** MemoryDuration **   <a name="DMS-Type-TimestreamSettings-MemoryDuration"></a>
Set this attribute to specify the length of time to store all of the tables in memory that are migrated into Amazon Timestream from the source database. Time is measured in units of hours. When Timestream data comes in, it first resides in memory for the specified duration, which allows quick access to it.
Type: Integer
Required: Yes

 ** CdcInsertsAndUpdates **   <a name="DMS-Type-TimestreamSettings-CdcInsertsAndUpdates"></a>
Set this attribute to `true` to specify that AWS DMS only applies inserts and updates, and not deletes. Amazon Timestream does not allow deleting records, so if this value is `false`, AWS DMS nulls out the corresponding record in the Timestream database rather than deleting it.
Type: Boolean
Required: No

 ** EnableMagneticStoreWrites **   <a name="DMS-Type-TimestreamSettings-EnableMagneticStoreWrites"></a>
Set this attribute to `true` to enable memory store writes. When this value is `false`, AWS DMS does not write records that are older in days than the value specified in `MagneticDuration`, because Amazon Timestream does not allow memory writes by default. For more information, see [Storage](https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html) in the [Amazon Timestream Developer Guide](https://docs.aws.amazon.com/timestream/latest/developerguide/).
Type: Boolean
Required: No

## See Also
<a name="API_TimestreamSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/TimestreamSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/TimestreamSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/TimestreamSettings)
