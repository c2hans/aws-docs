---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A set of key-value pairs that are used to manage the resource. Tags can only be applied to permission sets and cannot be applied to corresponding roles that IAM Identity Center creates in AWS accounts.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="singlesignon-Type-Tag-Key"></a>
The key for the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

 ** Value **   <a name="singlesignon-Type-Tag-Value"></a>
The value of the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/Tag)
