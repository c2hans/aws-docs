---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AuthenticationConfigurationInput.html
---

# AuthenticationConfigurationInput
<a name="API_AuthenticationConfigurationInput"></a>

A structure containing the authentication configuration in the CreateConnection request.

## Contents
<a name="API_AuthenticationConfigurationInput_Contents"></a>

 ** AuthenticationType **   <a name="Glue-Type-AuthenticationConfigurationInput-AuthenticationType"></a>
A structure containing the authentication configuration in the CreateConnection request.
Type: String
Valid Values: `BASIC | OAUTH2 | CUSTOM | IAM`
Required: No

 ** BasicAuthenticationCredentials **   <a name="Glue-Type-AuthenticationConfigurationInput-BasicAuthenticationCredentials"></a>
The credentials used when the authentication type is basic authentication.
Type: [BasicAuthenticationCredentials](API_BasicAuthenticationCredentials.md) object
Required: No

 ** CustomAuthenticationCredentials **   <a name="Glue-Type-AuthenticationConfigurationInput-CustomAuthenticationCredentials"></a>
The credentials used when the authentication type is custom authentication.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** KmsKeyArn **   <a name="Glue-Type-AuthenticationConfigurationInput-KmsKeyArn"></a>
The ARN of the KMS key used to encrypt the connection. Only taken an as input in the request and stored in the Secret Manager.
Type: String
Pattern: `^$|arn:aws[a-z0-9-]*:kms:.*`
Required: No

 ** OAuth2Properties **   <a name="Glue-Type-AuthenticationConfigurationInput-OAuth2Properties"></a>
The properties for OAuth2 authentication in the CreateConnection request.
Type: [OAuth2PropertiesInput](API_OAuth2PropertiesInput.md) object
Required: No

 ** SecretArn **   <a name="Glue-Type-AuthenticationConfigurationInput-SecretArn"></a>
The secret manager ARN to store credentials in the CreateConnection request.
Type: String
Pattern: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*$`
Required: No

## See Also
<a name="API_AuthenticationConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AuthenticationConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AuthenticationConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AuthenticationConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
