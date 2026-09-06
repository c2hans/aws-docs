---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html
---

# OnlineStoreConfig
<a name="API_OnlineStoreConfig"></a>

Use this to specify the AWS Key Management Service (KMS) Key ID, or `KMSKeyId`, for at rest data encryption. You can turn `OnlineStore` on or off by specifying the `EnableOnlineStore` flag at General Assembly.

The default value is `False`.

## Contents
<a name="API_OnlineStoreConfig_Contents"></a>

 ** EnableOnlineStore **   <a name="sagemaker-Type-OnlineStoreConfig-EnableOnlineStore"></a>
Turn `OnlineStore` off by specifying `False` for the `EnableOnlineStore` flag. Turn `OnlineStore` on by specifying `True` for the `EnableOnlineStore` flag.
The default value is `False`.
Type: Boolean
Required: No

 ** SecurityConfig **   <a name="sagemaker-Type-OnlineStoreConfig-SecurityConfig"></a>
Use to specify KMS Key ID (`KMSKeyId`) for at-rest encryption of your `OnlineStore`.
Type: [OnlineStoreSecurityConfig](API_OnlineStoreSecurityConfig.md) object
Required: No

 ** StorageType **   <a name="sagemaker-Type-OnlineStoreConfig-StorageType"></a>
Option for different tiers of low latency storage for real-time data retrieval.
+  `Standard`: A managed low latency data store for feature groups.
+  `Standard_V2`: A managed low latency data store for feature groups that supports partial updates to individual features using the [UpdateRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html) operation. Choose this storage type at feature group creation time if your use case requires updating specific feature values without rewriting the entire record.
+  `InMemory`: A managed data store for feature groups that supports very low latency retrieval.
Type: String
Valid Values: `Standard | Standard_V2 | InMemory`
Required: No

 ** TtlDuration **   <a name="sagemaker-Type-OnlineStoreConfig-TtlDuration"></a>
Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` \+ `TtlDuration`. For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.
Type: [TtlDuration](API_TtlDuration.md) object
Required: No

## See Also
<a name="API_OnlineStoreConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OnlineStoreConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OnlineStoreConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OnlineStoreConfig)
