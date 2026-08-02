---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Metadata that you can assign to a Firehose stream, consisting of a key-value pair.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="Firehose-Type-Tag-Key"></a>
A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, \_ . / = \+ - % @
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:\/=+\-@%]*$`
Required: Yes

 ** Value **   <a name="Firehose-Type-Tag-Value"></a>
An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, \_ . / = \+ - % @
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[\p{L}\p{Z}\p{N}_.:\/=+\-@%]*$`
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/Tag)
