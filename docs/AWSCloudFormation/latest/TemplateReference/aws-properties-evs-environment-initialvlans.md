---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-initialvlans.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment InitialVlans
<a name="aws-properties-evs-environment-initialvlans"></a>

The initial VLAN subnets for the environment. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.

## Syntax
<a name="aws-properties-evs-environment-initialvlans-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-initialvlans-syntax.json"></a>

```
{
  "[EdgeVTep](#cfn-evs-environment-initialvlans-edgevtep)" : {{InitialVlanInfo}},
  "[ExpansionVlan1](#cfn-evs-environment-initialvlans-expansionvlan1)" : {{InitialVlanInfo}},
  "[ExpansionVlan2](#cfn-evs-environment-initialvlans-expansionvlan2)" : {{InitialVlanInfo}},
  "[Hcx](#cfn-evs-environment-initialvlans-hcx)" : {{InitialVlanInfo}},
  "[HcxNetworkAclId](#cfn-evs-environment-initialvlans-hcxnetworkaclid)" : {{String}},
  "[IsHcxPublic](#cfn-evs-environment-initialvlans-ishcxpublic)" : {{Boolean}},
  "[NsxUpLink](#cfn-evs-environment-initialvlans-nsxuplink)" : {{InitialVlanInfo}},
  "[VmkManagement](#cfn-evs-environment-initialvlans-vmkmanagement)" : {{InitialVlanInfo}},
  "[VmManagement](#cfn-evs-environment-initialvlans-vmmanagement)" : {{InitialVlanInfo}},
  "[VMotion](#cfn-evs-environment-initialvlans-vmotion)" : {{InitialVlanInfo}},
  "[VSan](#cfn-evs-environment-initialvlans-vsan)" : {{InitialVlanInfo}},
  "[VTep](#cfn-evs-environment-initialvlans-vtep)" : {{InitialVlanInfo}}
}
```

### YAML
<a name="aws-properties-evs-environment-initialvlans-syntax.yaml"></a>

```
  [EdgeVTep](#cfn-evs-environment-initialvlans-edgevtep): {{
    InitialVlanInfo}}
  [ExpansionVlan1](#cfn-evs-environment-initialvlans-expansionvlan1): {{
    InitialVlanInfo}}
  [ExpansionVlan2](#cfn-evs-environment-initialvlans-expansionvlan2): {{
    InitialVlanInfo}}
  [Hcx](#cfn-evs-environment-initialvlans-hcx): {{
    InitialVlanInfo}}
  [HcxNetworkAclId](#cfn-evs-environment-initialvlans-hcxnetworkaclid): {{String}}
  [IsHcxPublic](#cfn-evs-environment-initialvlans-ishcxpublic): {{Boolean}}
  [NsxUpLink](#cfn-evs-environment-initialvlans-nsxuplink): {{
    InitialVlanInfo}}
  [VmkManagement](#cfn-evs-environment-initialvlans-vmkmanagement): {{
    InitialVlanInfo}}
  [VmManagement](#cfn-evs-environment-initialvlans-vmmanagement): {{
    InitialVlanInfo}}
  [VMotion](#cfn-evs-environment-initialvlans-vmotion): {{
    InitialVlanInfo}}
  [VSan](#cfn-evs-environment-initialvlans-vsan): {{
    InitialVlanInfo}}
  [VTep](#cfn-evs-environment-initialvlans-vtep): {{
    InitialVlanInfo}}
```

## Properties
<a name="aws-properties-evs-environment-initialvlans-properties"></a>

`EdgeVTep`  <a name="cfn-evs-environment-initialvlans-edgevtep"></a>
The edge VTEP VLAN subnet. This VLAN subnet manages traffic flowing between the internal network and external networks, including internet access and other site connections.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`ExpansionVlan1`  <a name="cfn-evs-environment-initialvlans-expansionvlan1"></a>
An additional VLAN subnet that can be used to extend VCF capabilities once configured. For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`ExpansionVlan2`  <a name="cfn-evs-environment-initialvlans-expansionvlan2"></a>
An additional VLAN subnet that can be used to extend VCF capabilities once configured. For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`Hcx`  <a name="cfn-evs-environment-initialvlans-hcx"></a>
The HCX VLAN subnet. This VLAN subnet allows the HCX Interconnnect (IX) and HCX Network Extension (NE) to reach their peers and enable HCX Service Mesh creation.
If you plan to use a public HCX VLAN subnet, the following requirements must be met:
+ Must have a /28 netmask and be allocated from the IPAM public pool. Required for HCX internet access configuration.
+ The HCX public VLAN CIDR block must be added to the VPC as a secondary CIDR block.
+ Must have at least two Elastic IP addresses to be allocated from the public IPAM pool for HCX components.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`HcxNetworkAclId`  <a name="cfn-evs-environment-initialvlans-hcxnetworkaclid"></a>
A unique ID for a network access control list that the HCX VLAN uses. Required when `isHcxPublic` is set to `true`.
*Required*: No
*Type*: String
*Pattern*: `^acl-[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsHcxPublic`  <a name="cfn-evs-environment-initialvlans-ishcxpublic"></a>
Determines if the HCX VLAN that Amazon EVS provisions is public or private.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NsxUpLink`  <a name="cfn-evs-environment-initialvlans-nsxuplink"></a>
 The NSX uplink VLAN subnet. This VLAN subnet allows connectivity to the NSX overlay network.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`VmkManagement`  <a name="cfn-evs-environment-initialvlans-vmkmanagement"></a>
 The host VMkernel management VLAN subnet. This VLAN subnet carries traffic for managing ESX hosts and communicating with VMware vCenter Server.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`VmManagement`  <a name="cfn-evs-environment-initialvlans-vmmanagement"></a>
The VM management VLAN subnet. This VLAN subnet carries traffic for vSphere virtual machines.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`VMotion`  <a name="cfn-evs-environment-initialvlans-vmotion"></a>
 The vMotion VLAN subnet. This VLAN subnet carries traffic for vSphere vMotion.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`VSan`  <a name="cfn-evs-environment-initialvlans-vsan"></a>
 The vSAN VLAN subnet. This VLAN subnet carries the communication between ESX hosts to implement a vSAN shared storage pool.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

`VTep`  <a name="cfn-evs-environment-initialvlans-vtep"></a>
 The VTEP VLAN subnet. This VLAN subnet handles internal network traffic between virtual machines within a VCF instance.
*Required*: Yes
*Type*: [InitialVlanInfo](aws-properties-evs-environment-initialvlaninfo.md)
*Update requires*: Updates are not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
