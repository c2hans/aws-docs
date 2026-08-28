---
source_url: https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_IdentityPoolShortDescription.html
---

# IdentityPoolShortDescription
<a name="API_IdentityPoolShortDescription"></a>

A description of the identity pool.

## Contents
<a name="API_IdentityPoolShortDescription_Contents"></a>

 ** IdentityPoolId **   <a name="CognitoIdentity-Type-IdentityPoolShortDescription-IdentityPoolId"></a>
An identity pool ID in the format REGION:GUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: No

 ** IdentityPoolName **   <a name="CognitoIdentity-Type-IdentityPoolShortDescription-IdentityPoolName"></a>
A string that you provide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s+=,.@-]+`
Required: No

## See Also
<a name="API_IdentityPoolShortDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/IdentityPoolShortDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/IdentityPoolShortDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/IdentityPoolShortDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitoidentity` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
