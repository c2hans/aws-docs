---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService ExpressGatewayScalingTarget
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget"></a>

Defines the auto-scaling configuration for an Express service. This determines how the service automatically adjusts the number of running tasks based on demand metrics such as CPU utilization, memory utilization, or request count per target.

Auto-scaling helps ensure your application can handle varying levels of traffic while optimizing costs by scaling down during low-demand periods. You can specify the minimum and maximum number of tasks, the scaling metric, and the target value for that metric.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget-syntax.json"></a>

```
{
  "[AutoScalingMetric](#cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-autoscalingmetric)" : {{String}},
  "[AutoScalingTargetValue](#cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-autoscalingtargetvalue)" : {{Integer}},
  "[MaxTaskCount](#cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-maxtaskcount)" : {{Integer}},
  "[MinTaskCount](#cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-mintaskcount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget-syntax.yaml"></a>

```
  [AutoScalingMetric](#cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-autoscalingmetric): {{String}}
  [AutoScalingTargetValue](#cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-autoscalingtargetvalue): {{Integer}}
  [MaxTaskCount](#cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-maxtaskcount): {{Integer}}
  [MinTaskCount](#cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-mintaskcount): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget-properties"></a>

`AutoScalingMetric`  <a name="cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-autoscalingmetric"></a>
The metric used for auto-scaling decisions. The default metric used for an Express service is `CPUUtilization`.
*Required*: No
*Type*: String
*Allowed values*: `AVERAGE_CPU | AVERAGE_MEMORY | REQUEST_COUNT_PER_TARGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoScalingTargetValue`  <a name="cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-autoscalingtargetvalue"></a>
The target value for the auto-scaling metric. The default value for an Express service is 60.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTaskCount`  <a name="cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-maxtaskcount"></a>
The maximum number of tasks to run in the Express service.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinTaskCount`  <a name="cfn-ecs-expressgatewayservice-expressgatewayscalingtarget-mintaskcount"></a>
The minimum number of tasks to run in the Express service.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
