---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FMKBParameters.html
---

# FMKBParameters
<a name="API_FMKBParameters"></a>

The connection parameters for a fully managed knowledge base data source. Provide these parameters in the `DataSourceParameters` object when you create or update a data source that uses a fully managed knowledge base.

## Contents
<a name="API_FMKBParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** KnowledgeBaseArn **   <a name="QS-Type-FMKBParameters-KnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the Amazon Bedrock knowledge base.
Type: String
Length Constraints: Minimum length of 47. Maximum length of 128.
Pattern: `^arn:aws(-cn|-us-gov)?:bedrock:[a-zA-Z0-9-]*:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+`
Required: Yes

 ** LinkedDataSourceIds **   <a name="QS-Type-FMKBParameters-LinkedDataSourceIds"></a>
The IDs of the linked data sources.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

## See Also
<a name="API_FMKBParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FMKBParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FMKBParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FMKBParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
