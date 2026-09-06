---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_BatchPutProfileObjectRequestItem.html
---

# BatchPutProfileObjectRequestItem
<a name="API_connect-customer-profiles_BatchPutProfileObjectRequestItem"></a>

An item to add to the domain as part of a batch request.

## Contents
<a name="API_connect-customer-profiles_BatchPutProfileObjectRequestItem_Contents"></a>

 ** Id **   <a name="connect-Type-connect-customer-profiles_BatchPutProfileObjectRequestItem-Id"></a>
A unique identifier for this item in the batch request. Used to correlate items in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** Object **   <a name="connect-Type-connect-customer-profiles_BatchPutProfileObjectRequestItem-Object"></a>
A string that is serialized from a JSON object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256000.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_BatchPutProfileObjectRequestItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/BatchPutProfileObjectRequestItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/BatchPutProfileObjectRequestItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/BatchPutProfileObjectRequestItem)
