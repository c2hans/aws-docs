---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KnowledgeBaseSearchFilter.html
---

# KnowledgeBaseSearchFilter
<a name="API_KnowledgeBaseSearchFilter"></a>

A filter to apply when searching knowledge bases.

## Contents
<a name="API_KnowledgeBaseSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="QS-Type-KnowledgeBaseSearchFilter-name"></a>
The name of the field to filter on.
Type: String
Valid Values: `KNOWLEDGE_BASE_ID | KNOWLEDGE_BASE_NAME | DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_VIEWER_OR_OWNER | DIRECT_QUICKSIGHT_SOLE_OWNER | KNOWLEDGE_BASE_SIZE_BYTES | PRIMARY_OWNER | DATASOURCE_ARN`
Required: Yes

 ** operator **   <a name="QS-Type-KnowledgeBaseSearchFilter-operator"></a>
The comparison operator to use for the filter.
Type: String
Valid Values: `STRING_EQUALS | STRING_LIKE | GREATER_THAN_OR_EQUALS | LESS_THAN_OR_EQUALS`
Required: Yes

 ** value **   <a name="QS-Type-KnowledgeBaseSearchFilter-value"></a>
The value to filter on.
Type: String
Required: Yes

## See Also
<a name="API_KnowledgeBaseSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KnowledgeBaseSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KnowledgeBaseSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KnowledgeBaseSearchFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
