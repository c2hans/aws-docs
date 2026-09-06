---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_Policy.html
---

# Policy
<a name="API_Policy"></a>

Contains details for a policy. Policies define what operations a team that define the permissions for team resources.

## Contents
<a name="API_Policy_Contents"></a>

 ** Arn **   <a name="mpa-Type-Policy-Arn"></a>
Amazon Resource Name (ARN) for the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1224.
Pattern: `arn:.{1,63}:mpa:::aws:policy/[a-zA-Z0-9_\.-]{1,1023}/[a-zA-Z0-9_\.-]{1,1023}`
Required: Yes

 ** DefaultVersion **   <a name="mpa-Type-Policy-DefaultVersion"></a>
Determines if the specified policy is the default for the team.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** Name **   <a name="mpa-Type-Policy-Name"></a>
Name of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: Yes

 ** PolicyType **   <a name="mpa-Type-Policy-PolicyType"></a>
The type of policy.
Type: String
Valid Values: `AWS_MANAGED | AWS_RAM`
Required: Yes

## See Also
<a name="API_Policy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/Policy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/Policy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/Policy)
