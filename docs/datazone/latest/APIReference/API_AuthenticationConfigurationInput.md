---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AuthenticationConfigurationInput.html
---

# AuthenticationConfigurationInput
<a name="API_AuthenticationConfigurationInput"></a>

The authentication configuration of a connection.

## Contents
<a name="API_AuthenticationConfigurationInput_Contents"></a>

 ** authenticationType **   <a name="datazone-Type-AuthenticationConfigurationInput-authenticationType"></a>
The authentication type of a connection.
Type: String
Valid Values: `BASIC | OAUTH2 | CUSTOM`
Required: No

 ** basicAuthenticationCredentials **   <a name="datazone-Type-AuthenticationConfigurationInput-basicAuthenticationCredentials"></a>
The basic authentication credentials of a connection.
Type: [BasicAuthenticationCredentials](API_BasicAuthenticationCredentials.md) object
Required: No

 ** customAuthenticationCredentials **   <a name="datazone-Type-AuthenticationConfigurationInput-customAuthenticationCredentials"></a>
The custom authentication credentials of a connection.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** kmsKeyArn **   <a name="datazone-Type-AuthenticationConfigurationInput-kmsKeyArn"></a>
The KMS key ARN of a connection.
Type: String
Pattern: `$|arn:aws[a-z0-9-]*:kms:.*`
Required: No

 ** oAuth2Properties **   <a name="datazone-Type-AuthenticationConfigurationInput-oAuth2Properties"></a>
The oAuth2 properties of a connection.
Type: [OAuth2Properties](API_OAuth2Properties.md) object
Required: No

 ** secretArn **   <a name="datazone-Type-AuthenticationConfigurationInput-secretArn"></a>
The secret ARN of a connection.
Type: String
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*`
Required: No

## See Also
<a name="API_AuthenticationConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AuthenticationConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AuthenticationConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AuthenticationConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
