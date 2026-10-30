---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DiffItems.html
---

# DiffItems
<a name="API_DiffItems"></a>

The items that differ within one metadata category.

## Contents
<a name="API_DiffItems_Contents"></a>

 ** Diverged **   <a name="opensearchservice-Type-DiffItems-Diverged"></a>
The items that exist on both domains but differ, with the diverging fields.
Type: Array of [DivergentItem](API_DivergentItem.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** SourceOnly **   <a name="opensearchservice-Type-DiffItems-SourceOnly"></a>
The names of items that exist only on the source domain.
Type: Array of strings
Array Members: Maximum number of 1000 items.
Length Constraints: Maximum length of 256.
Required: No

 ** TargetOnly **   <a name="opensearchservice-Type-DiffItems-TargetOnly"></a>
The names of items that exist only on the target domain.
Type: Array of strings
Array Members: Maximum number of 1000 items.
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_DiffItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DiffItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DiffItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DiffItems)
