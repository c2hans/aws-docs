---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserContextDataType.html
---

# UserContextDataType
<a name="API_UserContextDataType"></a>

Contextual data, such as the user's device fingerprint, IP address, or location, used for evaluating the risk of an unexpected event by Amazon Cognito threat protection.

This data type is a request parameter of public-client authentication operations like [InitiateAuth](API_InitiateAuth.md) and [RespondToAuthChallenge](API_RespondToAuthChallenge.md).

## Contents
<a name="API_UserContextDataType_Contents"></a>

 ** EncodedData **   <a name="CognitoUserPools-Type-UserContextDataType-EncodedData"></a>
Encoded device-fingerprint details that your app collected with the Amazon Cognito context data collection library. For more information, see [Adding user device and session data to API requests](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** IpAddress **   <a name="CognitoUserPools-Type-UserContextDataType-IpAddress"></a>
The source IP address of your user's device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_UserContextDataType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserContextDataType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserContextDataType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserContextDataType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
