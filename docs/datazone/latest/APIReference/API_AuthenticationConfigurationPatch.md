---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AuthenticationConfigurationPatch.html
---

# AuthenticationConfigurationPatch
<a name="API_AuthenticationConfigurationPatch"></a>

The authentication configuration patch of a connection.

## Contents
<a name="API_AuthenticationConfigurationPatch_Contents"></a>

 ** basicAuthenticationCredentials **   <a name="datazone-Type-AuthenticationConfigurationPatch-basicAuthenticationCredentials"></a>
The basic authentication credentials of a connection.
Type: [BasicAuthenticationCredentials](API_BasicAuthenticationCredentials.md) object
Required: No

 ** secretArn **   <a name="datazone-Type-AuthenticationConfigurationPatch-secretArn"></a>
The secret ARN of a connection.
Type: String
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*`
Required: No

## See Also
<a name="API_AuthenticationConfigurationPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AuthenticationConfigurationPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AuthenticationConfigurationPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AuthenticationConfigurationPatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
