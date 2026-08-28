---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DatadogConnectorProfileCredentials.html
---

# DatadogConnectorProfileCredentials
<a name="API_DatadogConnectorProfileCredentials"></a>

 The connector-specific credentials required by Datadog.

## Contents
<a name="API_DatadogConnectorProfileCredentials_Contents"></a>

 ** apiKey **   <a name="appflow-Type-DatadogConnectorProfileCredentials-apiKey"></a>
 A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** applicationKey **   <a name="appflow-Type-DatadogConnectorProfileCredentials-applicationKey"></a>
 Application keys, in conjunction with your API key, give you full access to Datadog’s programmatic API. Application keys are associated with the user account that created them. The application key is used to log all requests made to the API.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

## See Also
<a name="API_DatadogConnectorProfileCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DatadogConnectorProfileCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DatadogConnectorProfileCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DatadogConnectorProfileCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
