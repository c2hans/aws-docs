---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_QueryGenerationTable.html
---

# QueryGenerationTable
<a name="API_agent_QueryGenerationTable"></a>

Contains information about a table for the query engine to consider.

## Contents
<a name="API_agent_QueryGenerationTable_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_QueryGenerationTable-name"></a>
The name of the table for which the other fields in this object apply.
Type: String
Pattern: `.*\..*\..*`
Required: Yes

 ** columns **   <a name="bedrock-Type-agent_QueryGenerationTable-columns"></a>
An array of objects, each of which defines information about a column in the table.
Type: Array of [QueryGenerationColumn](API_agent_QueryGenerationColumn.md) objects
Required: No

 ** description **   <a name="bedrock-Type-agent_QueryGenerationTable-description"></a>
A description of the table that helps the query engine understand the contents of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** inclusion **   <a name="bedrock-Type-agent_QueryGenerationTable-inclusion"></a>
Specifies whether to include or exclude the table during query generation. If you specify `EXCLUDE`, the table will be ignored. If you specify `INCLUDE`, all other tables will be ignored.
Type: String
Valid Values: `INCLUDE | EXCLUDE`
Required: No

## See Also
<a name="API_agent_QueryGenerationTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/QueryGenerationTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/QueryGenerationTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/QueryGenerationTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
