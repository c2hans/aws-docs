---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-placement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet Placement
<a name="aws-properties-ec2-ec2fleet-placement"></a>

Describes the placement of an instance.

## Syntax
<a name="aws-properties-ec2-ec2fleet-placement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-placement-syntax.json"></a>

```
{
  "[Affinity](#cfn-ec2-ec2fleet-placement-affinity)" : {{String}},
  "[AvailabilityZone](#cfn-ec2-ec2fleet-placement-availabilityzone)" : {{String}},
  "[GroupName](#cfn-ec2-ec2fleet-placement-groupname)" : {{String}},
  "[HostId](#cfn-ec2-ec2fleet-placement-hostid)" : {{String}},
  "[HostResourceGroupArn](#cfn-ec2-ec2fleet-placement-hostresourcegrouparn)" : {{String}},
  "[PartitionNumber](#cfn-ec2-ec2fleet-placement-partitionnumber)" : {{Integer}},
  "[SpreadDomain](#cfn-ec2-ec2fleet-placement-spreaddomain)" : {{String}},
  "[Tenancy](#cfn-ec2-ec2fleet-placement-tenancy)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-placement-syntax.yaml"></a>

```
  [Affinity](#cfn-ec2-ec2fleet-placement-affinity): {{String}}
  [AvailabilityZone](#cfn-ec2-ec2fleet-placement-availabilityzone): {{String}}
  [GroupName](#cfn-ec2-ec2fleet-placement-groupname): {{String}}
  [HostId](#cfn-ec2-ec2fleet-placement-hostid): {{String}}
  [HostResourceGroupArn](#cfn-ec2-ec2fleet-placement-hostresourcegrouparn): {{String}}
  [PartitionNumber](#cfn-ec2-ec2fleet-placement-partitionnumber): {{Integer}}
  [SpreadDomain](#cfn-ec2-ec2fleet-placement-spreaddomain): {{String}}
  [Tenancy](#cfn-ec2-ec2fleet-placement-tenancy): {{String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-placement-properties"></a>

`Affinity`  <a name="cfn-ec2-ec2fleet-placement-affinity"></a>
The affinity setting for the instance on the Dedicated Host.
This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityZone`  <a name="cfn-ec2-ec2fleet-placement-availabilityzone"></a>
The Availability Zone of the instance.
On input, you can specify `AvailabilityZone` or `AvailabilityZoneId`, but not both. If you specify neither one, Amazon EC2 automatically selects an Availability Zone for you.
This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupName`  <a name="cfn-ec2-ec2fleet-placement-groupname"></a>
The name of the placement group that the instance is in.
On input, you can specify `GroupId` or `GroupName`, but not both.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostId`  <a name="cfn-ec2-ec2fleet-placement-hostid"></a>
The ID of the Dedicated Host on which the instance resides.
This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostResourceGroupArn`  <a name="cfn-ec2-ec2fleet-placement-hostresourcegrouparn"></a>
The ARN of the host resource group in which to launch the instances.
On input, if you specify this parameter, either omit the **Tenancy** parameter or set it to `host`.
This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PartitionNumber`  <a name="cfn-ec2-ec2fleet-placement-partitionnumber"></a>
The number of the partition that the instance is in. Valid only if the placement group strategy is set to `partition`.
This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet).
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpreadDomain`  <a name="cfn-ec2-ec2fleet-placement-spreaddomain"></a>
Reserved for future use.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tenancy`  <a name="cfn-ec2-ec2fleet-placement-tenancy"></a>
The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware.
This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet). The `host` tenancy is not supported for [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) or for T3 instances that are configured for the `unlimited` CPU credit option.
*Required*: No
*Type*: String
*Allowed values*: `default | dedicated | host`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
