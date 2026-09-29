---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ram-principalassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::PrincipalAssociation
<a name="aws-resource-ram-principalassociation"></a>

<a name="aws-resource-ram-principalassociation-description"></a>The `AWS::RAM::PrincipalAssociation` resource Property description not available. for RAM.

## Syntax
<a name="aws-resource-ram-principalassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ram-principalassociation-syntax.json"></a>

```
{
  "Type" : "AWS::RAM::PrincipalAssociation",
  "Properties" : {
      "[Principal](#cfn-ram-principalassociation-principal)" : {{String}},
      "[ResourceShareArn](#cfn-ram-principalassociation-resourcesharearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ram-principalassociation-syntax.yaml"></a>

```
Type: AWS::RAM::PrincipalAssociation
Properties:
  [Principal](#cfn-ram-principalassociation-principal): {{String}}
  [ResourceShareArn](#cfn-ram-principalassociation-resourcesharearn): {{String}}
```

## Properties
<a name="aws-resource-ram-principalassociation-properties"></a>

`Principal`  <a name="cfn-ram-principalassociation-principal"></a>
Describes a principal for use with AWS Resource Access Manager.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceShareArn`  <a name="cfn-ram-principalassociation-resourcesharearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ram-principalassociation-return-values"></a>

### Ref
<a name="aws-resource-ram-principalassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ram-principalassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-ram-principalassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationType`  <a name="AssociationType-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`External`  <a name="External-fn::getatt"></a>
Property description not available.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
