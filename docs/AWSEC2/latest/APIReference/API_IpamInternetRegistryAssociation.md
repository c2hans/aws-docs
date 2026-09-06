---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamInternetRegistryAssociation.html
---

# IpamInternetRegistryAssociation
<a name="API_IpamInternetRegistryAssociation"></a>

Contains information about an association between an IPAM and a Regional Internet Registry (RIR) for delegated RPKI management.

## Contents
<a name="API_IpamInternetRegistryAssociation_Contents"></a>

 ** childRequestXml **
The XML content for the child request to be submitted to the internet registry to complete the BPKI setup.
Type: String
Required: No

 ** description **
The description of the internet registry association.
Type: String
Required: No

 ** ipamId **
The ID of the associated IPAM.
Type: String
Required: No

 ** ipamInternetRegistryAssociationArn **
The Amazon Resource Name (ARN) of the internet registry association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamInternetRegistryAssociationId **
The ID of the internet registry association.
Type: String
Required: No

 ** ipamRegion **
The AWS Region of the IPAM.
Type: String
Required: No

 ** organizationHandle **
The organization handle at the internet registry.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the internet registry association.
Type: String
Required: No

 ** rir **
The Regional Internet Registry. Possible values:
+  `ripe` - RIPE NCC (Europe, the Middle East, and Central Asia).
+  `apnic` - APNIC (Asia Pacific).
+  `arin` - ARIN (North America).
+  `lacnic` - LACNIC (Latin America and the Caribbean).
Type: String
Valid Values: `ripe | apnic | arin | lacnic`
Required: No

 ** state **
The state of the internet registry association. Valid values: `pending-activation` \| `pending-enable` \| `create-in-progress` \| `create-failed` \| `enable-in-progress` \| `enable-complete` \| `enable-failed` \| `delete-in-progress` \| `delete-complete` \| `delete-failed`.
Type: String
Valid Values: `pending-enable | create-in-progress | create-failed | enable-in-progress | enable-complete | enable-failed | delete-in-progress | delete-complete | delete-failed`
Required: No

 ** TagSet.N **
The tags assigned to the internet registry association.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_IpamInternetRegistryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamInternetRegistryAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamInternetRegistryAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamInternetRegistryAssociation)
