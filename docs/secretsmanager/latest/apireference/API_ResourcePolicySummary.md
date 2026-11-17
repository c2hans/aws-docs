---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ResourcePolicySummary.html
---

# ResourcePolicySummary
<a name="API_ResourcePolicySummary"></a>

A structure that contains details about a resource policy attached to a secret. It does not contain the contents of the resource policy. To view the contents of the policy, use [GetResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html) .

## Contents
<a name="API_ResourcePolicySummary_Contents"></a>

 ** PolicyName **   <a name="SecretsManager-Type-ResourcePolicySummary-PolicyName"></a>
The name of the resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9A-Za-z\-\_]+`
Required: No

## See Also
<a name="API_ResourcePolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ResourcePolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ResourcePolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ResourcePolicySummary)
