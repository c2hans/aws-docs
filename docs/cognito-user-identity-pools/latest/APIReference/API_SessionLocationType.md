---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SessionLocationType.html
---

# SessionLocationType
<a name="API_SessionLocationType"></a>

The geographic location of the most recent activity on a session, derived from the IP address.

## Contents
<a name="API_SessionLocationType_Contents"></a>

 ** City **   <a name="CognitoUserPools-Type-SessionLocationType-City"></a>
The city of the most recent activity on the session, derived from the IP address. This value can be null if geo-IP resolution fails. The maximum length is 256 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** Country **   <a name="CognitoUserPools-Type-SessionLocationType-Country"></a>
The country of the most recent activity on the session, derived from the IP address and returned in English (for example, `United States`). This is a country name as returned by the geo-IP database, not an ISO country code, and can be `unknown` if geo-IP resolution fails.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_SessionLocationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SessionLocationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SessionLocationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SessionLocationType)
