---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ThroughputConfigDescription.html
---

# ThroughputConfigDescription
<a name="API_ThroughputConfigDescription"></a>

Active throughput configuration of the feature group. There are two modes: `ON_DEMAND` and `PROVISIONED`. With on-demand mode, you are charged for data reads and writes that your application performs on your feature group. You do not need to specify read and write throughput because Feature Store accommodates your workloads as they ramp up and down. You can switch a feature group to on-demand only once in a 24 hour period. With provisioned throughput mode, you specify the read and write capacity per second that you expect your application to require, and you are billed based on those limits. Exceeding provisioned throughput will result in your requests being throttled.

Note: `PROVISIONED` throughput mode is supported only for feature groups that are offline-only, or use the [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType) tier online store.

## Contents
<a name="API_ThroughputConfigDescription_Contents"></a>

 ** ThroughputMode **   <a name="sagemaker-Type-ThroughputConfigDescription-ThroughputMode"></a>
The mode used for your feature group throughput: `ON_DEMAND` or `PROVISIONED`.
Type: String
Valid Values: `OnDemand | Provisioned`
Required: Yes

 ** ProvisionedReadCapacityUnits **   <a name="sagemaker-Type-ThroughputConfigDescription-ProvisionedReadCapacityUnits"></a>
 For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling.
This field is not applicable for on-demand feature groups.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

 ** ProvisionedWriteCapacityUnits **   <a name="sagemaker-Type-ThroughputConfigDescription-ProvisionedWriteCapacityUnits"></a>
 For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling.
This field is not applicable for on-demand feature groups.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

## See Also
<a name="API_ThroughputConfigDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ThroughputConfigDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ThroughputConfigDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ThroughputConfigDescription)
