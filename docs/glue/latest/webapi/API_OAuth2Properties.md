---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_OAuth2Properties.html
---

# OAuth2Properties
<a name="API_OAuth2Properties"></a>

A structure containing properties for OAuth2 authentication.

## Contents
<a name="API_OAuth2Properties_Contents"></a>

 ** OAuth2ClientApplication **   <a name="Glue-Type-OAuth2Properties-OAuth2ClientApplication"></a>
The client application type. For example, AWS\_MANAGED or USER\_MANAGED.
Type: [OAuth2ClientApplication](API_OAuth2ClientApplication.md) object
Required: No

 ** OAuth2GrantType **   <a name="Glue-Type-OAuth2Properties-OAuth2GrantType"></a>
The OAuth2 grant type. For example, `AUTHORIZATION_CODE`, `JWT_BEARER`, or `CLIENT_CREDENTIALS`.
Type: String
Valid Values: `AUTHORIZATION_CODE | CLIENT_CREDENTIALS | JWT_BEARER`
Required: No

 ** TokenUrl **   <a name="Glue-Type-OAuth2Properties-TokenUrl"></a>
The URL of the provider's authentication server, to exchange an authorization code for an access token.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

 ** TokenUrlParametersMap **   <a name="Glue-Type-OAuth2Properties-TokenUrlParametersMap"></a>
A map of parameters that are added to the token `GET` request.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_OAuth2Properties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/OAuth2Properties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/OAuth2Properties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/OAuth2Properties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
