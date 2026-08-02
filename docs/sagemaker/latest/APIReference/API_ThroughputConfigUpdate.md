---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ThroughputConfigUpdate.html
---

# ThroughputConfigUpdate
<a name="API_ThroughputConfigUpdate"></a>

The new throughput configuration for the feature group. You can switch between on-demand and provisioned modes or update the read / write capacity of provisioned feature groups. You can switch a feature group to on-demand only once in a 24 hour period.

## Contents
<a name="API_ThroughputConfigUpdate_Contents"></a>

 ** ProvisionedReadCapacityUnits **   <a name="sagemaker-Type-ThroughputConfigUpdate-ProvisionedReadCapacityUnits"></a>
For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

 ** ProvisionedWriteCapacityUnits **   <a name="sagemaker-Type-ThroughputConfigUpdate-ProvisionedWriteCapacityUnits"></a>
For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

 ** ThroughputMode **   <a name="sagemaker-Type-ThroughputConfigUpdate-ThroughputMode"></a>
Target throughput mode of the feature group. Throughput update is an asynchronous operation, and the outcome should be monitored by polling `LastUpdateStatus` field in `DescribeFeatureGroup` response. You cannot update a feature group's throughput while another update is in progress.
Type: String
Valid Values: `OnDemand | Provisioned`
Required: No

## See Also
<a name="API_ThroughputConfigUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ThroughputConfigUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ThroughputConfigUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ThroughputConfigUpdate)
