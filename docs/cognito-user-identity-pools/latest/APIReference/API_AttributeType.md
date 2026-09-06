---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AttributeType.html
---

# AttributeType
<a name="API_AttributeType"></a>

The name and value of a user attribute.

This data type is a request parameter of [AdminUpdateUserAttributes](API_AdminUpdateUserAttributes.md) and [UpdateUserAttributes](API_UpdateUserAttributes.md).

## Contents
<a name="API_AttributeType_Contents"></a>

 ** Name **   <a name="CognitoUserPools-Type-AttributeType-Name"></a>
The name of the attribute, for example `email` or `custom:department`.
In some older user pools, the regex pattern for acceptable values of this parameter is `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`. Older pools will eventually be updated to use the new pattern. Affected user pools are those created before May 2024 in US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), Middle East (Bahrain), and South America (São Paulo).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+`
Required: Yes

 ** Value **   <a name="CognitoUserPools-Type-AttributeType-Value"></a>
The value of the attribute.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## See Also
<a name="API_AttributeType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AttributeType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AttributeType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AttributeType)
