---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_SourceDataSetting.html
---

# SourceDataSetting
<a name="API_SourceDataSetting"></a>

Defines settings for a source data provider for a data migration.

## Contents
<a name="API_SourceDataSetting_Contents"></a>

 ** CDCStartPosition **   <a name="DMS-Type-SourceDataSetting-CDCStartPosition"></a>
The change data capture (CDC) start position for the source data provider.
Type: String
Required: No

 ** CDCStartTime **   <a name="DMS-Type-SourceDataSetting-CDCStartTime"></a>
The change data capture (CDC) start time for the source data provider.
Type: Timestamp
Required: No

 ** CDCStopTime **   <a name="DMS-Type-SourceDataSetting-CDCStopTime"></a>
The change data capture (CDC) stop time for the source data provider.
Type: Timestamp
Required: No

 ** SlotName **   <a name="DMS-Type-SourceDataSetting-SlotName"></a>
The name of the replication slot on the source data provider. This attribute is only valid for a PostgreSQL or Aurora PostgreSQL source.
Type: String
Required: No

## See Also
<a name="API_SourceDataSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/SourceDataSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/SourceDataSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/SourceDataSetting)
