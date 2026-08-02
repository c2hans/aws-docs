---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SerDeInfo.html
---

# SerDeInfo
<a name="API_SerDeInfo"></a>

Information about a serialization/deserialization program (SerDe) that serves as an extractor and loader.

## Contents
<a name="API_SerDeInfo_Contents"></a>

 ** Name **   <a name="Glue-Type-SerDeInfo-Name"></a>
Name of the SerDe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Parameters **   <a name="Glue-Type-SerDeInfo-Parameters"></a>
These key-value pairs define initialization parameters for the SerDe.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** SerializationLibrary **   <a name="Glue-Type-SerDeInfo-SerializationLibrary"></a>
Usually the class that implements the SerDe. An example is `org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_SerDeInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SerDeInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SerDeInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SerDeInfo)
