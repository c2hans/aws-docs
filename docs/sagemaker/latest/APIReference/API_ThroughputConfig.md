---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ThroughputConfig.html
---

# ThroughputConfig
<a name="API_ThroughputConfig"></a>

Used to set feature group throughput configuration. There are two modes: `ON_DEMAND` and `PROVISIONED`. With on-demand mode, you are charged for data reads and writes that your application performs on your feature group. You do not need to specify read and write throughput because Feature Store accommodates your workloads as they ramp up and down. You can switch a feature group to on-demand only once in a 24 hour period. With provisioned throughput mode, you specify the read and write capacity per second that you expect your application to require, and you are billed based on those limits. Exceeding provisioned throughput will result in your requests being throttled.

Note: `PROVISIONED` throughput mode is supported only for feature groups that are offline-only, or use the [`Standard`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType) tier online store.

## Contents
<a name="API_ThroughputConfig_Contents"></a>

 ** ThroughputMode **   <a name="sagemaker-Type-ThroughputConfig-ThroughputMode"></a>
The mode used for your feature group throughput: `ON_DEMAND` or `PROVISIONED`.
Type: String
Valid Values: `OnDemand | Provisioned`
Required: Yes

 ** ProvisionedReadCapacityUnits **   <a name="sagemaker-Type-ThroughputConfig-ProvisionedReadCapacityUnits"></a>
 For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling.
This field is not applicable for on-demand feature groups.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

 ** ProvisionedWriteCapacityUnits **   <a name="sagemaker-Type-ThroughputConfig-ProvisionedWriteCapacityUnits"></a>
 For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling.
This field is not applicable for on-demand feature groups.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

## See Also
<a name="API_ThroughputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ThroughputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ThroughputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ThroughputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
