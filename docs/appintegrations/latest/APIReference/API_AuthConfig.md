---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_AuthConfig.html
---

# AuthConfig
<a name="API_connect-app-integrations_AuthConfig"></a>

Contains the authentication settings that Connect Customer uses to call an external application endpoint.

## Contents
<a name="API_connect-app-integrations_AuthConfig_Contents"></a>

 ** AudienceOverride **   <a name="connect-Type-connect-app-integrations_AuthConfig-AudienceOverride"></a>
The value that Connect Customer uses as the audience (`aud`) claim of the JSON Web Token (JWT) that it issues. You can specify this parameter only when `AuthType` is `CONNECT_JWT`. If you don't specify it, the audience is the `AccessUrl` of the application. The value can't contain `connect.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: No

 ** AuthType **   <a name="connect-Type-connect-app-integrations_AuthConfig-AuthType"></a>
The type of authentication that Connect Customer uses to call the external application endpoint. You must specify an authentication type for `A2A_SERVER` applications. Valid values:
+  `API_KEY`: Connect Customer sends an API key that is stored in the AWS Secrets Manager secret that you specify in `CredentialProviderIdentifier`.
+  `CONNECT_JWT`: Connect Customer issues a short-lived, signed JSON Web Token (JWT). This authentication type doesn't require a stored credential.
Type: String
Valid Values: `API_KEY | CONNECT_JWT`
Required: No

 ** CredentialProviderIdentifier **   <a name="connect-Type-connect-app-integrations_AuthConfig-CredentialProviderIdentifier"></a>
The ARN of the AWS Secrets Manager secret that stores the credentials. The secret must be accessible to Connect Customer.
You must specify this ARN when `AuthType` is `API_KEY`. Don't specify it when `AuthType` is `CONNECT_JWT`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

## See Also
<a name="API_connect-app-integrations_AuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/AuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/AuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/AuthConfig)
