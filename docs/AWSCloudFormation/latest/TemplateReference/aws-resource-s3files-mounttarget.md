---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3files-mounttarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::MountTarget
<a name="aws-resource-s3files-mounttarget"></a>

The `AWS::S3Files::MountTarget` resource specifies a mount target for an Amazon S3 Files file system. Mount targets provide network access to the file system from compute resources in a specific Availability Zone and VPC.

## Syntax
<a name="aws-resource-s3files-mounttarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3files-mounttarget-syntax.json"></a>

```
{
  "Type" : "AWS::S3Files::MountTarget",
  "Properties" : {
      "[FileSystemId](#cfn-s3files-mounttarget-filesystemid)" : {{String}},
      "[IpAddressType](#cfn-s3files-mounttarget-ipaddresstype)" : {{String}},
      "[Ipv4Address](#cfn-s3files-mounttarget-ipv4address)" : {{String}},
      "[Ipv6Address](#cfn-s3files-mounttarget-ipv6address)" : {{String}},
      "[SecurityGroups](#cfn-s3files-mounttarget-securitygroups)" : {{[ String, ... ]}},
      "[SubnetId](#cfn-s3files-mounttarget-subnetid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-s3files-mounttarget-syntax.yaml"></a>

```
Type: AWS::S3Files::MountTarget
Properties:
  [FileSystemId](#cfn-s3files-mounttarget-filesystemid): {{String}}
  [IpAddressType](#cfn-s3files-mounttarget-ipaddresstype): {{String}}
  [Ipv4Address](#cfn-s3files-mounttarget-ipv4address): {{String}}
  [Ipv6Address](#cfn-s3files-mounttarget-ipv6address): {{String}}
  [SecurityGroups](#cfn-s3files-mounttarget-securitygroups): {{
    - String}}
  [SubnetId](#cfn-s3files-mounttarget-subnetid): {{String}}
```

## Properties
<a name="aws-resource-s3files-mounttarget-properties"></a>

`FileSystemId`  <a name="cfn-s3files-mounttarget-filesystemid"></a>
The ID of the S3 Files file system for which to create the mount target.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddressType`  <a name="cfn-s3files-mounttarget-ipaddresstype"></a>
The type of IP address used by the mount target. Valid values are `IPV4_ONLY`, `IPV6_ONLY`, and `DUAL_STACK`.
*Required*: No
*Type*: String
*Allowed values*: `IPV4_ONLY | IPV6_ONLY | DUAL_STACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv4Address`  <a name="cfn-s3files-mounttarget-ipv4address"></a>
The IPv4 address of the mount target.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$`
*Minimum*: `7`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6Address`  <a name="cfn-s3files-mounttarget-ipv6address"></a>
The IPv6 address of the mount target.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `39`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroups`  <a name="cfn-s3files-mounttarget-securitygroups"></a>
Up to 100 VPC security group IDs that control network access to the mount target.
*Required*: No
*Type*: Array of String
*Minimum*: `11`
*Maximum*: `43 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-s3files-mounttarget-subnetid"></a>
The ID of the subnet where the mount target is located.
*Required*: Yes
*Type*: String
*Pattern*: `^subnet-[0-9a-f]{8,40}$`
*Minimum*: `15`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3files-mounttarget-return-values"></a>

### Ref
<a name="aws-resource-s3files-mounttarget-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the mount target ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3files-mounttarget-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3files-mounttarget-return-values-fn--getatt-fn--getatt"></a>

`AvailabilityZoneId`  <a name="AvailabilityZoneId-fn::getatt"></a>
The ID of the Availability Zone in which the mount target is located.

`MountTargetId`  <a name="MountTargetId-fn::getatt"></a>
The ID of the mount target.

`NetworkInterfaceId`  <a name="NetworkInterfaceId-fn::getatt"></a>
The ID of the network interface that Amazon S3 Files created when it created the mount target.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The AWS account ID of the mount target owner.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the mount target.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
Additional information about the mount target status.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the VPC in which the mount target is located.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
