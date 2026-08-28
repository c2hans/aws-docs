---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ApiKeyCredentials.html
---

# ApiKeyCredentials
<a name="API_ApiKeyCredentials"></a>

The API key credentials required for API key authentication.

## Contents
<a name="API_ApiKeyCredentials_Contents"></a>

 ** apiKey **   <a name="appflow-Type-ApiKeyCredentials-apiKey"></a>
The API key required for API key authentication.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** apiSecretKey **   <a name="appflow-Type-ApiKeyCredentials-apiSecretKey"></a>
The API secret key required for API key authentication.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

## See Also
<a name="API_ApiKeyCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ApiKeyCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ApiKeyCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ApiKeyCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
