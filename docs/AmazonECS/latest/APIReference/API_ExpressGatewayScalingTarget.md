---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExpressGatewayScalingTarget.html
---

# ExpressGatewayScalingTarget
<a name="API_ExpressGatewayScalingTarget"></a>

Defines the auto-scaling configuration for an Express service. This determines how the service automatically adjusts the number of running tasks based on demand metrics such as CPU utilization, memory utilization, or request count per target.

Auto-scaling helps ensure your application can handle varying levels of traffic while optimizing costs by scaling down during low-demand periods. You can specify the minimum and maximum number of tasks, the scaling metric, and the target value for that metric.

## Contents
<a name="API_ExpressGatewayScalingTarget_Contents"></a>

 ** autoScalingMetric **   <a name="ECS-Type-ExpressGatewayScalingTarget-autoScalingMetric"></a>
The metric used for auto-scaling decisions. The default metric used for an Express service is `CPUUtilization`.
Type: String
Valid Values: `AVERAGE_CPU | AVERAGE_MEMORY | REQUEST_COUNT_PER_TARGET`
Required: No

 ** autoScalingTargetValue **   <a name="ECS-Type-ExpressGatewayScalingTarget-autoScalingTargetValue"></a>
The target value for the auto-scaling metric. The default value for an Express service is 60.
Type: Integer
Required: No

 ** maxTaskCount **   <a name="ECS-Type-ExpressGatewayScalingTarget-maxTaskCount"></a>
The maximum number of tasks to run in the Express service.
Type: Integer
Required: No

 ** minTaskCount **   <a name="ECS-Type-ExpressGatewayScalingTarget-minTaskCount"></a>
The minimum number of tasks to run in the Express service.
Type: Integer
Required: No

## See Also
<a name="API_ExpressGatewayScalingTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExpressGatewayScalingTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExpressGatewayScalingTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExpressGatewayScalingTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
