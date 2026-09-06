---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_PolicyReference.html
---

# PolicyReference
<a name="API_PolicyReference"></a>

Contains the Amazon Resource Name (ARN) for a policy. Policies define what operations a team that define the permissions for team resources.

## Contents
<a name="API_PolicyReference_Contents"></a>

 ** PolicyArn **   <a name="mpa-Type-PolicyReference-PolicyArn"></a>
Amazon Resource Name (ARN) for the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1224.
Pattern: `arn:.{1,63}:mpa:::aws:policy/[a-zA-Z0-9_\.-]{1,1023}/[a-zA-Z0-9_\.-]{1,1023}/(?:[\d]+|\$DEFAULT)`
Required: Yes

## See Also
<a name="API_PolicyReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/PolicyReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/PolicyReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/PolicyReference)
