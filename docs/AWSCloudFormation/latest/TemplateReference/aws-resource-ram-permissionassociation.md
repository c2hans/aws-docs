---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ram-permissionassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::PermissionAssociation
<a name="aws-resource-ram-permissionassociation"></a>

Associates a specified AWS RAM permission with a resource share. You can only associate one permission with each resource type in a resource share.

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
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS RAM permission to associate with the resource share.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Replace`  <a name="cfn-ram-permissionassociation-replace"></a>
Specifies whether to replace the existing permission on the resource share. Use `true` to replace the current permission. Use `false` to add the permission when no permission is currently associated. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceShareArn`  <a name="cfn-ram-permissionassociation-resourcesharearn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ram-permissionassociation-return-values"></a>

### Ref
<a name="aws-resource-ram-permissionassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource share ARN and permission ARN in the format `resource-share-arn|permission-arn`. For example: `arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2|arn:aws:ram::aws:permission/AWSRAMPermissionGlueDatabaseReadWrite`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ram-permissionassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ram-permissionassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationStatus`  <a name="AssociationStatus-fn::getatt"></a>
The current status of the association between the permission and the resource share. Possible values include `ASSOCIATING`, `ASSOCIATED`, `FAILED`, `DISASSOCIATING`, `DISASSOCIATED`, `SUSPENDED`, `SUSPENDING`, and `RESTORING`.

`FeatureSet`  <a name="FeatureSet-fn::getatt"></a>
The feature set of the resource share. Possible values include `STANDARD`, `CREATED_FROM_POLICY`, and `PROMOTING_TO_STANDARD`.

`IsDefault`  <a name="IsDefault-fn::getatt"></a>
Indicates whether the associated resource share is using the default version of the permission.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The date and time when the association between the permission and the resource share was last updated.

`PermissionVersion`  <a name="PermissionVersion-fn::getatt"></a>
The version of the permission currently associated with the resource share.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
The resource type to which the permission applies.

## Examples
<a name="aws-resource-ram-permissionassociation--examples"></a>

### Associating a permission with a resource share
<a name="aws-resource-ram-permissionassociation--examples--Associating_a_permission_with_a_resource_share"></a>

The following example associates a permission with a resource share.

#### YAML
<a name="aws-resource-ram-permissionassociation--examples--Associating_a_permission_with_a_resource_share--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyPermissionAssociation:
    Type: AWS::RAM::PermissionAssociation
    Properties:
      PermissionArn: arn:aws:ram::aws:permission/AWSRAMPermissionGlueDatabaseReadWrite
      ResourceShareArn: !Sub arn:aws:ram:${AWS::Region}:${AWS::AccountId}:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2
```

#### JSON
<a name="aws-resource-ram-permissionassociation--examples--Associating_a_permission_with_a_resource_share--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyPermissionAssociation": {
      "Type": "AWS::RAM::PermissionAssociation",
      "Properties": {
        "PermissionArn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueDatabaseReadWrite",
        "ResourceShareArn": {
          "Fn::Sub": "arn:aws:ram:${AWS::Region}:${AWS::AccountId}:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2"
        }
      }
    }
  }
}
```

## See also
<a name="aws-resource-ram-permissionassociation--seealso"></a>
+ [AssociateResourceSharePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceSharePermission.html) in the *AWS Resource Access Manager API Reference*
+  [AWS Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide)
