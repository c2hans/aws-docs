---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfigUpdate.html
---

# OnlineStoreConfigUpdate
<a name="API_OnlineStoreConfigUpdate"></a>

Updates the feature group online store configuration.

## Contents
<a name="API_OnlineStoreConfigUpdate_Contents"></a>

 ** StorageType **   <a name="sagemaker-Type-OnlineStoreConfigUpdate-StorageType"></a>
The online store storage type to migrate the feature group to. Use this parameter to migrate an existing feature group from `Standard` to `Standard_V2` storage format, enabling support for the [UpdateRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html) operation. Migration is a one-way operation and cannot be reversed.
Type: String
Valid Values: `Standard | Standard_V2 | InMemory`
Required: No

 ** TtlDuration **   <a name="sagemaker-Type-OnlineStoreConfigUpdate-TtlDuration"></a>
Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` \+ `TtlDuration`. For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.
Type: [TtlDuration](API_TtlDuration.md) object
Required: No

## See Also
<a name="API_OnlineStoreConfigUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OnlineStoreConfigUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OnlineStoreConfigUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OnlineStoreConfigUpdate)
