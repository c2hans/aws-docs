---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_OAuth2ClientCredentialConfiguration.html
---

# OAuth2ClientCredentialConfiguration
<a name="API_OAuth2ClientCredentialConfiguration"></a>

Information about the OAuth 2.0 authentication credential/token used to configure a plugin.

## Contents
<a name="API_OAuth2ClientCredentialConfiguration_Contents"></a>

 ** roleArn **   <a name="qbusiness-Type-OAuth2ClientCredentialConfiguration-roleArn"></a>
The ARN of an IAM role used by Amazon Q Business to access the OAuth 2.0 authentication credentials stored in a Secrets Manager secret.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** secretArn **   <a name="qbusiness-Type-OAuth2ClientCredentialConfiguration-secretArn"></a>
The ARN of the Secrets Manager secret that stores the OAuth 2.0 credentials/token used for plugin configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** authorizationUrl **   <a name="qbusiness-Type-OAuth2ClientCredentialConfiguration-authorizationUrl"></a>
The redirect URL required by the OAuth 2.0 protocol for Amazon Q Business to authenticate a plugin user through a third party authentication server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`
Required: No

 ** tokenUrl **   <a name="qbusiness-Type-OAuth2ClientCredentialConfiguration-tokenUrl"></a>
The URL required by the OAuth 2.0 protocol to exchange an end user authorization code for an access token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`
Required: No

## See Also
<a name="API_OAuth2ClientCredentialConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/OAuth2ClientCredentialConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/OAuth2ClientCredentialConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/OAuth2ClientCredentialConfiguration)
