---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RelationalFilterConfiguration.html
---

# RelationalFilterConfiguration
<a name="API_RelationalFilterConfiguration"></a>

The relational filter configuration for the data source.

## Contents
<a name="API_RelationalFilterConfiguration_Contents"></a>

 ** databaseName **   <a name="datazone-Type-RelationalFilterConfiguration-databaseName"></a>
The database name specified in the relational filter configuration for the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** filterExpressions **   <a name="datazone-Type-RelationalFilterConfiguration-filterExpressions"></a>
The filter expressions specified in the relational filter configuration for the data source.
Type: Array of [FilterExpression](API_FilterExpression.md) objects
Required: No

 ** schemaName **   <a name="datazone-Type-RelationalFilterConfiguration-schemaName"></a>
The schema name specified in the relational filter configuration for the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_RelationalFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RelationalFilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RelationalFilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RelationalFilterConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
