---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_QueryDefinition.html
---

# QueryDefinition
<a name="API_QueryDefinition"></a>

This structure contains details about a saved CloudWatch Logs Insights query definition.

## Contents
<a name="API_QueryDefinition_Contents"></a>

 ** lastModified **   <a name="CWL-Type-QueryDefinition-lastModified"></a>
The date that the query definition was most recently modified.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logGroupNames **   <a name="CWL-Type-QueryDefinition-logGroupNames"></a>
If this query definition contains a list of log groups that it is limited to, that list appears here.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** name **   <a name="CWL-Type-QueryDefinition-name"></a>
The name of the query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** parameters **   <a name="CWL-Type-QueryDefinition-parameters"></a>
If this query definition contains a list of query parameters that define placeholder variables for the query string, that list appears here.
Type: Array of [QueryParameter](API_QueryParameter.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** queryDefinitionId **   <a name="CWL-Type-QueryDefinition-queryDefinitionId"></a>
The unique ID of the query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** queryLanguage **   <a name="CWL-Type-QueryDefinition-queryLanguage"></a>
The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see [Supported query languages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html).
Type: String
Valid Values: `CWLI | SQL | PPL`
Required: No

 ** queryString **   <a name="CWL-Type-QueryDefinition-queryString"></a>
The query string to use for this definition. For more information, see [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

## See Also
<a name="API_QueryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/QueryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/QueryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/QueryDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
