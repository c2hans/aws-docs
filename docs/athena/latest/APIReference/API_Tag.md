---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A label that you assign to a resource. Athena resources include workgroups, data catalogs, and capacity reservations. Each tag consists of a key and an optional value, both of which you define. For example, you can use tags to categorize Athena resources by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter the resources in your account. For best practices, see [Tagging Best Practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). Tag keys can be from 1 to 128 UTF-8 Unicode characters, and tag values can be from 0 to 256 UTF-8 Unicode characters. Tags can use letters and numbers representable in UTF-8, and the following characters: \+ - = . \_ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource. If you specify more than one tag, separate them by commas.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="athena-Type-Tag-Key"></a>
A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: \+ - = . \_ : / @. Tag keys are case-sensitive and must be unique per resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Value **   <a name="athena-Type-Tag-Value"></a>
A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: \+ - = . \_ : / @. Tag values are case-sensitive.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/Tag)
