---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A set of key/value pairs that are used to manage the resource.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="iot-Type-Tag-Key"></a>
The tag's key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Value **   <a name="iot-Type-Tag-Value"></a>
The tag's value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/Tag)
