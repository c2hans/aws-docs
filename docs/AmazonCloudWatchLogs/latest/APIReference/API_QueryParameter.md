---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_QueryParameter.html
---

# QueryParameter
<a name="API_QueryParameter"></a>

This structure defines a query parameter for a saved CloudWatch Logs Insights query definition. Query parameters are supported only for Logs Insights QL queries. They are placeholder variables that you can reference in a query string using the `{{parameterName}}` syntax. Each parameter can include a default value and a description.

## Contents
<a name="API_QueryParameter_Contents"></a>

 ** name **   <a name="CWL-Type-QueryParameter-name"></a>
The name of the query parameter. A query parameter name must start with a letter or underscore, and contain only letters, digits, and underscores.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z_][a-zA-Z0-9_]*`
Required: Yes

 ** defaultValue **   <a name="CWL-Type-QueryParameter-defaultValue"></a>
The default value to use for this query parameter if no value is supplied at execution time.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** description **   <a name="CWL-Type-QueryParameter-description"></a>
A description of the query parameter that explains its purpose or expected values.
Type: String
Length Constraints: Maximum length of 512.
Required: No

## See Also
<a name="API_QueryParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/QueryParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/QueryParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/QueryParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
