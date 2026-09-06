---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_JSONMappingParameters.html
---

# JSONMappingParameters
<a name="API_JSONMappingParameters"></a>

For a SQL-based Kinesis Data Analytics application, provides additional mapping information when JSON is the record format on the streaming source.

## Contents
<a name="API_JSONMappingParameters_Contents"></a>

 ** RecordRowPath **   <a name="APIReference-Type-JSONMappingParameters-RecordRowPath"></a>
The path to the top-level parent that contains the records.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `^(?=^\$)(?=^\S+$).*$`
Required: Yes

## See Also
<a name="API_JSONMappingParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/JSONMappingParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/JSONMappingParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/JSONMappingParameters)
