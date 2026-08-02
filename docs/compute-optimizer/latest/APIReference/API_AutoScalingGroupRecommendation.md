---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupRecommendation.html
---

# AutoScalingGroupRecommendation
<a name="API_AutoScalingGroupRecommendation"></a>

Describes an Auto Scaling group recommendation.

## Contents
<a name="API_AutoScalingGroupRecommendation_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-accountId"></a>
The AWS account ID of the Auto Scaling group.
Type: String
Required: No

 ** autoScalingGroupArn **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-autoScalingGroupArn"></a>
The Amazon Resource Name (ARN) of the Auto Scaling group.
Type: String
Required: No

 ** autoScalingGroupName **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-autoScalingGroupName"></a>
The name of the Auto Scaling group.
Type: String
Required: No

 ** currentConfiguration **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-currentConfiguration"></a>
An array of objects that describe the current configuration of the Auto Scaling group.
Type: [AutoScalingGroupConfiguration](API_AutoScalingGroupConfiguration.md) object
Required: No

 ** currentInstanceGpuInfo **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-currentInstanceGpuInfo"></a>
 Describes the GPU accelerator settings for the current instance type of the Auto Scaling group.
Type: [GpuInfo](API_GpuInfo.md) object
Required: No

 ** currentPerformanceRisk **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-currentPerformanceRisk"></a>
The risk of the current Auto Scaling group not meeting the performance needs of its workloads. The higher the risk, the more likely the current Auto Scaling group configuration has insufficient capacity and cannot meet workload requirements.
Type: String
Valid Values: `VeryLow | Low | Medium | High`
Required: No

 ** effectiveRecommendationPreferences **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-effectiveRecommendationPreferences"></a>
An object that describes the effective recommendation preferences for the Auto Scaling group.
Type: [EffectiveRecommendationPreferences](API_EffectiveRecommendationPreferences.md) object
Required: No

 ** finding **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-finding"></a>
The finding classification of the Auto Scaling group.
Findings for Auto Scaling groups include:
+  ** `NotOptimized` **—An Auto Scaling group is considered not optimized when AWS Compute Optimizer identifies a recommendation that can provide better performance for your workload.
+  ** `Optimized` **—An Auto Scaling group is considered optimized when Compute Optimizer determines that the group is correctly provisioned to run your workload based on the chosen instance type. For optimized resources, Compute Optimizer might recommend a new generation instance type.
Type: String
Valid Values: `Underprovisioned | Overprovisioned | Optimized | NotOptimized`
Required: No

 ** inferredWorkloadTypes **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-inferredWorkloadTypes"></a>
The applications that might be running on the instances in the Auto Scaling group as inferred by Compute Optimizer.
Compute Optimizer can infer if one of the following applications might be running on the instances:
+  `AmazonEmr` - Infers that Amazon EMR might be running on the instances.
+  `ApacheCassandra` - Infers that Apache Cassandra might be running on the instances.
+  `ApacheHadoop` - Infers that Apache Hadoop might be running on the instances.
+  `Memcached` - Infers that Memcached might be running on the instances.
+  `NGINX` - Infers that NGINX might be running on the instances.
+  `PostgreSql` - Infers that PostgreSQL might be running on the instances.
+  `Redis` - Infers that Redis might be running on the instances.
+  `Kafka` - Infers that Kafka might be running on the instance.
+  `SQLServer` - Infers that SQLServer might be running on the instance.
Type: Array of strings
Valid Values: `AmazonEmr | ApacheCassandra | ApacheHadoop | Memcached | Nginx | PostgreSql | Redis | Kafka | SQLServer`
Required: No

 ** lastRefreshTimestamp **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-lastRefreshTimestamp"></a>
The timestamp of when the Auto Scaling group recommendation was last generated.
Type: Timestamp
Required: No

 ** lookBackPeriodInDays **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-lookBackPeriodInDays"></a>
The number of days for which utilization metrics were analyzed for the Auto Scaling group.
Type: Double
Required: No

 ** recommendationOptions **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-recommendationOptions"></a>
An array of objects that describe the recommendation options for the Auto Scaling group.
Type: Array of [AutoScalingGroupRecommendationOption](API_AutoScalingGroupRecommendationOption.md) objects
Required: No

 ** utilizationMetrics **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendation-utilizationMetrics"></a>
An array of objects that describe the utilization metrics of the Auto Scaling group.
Type: Array of [UtilizationMetric](API_UtilizationMetric.md) objects
Required: No

## See Also
<a name="API_AutoScalingGroupRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/AutoScalingGroupRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/AutoScalingGroupRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/AutoScalingGroupRecommendation)
