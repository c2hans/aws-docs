---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSUtilizationMetric.html
---

# EBSUtilizationMetric
<a name="API_EBSUtilizationMetric"></a>

Describes a utilization metric of an Amazon Elastic Block Store (Amazon EBS) volume.

Compare the utilization metric data of your resource against its projected utilization metric data to determine the performance difference between your current resource and the recommended option.

## Contents
<a name="API_EBSUtilizationMetric_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-EBSUtilizationMetric-name"></a>
The name of the utilization metric.
The following utilization metrics are available:
+  `VolumeReadOpsPerSecond` - The completed read operations per second from the volume in a specified period of time.

  Unit: Count
+  `VolumeWriteOpsPerSecond` - The completed write operations per second to the volume in a specified period of time.

  Unit: Count
+  `VolumeReadBytesPerSecond` - The bytes read per second from the volume in a specified period of time.

  Unit: Bytes
+  `VolumeWriteBytesPerSecond` - The bytes written to the volume in a specified period of time.

  Unit: Bytes
Type: String
Valid Values: `VolumeReadOpsPerSecond | VolumeWriteOpsPerSecond | VolumeReadBytesPerSecond | VolumeWriteBytesPerSecond | VolumeIOPSExceeded | VolumeThroughputExceeded`
Required: No

 ** statistic **   <a name="computeoptimizer-Type-EBSUtilizationMetric-statistic"></a>
The statistic of the utilization metric.
The Compute Optimizer API, AWS Command Line Interface (AWS CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.
The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the * AWS Compute Optimizer User Guide*. You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).
Type: String
Valid Values: `Maximum | Average`
Required: No

 ** value **   <a name="computeoptimizer-Type-EBSUtilizationMetric-value"></a>
The value of the utilization metric.
Type: Double
Required: No

## See Also
<a name="API_EBSUtilizationMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/EBSUtilizationMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/EBSUtilizationMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/EBSUtilizationMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
