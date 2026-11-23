---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListDatasetExamplesFilter.html
---

# ListDatasetExamplesFilter

 A filter for `ListDatasetExamples`.

## Contents
<a name="API_ListDatasetExamplesFilter_Contents"></a>

 ** exampleFields **   <a name="bedrockagentcorecontrol-Type-ListDatasetExamplesFilter-exampleFields"></a>
 Returns only examples that meet at least one of these conditions. Examples last written before example field filtering was available never match.
Type: Array of [ExampleFieldCondition](API_ExampleFieldCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

 ** generationIds **   <a name="bedrockagentcorecontrol-Type-ListDatasetExamplesFilter-generationIds"></a>
 Returns only examples created by this dataset generation. Specify one ID.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
Required: No

## See Also
<a name="API_ListDatasetExamplesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListDatasetExamplesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListDatasetExamplesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListDatasetExamplesFilter)
