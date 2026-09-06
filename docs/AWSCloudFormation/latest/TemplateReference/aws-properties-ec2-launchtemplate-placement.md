---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-placement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate Placement
<a name="aws-properties-ec2-launchtemplate-placement"></a>

Specifies the placement of an instance.

`Placement` is a property of [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-placement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-placement-syntax.json"></a>

```
{
  "[Affinity](#cfn-ec2-launchtemplate-placement-affinity)" : {{String}},
  "[AvailabilityZone](#cfn-ec2-launchtemplate-placement-availabilityzone)" : {{String}},
  "[GroupId](#cfn-ec2-launchtemplate-placement-groupid)" : {{String}},
  "[GroupName](#cfn-ec2-launchtemplate-placement-groupname)" : {{String}},
  "[HostId](#cfn-ec2-launchtemplate-placement-hostid)" : {{String}},
  "[HostResourceGroupArn](#cfn-ec2-launchtemplate-placement-hostresourcegrouparn)" : {{String}},
  "[PartitionNumber](#cfn-ec2-launchtemplate-placement-partitionnumber)" : {{Integer}},
  "[SpreadDomain](#cfn-ec2-launchtemplate-placement-spreaddomain)" : {{String}},
  "[Tenancy](#cfn-ec2-launchtemplate-placement-tenancy)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-placement-syntax.yaml"></a>

```
  [Affinity](#cfn-ec2-launchtemplate-placement-affinity): {{String}}
  [AvailabilityZone](#cfn-ec2-launchtemplate-placement-availabilityzone): {{String}}
  [GroupId](#cfn-ec2-launchtemplate-placement-groupid): {{String}}
  [GroupName](#cfn-ec2-launchtemplate-placement-groupname): {{String}}
  [HostId](#cfn-ec2-launchtemplate-placement-hostid): {{String}}
  [HostResourceGroupArn](#cfn-ec2-launchtemplate-placement-hostresourcegrouparn): {{String}}
  [PartitionNumber](#cfn-ec2-launchtemplate-placement-partitionnumber): {{Integer}}
  [SpreadDomain](#cfn-ec2-launchtemplate-placement-spreaddomain): {{String}}
  [Tenancy](#cfn-ec2-launchtemplate-placement-tenancy): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-placement-properties"></a>

`Affinity`  <a name="cfn-ec2-launchtemplate-placement-affinity"></a>
The affinity setting for an instance on a Dedicated Host.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZone`  <a name="cfn-ec2-launchtemplate-placement-availabilityzone"></a>
The Availability Zone for the instance.
Either `AvailabilityZone` or `AvailabilityZoneId` can be specified, but not both
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupId`  <a name="cfn-ec2-launchtemplate-placement-groupid"></a>
The Group Id of a placement group. You must specify the Placement Group **Group Id** to launch an instance in a shared placement group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupName`  <a name="cfn-ec2-launchtemplate-placement-groupname"></a>
The name of the placement group for the instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostId`  <a name="cfn-ec2-launchtemplate-placement-hostid"></a>
The ID of the Dedicated Host for the instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostResourceGroupArn`  <a name="cfn-ec2-launchtemplate-placement-hostresourcegrouparn"></a>
The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the **Tenancy** parameter or set it to `host`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartitionNumber`  <a name="cfn-ec2-launchtemplate-placement-partitionnumber"></a>
The number of the partition the instance should launch in. Valid only if the placement group strategy is set to `partition`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpreadDomain`  <a name="cfn-ec2-launchtemplate-placement-spreaddomain"></a>
Reserved for future use.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tenancy`  <a name="cfn-ec2-launchtemplate-placement-tenancy"></a>
The tenancy of the instance. An instance with a tenancy of dedicated runs on single-tenant hardware.
*Required*: No
*Type*: String
*Allowed values*: `default | dedicated | host`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-placement--seealso"></a>
+ [ LaunchTemplatePlacementRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplatePlacementRequest.html) in the *Amazon EC2 API Reference*
+ [ Create a launch template using advanced settings](https://docs.aws.amazon.com/autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*
