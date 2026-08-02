---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-snapshotblockpublicaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SnapshotBlockPublicAccess
<a name="aws-resource-ec2-snapshotblockpublicaccess"></a>

Specifies the state of the *block public access for snapshots* setting for the Region. For more information, see [Block public access for snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots.html).

## Syntax
<a name="aws-resource-ec2-snapshotblockpublicaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-snapshotblockpublicaccess-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::SnapshotBlockPublicAccess",
  "Properties" : {
      "[State](#cfn-ec2-snapshotblockpublicaccess-state)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-snapshotblockpublicaccess-syntax.yaml"></a>

```
Type: AWS::EC2::SnapshotBlockPublicAccess
Properties:
  [State](#cfn-ec2-snapshotblockpublicaccess-state): {{String}}
```

## Properties
<a name="aws-resource-ec2-snapshotblockpublicaccess-properties"></a>

`State`  <a name="cfn-ec2-snapshotblockpublicaccess-state"></a>
The mode in which to enable block public access for snapshots for the Region. Specify one of the following values:
+ `block-all-sharing` - Prevents all public sharing of snapshots in the Region. Users in the account will no longer be able to request new public sharing. Additionally, snapshots that are already publicly shared are treated as private and they are no longer publicly available.
**Note**
If you enable block public access for snapshots in `block-all-sharing` mode, it does not change the permissions for snapshots that are already publicly shared. Instead, it prevents these snapshots from be publicly visible and publicly accessible. Therefore, the attributes for these snapshots still indicate that they are publicly shared, even though they are not publicly available.
+ `block-new-sharing` - Prevents only new public sharing of snapshots in the Region. Users in the account will no longer be able to request new public sharing. However, snapshots that are already publicly shared, remain publicly available.
*Required*: Yes
*Type*: String
*Allowed values*: `block-all-sharing | block-new-sharing`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-snapshotblockpublicaccess-return-values"></a>

### Ref
<a name="aws-resource-ec2-snapshotblockpublicaccess-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the AWS account.

### Fn::GetAtt
<a name="aws-resource-ec2-snapshotblockpublicaccess-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-snapshotblockpublicaccess-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the AWS account.
