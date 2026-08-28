---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_InitialVlans.html
---

# InitialVlans
<a name="API_InitialVlans"></a>

The initial VLAN subnets for the environment. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.

## Contents
<a name="API_InitialVlans_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** edgeVTep **   <a name="evs-Type-InitialVlans-edgeVTep"></a>
The edge VTEP VLAN subnet. This VLAN subnet manages traffic flowing between the internal network and external networks, including internet access and other site connections.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** expansionVlan1 **   <a name="evs-Type-InitialVlans-expansionVlan1"></a>
An additional VLAN subnet that can be used to extend VCF capabilities once configured. For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** expansionVlan2 **   <a name="evs-Type-InitialVlans-expansionVlan2"></a>
An additional VLAN subnet that can be used to extend VCF capabilities once configured. For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** hcx **   <a name="evs-Type-InitialVlans-hcx"></a>
The HCX VLAN subnet. This VLAN subnet allows the HCX Interconnnect (IX) and HCX Network Extension (NE) to reach their peers and enable HCX Service Mesh creation.
If you plan to use a public HCX VLAN subnet, the following requirements must be met:
+ Must have a /28 netmask and be allocated from the IPAM public pool. Required for HCX internet access configuration.
+ The HCX public VLAN CIDR block must be added to the VPC as a secondary CIDR block.
+ Must have at least two Elastic IP addresses to be allocated from the public IPAM pool for HCX components.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** nsxUplink **   <a name="evs-Type-InitialVlans-nsxUplink"></a>
 The NSX uplink VLAN subnet. This VLAN subnet allows connectivity to the NSX overlay network.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** vmkManagement **   <a name="evs-Type-InitialVlans-vmkManagement"></a>
 The host VMkernel management VLAN subnet. This VLAN subnet carries traffic for managing ESX hosts and communicating with VMware vCenter Server.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** vmManagement **   <a name="evs-Type-InitialVlans-vmManagement"></a>
The VM management VLAN subnet. This VLAN subnet carries traffic for vSphere virtual machines.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** vMotion **   <a name="evs-Type-InitialVlans-vMotion"></a>
 The vMotion VLAN subnet. This VLAN subnet carries traffic for vSphere vMotion.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** vSan **   <a name="evs-Type-InitialVlans-vSan"></a>
 The vSAN VLAN subnet. This VLAN subnet carries the communication between ESX hosts to implement a vSAN shared storage pool.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** vTep **   <a name="evs-Type-InitialVlans-vTep"></a>
 The VTEP VLAN subnet. This VLAN subnet handles internal network traffic between virtual machines within a VCF instance.
Type: [InitialVlanInfo](API_InitialVlanInfo.md) object
Required: Yes

 ** hcxNetworkAclId **   <a name="evs-Type-InitialVlans-hcxNetworkAclId"></a>
A unique ID for a network access control list that the HCX VLAN uses. Required when `isHcxPublic` is set to `true`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 21.
Pattern: `acl-[a-zA-Z0-9_-]+`
Required: No

 ** isHcxPublic **   <a name="evs-Type-InitialVlans-isHcxPublic"></a>
Determines if the HCX VLAN that Amazon EVS provisions is public or private.
Type: Boolean
Required: No

## See Also
<a name="API_InitialVlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/InitialVlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/InitialVlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/InitialVlans)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
