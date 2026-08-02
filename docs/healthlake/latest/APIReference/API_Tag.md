---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A label consisting of a user-defined key and value. The form for tags is {"Key", "Value"}

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="HealthLake-Type-Tag-Key"></a>
The key portion of a tag. Tag keys are case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

 ** Value **   <a name="HealthLake-Type-Tag-Value"></a>
 The value portion of a tag. Tag values are case-sensitive.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/Tag)
