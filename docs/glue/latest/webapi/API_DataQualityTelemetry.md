---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityTelemetry.html
---

# DataQualityTelemetry
<a name="API_DataQualityTelemetry"></a>

## Contents
<a name="API_DataQualityTelemetry_Contents"></a>

 ** Engine **   <a name="Glue-Type-DataQualityTelemetry-Engine"></a>

Type: String
Valid Values: `SPARK | PYTHON | DUCK`
Required: No

 ** FlagsEnabled **   <a name="Glue-Type-DataQualityTelemetry-FlagsEnabled"></a>

Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** HostRuntimeVersion **   <a name="Glue-Type-DataQualityTelemetry-HostRuntimeVersion"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** LibraryVersion **   <a name="Glue-Type-DataQualityTelemetry-LibraryVersion"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** SparkVersion **   <a name="Glue-Type-DataQualityTelemetry-SparkVersion"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** VcpuHours **   <a name="Glue-Type-DataQualityTelemetry-VcpuHours"></a>

Type: Double
Required: No

## See Also
<a name="API_DataQualityTelemetry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityTelemetry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityTelemetry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityTelemetry)
