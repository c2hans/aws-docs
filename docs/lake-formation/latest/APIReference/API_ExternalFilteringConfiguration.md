---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ExternalFilteringConfiguration.html
---

# ExternalFilteringConfiguration
<a name="API_ExternalFilteringConfiguration"></a>

Configuration for enabling external data filtering for third-party applications to access data managed by Lake Formation .

## Contents
<a name="API_ExternalFilteringConfiguration_Contents"></a>

 ** AuthorizedTargets **   <a name="lakeformation-Type-ExternalFilteringConfiguration-AuthorizedTargets"></a>
List of third-party application `ARNs` integrated with Lake Formation.
Type: Array of strings
Required: Yes

 ** Status **   <a name="lakeformation-Type-ExternalFilteringConfiguration-Status"></a>
Allows to enable or disable the third-party applications that are allowed to access data managed by Lake Formation.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_ExternalFilteringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ExternalFilteringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ExternalFilteringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ExternalFilteringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
