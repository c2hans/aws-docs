---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-gatewayclusterassociations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::GatewayClusterAssociations
<a name="aws-resource-ecs-gatewayclusterassociations"></a>

<a name="aws-resource-ecs-gatewayclusterassociations-description"></a>The `AWS::ECS::GatewayClusterAssociations` resource Property description not available. for ECS.

## Syntax
<a name="aws-resource-ecs-gatewayclusterassociations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-gatewayclusterassociations-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::GatewayClusterAssociations",
  "Properties" : {
      "[Cluster](#cfn-ecs-gatewayclusterassociations-cluster)" : {{String}},
      "[Gateway](#cfn-ecs-gatewayclusterassociations-gateway)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ecs-gatewayclusterassociations-syntax.yaml"></a>

```
Type: AWS::ECS::GatewayClusterAssociations
Properties:
  [Cluster](#cfn-ecs-gatewayclusterassociations-cluster): {{String}}
  [Gateway](#cfn-ecs-gatewayclusterassociations-gateway): {{String}}
```

## Properties
<a name="aws-resource-ecs-gatewayclusterassociations-properties"></a>

`Cluster`  <a name="cfn-ecs-gatewayclusterassociations-cluster"></a>
A regional grouping of one or more container instances where you can run task requests. Each account receives a default cluster the first time you use the Amazon ECS service, but you may also create other clusters. Clusters may contain more than one instance type simultaneously.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Gateway`  <a name="cfn-ecs-gatewayclusterassociations-gateway"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ecs-gatewayclusterassociations-return-values"></a>

### Ref
<a name="aws-resource-ecs-gatewayclusterassociations-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecs-gatewayclusterassociations-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecs-gatewayclusterassociations-return-values-fn--getatt-fn--getatt"></a>

`ClusterArn`  <a name="ClusterArn-fn::getatt"></a>
Property description not available.

`GatewayArn`  <a name="GatewayArn-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
