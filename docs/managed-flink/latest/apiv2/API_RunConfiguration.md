---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RunConfiguration.html
---

# RunConfiguration
<a name="API_RunConfiguration"></a>

Describes the starting parameters for an Managed Service for Apache Flink application.

## Contents
<a name="API_RunConfiguration_Contents"></a>

 ** ApplicationRestoreConfiguration **   <a name="APIReference-Type-RunConfiguration-ApplicationRestoreConfiguration"></a>
Describes the restore behavior of a restarting application.
Type: [ApplicationRestoreConfiguration](API_ApplicationRestoreConfiguration.md) object
Required: No

 ** FlinkRunConfiguration **   <a name="APIReference-Type-RunConfiguration-FlinkRunConfiguration"></a>
Describes the starting parameters for a Managed Service for Apache Flink application.
Type: [FlinkRunConfiguration](API_FlinkRunConfiguration.md) object
Required: No

 ** SqlRunConfigurations **   <a name="APIReference-Type-RunConfiguration-SqlRunConfigurations"></a>
Describes the starting parameters for a SQL-based Kinesis Data Analytics application application.
Type: Array of [SqlRunConfiguration](API_SqlRunConfiguration.md) objects
Required: No

## See Also
<a name="API_RunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/RunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/RunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/RunConfiguration)
