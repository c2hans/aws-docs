---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

You can pass custom key-value pair attributes when you assume a role or federate a user. These are called session tags. You can then use the session tags to control access to resources. For more information, see [Tagging AWS STS Sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) in the *IAM User Guide*.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **
The key for a session tag.
You can pass up to 50 session tags. The plain text session tag keys can’t exceed 128 characters. For these and additional limits, see [IAM and AWS STS Character Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`
Required: Yes

 ** Value **
The value for a session tag.
You can pass up to 50 session tags. The plain text session tag values can’t exceed 256 characters. For these and additional limits, see [IAM and AWS STS Character Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/Tag)
