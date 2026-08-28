---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RelationalTable.html
---

# RelationalTable
<a name="API_RelationalTable"></a>

A physical table type for relational data sources.

## Contents
<a name="API_RelationalTable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSourceArn **   <a name="QS-Type-RelationalTable-DataSourceArn"></a>
The Amazon Resource Name (ARN) for the data source.
Type: String
Required: Yes

 ** InputColumns **   <a name="QS-Type-RelationalTable-InputColumns"></a>
The column schema of the table.
Type: Array of [InputColumn](API_InputColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

 ** Name **   <a name="QS-Type-RelationalTable-Name"></a>
The name of the relational table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Catalog **   <a name="QS-Type-RelationalTable-Catalog"></a>
The catalog associated with a table.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Schema **   <a name="QS-Type-RelationalTable-Schema"></a>
The schema name. This name applies to certain relational database engines.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_RelationalTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RelationalTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RelationalTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RelationalTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
