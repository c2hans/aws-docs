---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BasicAuthenticationCredentials.html
---

# BasicAuthenticationCredentials
<a name="API_BasicAuthenticationCredentials"></a>

For supplying basic auth credentials when not providing a `SecretArn` value.

## Contents
<a name="API_BasicAuthenticationCredentials_Contents"></a>

 ** Password **   <a name="Glue-Type-BasicAuthenticationCredentials-Password"></a>
The password to connect to the data source.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** Username **   <a name="Glue-Type-BasicAuthenticationCredentials-Username"></a>
The username to connect to the data source.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

## See Also
<a name="API_BasicAuthenticationCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BasicAuthenticationCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BasicAuthenticationCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BasicAuthenticationCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
