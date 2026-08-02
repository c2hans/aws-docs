---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OfflineStoreStatus.html
---

# OfflineStoreStatus
<a name="API_OfflineStoreStatus"></a>

The status of `OfflineStore`.

## Contents
<a name="API_OfflineStoreStatus_Contents"></a>

 ** Status **   <a name="sagemaker-Type-OfflineStoreStatus-Status"></a>
An `OfflineStore` status.
Type: String
Valid Values: `Active | Blocked | Disabled`
Required: Yes

 ** BlockedReason **   <a name="sagemaker-Type-OfflineStoreStatus-BlockedReason"></a>
The justification for why the OfflineStoreStatus is Blocked (if applicable).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_OfflineStoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OfflineStoreStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OfflineStoreStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OfflineStoreStatus)
