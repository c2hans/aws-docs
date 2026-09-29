---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ram-permissionassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::PermissionAssociation
<a name="aws-resource-ram-permissionassociation"></a>

<a name="aws-resource-ram-permissionassociation-description"></a>The `AWS::RAM::PermissionAssociation` resource Property description not available. for RAM.

## Syntax
<a name="aws-resource-ram-permissionassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ram-permissionassociation-syntax.json"></a>

```
{
  "Type" : "AWS::RAM::PermissionAssociation",
  "Properties" : {
      "[PermissionArn](#cfn-ram-permissionassociation-permissionarn)" : {{String}},
      "[Replace](#cfn-ram-permissionassociation-replace)" : {{Boolean}},
      "[ResourceShareArn](#cfn-ram-permissionassociation-resourcesharearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ram-permissionassociation-syntax.yaml"></a>

```
Type: AWS::RAM::PermissionAssociation
Properties:
  [PermissionArn](#cfn-ram-permissionassociation-permissionarn): {{String}}
  [Replace](#cfn-ram-permissionassociation-replace): {{Boolean}}
  [ResourceShareArn](#cfn-ram-permissionassociation-resourcesharearn): {{String}}
```

## Properties
<a name="aws-resource-ram-permissionassociation-properties"></a>

`PermissionArn`  <a name="cfn-ram-permissionassociation-permissionarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Replace`  <a name="cfn-ram-permissionassociation-replace"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceShareArn`  <a name="cfn-ram-permissionassociation-resourcesharearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ram-permissionassociation-return-values"></a>

### Ref
<a name="aws-resource-ram-permissionassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ram-permissionassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-ram-permissionassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationStatus`  <a name="AssociationStatus-fn::getatt"></a>
Property description not available.

`FeatureSet`  <a name="FeatureSet-fn::getatt"></a>
Property description not available.

`IsDefault`  <a name="IsDefault-fn::getatt"></a>
Property description not available.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The date and time when the status of this background task was last updated.

`PermissionVersion`  <a name="PermissionVersion-fn::getatt"></a>
Property description not available.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
The resource type. This takes the form of: `service-code`:`resource-code`, and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string `ec2:subnet`.
