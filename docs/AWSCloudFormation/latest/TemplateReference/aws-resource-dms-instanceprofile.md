---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-instanceprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::InstanceProfile
<a name="aws-resource-dms-instanceprofile"></a>

Provides information that defines an instance profile.

## Syntax
<a name="aws-resource-dms-instanceprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dms-instanceprofile-syntax.json"></a>

```
{
  "Type" : "AWS::DMS::InstanceProfile",
  "Properties" : {
      "[AvailabilityZone](#cfn-dms-instanceprofile-availabilityzone)" : {{String}},
      "[Description](#cfn-dms-instanceprofile-description)" : {{String}},
      "[InstanceProfileIdentifier](#cfn-dms-instanceprofile-instanceprofileidentifier)" : {{String}},
      "[InstanceProfileName](#cfn-dms-instanceprofile-instanceprofilename)" : {{String}},
      "[KmsKeyArn](#cfn-dms-instanceprofile-kmskeyarn)" : {{String}},
      "[NetworkType](#cfn-dms-instanceprofile-networktype)" : {{String}},
      "[PubliclyAccessible](#cfn-dms-instanceprofile-publiclyaccessible)" : {{Boolean}},
      "[SubnetGroupIdentifier](#cfn-dms-instanceprofile-subnetgroupidentifier)" : {{String}},
      "[Tags](#cfn-dms-instanceprofile-tags)" : {{[ Tag, ... ]}},
      "[VpcSecurityGroups](#cfn-dms-instanceprofile-vpcsecuritygroups)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-dms-instanceprofile-syntax.yaml"></a>

```
Type: AWS::DMS::InstanceProfile
Properties:
  [AvailabilityZone](#cfn-dms-instanceprofile-availabilityzone): {{String}}
  [Description](#cfn-dms-instanceprofile-description): {{String}}
  [InstanceProfileIdentifier](#cfn-dms-instanceprofile-instanceprofileidentifier): {{String}}
  [InstanceProfileName](#cfn-dms-instanceprofile-instanceprofilename): {{String}}
  [KmsKeyArn](#cfn-dms-instanceprofile-kmskeyarn): {{String}}
  [NetworkType](#cfn-dms-instanceprofile-networktype): {{String}}
  [PubliclyAccessible](#cfn-dms-instanceprofile-publiclyaccessible): {{Boolean}}
  [SubnetGroupIdentifier](#cfn-dms-instanceprofile-subnetgroupidentifier): {{String}}
  [Tags](#cfn-dms-instanceprofile-tags): {{
    - Tag}}
  [VpcSecurityGroups](#cfn-dms-instanceprofile-vpcsecuritygroups): {{
    - String}}
```

## Properties
<a name="aws-resource-dms-instanceprofile-properties"></a>

`AvailabilityZone`  <a name="cfn-dms-instanceprofile-availabilityzone"></a>
The Availability Zone where the instance profile runs.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-dms-instanceprofile-description"></a>
A description of the instance profile. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceProfileIdentifier`  <a name="cfn-dms-instanceprofile-instanceprofileidentifier"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceProfileName`  <a name="cfn-dms-instanceprofile-instanceprofilename"></a>
The user-friendly name for the instance profile.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-dms-instanceprofile-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt the connection parameters for the instance profile.
If you don't specify a value for the `KmsKeyArn` parameter, then AWS DMS uses an AWS owned encryption key to encrypt your resources.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkType`  <a name="cfn-dms-instanceprofile-networktype"></a>
Specifies the network type for the instance profile. A value of `IPV4` represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of `IPV6` represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of `DUAL` represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-dms-instanceprofile-publiclyaccessible"></a>
Specifies the accessibility options for the instance profile. A value of `true` represents an instance profile with a public IP address. A value of `false` represents an instance profile with a private IP address. The default value is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetGroupIdentifier`  <a name="cfn-dms-instanceprofile-subnetgroupidentifier"></a>
The identifier of the subnet group that is associated with the instance profile.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dms-instanceprofile-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-dms-instanceprofile-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcSecurityGroups`  <a name="cfn-dms-instanceprofile-vpcsecuritygroups"></a>
The VPC security groups that are used with the instance profile. The VPC security group must work with the VPC containing the instance profile.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dms-instanceprofile-return-values"></a>

### Ref
<a name="aws-resource-dms-instanceprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dms-instanceprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-dms-instanceprofile-return-values-fn--getatt-fn--getatt"></a>

`InstanceProfileArn`  <a name="InstanceProfileArn-fn::getatt"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the instance profile.

`InstanceProfileCreationTime`  <a name="InstanceProfileCreationTime-fn::getatt"></a>
The time the instance profile was created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
