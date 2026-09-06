---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_FailedItemDetails.html
---

# FailedItemDetails
<a name="API_FailedItemDetails"></a>

Includes details about the failed items.

## Contents
<a name="API_FailedItemDetails_Contents"></a>

 ** failureCode **   <a name="Inspector-Type-FailedItemDetails-failureCode"></a>
The status code of a failed item.
Type: String
Valid Values: `INVALID_ARN | DUPLICATE_ARN | ITEM_DOES_NOT_EXIST | ACCESS_DENIED | LIMIT_EXCEEDED | INTERNAL_ERROR`
Required: Yes

 ** retryable **   <a name="Inspector-Type-FailedItemDetails-retryable"></a>
Indicates whether you can immediately retry a request for this item for a specified resource.
Type: Boolean
Required: Yes

## See Also
<a name="API_FailedItemDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/FailedItemDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/FailedItemDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/FailedItemDetails)
