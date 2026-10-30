---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CategoryDiffResult.html
---

# CategoryDiffResult
<a name="API_CategoryDiffResult"></a>

The result of comparing one metadata category between two domains.

## Contents
<a name="API_CategoryDiffResult_Contents"></a>

 ** Diverged **   <a name="opensearchservice-Type-CategoryDiffResult-Diverged"></a>
The number of items that exist on both domains but differ.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** InSync **   <a name="opensearchservice-Type-CategoryDiffResult-InSync"></a>
The number of items that are identical on both domains.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Items **   <a name="opensearchservice-Type-CategoryDiffResult-Items"></a>
The names of the items that differ, and for diverging items, the fields that differ.
Type: [DiffItems](API_DiffItems.md) object
Required: No

 ** SourceOnly **   <a name="opensearchservice-Type-CategoryDiffResult-SourceOnly"></a>
The number of items that exist only on the source domain.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Status **   <a name="opensearchservice-Type-CategoryDiffResult-Status"></a>
Whether the category was compared successfully. `compared` means the result is complete; `error` means the category could not be read.
Type: String
Valid Values: `compared | error`
Required: No

 ** TargetOnly **   <a name="opensearchservice-Type-CategoryDiffResult-TargetOnly"></a>
The number of items that exist only on the target domain.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Truncated **   <a name="opensearchservice-Type-CategoryDiffResult-Truncated"></a>
Whether `Items` omits some differences because the category contained more than the response can carry. The counts remain complete when this is `true`.
Type: Boolean
Required: No

## See Also
<a name="API_CategoryDiffResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CategoryDiffResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CategoryDiffResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CategoryDiffResult)
