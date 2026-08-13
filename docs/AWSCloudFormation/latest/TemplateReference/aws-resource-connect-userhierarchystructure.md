---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-userhierarchystructure.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::UserHierarchyStructure
<a name="aws-resource-connect-userhierarchystructure"></a>

Contains information about a hierarchy structure.

## Syntax
<a name="aws-resource-connect-userhierarchystructure-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-userhierarchystructure-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::UserHierarchyStructure",
  "Properties" : {
      "[InstanceArn](#cfn-connect-userhierarchystructure-instancearn)" : {{String}},
      "[UserHierarchyStructure](#cfn-connect-userhierarchystructure-userhierarchystructure)" : {{UserHierarchyStructure}}
    }
}
```

### YAML
<a name="aws-resource-connect-userhierarchystructure-syntax.yaml"></a>

```
Type: AWS::Connect::UserHierarchyStructure
Properties:
  [InstanceArn](#cfn-connect-userhierarchystructure-instancearn): {{String}}
  [UserHierarchyStructure](#cfn-connect-userhierarchystructure-userhierarchystructure): {{
    UserHierarchyStructure}}
```

## Properties
<a name="aws-resource-connect-userhierarchystructure-properties"></a>

`InstanceArn`  <a name="cfn-connect-userhierarchystructure-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserHierarchyStructure`  <a name="cfn-connect-userhierarchystructure-userhierarchystructure"></a>
Contains information about a hierarchy structure.
*Required*: No
*Type*: [UserHierarchyStructure](aws-properties-connect-userhierarchystructure-userhierarchystructure.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-userhierarchystructure-return-values"></a>

### Ref
<a name="aws-resource-connect-userhierarchystructure-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the user hierarchy structure. For example:

 `{ "Ref": "myhierarchystructure" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-userhierarchystructure-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-userhierarchystructure-return-values-fn--getatt-fn--getatt"></a>

`UserHierarchyStructureArn`  <a name="UserHierarchyStructureArn-fn::getatt"></a>
The identifier for the user hierarchy structure.
