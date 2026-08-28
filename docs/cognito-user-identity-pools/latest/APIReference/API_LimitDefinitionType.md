---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_LimitDefinitionType.html
---

# LimitDefinitionType
<a name="API_LimitDefinitionType"></a>

The class and attributes that identify a specific limit at the account level.

A request parameter of [GetProvisionedLimit](API_GetProvisionedLimit.md) and [UpdateProvisionedLimit](API_UpdateProvisionedLimit.md).

## Contents
<a name="API_LimitDefinitionType_Contents"></a>

 ** Attributes **   <a name="CognitoUserPools-Type-LimitDefinitionType-Attributes"></a>
The attributes that identify the specific limit. For API rate limits, specify the `Category` key with a value like `UserAuthentication` or `UserCreation`.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

 ** LimitClass **   <a name="CognitoUserPools-Type-LimitDefinitionType-LimitClass"></a>
The class of the limit. For API rate limits, this is `API_CATEGORY`.
Type: String
Valid Values: `API_CATEGORY`
Required: Yes

## See Also
<a name="API_LimitDefinitionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/LimitDefinitionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/LimitDefinitionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/LimitDefinitionType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
