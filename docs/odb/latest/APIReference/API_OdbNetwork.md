---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_OdbNetwork.html
---

# OdbNetwork
<a name="API_OdbNetwork"></a>

Information about an ODB network.

## Contents
<a name="API_OdbNetwork_Contents"></a>

 ** odbNetworkId **   <a name="odb-Type-OdbNetwork-odbNetworkId"></a>
The unique identifier of the ODB network.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** availabilityZone **   <a name="odb-Type-OdbNetwork-availabilityZone"></a>
The AWS Availability Zone (AZ) where the ODB network is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** availabilityZoneId **   <a name="odb-Type-OdbNetwork-availabilityZoneId"></a>
The AZ ID of the AZ where the ODB network is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** backupSubnetCidr **   <a name="odb-Type-OdbNetwork-backupSubnetCidr"></a>
The CIDR range of the backup subnet in the ODB network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** clientSubnetCidr **   <a name="odb-Type-OdbNetwork-clientSubnetCidr"></a>
The CIDR range of the client subnet in the ODB network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** createdAt **   <a name="odb-Type-OdbNetwork-createdAt"></a>
The date and time when the ODB network was created.
Type: Timestamp
Required: No

 ** customDomainName **   <a name="odb-Type-OdbNetwork-customDomainName"></a>
The domain name for the resources in the ODB network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** defaultDnsPrefix **   <a name="odb-Type-OdbNetwork-defaultDnsPrefix"></a>
The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** displayName **   <a name="odb-Type-OdbNetwork-displayName"></a>
The user-friendly name of the ODB network.
Type: String
Required: No

 ** ec2PlacementGroupIds **   <a name="odb-Type-OdbNetwork-ec2PlacementGroupIds"></a>
The list of EC2 Placement Group IDs associated with your ODB network.
Type: Array of strings
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** managedServices **   <a name="odb-Type-OdbNetwork-managedServices"></a>
The managed services configuration for the ODB network.
Type: [ManagedServices](API_ManagedServices.md) object
Required: No

 ** ociDnsForwardingConfigs **   <a name="odb-Type-OdbNetwork-ociDnsForwardingConfigs"></a>
The DNS resolver endpoint in OCI for forwarding DNS queries for the ociPrivateZone domain.
Type: Array of [OciDnsForwardingConfig](API_OciDnsForwardingConfig.md) objects
Required: No

 ** ociNetworkAnchorId **   <a name="odb-Type-OdbNetwork-ociNetworkAnchorId"></a>
The unique identifier of the OCI network anchor for the ODB network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ociNetworkAnchorUrl **   <a name="odb-Type-OdbNetwork-ociNetworkAnchorUrl"></a>
The URL of the OCI network anchor for the ODB network.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-OdbNetwork-ociResourceAnchorName"></a>
The name of the OCI resource anchor that's associated with the ODB network.
Type: String
Required: No

 ** ociVcnId **   <a name="odb-Type-OdbNetwork-ociVcnId"></a>
The Oracle Cloud ID (OCID) for the Virtual Cloud Network (VCN) that's associated with the ODB network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ociVcnUrl **   <a name="odb-Type-OdbNetwork-ociVcnUrl"></a>
The URL for the VCN that's associated with the ODB network.
Type: String
Required: No

 ** odbNetworkArn **   <a name="odb-Type-OdbNetwork-odbNetworkArn"></a>
The Amazon Resource Name (ARN) of the ODB network.
Type: String
Required: No

 ** peeredCidrs **   <a name="odb-Type-OdbNetwork-peeredCidrs"></a>
The list of CIDR ranges from the peered VPC that are allowed access to the ODB network.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** percentProgress **   <a name="odb-Type-OdbNetwork-percentProgress"></a>
The amount of progress made on the current operation on the ODB network, expressed as a percentage.
Type: Float
Required: No

 ** status **   <a name="odb-Type-OdbNetwork-status"></a>
The current status of the ODB network.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-OdbNetwork-statusReason"></a>
Additional information about the current status of the ODB network.
Type: String
Required: No

## See Also
<a name="API_OdbNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/OdbNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/OdbNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/OdbNetwork)
