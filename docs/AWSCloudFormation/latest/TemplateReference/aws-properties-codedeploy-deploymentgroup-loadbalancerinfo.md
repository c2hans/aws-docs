---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup LoadBalancerInfo
<a name="aws-properties-codedeploy-deploymentgroup-loadbalancerinfo"></a>

The `LoadBalancerInfo` property type specifies information about the load balancer or target group used for an AWS CodeDeploy deployment group. For more information, see [ Integrating CodeDeploy with Elastic Load Balancing](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-elastic-load-balancing.html) in the *AWS CodeDeploy User Guide*.

For CloudFormation to use the properties specified in `LoadBalancerInfo`, the `DeploymentStyle.DeploymentOption` property must be set to `WITH_TRAFFIC_CONTROL`. If `DeploymentStyle.DeploymentOption` is not set to `WITH_TRAFFIC_CONTROL`, CloudFormation ignores any settings specified in `LoadBalancerInfo`.

**Note**
CloudFormation supports blue/green deployments on the AWS Lambda compute platform only.

`LoadBalancerInfo` is a property of the [DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html) resource.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-loadbalancerinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-loadbalancerinfo-syntax.json"></a>

```
{
  "[ElbInfoList](#cfn-codedeploy-deploymentgroup-loadbalancerinfo-elbinfolist)" : {{[ ELBInfo, ... ]}},
  "[TargetGroupInfoList](#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgroupinfolist)" : {{[ TargetGroupInfo, ... ]}},
  "[TargetGroupPairInfoList](#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgrouppairinfolist)" : {{[ TargetGroupPairInfo, ... ]}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-loadbalancerinfo-syntax.yaml"></a>

```
  [ElbInfoList](#cfn-codedeploy-deploymentgroup-loadbalancerinfo-elbinfolist): {{
    - ELBInfo}}
  [TargetGroupInfoList](#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgroupinfolist): {{
    - TargetGroupInfo}}
  [TargetGroupPairInfoList](#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgrouppairinfolist): {{
    - TargetGroupPairInfo}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-loadbalancerinfo-properties"></a>

`ElbInfoList`  <a name="cfn-codedeploy-deploymentgroup-loadbalancerinfo-elbinfolist"></a>
An array that contains information about the load balancers to use for load balancing in a deployment. If you're using Classic Load Balancers, specify those load balancers in this array.
You can add up to 10 load balancers to the array.
If you're using Application Load Balancers or Network Load Balancers, use the `targetGroupInfoList` array instead of this one.
*Required*: No
*Type*: Array of [ELBInfo](aws-properties-codedeploy-deploymentgroup-elbinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetGroupInfoList`  <a name="cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgroupinfolist"></a>
An array that contains information about the target groups to use for load balancing in a deployment. If you're using Application Load Balancers and Network Load Balancers, specify their associated target groups in this array.
You can add up to 10 target groups to the array.
If you're using Classic Load Balancers, use the `elbInfoList` array instead of this one.
*Required*: Conditional
*Type*: Array of [TargetGroupInfo](aws-properties-codedeploy-deploymentgroup-targetgroupinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetGroupPairInfoList`  <a name="cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgrouppairinfolist"></a>
 The target group pair information. This is an array of `TargeGroupPairInfo` objects with a maximum size of one.
*Required*: No
*Type*: Array of [TargetGroupPairInfo](aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
