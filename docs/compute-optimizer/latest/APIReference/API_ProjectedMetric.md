---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ProjectedMetric.html
---

# ProjectedMetric
<a name="API_ProjectedMetric"></a>

Describes a projected utilization metric of a recommendation option, such as an Amazon EC2 instance. This represents the projected utilization of a recommendation option had you used that resource during the analyzed period.

Compare the utilization metric data of your resource against its projected utilization metric data to determine the performance difference between your current resource and the recommended option.

**Note**
The `Cpu`, `Memory`, `GPU`, and `GPU_MEMORY` metrics are the only projected utilization metrics returned when you run the [GetEC2RecommendationProjectedMetrics](API_GetEC2RecommendationProjectedMetrics.md) action. Additionally, these metrics are only returned for resources with the unified CloudWatch agent installed on them. For more information, see [Enabling Memory Utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent) and [Enabling NVIDIA GPU utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#nvidia-cw-agent).

## Contents
<a name="API_ProjectedMetric_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-ProjectedMetric-name"></a>
The name of the projected utilization metric.
The following projected utilization metrics are returned:
+  `Cpu` - The projected percentage of allocated EC2 compute units that would be in use on the recommendation option had you used that resource during the analyzed period. This metric identifies the processing power required to run an application on the recommendation option.

  Depending on the instance type, tools in your operating system can show a lower percentage than CloudWatch when the instance is not allocated a full processor core.
+  `Memory` - The percentage of memory that would be in use on the recommendation option had you used that resource during the analyzed period. This metric identifies the amount of memory required to run an application on the recommendation option.

  Units: Percent
**Note**
The `Memory` metric is only returned for resources with the unified CloudWatch agent installed on them. For more information, see [Enabling Memory Utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent).
+  `GPU` - The projected percentage of allocated GPUs if you adjust your configurations to Compute Optimizer's recommendation option.
+  `GPU_MEMORY` - The projected percentage of total GPU memory if you adjust your configurations to Compute Optimizer's recommendation option.
**Note**
The `GPU` and `GPU_MEMORY` metrics are only returned for resources with the unified CloudWatch Agent installed on them. For more information, see [Enabling NVIDIA GPU utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#nvidia-cw-agent).
Type: String
Valid Values: `Cpu | Memory | EBS_READ_OPS_PER_SECOND | EBS_WRITE_OPS_PER_SECOND | EBS_READ_BYTES_PER_SECOND | EBS_WRITE_BYTES_PER_SECOND | DISK_READ_OPS_PER_SECOND | DISK_WRITE_OPS_PER_SECOND | DISK_READ_BYTES_PER_SECOND | DISK_WRITE_BYTES_PER_SECOND | NETWORK_IN_BYTES_PER_SECOND | NETWORK_OUT_BYTES_PER_SECOND | NETWORK_PACKETS_IN_PER_SECOND | NETWORK_PACKETS_OUT_PER_SECOND | GPU_PERCENTAGE | GPU_MEMORY_PERCENTAGE`
Required: No

 ** timestamps **   <a name="computeoptimizer-Type-ProjectedMetric-timestamps"></a>
The timestamps of the projected utilization metric.
Type: Array of timestamps
Required: No

 ** values **   <a name="computeoptimizer-Type-ProjectedMetric-values"></a>
The values of the projected utilization metrics.
Type: Array of doubles
Required: No

## See Also
<a name="API_ProjectedMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ProjectedMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ProjectedMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ProjectedMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
