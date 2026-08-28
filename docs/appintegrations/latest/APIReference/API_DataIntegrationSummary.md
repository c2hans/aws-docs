---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationSummary.html
---

# DataIntegrationSummary
<a name="API_connect-app-integrations_DataIntegrationSummary"></a>

Summary information about the DataIntegration.

## Contents
<a name="API_connect-app-integrations_DataIntegrationSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-connect-app-integrations_DataIntegrationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** Name **   <a name="connect-Type-connect-app-integrations_DataIntegrationSummary-Name"></a>
The name of the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

 ** SourceURI **   <a name="connect-Type-connect-app-integrations_DataIntegrationSummary-SourceURI"></a>
The URI of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+$)|(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+[\w/!@#+=.-]+[\w/!@#+=.,-]+$)`
Required: No

## See Also
<a name="API_connect-app-integrations_DataIntegrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/DataIntegrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/DataIntegrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/DataIntegrationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
