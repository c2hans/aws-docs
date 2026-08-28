---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-hostinfoforcreate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment HostInfoForCreate
<a name="aws-properties-evs-environment-hostinfoforcreate"></a>

An object that represents a host.

**Note**
You cannot use `dedicatedHostId` and `placementGroupId` together in the same `HostInfoForCreate`object. This results in a `ValidationException` response.

## Syntax
<a name="aws-properties-evs-environment-hostinfoforcreate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-hostinfoforcreate-syntax.json"></a>

```
{
  "[DedicatedHostId](#cfn-evs-environment-hostinfoforcreate-dedicatedhostid)" : {{String}},
  "[HostName](#cfn-evs-environment-hostinfoforcreate-hostname)" : {{String}},
  "[InstanceType](#cfn-evs-environment-hostinfoforcreate-instancetype)" : {{String}},
  "[KeyName](#cfn-evs-environment-hostinfoforcreate-keyname)" : {{String}},
  "[PlacementGroupId](#cfn-evs-environment-hostinfoforcreate-placementgroupid)" : {{String}}
}
```

### YAML
<a name="aws-properties-evs-environment-hostinfoforcreate-syntax.yaml"></a>

```
  [DedicatedHostId](#cfn-evs-environment-hostinfoforcreate-dedicatedhostid): {{String}}
  [HostName](#cfn-evs-environment-hostinfoforcreate-hostname): {{String}}
  [InstanceType](#cfn-evs-environment-hostinfoforcreate-instancetype): {{String}}
  [KeyName](#cfn-evs-environment-hostinfoforcreate-keyname): {{String}}
  [PlacementGroupId](#cfn-evs-environment-hostinfoforcreate-placementgroupid): {{String}}
```

## Properties
<a name="aws-properties-evs-environment-hostinfoforcreate-properties"></a>

`DedicatedHostId`  <a name="cfn-evs-environment-hostinfoforcreate-dedicatedhostid"></a>
The unique ID of the Amazon EC2 Dedicated Host.
*Required*: No
*Type*: String
*Pattern*: `^h-[a-f0-9]{8}([a-f0-9]{9})?$`
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: Updates are not supported.

`HostName`  <a name="cfn-evs-environment-hostinfoforcreate-hostname"></a>
The DNS hostname of the host. DNS hostnames for hosts must be unique across Amazon EVS environments and within VCF.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`InstanceType`  <a name="cfn-evs-environment-hostinfoforcreate-instancetype"></a>
The EC2 instance type that represents the host.
*Required*: Yes
*Type*: String
*Allowed values*: `i4i.metal | i7i.metal-24xl | i7i.metal-48xl`
*Update requires*: Updates are not supported.

`KeyName`  <a name="cfn-evs-environment-hostinfoforcreate-keyname"></a>
The name of the SSH key that is used to access the host.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: Updates are not supported.

`PlacementGroupId`  <a name="cfn-evs-environment-hostinfoforcreate-placementgroupid"></a>
The unique ID of the placement group where the host is placed.
*Required*: No
*Type*: String
*Pattern*: `^pg-[a-f0-9]{8}([a-f0-9]{9})?$`
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: Updates are not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
