---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-mounttarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::MountTarget
<a name="aws-resource-efs-mounttarget"></a>

The `AWS::EFS::MountTarget` resource is an Amazon EFS resource that creates a mount target for an EFS file system. You can then mount the file system on Amazon EC2 instances or other resources by using the mount target.

## Syntax
<a name="aws-resource-efs-mounttarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-efs-mounttarget-syntax.json"></a>

```
{
  "Type" : "AWS::EFS::MountTarget",
  "Properties" : {
      "[FileSystemId](#cfn-efs-mounttarget-filesystemid)" : {{String}},
      "[IpAddress](#cfn-efs-mounttarget-ipaddress)" : {{String}},
      "[IpAddressType](#cfn-efs-mounttarget-ipaddresstype)" : {{String}},
      "[Ipv6Address](#cfn-efs-mounttarget-ipv6address)" : {{String}},
      "[SecurityGroups](#cfn-efs-mounttarget-securitygroups)" : {{[ String, ... ]}},
      "[SubnetId](#cfn-efs-mounttarget-subnetid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-efs-mounttarget-syntax.yaml"></a>

```
Type: AWS::EFS::MountTarget
Properties:
  [FileSystemId](#cfn-efs-mounttarget-filesystemid): {{String}}
  [IpAddress](#cfn-efs-mounttarget-ipaddress): {{String}}
  [IpAddressType](#cfn-efs-mounttarget-ipaddresstype): {{String}}
  [Ipv6Address](#cfn-efs-mounttarget-ipv6address): {{String}}
  [SecurityGroups](#cfn-efs-mounttarget-securitygroups): {{
    - String}}
  [SubnetId](#cfn-efs-mounttarget-subnetid): {{String}}
```

## Properties
<a name="aws-resource-efs-mounttarget-properties"></a>

`FileSystemId`  <a name="cfn-efs-mounttarget-filesystemid"></a>
The ID of the file system for which to create the mount target.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddress`  <a name="cfn-efs-mounttarget-ipaddress"></a>
If the `IpAddressType` for the mount target is IPv4 ( `IPV4_ONLY` or `DUAL_STACK`), then specify the IPv4 address to use. If you do not specify an `IpAddress`, then Amazon EFS selects an unused IP address from the subnet specified for `SubnetId`.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$`
*Minimum*: `7`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddressType`  <a name="cfn-efs-mounttarget-ipaddresstype"></a>
The IP address type for the mount target. The possible values are `IPV4_ONLY` (only IPv4 addresses), `IPV6_ONLY` (only IPv6 addresses), and `DUAL_STACK` (dual-stack, both IPv4 and IPv6 addresses). If you don’t specify an `IpAddressType`, then `IPV4_ONLY` is used.
The `IPAddressType` must match the IP type of the subnet. Additionally, the `IPAddressType` parameter overrides the value set as the default IP address for the subnet in the VPC. For example, if the `IPAddressType` is `IPV4_ONLY` and `AssignIpv6AddressOnCreation` is `true`, then IPv4 is used for the mount target. For more information, see [Modify the IP addressing attributes of your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-public-ip.html).
*Required*: No
*Type*: String
*Allowed values*: `IPV4_ONLY | IPV6_ONLY | DUAL_STACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6Address`  <a name="cfn-efs-mounttarget-ipv6address"></a>
If the `IPAddressType` for the mount target is IPv6 (`IPV6_ONLY` or `DUAL_STACK`), then specify the IPv6 address to use. If you do not specify an `Ipv6Address`, then Amazon EFS selects an unused IP address from the subnet specified for `SubnetId`.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `39`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroups`  <a name="cfn-efs-mounttarget-securitygroups"></a>
VPC security group IDs, of the form `sg-xxxxxxxx`. These must be for the same VPC as the subnet specified. The maximum number of security groups depends on account quota. For more information, see [Amazon VPC Quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the *Amazon VPC User Guide* (see the **Security Groups** table). If you don't specify a security group, then Amazon EFS uses the default security group for the subnet's VPC.
*Required*: Yes
*Type*: Array of String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-efs-mounttarget-subnetid"></a>
The ID of the subnet to add the mount target in. For One Zone file systems, use the subnet that is associated with the file system's Availability Zone. The subnet type must be the same type as the `IpAddressType`.
*Required*: Yes
*Type*: String
*Pattern*: `^subnet-[0-9a-f]{8,40}$`
*Minimum*: `15`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-efs-mounttarget-return-values"></a>

### Ref
<a name="aws-resource-efs-mounttarget-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the MountTarget ID. For example:

`{"Ref":"logical_mount_target_id"}` returns

`fsmt-0123456789abcdef8`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-efs-mounttarget-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-efs-mounttarget-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the Amazon EFS file system that the mount target provides access to.
Example: `fs-0123456789111222a`

`IpAddress`  <a name="IpAddress-fn::getatt"></a>
The IPv4 address of the mount target.
Example: 192.0.2.0

## Examples
<a name="aws-resource-efs-mounttarget--examples"></a>

### Declare a Mount Target for an EFS File System
<a name="aws-resource-efs-mounttarget--examples--Declare_a_Mount_Target_for_an_EFS_File_System"></a>

The following example declares a mount target that is associated with a file system, subnet, and security group, which are all declared in the same template. EC2 instances that are in the same Availability Zone (AZ) as the mount target can use the mount target to connect to the associated file system. For information about mounting file systems on EC2 instances, see [Mounting File Systems](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs.html) in the *EFS User Guide*.

#### JSON
<a name="aws-resource-efs-mounttarget--examples--Declare_a_Mount_Target_for_an_EFS_File_System--json"></a>

```
"MountTarget": {
  "Type": "AWS::EFS::MountTarget",
  "Properties": {
    "FileSystemId": { "Ref": "FileSystem" },
    "SubnetId": { "Ref": "Subnet" },
    "SecurityGroups": [ { "Ref": "MountTargetSecurityGroup" } ]
  }
}
```

#### YAML
<a name="aws-resource-efs-mounttarget--examples--Declare_a_Mount_Target_for_an_EFS_File_System--yaml"></a>

```
MountTarget:
  Type: AWS::EFS::MountTarget
  Properties:
    FileSystemId:
      Ref: "FileSystem"
    SubnetId:
      Ref: "Subnet"
    SecurityGroups:
      - Ref: "MountTargetSecurityGroup"
```

## See also
<a name="aws-resource-efs-mounttarget--seealso"></a>
+  [Amazon EFS: How it works](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)
+  [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)
+  [Walkthrough: Mounting a file system on-premises](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
