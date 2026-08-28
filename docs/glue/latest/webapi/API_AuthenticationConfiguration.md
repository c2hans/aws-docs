---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AuthenticationConfiguration.html
---

# AuthenticationConfiguration
<a name="API_AuthenticationConfiguration"></a>

A structure containing the authentication configuration.

## Contents
<a name="API_AuthenticationConfiguration_Contents"></a>

 ** AuthenticationType **   <a name="Glue-Type-AuthenticationConfiguration-AuthenticationType"></a>
A structure containing the authentication configuration.
Type: String
Valid Values: `BASIC | OAUTH2 | CUSTOM | IAM`
Required: No

 ** KmsKeyArn **   <a name="Glue-Type-AuthenticationConfiguration-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt sensitive authentication information. This key is used to protect credentials and other sensitive data stored within the authentication configuration.
Type: String
Pattern: `^$|arn:aws[a-z0-9-]*:kms:.*`
Required: No

 ** OAuth2Properties **   <a name="Glue-Type-AuthenticationConfiguration-OAuth2Properties"></a>
The properties for OAuth2 authentication.
Type: [OAuth2Properties](API_OAuth2Properties.md) object
Required: No

 ** SecretArn **   <a name="Glue-Type-AuthenticationConfiguration-SecretArn"></a>
The secret manager ARN to store credentials.
Type: String
Pattern: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*$`
Required: No

## See Also
<a name="API_AuthenticationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AuthenticationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AuthenticationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AuthenticationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
