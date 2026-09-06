---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleUtilizationMetric.html
---

# IdleUtilizationMetric
<a name="API_IdleUtilizationMetric"></a>

Describes the utilization metric of an idle resource.

## Contents
<a name="API_IdleUtilizationMetric_Contents"></a>

 ** dimensions **   <a name="computeoptimizer-Type-IdleUtilizationMetric-dimensions"></a>
The dimensions of the utilization metric.
Type: Array of [IdleDimension](API_IdleDimension.md) objects
Required: No

 ** name **   <a name="computeoptimizer-Type-IdleUtilizationMetric-name"></a>
The name of the utilization metric.
Type: String
Valid Values: `CPU | Memory | NetworkOutBytesPerSecond | NetworkInBytesPerSecond | DatabaseConnections | EBSVolumeReadIOPS | EBSVolumeWriteIOPS | VolumeReadOpsPerSecond | VolumeWriteOpsPerSecond | ActiveConnectionCount | PacketsInFromSource | PacketsInFromDestination | ConsumedReadCapacityUnits | ConsumedWriteCapacityUnits | ConsumedChangeDataCaptureUnits | NewConnections | EngineCPUUtilization | CacheHits | CacheMisses | KeyspaceHits | KeyspaceMisses | IsIdle | UserConnected | Invocations | GetTypeCmds | SetTypeCmds | ElastiCacheProcessingUnits | CurrConnections`
Required: No

 ** statistic **   <a name="computeoptimizer-Type-IdleUtilizationMetric-statistic"></a>
 The statistic of the utilization metric.
The Compute Optimizer API, AWS Command Line Interface (AWS CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.
The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the * AWS Compute Optimizer User Guide*. You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).
Type: String
Valid Values: `Maximum | Average`
Required: No

 ** value **   <a name="computeoptimizer-Type-IdleUtilizationMetric-value"></a>
The value of the utilization metric.
Type: Double
Required: No

## See Also
<a name="API_IdleUtilizationMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/IdleUtilizationMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/IdleUtilizationMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/IdleUtilizationMetric)
