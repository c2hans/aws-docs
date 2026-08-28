---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_InstanceRecommendation.html
---

# InstanceRecommendation
<a name="API_InstanceRecommendation"></a>

Describes an Amazon EC2 instance recommendation.

## Contents
<a name="API_InstanceRecommendation_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-InstanceRecommendation-accountId"></a>
The AWS account ID of the instance.
Type: String
Required: No

 ** currentInstanceGpuInfo **   <a name="computeoptimizer-Type-InstanceRecommendation-currentInstanceGpuInfo"></a>
 Describes the GPU accelerator settings for the current instance type.
Type: [GpuInfo](API_GpuInfo.md) object
Required: No

 ** currentInstanceType **   <a name="computeoptimizer-Type-InstanceRecommendation-currentInstanceType"></a>
The instance type of the current instance.
Type: String
Required: No

 ** currentPerformanceRisk **   <a name="computeoptimizer-Type-InstanceRecommendation-currentPerformanceRisk"></a>
The risk of the current instance not meeting the performance needs of its workloads. The higher the risk, the more likely the current instance cannot meet the performance requirements of its workload.
Type: String
Valid Values: `VeryLow | Low | Medium | High`
Required: No

 ** effectiveRecommendationPreferences **   <a name="computeoptimizer-Type-InstanceRecommendation-effectiveRecommendationPreferences"></a>
An object that describes the effective recommendation preferences for the instance.
Type: [EffectiveRecommendationPreferences](API_EffectiveRecommendationPreferences.md) object
Required: No

 ** externalMetricStatus **   <a name="computeoptimizer-Type-InstanceRecommendation-externalMetricStatus"></a>
 An object that describes Compute Optimizer's integration status with your external metrics provider.
Type: [ExternalMetricStatus](API_ExternalMetricStatus.md) object
Required: No

 ** finding **   <a name="computeoptimizer-Type-InstanceRecommendation-finding"></a>
The finding classification of the instance.
Findings for instances include:
+  ** `Underprovisioned` **—An instance is considered under-provisioned when at least one specification of your instance, such as CPU, memory, or network, does not meet the performance requirements of your workload. Under-provisioned instances may lead to poor application performance.
+  ** `Overprovisioned` **—An instance is considered over-provisioned when at least one specification of your instance, such as CPU, memory, or network, can be sized down while still meeting the performance requirements of your workload, and no specification is under-provisioned. Over-provisioned instances may lead to unnecessary infrastructure cost.
+  ** `Optimized` **—An instance is considered optimized when all specifications of your instance, such as CPU, memory, and network, meet the performance requirements of your workload and is not over provisioned. For optimized resources, AWS Compute Optimizer might recommend a new generation instance type.
The valid values in your API responses appear as OVER\_PROVISIONED, UNDER\_PROVISIONED, or OPTIMIZED.
Type: String
Valid Values: `Underprovisioned | Overprovisioned | Optimized | NotOptimized`
Required: No

 ** findingReasonCodes **   <a name="computeoptimizer-Type-InstanceRecommendation-findingReasonCodes"></a>
The reason for the finding classification of the instance.
Finding reason codes for instances include:
+  ** `CPUOverprovisioned` ** — The instance’s CPU configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `CPUUtilization` metric of the current instance during the look-back period.
+  ** `CPUUnderprovisioned` ** — The instance’s CPU configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance. This is identified by analyzing the `CPUUtilization` metric of the current instance during the look-back period.
+  ** `MemoryOverprovisioned` ** — The instance’s memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the memory utilization metric of the current instance during the look-back period.
+  ** `MemoryUnderprovisioned` ** — The instance’s memory configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better memory performance. This is identified by analyzing the memory utilization metric of the current instance during the look-back period.
**Note**
Memory utilization is analyzed only for resources that have the unified CloudWatch agent installed on them. For more information, see [Enabling memory utilization with the Amazon CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent) in the * AWS Compute Optimizer User Guide*. On Linux instances, Compute Optimizer analyses the `mem_used_percent` metric in the `CWAgent` namespace, or the legacy `MemoryUtilization` metric in the `System/Linux` namespace. On Windows instances, Compute Optimizer analyses the `Memory % Committed Bytes In Use` metric in the `CWAgent` namespace.
+  ** `EBSThroughputOverprovisioned` ** — The instance’s EBS throughput configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metrics of EBS volumes attached to the current instance during the look-back period.
+  ** `EBSThroughputUnderprovisioned` ** — The instance’s EBS throughput configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metrics of EBS volumes attached to the current instance during the look-back period.
+  ** `EBSIOPSOverprovisioned` ** — The instance’s EBS IOPS configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metric of EBS volumes attached to the current instance during the look-back period.
+  ** `EBSIOPSUnderprovisioned` ** — The instance’s EBS IOPS configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS IOPS performance. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metric of EBS volumes attached to the current instance during the look-back period.
+  ** `NetworkBandwidthOverprovisioned` ** — The instance’s network bandwidth configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `NetworkIn` and `NetworkOut` metrics of the current instance during the look-back period.
+  ** `NetworkBandwidthUnderprovisioned` ** — The instance’s network bandwidth configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance. This is identified by analyzing the `NetworkIn` and `NetworkOut` metrics of the current instance during the look-back period. This finding reason happens when the `NetworkIn` or `NetworkOut` performance of an instance is impacted.
+  ** `NetworkPPSOverprovisioned` ** — The instance’s network PPS (packets per second) configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `NetworkPacketsIn` and `NetworkPacketsIn` metrics of the current instance during the look-back period.
+  ** `NetworkPPSUnderprovisioned` ** — The instance’s network PPS (packets per second) configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better network PPS performance. This is identified by analyzing the `NetworkPacketsIn` and `NetworkPacketsIn` metrics of the current instance during the look-back period.
+  ** `DiskIOPSOverprovisioned` ** — The instance’s disk IOPS configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `DiskReadOps` and `DiskWriteOps` metrics of the current instance during the look-back period.
+  ** `DiskIOPSUnderprovisioned` ** — The instance’s disk IOPS configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better disk IOPS performance. This is identified by analyzing the `DiskReadOps` and `DiskWriteOps` metrics of the current instance during the look-back period.
+  ** `DiskThroughputOverprovisioned` ** — The instance’s disk throughput configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `DiskReadBytes` and `DiskWriteBytes` metrics of the current instance during the look-back period.
+  ** `DiskThroughputUnderprovisioned` ** — The instance’s disk throughput configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better disk throughput performance. This is identified by analyzing the `DiskReadBytes` and `DiskWriteBytes` metrics of the current instance during the look-back period.
For more information about instance metrics, see [List the available CloudWatch metrics for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html) in the *Amazon Elastic Compute Cloud User Guide*. For more information about EBS volume metrics, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) in the *Amazon Elastic Compute Cloud User Guide*.
Type: Array of strings
Valid Values: `CPUOverprovisioned | CPUUnderprovisioned | MemoryOverprovisioned | MemoryUnderprovisioned | EBSThroughputOverprovisioned | EBSThroughputUnderprovisioned | EBSIOPSOverprovisioned | EBSIOPSUnderprovisioned | NetworkBandwidthOverprovisioned | NetworkBandwidthUnderprovisioned | NetworkPPSOverprovisioned | NetworkPPSUnderprovisioned | DiskIOPSOverprovisioned | DiskIOPSUnderprovisioned | DiskThroughputOverprovisioned | DiskThroughputUnderprovisioned | GPUUnderprovisioned | GPUOverprovisioned | GPUMemoryUnderprovisioned | GPUMemoryOverprovisioned`
Required: No

 ** idle **   <a name="computeoptimizer-Type-InstanceRecommendation-idle"></a>
 Describes if an Amazon EC2 instance is idle.
Type: String
Valid Values: `True | False`
Required: No

 ** inferredWorkloadTypes **   <a name="computeoptimizer-Type-InstanceRecommendation-inferredWorkloadTypes"></a>
The applications that might be running on the instance as inferred by Compute Optimizer.
Compute Optimizer can infer if one of the following applications might be running on the instance:
+  `AmazonEmr` - Infers that Amazon EMR might be running on the instance.
+  `ApacheCassandra` - Infers that Apache Cassandra might be running on the instance.
+  `ApacheHadoop` - Infers that Apache Hadoop might be running on the instance.
+  `Memcached` - Infers that Memcached might be running on the instance.
+  `NGINX` - Infers that NGINX might be running on the instance.
+  `PostgreSql` - Infers that PostgreSQL might be running on the instance.
+  `Redis` - Infers that Redis might be running on the instance.
+  `Kafka` - Infers that Kafka might be running on the instance.
+  `SQLServer` - Infers that SQLServer might be running on the instance.
Type: Array of strings
Valid Values: `AmazonEmr | ApacheCassandra | ApacheHadoop | Memcached | Nginx | PostgreSql | Redis | Kafka | SQLServer`
Required: No

 ** instanceArn **   <a name="computeoptimizer-Type-InstanceRecommendation-instanceArn"></a>
The Amazon Resource Name (ARN) of the current instance.
Type: String
Required: No

 ** instanceName **   <a name="computeoptimizer-Type-InstanceRecommendation-instanceName"></a>
The name of the current instance.
Type: String
Required: No

 ** instanceState **   <a name="computeoptimizer-Type-InstanceRecommendation-instanceState"></a>
 The state of the instance when the recommendation was generated.
Type: String
Valid Values: `pending | running | shutting-down | terminated | stopping | stopped`
Required: No

 ** lastRefreshTimestamp **   <a name="computeoptimizer-Type-InstanceRecommendation-lastRefreshTimestamp"></a>
The timestamp of when the instance recommendation was last generated.
Type: Timestamp
Required: No

 ** lookBackPeriodInDays **   <a name="computeoptimizer-Type-InstanceRecommendation-lookBackPeriodInDays"></a>
The number of days for which utilization metrics were analyzed for the instance.
Type: Double
Required: No

 ** recommendationOptions **   <a name="computeoptimizer-Type-InstanceRecommendation-recommendationOptions"></a>
An array of objects that describe the recommendation options for the instance.
Type: Array of [InstanceRecommendationOption](API_InstanceRecommendationOption.md) objects
Required: No

 ** recommendationSources **   <a name="computeoptimizer-Type-InstanceRecommendation-recommendationSources"></a>
An array of objects that describe the source resource of the recommendation.
Type: Array of [RecommendationSource](API_RecommendationSource.md) objects
Required: No

 ** tags **   <a name="computeoptimizer-Type-InstanceRecommendation-tags"></a>
 A list of tags assigned to your Amazon EC2 instance recommendations.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** utilizationMetrics **   <a name="computeoptimizer-Type-InstanceRecommendation-utilizationMetrics"></a>
An array of objects that describe the utilization metrics of the instance.
Type: Array of [UtilizationMetric](API_UtilizationMetric.md) objects
Required: No

## See Also
<a name="API_InstanceRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/InstanceRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/InstanceRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/InstanceRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
