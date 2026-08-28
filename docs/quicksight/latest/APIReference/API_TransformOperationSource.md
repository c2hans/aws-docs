---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TransformOperationSource.html
---

# TransformOperationSource
<a name="API_TransformOperationSource"></a>

Specifies the source of data for a transform operation, including the source operation and column mappings.

## Contents
<a name="API_TransformOperationSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TransformOperationId **   <a name="QS-Type-TransformOperationSource-TransformOperationId"></a>
The identifier of the transform operation that provides input data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-]*`
Required: Yes

 ** ColumnIdMappings **   <a name="QS-Type-TransformOperationSource-ColumnIdMappings"></a>
The mappings between source column identifiers and target column identifiers for this transformation.
Type: Array of [DataSetColumnIdMapping](API_DataSetColumnIdMapping.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Required: No

## See Also
<a name="API_TransformOperationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TransformOperationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TransformOperationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TransformOperationSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
