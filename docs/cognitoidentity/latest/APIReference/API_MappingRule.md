---
source_url: https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_MappingRule.html
---

# MappingRule
<a name="API_MappingRule"></a>

A rule that maps a claim name, a claim value, and a match type to a role ARN.

## Contents
<a name="API_MappingRule_Contents"></a>

 ** Claim **   <a name="CognitoIdentity-Type-MappingRule-Claim"></a>
The claim name that must be present in the token, for example, "isAdmin" or "paid".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** MatchType **   <a name="CognitoIdentity-Type-MappingRule-MatchType"></a>
The match condition that specifies how closely the claim value in the IdP token must match `Value`.
Type: String
Valid Values: `Equals | Contains | StartsWith | NotEqual`
Required: Yes

 ** RoleARN **   <a name="CognitoIdentity-Type-MappingRule-RoleARN"></a>
The role ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** Value **   <a name="CognitoIdentity-Type-MappingRule-Value"></a>
A brief string that the claim must match, for example, "paid" or "yes".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_MappingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/MappingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/MappingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/MappingRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitoidentity` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
