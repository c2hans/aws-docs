---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-ipamprefixlistresolvertarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAMPrefixListResolverTarget
<a name="aws-resource-ec2-ipamprefixlistresolvertarget"></a>

An IPAM prefix list resolver target is an association between a specific customer-managed prefix list and an IPAM prefix list resolver. The target enables the resolver to synchronize CIDRs selected by its rules into the specified prefix list, which can then be referenced in AWS resources.

## Syntax
<a name="aws-resource-ec2-ipamprefixlistresolvertarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-ipamprefixlistresolvertarget-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::IPAMPrefixListResolverTarget",
  "Properties" : {
      "[DesiredVersion](#cfn-ec2-ipamprefixlistresolvertarget-desiredversion)" : {{Integer}},
      "[IpamPrefixListResolverId](#cfn-ec2-ipamprefixlistresolvertarget-ipamprefixlistresolverid)" : {{String}},
      "[PrefixListId](#cfn-ec2-ipamprefixlistresolvertarget-prefixlistid)" : {{String}},
      "[PrefixListRegion](#cfn-ec2-ipamprefixlistresolvertarget-prefixlistregion)" : {{String}},
      "[Tags](#cfn-ec2-ipamprefixlistresolvertarget-tags)" : {{[ Tag, ... ]}},
      "[TrackLatestVersion](#cfn-ec2-ipamprefixlistresolvertarget-tracklatestversion)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-ec2-ipamprefixlistresolvertarget-syntax.yaml"></a>

```
Type: AWS::EC2::IPAMPrefixListResolverTarget
Properties:
  [DesiredVersion](#cfn-ec2-ipamprefixlistresolvertarget-desiredversion): {{Integer}}
  [IpamPrefixListResolverId](#cfn-ec2-ipamprefixlistresolvertarget-ipamprefixlistresolverid): {{String}}
  [PrefixListId](#cfn-ec2-ipamprefixlistresolvertarget-prefixlistid): {{String}}
  [PrefixListRegion](#cfn-ec2-ipamprefixlistresolvertarget-prefixlistregion): {{String}}
  [Tags](#cfn-ec2-ipamprefixlistresolvertarget-tags): {{
    - Tag}}
  [TrackLatestVersion](#cfn-ec2-ipamprefixlistresolvertarget-tracklatestversion): {{Boolean}}
```

## Properties
<a name="aws-resource-ec2-ipamprefixlistresolvertarget-properties"></a>

`DesiredVersion`  <a name="cfn-ec2-ipamprefixlistresolvertarget-desiredversion"></a>
The desired version of the prefix list that this target should synchronize with.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamPrefixListResolverId`  <a name="cfn-ec2-ipamprefixlistresolvertarget-ipamprefixlistresolverid"></a>
The ID of the IPAM prefix list resolver associated with this target.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrefixListId`  <a name="cfn-ec2-ipamprefixlistresolvertarget-prefixlistid"></a>
The ID of the managed prefix list associated with this target.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrefixListRegion`  <a name="cfn-ec2-ipamprefixlistresolvertarget-prefixlistregion"></a>
The AWS Region where the prefix list associated with this target is located.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-ipamprefixlistresolvertarget-tags"></a>
The tags assigned to the IPAM prefix list resolver target.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-ipamprefixlistresolvertarget-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrackLatestVersion`  <a name="cfn-ec2-ipamprefixlistresolvertarget-tracklatestversion"></a>
Indicates whether this target automatically tracks the latest version of the prefix list.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-ipamprefixlistresolvertarget-return-values"></a>

### Ref
<a name="aws-resource-ec2-ipamprefixlistresolvertarget-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the prefix list resolver target ID. For example: `ipam-plrt-111122223333`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-ipamprefixlistresolvertarget-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-ipamprefixlistresolvertarget-return-values-fn--getatt-fn--getatt"></a>

`IpamPrefixListResolverTargetArn`  <a name="IpamPrefixListResolverTargetArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the IPAM prefix list resolver target.

`IpamPrefixListResolverTargetId`  <a name="IpamPrefixListResolverTargetId-fn::getatt"></a>
The ID of the IPAM prefix list resolver target.
