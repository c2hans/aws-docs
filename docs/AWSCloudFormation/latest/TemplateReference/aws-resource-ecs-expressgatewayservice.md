---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-expressgatewayservice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService
<a name="aws-resource-ecs-expressgatewayservice"></a>

Creates an Express service that simplifies deploying containerized web applications on Amazon ECS with managed AWS infrastructure. This operation provisions and configures Application Load Balancers, target groups, security groups, and auto-scaling policies automatically.

Specify a primary container configuration with your application image and basic settings. Amazon ECS creates the necessary AWS resources for traffic distribution, health monitoring, network access control, and capacity management.

Provide an execution role for task operations and an infrastructure role for managing AWS resources on your behalf.

## Syntax
<a name="aws-resource-ecs-expressgatewayservice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-expressgatewayservice-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::ExpressGatewayService",
  "Properties" : {
      "[Cluster](#cfn-ecs-expressgatewayservice-cluster)" : {{String}},
      "[Cpu](#cfn-ecs-expressgatewayservice-cpu)" : {{String}},
      "[ExecutionRoleArn](#cfn-ecs-expressgatewayservice-executionrolearn)" : {{String}},
      "[HealthCheckPath](#cfn-ecs-expressgatewayservice-healthcheckpath)" : {{String}},
      "[InfrastructureRoleArn](#cfn-ecs-expressgatewayservice-infrastructurerolearn)" : {{String}},
      "[Memory](#cfn-ecs-expressgatewayservice-memory)" : {{String}},
      "[NetworkConfiguration](#cfn-ecs-expressgatewayservice-networkconfiguration)" : {{ExpressGatewayServiceNetworkConfiguration}},
      "[PrimaryContainer](#cfn-ecs-expressgatewayservice-primarycontainer)" : {{ExpressGatewayContainer}},
      "[ScalingTarget](#cfn-ecs-expressgatewayservice-scalingtarget)" : {{ExpressGatewayScalingTarget}},
      "[ServiceName](#cfn-ecs-expressgatewayservice-servicename)" : {{String}},
      "[Tags](#cfn-ecs-expressgatewayservice-tags)" : {{[ Tag, ... ]}},
      "[TaskDefinitionArn](#cfn-ecs-expressgatewayservice-taskdefinitionarn)" : {{String}},
      "[TaskRoleArn](#cfn-ecs-expressgatewayservice-taskrolearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ecs-expressgatewayservice-syntax.yaml"></a>

```
Type: AWS::ECS::ExpressGatewayService
Properties:
  [Cluster](#cfn-ecs-expressgatewayservice-cluster): {{String}}
  [Cpu](#cfn-ecs-expressgatewayservice-cpu): {{String}}
  [ExecutionRoleArn](#cfn-ecs-expressgatewayservice-executionrolearn): {{String}}
  [HealthCheckPath](#cfn-ecs-expressgatewayservice-healthcheckpath): {{String}}
  [InfrastructureRoleArn](#cfn-ecs-expressgatewayservice-infrastructurerolearn): {{String}}
  [Memory](#cfn-ecs-expressgatewayservice-memory): {{String}}
  [NetworkConfiguration](#cfn-ecs-expressgatewayservice-networkconfiguration): {{
    ExpressGatewayServiceNetworkConfiguration}}
  [PrimaryContainer](#cfn-ecs-expressgatewayservice-primarycontainer): {{
    ExpressGatewayContainer}}
  [ScalingTarget](#cfn-ecs-expressgatewayservice-scalingtarget): {{
    ExpressGatewayScalingTarget}}
  [ServiceName](#cfn-ecs-expressgatewayservice-servicename): {{String}}
  [Tags](#cfn-ecs-expressgatewayservice-tags): {{
    - Tag}}
  [TaskDefinitionArn](#cfn-ecs-expressgatewayservice-taskdefinitionarn): {{String}}
  [TaskRoleArn](#cfn-ecs-expressgatewayservice-taskrolearn): {{String}}
```

## Properties
<a name="aws-resource-ecs-expressgatewayservice-properties"></a>

`Cluster`  <a name="cfn-ecs-expressgatewayservice-cluster"></a>
The short name or full ARN of the cluster that hosts the Express service.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Cpu`  <a name="cfn-ecs-expressgatewayservice-cpu"></a>
The CPU allocation for tasks in this service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-ecs-expressgatewayservice-executionrolearn"></a>
The ARN of the task execution role for the service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckPath`  <a name="cfn-ecs-expressgatewayservice-healthcheckpath"></a>
The health check path for this service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfrastructureRoleArn`  <a name="cfn-ecs-expressgatewayservice-infrastructurerolearn"></a>
The ARN of the infrastructure role that manages AWS resources for the Express service.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Memory`  <a name="cfn-ecs-expressgatewayservice-memory"></a>
The memory allocation for tasks in this service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-ecs-expressgatewayservice-networkconfiguration"></a>
The network configuration for tasks in this service revision.
*Required*: No
*Type*: [ExpressGatewayServiceNetworkConfiguration](aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryContainer`  <a name="cfn-ecs-expressgatewayservice-primarycontainer"></a>
The primary container configuration for this service revision.
*Required*: No
*Type*: [ExpressGatewayContainer](aws-properties-ecs-expressgatewayservice-expressgatewaycontainer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingTarget`  <a name="cfn-ecs-expressgatewayservice-scalingtarget"></a>
The auto-scaling configuration for this service revision.
*Required*: No
*Type*: [ExpressGatewayScalingTarget](aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceName`  <a name="cfn-ecs-expressgatewayservice-servicename"></a>
The name of the Express service.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ecs-expressgatewayservice-tags"></a>
The metadata applied to the Express service.
*Required*: No
*Type*: Array of [Tag](aws-properties-ecs-expressgatewayservice-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TaskDefinitionArn`  <a name="cfn-ecs-expressgatewayservice-taskdefinitionarn"></a>
The ARN of the task definition used by this service revision. This is present for all Express services and reflects the task definition in use, whether managed by Amazon ECS or provided by the customer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskRoleArn`  <a name="cfn-ecs-expressgatewayservice-taskrolearn"></a>
The ARN of the task role for the service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ecs-expressgatewayservice-return-values"></a>

### Ref
<a name="aws-resource-ecs-expressgatewayservice-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecs-expressgatewayservice-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecs-expressgatewayservice-return-values-fn--getatt-fn--getatt"></a>

`ActiveConfigurations`  <a name="ActiveConfigurations-fn::getatt"></a>
The list of active service configurations for the Express service.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp for when the Express service was created.

`ECSManagedResourceArns.AutoScaling.ApplicationAutoScalingPolicies`  <a name="ECSManagedResourceArns.AutoScaling.ApplicationAutoScalingPolicies-fn::getatt"></a>
The list of Auto Scaling policy ARNs associated with the express service.

`ECSManagedResourceArns.AutoScaling.ScalableTarget`  <a name="ECSManagedResourceArns.AutoScaling.ScalableTarget-fn::getatt"></a>
The Auto Scaling Scalable Target ARN associated with the express service.

`ECSManagedResourceArns.IngressPath.CertificateArn`  <a name="ECSManagedResourceArns.IngressPath.CertificateArn-fn::getatt"></a>
The Certificate ARN associated with the express service.

`ECSManagedResourceArns.IngressPath.ListenerArn`  <a name="ECSManagedResourceArns.IngressPath.ListenerArn-fn::getatt"></a>
The ARN of the Load Balancer listener associated with the express service.

`ECSManagedResourceArns.IngressPath.ListenerRuleArn`  <a name="ECSManagedResourceArns.IngressPath.ListenerRuleArn-fn::getatt"></a>
The ARN of the Load Balancer listener rule associated with the express service.

`ECSManagedResourceArns.IngressPath.LoadBalancerArn`  <a name="ECSManagedResourceArns.IngressPath.LoadBalancerArn-fn::getatt"></a>
The ARN of the Load Balancer associated with the express service.

`ECSManagedResourceArns.IngressPath.LoadBalancerSecurityGroups`  <a name="ECSManagedResourceArns.IngressPath.LoadBalancerSecurityGroups-fn::getatt"></a>
The list of Load Balancer Security Group ARNs associated with the express service.

`ECSManagedResourceArns.IngressPath.TargetGroupArns`  <a name="ECSManagedResourceArns.IngressPath.TargetGroupArns-fn::getatt"></a>
The list of Target Group ARNs associated with the express service.

`ECSManagedResourceArns.LogGroups`  <a name="ECSManagedResourceArns.LogGroups-fn::getatt"></a>
The list of Log Group ARNs associated with the express service.

`ECSManagedResourceArns.MetricAlarms`  <a name="ECSManagedResourceArns.MetricAlarms-fn::getatt"></a>
The list of Metric Alarm ARNs associated with the express service.

`ECSManagedResourceArns.ServiceSecurityGroups`  <a name="ECSManagedResourceArns.ServiceSecurityGroups-fn::getatt"></a>
The list of Security Group ARNs associated with the express service.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The Endpoint of the express service.

`ServiceArn`  <a name="ServiceArn-fn::getatt"></a>
The ARN that identifies the Express service.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp for when the Express service was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
