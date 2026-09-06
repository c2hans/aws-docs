---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53recoveryreadiness-cell.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53RecoveryReadiness::Cell
<a name="aws-resource-route53recoveryreadiness-cell"></a>

Creates a cell in recovery group in Amazon Route 53 Application Recovery Controller. A cell in Route 53 ARC represents replicas or independent units of failover in your application. It groups within it all the AWS resources that are necessary for your application to run independently. Typically, you would have define one set of resources in a primary cell and another set in a standby cell in your recovery group.

After you set up the cells for your application, you can create readiness checks in Route 53 ARC to continually audit readiness for AWS resource quotas, capacity, network routing policies, and other predefined rules.

You can set up notifications about changes that would affect your ability to fail over to a replica and recover. However, you should make decisions about whether to fail away from or to a replica based on your monitoring and health check systems. You should consider readiness checks as a complementary service to those systems.

Route 53 ARC Readiness supports us-east-1 and us-west-2 AWS Regions only.

## Syntax
<a name="aws-resource-route53recoveryreadiness-cell-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53recoveryreadiness-cell-syntax.json"></a>

```
{
  "Type" : "AWS::Route53RecoveryReadiness::Cell",
  "Properties" : {
      "[CellName](#cfn-route53recoveryreadiness-cell-cellname)" : {{String}},
      "[Cells](#cfn-route53recoveryreadiness-cell-cells)" : {{[ String, ... ]}},
      "[Tags](#cfn-route53recoveryreadiness-cell-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53recoveryreadiness-cell-syntax.yaml"></a>

```
Type: AWS::Route53RecoveryReadiness::Cell
Properties:
  [CellName](#cfn-route53recoveryreadiness-cell-cellname): {{String}}
  [Cells](#cfn-route53recoveryreadiness-cell-cells): {{
    - String}}
  [Tags](#cfn-route53recoveryreadiness-cell-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53recoveryreadiness-cell-properties"></a>

`CellName`  <a name="cfn-route53recoveryreadiness-cell-cellname"></a>
The name of the cell to create.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_]+`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Cells`  <a name="cfn-route53recoveryreadiness-cell-cells"></a>
A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific AWS Regions.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-route53recoveryreadiness-cell-tags"></a>
A collection of tags associated with a resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53recoveryreadiness-cell-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53recoveryreadiness-cell-return-values"></a>

### Ref
<a name="aws-resource-route53recoveryreadiness-cell-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `CellName`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53recoveryreadiness-cell-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53recoveryreadiness-cell-return-values-fn--getatt-fn--getatt"></a>

`CellArn`  <a name="CellArn-fn::getatt"></a>
The ARN of the cell.

`ParentReadinessScopes`  <a name="ParentReadinessScopes-fn::getatt"></a>
The readiness scope for the cell, which can be the Amazon Resource Name (ARN) of a cell or the ARN of a recovery group. Although this is a list, it can currently have only one element.
