---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-initialvlaninfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment InitialVlanInfo
<a name="aws-properties-evs-environment-initialvlaninfo"></a>

An object that represents an initial VLAN subnet for the Amazon EVS environment. Amazon EVS creates initial VLAN subnets when you first create the environment. Amazon EVS creates the following 10 VLAN subnets: host management VLAN, vMotion VLAN, vSAN VLAN, VTEP VLAN, Edge VTEP VLAN, Management VM VLAN, HCX uplink VLAN, NSX uplink VLAN, expansion VLAN 1, expansion VLAN 2.

**Note**
For each Amazon EVS VLAN subnet, you must specify a non-overlapping CIDR block. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.

## Syntax
<a name="aws-properties-evs-environment-initialvlaninfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-initialvlaninfo-syntax.json"></a>

```
{
  "[Cidr](#cfn-evs-environment-initialvlaninfo-cidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-evs-environment-initialvlaninfo-syntax.yaml"></a>

```
  [Cidr](#cfn-evs-environment-initialvlaninfo-cidr): {{String}}
```

## Properties
<a name="aws-properties-evs-environment-initialvlaninfo-properties"></a>

`Cidr`  <a name="cfn-evs-environment-initialvlaninfo-cidr"></a>
 The CIDR block that you provide to create an Amazon EVS VLAN subnet. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.
*Required*: Yes
*Type*: String
*Pattern*: `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/(3[0-2]|[1-2][0-9]|[0-9])$`
*Update requires*: Updates are not supported.
