---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EventContextDataType.html
---

# EventContextDataType
<a name="API_EventContextDataType"></a>

The context data that your application submitted in an authentication request with threat protection, as displayed in an `AdminListUserAuthEvents` response.

## Contents
<a name="API_EventContextDataType_Contents"></a>

 ** City **   <a name="CognitoUserPools-Type-EventContextDataType-City"></a>
The user's city.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** Country **   <a name="CognitoUserPools-Type-EventContextDataType-Country"></a>
The user's country.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** DeviceName **   <a name="CognitoUserPools-Type-EventContextDataType-DeviceName"></a>
The user's device name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** IpAddress **   <a name="CognitoUserPools-Type-EventContextDataType-IpAddress"></a>
The source IP address of your user's device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** Timezone **   <a name="CognitoUserPools-Type-EventContextDataType-Timezone"></a>
The user's time zone.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_EventContextDataType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/EventContextDataType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/EventContextDataType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/EventContextDataType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
