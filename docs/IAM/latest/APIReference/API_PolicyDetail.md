---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyDetail.html
---

# PolicyDetail
<a name="API_PolicyDetail"></a>

Contains information about an IAM policy, including the policy document.

This data type is used as a response element in the [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html) operation.

## Contents
<a name="API_PolicyDetail_Contents"></a>

 ** PolicyDocument **
The policy document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** PolicyName **
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

## See Also
<a name="API_PolicyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/PolicyDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/PolicyDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/PolicyDetail)
