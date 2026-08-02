---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TypeConverterEntry.html
---

# TypeConverterEntry
<a name="API_TypeConverterEntry"></a>

This object defines one value type that will be converted using the [ typeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-typeConverter) processor.

## Contents
<a name="API_TypeConverterEntry_Contents"></a>

 ** key **   <a name="CWL-Type-TypeConverterEntry-key"></a>
The key with the value that is to be converted to a different type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** type **   <a name="CWL-Type-TypeConverterEntry-type"></a>
The type to convert the field value to. Valid values are `integer`, `double`, `string` and `boolean`.
Type: String
Valid Values: `boolean | integer | double | string`
Required: Yes

## See Also
<a name="API_TypeConverterEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/TypeConverterEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/TypeConverterEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/TypeConverterEntry)
