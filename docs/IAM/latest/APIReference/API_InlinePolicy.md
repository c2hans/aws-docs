---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_InlinePolicy.html
---

# InlinePolicy
<a name="API_InlinePolicy"></a>

Contains an inline policy template that the service embeds in roles that you create from a role template.

## Contents
<a name="API_InlinePolicy_Contents"></a>

 ** PolicyDocument **
The inline policy document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** PolicyName **
The name of the inline policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## See Also
<a name="API_InlinePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/InlinePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/InlinePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/InlinePolicy)
