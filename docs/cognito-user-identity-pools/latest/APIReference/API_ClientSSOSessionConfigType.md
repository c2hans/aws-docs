---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ClientSSOSessionConfigType.html
---

# ClientSSOSessionConfigType
<a name="API_ClientSSOSessionConfigType"></a>

The SSO session settings for a user pool app client.

## Contents
<a name="API_ClientSSOSessionConfigType_Contents"></a>

 ** MaxValidityMinutes **   <a name="CognitoUserPools-Type-ClientSSOSessionConfigType-MaxValidityMinutes"></a>
The maximum amount of time, in minutes, that this app client silently reuses an existing SSO session, returning a new set of tokens without requiring the user to re-authenticate, measured from the user's last fresh authentication. The minimum value is `0` and the maximum value is `129600` (90 days). The default is `60`. A value of `0` means that this app client never silently reuses the SSO session and always re-authenticates the user. The SSO session record and its cookie are still created regardless of this value, and other app clients in the same user pool can still reuse the session.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 129600.
Required: Yes

## See Also
<a name="API_ClientSSOSessionConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ClientSSOSessionConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ClientSSOSessionConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ClientSSOSessionConfigType)
