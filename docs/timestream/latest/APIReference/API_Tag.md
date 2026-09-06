---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

 A tag is a label that you assign to a Timestream database and/or table. Each tag consists of a key and an optional value, both of which you define. With tags, you can categorize databases and/or tables, for example, by purpose, owner, or environment.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="timestream-Type-Tag-Key"></a>
 The key of the tag. Tag keys are case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Value **   <a name="timestream-Type-Tag-Value"></a>
 The value of the tag. Tag values are case-sensitive and can be null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/Tag)
