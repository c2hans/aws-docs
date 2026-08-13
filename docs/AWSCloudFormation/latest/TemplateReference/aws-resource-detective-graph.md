---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-detective-graph.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Detective::Graph
<a name="aws-resource-detective-graph"></a>

The `AWS::Detective::Graph` resource is an Amazon Detective resource type that creates a Detective behavior graph. The requesting account becomes the administrator account for the behavior graph.

## Syntax
<a name="aws-resource-detective-graph-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-detective-graph-syntax.json"></a>

```
{
  "Type" : "AWS::Detective::Graph",
  "Properties" : {
      "[AutoEnableMembers](#cfn-detective-graph-autoenablemembers)" : {{Boolean}},
      "[Tags](#cfn-detective-graph-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-detective-graph-syntax.yaml"></a>

```
Type: AWS::Detective::Graph
Properties:
  [AutoEnableMembers](#cfn-detective-graph-autoenablemembers): {{Boolean}}
  [Tags](#cfn-detective-graph-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-detective-graph-properties"></a>

`AutoEnableMembers`  <a name="cfn-detective-graph-autoenablemembers"></a>
Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.
By default, this property is set to `false`. If you want to change the value of this property, you must be the Detective administrator for the organization. For more information on setting a Detective administrator account, see [AWS::Detective::OrganizationAdmin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-detective-graph-tags"></a>
The tag values to assign to the new behavior graph.
*Required*: No
*Type*: Array of [Tag](aws-properties-detective-graph-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-detective-graph-return-values"></a>

### Ref
<a name="aws-resource-detective-graph-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the new behavior graph.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-detective-graph-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-detective-graph-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the new behavior graph.

## Examples
<a name="aws-resource-detective-graph--examples"></a>

### Creating a new Detective behavior graph
<a name="aws-resource-detective-graph--examples--Creating_a_new_Detective_behavior_graph"></a>

This example shows how to declare a new `AWS:Detective:Graph` resource to create a new Detective behavior graph

#### JSON
<a name="aws-resource-detective-graph--examples--Creating_a_new_Detective_behavior_graph--json"></a>

```
"NewGraph": {
    "Type": "AWS::Detective::Graph"
    "Properties": {
        "Tags": [
            {
                "Key": "Tag1Name",
                "Value": "Tag1Value"
            },
            {
                "Key": "Tag2Name".
                "Value": "Tag2alue"
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-detective-graph--examples--Creating_a_new_Detective_behavior_graph--yaml"></a>

```
NewGraph:
    Type: AWS::Detective::Graph
    Properties:
        Tags:
            - Key: Tag1Name
              Value: Tag1Value
            - Key: Tag2Name
              Value: Tag2Value
```
