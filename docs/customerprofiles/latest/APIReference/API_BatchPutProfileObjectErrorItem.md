---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_BatchPutProfileObjectErrorItem.html
---

# BatchPutProfileObjectErrorItem
<a name="API_connect-customer-profiles_BatchPutProfileObjectErrorItem"></a>

An item that failed to be added to the domain.

## Contents
<a name="API_connect-customer-profiles_BatchPutProfileObjectErrorItem_Contents"></a>

 ** Code **   <a name="connect-Type-connect-customer-profiles_BatchPutProfileObjectErrorItem-Code"></a>
The HTTP status code for the error.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 599.
Required: Yes

 ** Id **   <a name="connect-Type-connect-customer-profiles_BatchPutProfileObjectErrorItem-Id"></a>
The unique identifier of the item in the batch request that failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** Message **   <a name="connect-Type-connect-customer-profiles_BatchPutProfileObjectErrorItem-Message"></a>
A message describing the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_connect-customer-profiles_BatchPutProfileObjectErrorItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/BatchPutProfileObjectErrorItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/BatchPutProfileObjectErrorItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/BatchPutProfileObjectErrorItem)
