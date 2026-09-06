---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_Vlan.html
---

# Vlan
<a name="API_Vlan"></a>

The VLANs that Amazon EVS creates during environment creation.

## Contents
<a name="API_Vlan_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** availabilityZone **   <a name="evs-Type-Vlan-availabilityZone"></a>
The availability zone of the VLAN.
Type: String
Required: No

 ** cidr **   <a name="evs-Type-Vlan-cidr"></a>
The CIDR block of the VLAN. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.
Type: String
Pattern: `((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/(3[0-2]|[1-2][0-9]|[0-9])`
Required: No

 ** createdAt **   <a name="evs-Type-Vlan-createdAt"></a>
The date and time that the VLAN was created.
Type: Timestamp
Required: No

 ** eipAssociations **   <a name="evs-Type-Vlan-eipAssociations"></a>
An array of Elastic IP address associations.
Type: Array of [EipAssociation](API_EipAssociation.md) objects
Required: No

 ** functionName **   <a name="evs-Type-Vlan-functionName"></a>
The VMware VCF traffic type that is carried over the VLAN. For example, a VLAN with a `functionName` of `hcx` is being used to carry VMware HCX traffic.
Type: String
Required: No

 ** isPublic **   <a name="evs-Type-Vlan-isPublic"></a>
Determines if the VLAN that Amazon EVS provisions is public or private.
Type: Boolean
Required: No

 ** modifiedAt **   <a name="evs-Type-Vlan-modifiedAt"></a>
 The date and time that the VLAN was modified.
Type: Timestamp
Required: No

 ** networkAclId **   <a name="evs-Type-Vlan-networkAclId"></a>
A unique ID for a network access control list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 21.
Pattern: `acl-[a-zA-Z0-9_-]+`
Required: No

 ** stateDetails **   <a name="evs-Type-Vlan-stateDetails"></a>
The state details of the VLAN.
Type: String
Required: No

 ** subnetId **   <a name="evs-Type-Vlan-subnetId"></a>
 The unique ID of the VLAN subnet.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-[a-f0-9]{8}([a-f0-9]{9})?`
Required: No

 ** vlanId **   <a name="evs-Type-Vlan-vlanId"></a>
The unique ID of the VLAN.
Type: Integer
Required: No

 ** vlanState **   <a name="evs-Type-Vlan-vlanState"></a>
 The state of the VLAN.
Type: String
Valid Values: `CREATING | CREATED | DELETING | DELETED | CREATE_FAILED`
Required: No

## See Also
<a name="API_Vlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/Vlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/Vlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/Vlan)
