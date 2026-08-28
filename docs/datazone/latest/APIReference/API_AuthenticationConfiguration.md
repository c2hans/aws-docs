---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AuthenticationConfiguration.html
---

# AuthenticationConfiguration
<a name="API_AuthenticationConfiguration"></a>

The authentication configuration of a connection.

## Contents
<a name="API_AuthenticationConfiguration_Contents"></a>

 ** authenticationType **   <a name="datazone-Type-AuthenticationConfiguration-authenticationType"></a>
The authentication type of a connection.
Type: String
Valid Values: `BASIC | OAUTH2 | CUSTOM`
Required: No

 ** oAuth2Properties **   <a name="datazone-Type-AuthenticationConfiguration-oAuth2Properties"></a>
The oAuth2 properties of a connection.
Type: [OAuth2Properties](API_OAuth2Properties.md) object
Required: No

 ** secretArn **   <a name="datazone-Type-AuthenticationConfiguration-secretArn"></a>
The secret ARN of a connection.
Type: String
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*`
Required: No

## See Also
<a name="API_AuthenticationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AuthenticationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AuthenticationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AuthenticationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
