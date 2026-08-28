---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetSemanticMetadata.html
---

# DataSetSemanticMetadata
<a name="API_DataSetSemanticMetadata"></a>

Semantic metadata for a dataset, including a description and custom instructions.

## Contents
<a name="API_DataSetSemanticMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomInstructions **   <a name="QS-Type-DataSetSemanticMetadata-CustomInstructions"></a>
A list of custom instructions that guide how the dataset should be consumed.
Type: Array of [CustomInstruction](API_CustomInstruction.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** Description **   <a name="QS-Type-DataSetSemanticMetadata-Description"></a>
A description of the dataset.
Type: [DataSetSemanticDescription](API_DataSetSemanticDescription.md) object
Required: No

## See Also
<a name="API_DataSetSemanticMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetSemanticMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetSemanticMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetSemanticMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
