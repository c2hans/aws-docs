---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-weightedtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route WeightedTarget
<a name="aws-properties-appmesh-route-weightedtarget"></a>

An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

## Syntax
<a name="aws-properties-appmesh-route-weightedtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-weightedtarget-syntax.json"></a>

```
{
  "[Port](#cfn-appmesh-route-weightedtarget-port)" : {{Integer}},
  "[VirtualNode](#cfn-appmesh-route-weightedtarget-virtualnode)" : {{String}},
  "[Weight](#cfn-appmesh-route-weightedtarget-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appmesh-route-weightedtarget-syntax.yaml"></a>

```
  [Port](#cfn-appmesh-route-weightedtarget-port): {{Integer}}
  [VirtualNode](#cfn-appmesh-route-weightedtarget-virtualnode): {{String}}
  [Weight](#cfn-appmesh-route-weightedtarget-weight): {{Integer}}
```

## Properties
<a name="aws-properties-appmesh-route-weightedtarget-properties"></a>

`Port`  <a name="cfn-appmesh-route-weightedtarget-port"></a>
The targeted port of the weighted object.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualNode`  <a name="cfn-appmesh-route-weightedtarget-virtualnode"></a>
The virtual node to associate with the weighted target.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-appmesh-route-weightedtarget-weight"></a>
The relative weight of the weighted target.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
