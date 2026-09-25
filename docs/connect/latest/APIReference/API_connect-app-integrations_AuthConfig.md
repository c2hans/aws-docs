---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_AuthConfig.html
---

# AuthConfig
<a name="API_connect-app-integrations_AuthConfig"></a>

Contains the authentication settings that Connect Customer uses to call an external application endpoint. The configuration includes the authentication type and credential location.

## Contents
<a name="API_connect-app-integrations_AuthConfig_Contents"></a>

 ** AuthType **   <a name="connect-Type-connect-app-integrations_AuthConfig-AuthType"></a>
The type of authentication used when calling the external application.
Type: String
Valid Values: `API_KEY`
Required: No

 ** CredentialProviderIdentifier **   <a name="connect-Type-connect-app-integrations_AuthConfig-CredentialProviderIdentifier"></a>
The ARN of the AWS Secrets Manager secret that stores the credentials. The secret must be accessible to Connect Customer.
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
