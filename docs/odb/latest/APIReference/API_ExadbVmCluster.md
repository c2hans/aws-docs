---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ExadbVmCluster.html
---

# ExadbVmCluster
<a name="API_ExadbVmCluster"></a>

Information about an Exascale VM cluster.

## Contents
<a name="API_ExadbVmCluster_Contents"></a>

 ** exadbVmClusterId **   <a name="odb-Type-ExadbVmCluster-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** clusterName **   <a name="odb-Type-ExadbVmCluster-clusterName"></a>
The name of the Grid Infrastructure (GI) cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** createdAt **   <a name="odb-Type-ExadbVmCluster-createdAt"></a>
The date and time when the Exascale VM cluster was created.
Type: Timestamp
Required: No

 ** dataCollectionOptions **   <a name="odb-Type-ExadbVmCluster-dataCollectionOptions"></a>
The set of diagnostic collection options enabled for the Exascale VM cluster.
Type: [DataCollectionOptions](API_DataCollectionOptions.md) object
Required: No

 ** displayName **   <a name="odb-Type-ExadbVmCluster-displayName"></a>
The user-friendly name for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** domain **   <a name="odb-Type-ExadbVmCluster-domain"></a>
The domain of the Exascale VM cluster.
Type: String
Required: No

 ** enabledEcpuCount **   <a name="odb-Type-ExadbVmCluster-enabledEcpuCount"></a>
The number of elastic compute processing units (ECPUs) enabled on the Exascale VM cluster.
Type: Integer
Required: No

 ** exadbVmClusterArn **   <a name="odb-Type-ExadbVmCluster-exadbVmClusterArn"></a>
The Amazon Resource Name (ARN) of the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** exascaleDbStorageVaultArn **   <a name="odb-Type-ExadbVmCluster-exascaleDbStorageVaultArn"></a>
The Amazon Resource Name (ARN) of the Exascale storage vault associated with this Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** exascaleDbStorageVaultId **   <a name="odb-Type-ExadbVmCluster-exascaleDbStorageVaultId"></a>
The unique identifier of the Exascale storage vault associated with this Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** giVersion **   <a name="odb-Type-ExadbVmCluster-giVersion"></a>
The software version of the Oracle Grid Infrastructure (GI) for the Exascale VM cluster.
Type: String
Required: No

 ** gridImageId **   <a name="odb-Type-ExadbVmCluster-gridImageId"></a>
The Grid Infrastructure software image ID for the Exascale VM cluster.
Type: String
Required: No

 ** gridImageType **   <a name="odb-Type-ExadbVmCluster-gridImageType"></a>
The type of Grid Infrastructure image for the Exascale VM cluster.
Type: String
Valid Values: `RELEASE_UPDATE | CUSTOM_IMAGE`
Required: No

 ** hostname **   <a name="odb-Type-ExadbVmCluster-hostname"></a>
The host name for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*[a-zA-Z0-9]`
Required: No

 ** iamRoles **   <a name="odb-Type-ExadbVmCluster-iamRoles"></a>
The AWS Identity and Access Management (IAM) service roles associated with the Exascale VM cluster.
Type: Array of [IamRole](API_IamRole.md) objects
Required: No

 ** iormConfigCache **   <a name="odb-Type-ExadbVmCluster-iormConfigCache"></a>
The I/O Resource Management (IORM) configuration cache details for the Exascale VM cluster.
Type: [ExadataIormConfig](API_ExadataIormConfig.md) object
Required: No

 ** lastUpdateHistoryEntryId **   <a name="odb-Type-ExadbVmCluster-lastUpdateHistoryEntryId"></a>
The Oracle Cloud ID (OCID) of the last maintenance update history entry.
Type: String
Required: No

 ** licenseModel **   <a name="odb-Type-ExadbVmCluster-licenseModel"></a>
The Oracle license model applied to the Exascale VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** listenerPort **   <a name="odb-Type-ExadbVmCluster-listenerPort"></a>
The port number configured for the listener on the Exascale VM cluster.
Type: Integer
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-ExadbVmCluster-memorySizeInGBs"></a>
The amount of memory, in gigabytes (GB), that's allocated for the Exascale VM cluster.
Type: Integer
Required: No

 ** nodeCount **   <a name="odb-Type-ExadbVmCluster-nodeCount"></a>
The number of nodes in the Exascale VM cluster.
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-ExadbVmCluster-ocid"></a>
The OCID of the Exascale VM cluster.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-ExadbVmCluster-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the Exascale VM cluster.
Type: String
Required: No

 ** ociUrl **   <a name="odb-Type-ExadbVmCluster-ociUrl"></a>
The HTTPS link to the Exascale VM cluster in Oracle Cloud Infrastructure (OCI).
Type: String
Required: No

 ** odbNetworkArn **   <a name="odb-Type-ExadbVmCluster-odbNetworkArn"></a>
The Amazon Resource Name (ARN) of the ODB network associated with this Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** odbNetworkId **   <a name="odb-Type-ExadbVmCluster-odbNetworkId"></a>
The unique identifier of the ODB network for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** percentProgress **   <a name="odb-Type-ExadbVmCluster-percentProgress"></a>
The amount of progress made on the current operation on the Exascale VM cluster, expressed as a percentage.
Type: Float
Required: No

 ** scanDnsName **   <a name="odb-Type-ExadbVmCluster-scanDnsName"></a>
The fully qualified domain name (FQDN) of the DNS record for the Single Client Access Name (SCAN) IP addresses that are associated with the Exascale VM cluster.
Type: String
Required: No

 ** scanDnsRecordId **   <a name="odb-Type-ExadbVmCluster-scanDnsRecordId"></a>
The OCID of the DNS record for the SCAN IP addresses that are associated with the Exascale VM cluster.
Type: String
Required: No

 ** scanIpIds **   <a name="odb-Type-ExadbVmCluster-scanIpIds"></a>
The OCID of the SCAN IP addresses that are associated with the Exascale VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** scanListenerPortTcp **   <a name="odb-Type-ExadbVmCluster-scanListenerPortTcp"></a>
The port number for TCP connections to the single client access name (SCAN) listener for the Exascale VM cluster.
Type: Integer
Required: No

 ** scanListenerPortTcpSsl **   <a name="odb-Type-ExadbVmCluster-scanListenerPortTcpSsl"></a>
The port number for TCP connections with SSL to the single client access name (SCAN) listener for the Exascale VM cluster.
Type: Integer
Required: No

 ** shape **   <a name="odb-Type-ExadbVmCluster-shape"></a>
The hardware model name of the Exadata infrastructure that's running the Exascale VM cluster.
Type: String
Required: No

 ** shapeAttribute **   <a name="odb-Type-ExadbVmCluster-shapeAttribute"></a>
The shape attribute for the Exascale VM cluster.
Type: String
Valid Values: `SMART_STORAGE | BLOCK_STORAGE`
Required: No

 ** snapshotFileSystemStorage **   <a name="odb-Type-ExadbVmCluster-snapshotFileSystemStorage"></a>
The snapshot file system storage details for the Exascale VM cluster.
Type: [ExadbVmClusterStorageDetails](API_ExadbVmClusterStorageDetails.md) object
Required: No

 ** sshPublicKeys **   <a name="odb-Type-ExadbVmCluster-sshPublicKeys"></a>
The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** status **   <a name="odb-Type-ExadbVmCluster-status"></a>
The current status of the Exascale VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-ExadbVmCluster-statusReason"></a>
Additional information about the status of the Exascale VM cluster.
Type: String
Required: No

 ** systemVersion **   <a name="odb-Type-ExadbVmCluster-systemVersion"></a>
The operating system version of the image chosen for the Exascale VM cluster.
Type: String
Required: No

 ** timeZone **   <a name="odb-Type-ExadbVmCluster-timeZone"></a>
The time zone of the Exascale VM cluster.
Type: String
Required: No

 ** totalEcpuCount **   <a name="odb-Type-ExadbVmCluster-totalEcpuCount"></a>
The total number of ECPUs for the Exascale VM cluster.
Type: Integer
Required: No

 ** totalFileSystemStorage **   <a name="odb-Type-ExadbVmCluster-totalFileSystemStorage"></a>
The total file system storage details for the Exascale VM cluster.
Type: [ExadbVmClusterStorageDetails](API_ExadbVmClusterStorageDetails.md) object
Required: No

 ** vipIds **   <a name="odb-Type-ExadbVmCluster-vipIds"></a>
The virtual IP (VIP) addresses associated with the Exascale VM cluster. One VIP address is assigned per node to support failover. If a node fails, its VIP is reassigned to another active node in the cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** vmFileSystemStorage **   <a name="odb-Type-ExadbVmCluster-vmFileSystemStorage"></a>
The VM file system storage details for the Exascale VM cluster.
Type: [ExadbVmClusterStorageDetails](API_ExadbVmClusterStorageDetails.md) object
Required: No

## See Also
<a name="API_ExadbVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ExadbVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ExadbVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ExadbVmCluster)
