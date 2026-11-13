---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SessionDescriptionType.html
---

# SessionDescriptionType
<a name="API_SessionDescriptionType"></a>

Describes an active user session. Amazon Cognito returns this type in the responses of `ListUserSessions` and `AdminListUserSessions`, for both token sessions and SSO sessions.

## Contents
<a name="API_SessionDescriptionType_Contents"></a>

 ** ClientId **   <a name="CognitoUserPools-Type-SessionDescriptionType-ClientId"></a>
The ID of the app client that the session belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: No

 ** CreateDate **   <a name="CognitoUserPools-Type-SessionDescriptionType-CreateDate"></a>
The date and time when the session was created.
Type: Timestamp
Required: No

 ** DeviceType **   <a name="CognitoUserPools-Type-SessionDescriptionType-DeviceType"></a>
A description of the device associated with the most recent activity on the session, derived from the parsed user agent (operating system and browser or app). Amazon Cognito overwrites this value on each sign-in, refresh, and rotation. The value can be `unknown`. The maximum length is 1,024 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** IsCurrentSession **   <a name="CognitoUserPools-Type-SessionDescriptionType-IsCurrentSession"></a>
Specifies whether this session matches the access token supplied in the request. This value is always `false` for the `AdminListUserSessions` operation, which doesn't take an access token.
Type: Boolean
Required: No

 ** LastActiveDate **   <a name="CognitoUserPools-Type-SessionDescriptionType-LastActiveDate"></a>
The date and time of the most recent activity on the session. For a token session, this is the most recent token refresh or rotation; a new authentication creates a new token session rather than updating an existing one. For an SSO session, this is the most recent authentication, token grant, or token rotation.
Type: Timestamp
Required: No

 ** LastIPAddress **   <a name="CognitoUserPools-Type-SessionDescriptionType-LastIPAddress"></a>
The IP address associated with the most recent activity on the session. Amazon Cognito overwrites this value on each refresh and rotation. The maximum length is 128 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** LastLocation **   <a name="CognitoUserPools-Type-SessionDescriptionType-LastLocation"></a>
The geographic location of the most recent activity on the session, derived from the IP address.
Type: [SessionLocationType](API_SessionLocationType.md) object
Required: No

 ** OriginSessionId **   <a name="CognitoUserPools-Type-SessionDescriptionType-OriginSessionId"></a>
For a token session, the ID of the SSO session that the token session originated from. This value is null for sessions that were initiated through the API and didn't come through an SSO session. Amazon Cognito returns this value for token sessions only.
Type: String
Length Constraints: Fixed length of 28.
Pattern: `^(tkn|sso)[a-z0-9]{25}$`
Required: No

 ** SessionId **   <a name="CognitoUserPools-Type-SessionDescriptionType-SessionId"></a>
The unique identifier for the session. This is a 28-character string of lowercase letters and digits, prefixed with `tkn` for a token session or `sso` for an SSO session.
Type: String
Length Constraints: Fixed length of 28.
Pattern: `^(tkn|sso)[a-z0-9]{25}$`
Required: No

 ** SessionType **   <a name="CognitoUserPools-Type-SessionDescriptionType-SessionType"></a>
The type of the session. Valid values are `TOKEN` and `SSO`.
Type: String
Valid Values: `TOKEN | SSO`
Required: No

## See Also
<a name="API_SessionDescriptionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SessionDescriptionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SessionDescriptionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SessionDescriptionType)
