---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A structure that represents user-provided metadata that can be associated with an IAM resource. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **
The key name that can be used to look up or retrieve the associated value. For example, `Department` or `Cost Center` are common choices.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`
Required: Yes

 ** Value **
The value associated with this tag. For example, tags with a key name of `Department` could have values such as `Human Resources`, `Accounting`, and `Support`. Tags with a key name of `Cost Center` might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/Tag)
