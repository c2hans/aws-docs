---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Credentials.html
---

# Credentials
<a name="API_Credentials"></a>

Contains credentials to use for federation.

## Contents
<a name="API_Credentials_Contents"></a>

 ** AccessToken **   <a name="connect-Type-Credentials-AccessToken"></a>
An access token generated for a federated user to access Connect Customer.
Type: String
Required: No

 ** AccessTokenExpiration **   <a name="connect-Type-Credentials-AccessTokenExpiration"></a>
A token generated with an expiration time for the session a user is logged in to Connect Customer.
Type: Timestamp
Required: No

 ** RefreshToken **   <a name="connect-Type-Credentials-RefreshToken"></a>
Renews a token generated for a user to access the Connect Customer instance.
Type: String
Required: No

 ** RefreshTokenExpiration **   <a name="connect-Type-Credentials-RefreshTokenExpiration"></a>
Renews the expiration timer for a generated token.
Type: Timestamp
Required: No

## See Also
<a name="API_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Credentials)
