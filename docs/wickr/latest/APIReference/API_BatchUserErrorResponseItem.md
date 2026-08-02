---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchUserErrorResponseItem.html
---

# BatchUserErrorResponseItem
<a name="API_BatchUserErrorResponseItem"></a>

Contains error information for a user operation that failed in a batch user request.

## Contents
<a name="API_BatchUserErrorResponseItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** userId **   <a name="wickr-Type-BatchUserErrorResponseItem-userId"></a>
The user ID associated with the failed operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`
Required: Yes

 ** field **   <a name="wickr-Type-BatchUserErrorResponseItem-field"></a>
The field that caused the error.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** reason **   <a name="wickr-Type-BatchUserErrorResponseItem-reason"></a>
A description of why the user operation failed.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_BatchUserErrorResponseItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/BatchUserErrorResponseItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/BatchUserErrorResponseItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/BatchUserErrorResponseItem)
