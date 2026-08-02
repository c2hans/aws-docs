---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudVmCluster.html
---

# CloudVmCluster
<a name="API_CloudVmCluster"></a>

Information about a VM cluster.

## Contents
<a name="API_CloudVmCluster_Contents"></a>

 ** cloudVmClusterId **   <a name="odb-Type-CloudVmCluster-cloudVmClusterId"></a>
The unique identifier of the VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** cloudExadataInfrastructureArn **   <a name="odb-Type-CloudVmCluster-cloudExadataInfrastructureArn"></a>
The Amazon Resource Name (ARN) of the Exadata infrastructure that this VM cluster belongs to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** cloudExadataInfrastructureId **   <a name="odb-Type-CloudVmCluster-cloudExadataInfrastructureId"></a>
The unique identifier of the Exadata infrastructure that this VM cluster belongs to.
Type: String
Required: No

 ** cloudVmClusterArn **   <a name="odb-Type-CloudVmCluster-cloudVmClusterArn"></a>
The Amazon Resource Name (ARN) of the VM cluster.
Type: String
Required: No

 ** clusterName **   <a name="odb-Type-CloudVmCluster-clusterName"></a>
The name of the Grid Infrastructure (GI) cluster.
Type: String
Required: No

 ** computeModel **   <a name="odb-Type-CloudVmCluster-computeModel"></a>
The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** cpuCoreCount **   <a name="odb-Type-CloudVmCluster-cpuCoreCount"></a>
The number of CPU cores enabled on the VM cluster.
Type: Integer
Required: No

 ** createdAt **   <a name="odb-Type-CloudVmCluster-createdAt"></a>
The date and time when the VM cluster was created.
Type: Timestamp
Required: No

 ** dataCollectionOptions **   <a name="odb-Type-CloudVmCluster-dataCollectionOptions"></a>
The set of diagnostic collection options enabled for the VM cluster.
Type: [DataCollectionOptions](API_DataCollectionOptions.md) object
Required: No

 ** dataStorageSizeInTBs **   <a name="odb-Type-CloudVmCluster-dataStorageSizeInTBs"></a>
The size of the data disk group, in terabytes (TB), that's allocated for the VM cluster.
Type: Double
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-CloudVmCluster-dbNodeStorageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GB), that's allocated for the VM cluster.
Type: Integer
Required: No

 ** dbServers **   <a name="odb-Type-CloudVmCluster-dbServers"></a>
The list of database servers for the VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** diskRedundancy **   <a name="odb-Type-CloudVmCluster-diskRedundancy"></a>
The type of redundancy configured for the VM cluster. `NORMAL` is 2-way redundancy. `HIGH` is 3-way redundancy.
Type: String
Valid Values: `HIGH | NORMAL`
Required: No

 ** displayName **   <a name="odb-Type-CloudVmCluster-displayName"></a>
The user-friendly name for the VM cluster.
Type: String
Required: No

 ** domain **   <a name="odb-Type-CloudVmCluster-domain"></a>
The domain of the VM cluster.
Type: String
Required: No

 ** giVersion **   <a name="odb-Type-CloudVmCluster-giVersion"></a>
The software version of the Oracle Grid Infrastructure (GI) for the VM cluster.
Type: String
Required: No

 ** hostname **   <a name="odb-Type-CloudVmCluster-hostname"></a>
The host name for the VM cluster.
Type: String
Required: No

 ** iamRoles **   <a name="odb-Type-CloudVmCluster-iamRoles"></a>
The AWS Identity and Access Management (IAM) service roles associated with the VM cluster.
Type: Array of [IamRole](API_IamRole.md) objects
Required: No

 ** iormConfigCache **   <a name="odb-Type-CloudVmCluster-iormConfigCache"></a>
The ExadataIormConfig cache details for the VM cluster.
Type: [ExadataIormConfig](API_ExadataIormConfig.md) object
Required: No

 ** isLocalBackupEnabled **   <a name="odb-Type-CloudVmCluster-isLocalBackupEnabled"></a>
Indicates whether database backups to local Exadata storage is enabled for the VM cluster.
Type: Boolean
Required: No

 ** isSparseDiskgroupEnabled **   <a name="odb-Type-CloudVmCluster-isSparseDiskgroupEnabled"></a>
Indicates whether the VM cluster is configured with a sparse disk group.
Type: Boolean
Required: No

 ** lastUpdateHistoryEntryId **   <a name="odb-Type-CloudVmCluster-lastUpdateHistoryEntryId"></a>
The Oracle Cloud ID (OCID) of the last maintenance update history entry.
Type: String
Required: No

 ** licenseModel **   <a name="odb-Type-CloudVmCluster-licenseModel"></a>
The Oracle license model applied to the VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** listenerPort **   <a name="odb-Type-CloudVmCluster-listenerPort"></a>
The port number configured for the listener on the VM cluster.
Type: Integer
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-CloudVmCluster-memorySizeInGBs"></a>
The amount of memory, in gigabytes (GB), that's allocated for the VM cluster.
Type: Integer
Required: No

 ** nodeCount **   <a name="odb-Type-CloudVmCluster-nodeCount"></a>
The number of nodes in the VM cluster.
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-CloudVmCluster-ocid"></a>
The OCID of the VM cluster.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-CloudVmCluster-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the VM cluster.
Type: String
Required: No

 ** ociUrl **   <a name="odb-Type-CloudVmCluster-ociUrl"></a>
The HTTPS link to the VM cluster in OCI.
Type: String
Required: No

 ** odbNetworkArn **   <a name="odb-Type-CloudVmCluster-odbNetworkArn"></a>
The Amazon Resource Name (ARN) of the ODB network associated with this VM cluster.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** odbNetworkId **   <a name="odb-Type-CloudVmCluster-odbNetworkId"></a>
The unique identifier of the ODB network for the VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** percentProgress **   <a name="odb-Type-CloudVmCluster-percentProgress"></a>
The amount of progress made on the current operation on the VM cluster, expressed as a percentage.
Type: Float
Required: No

 ** scanDnsName **   <a name="odb-Type-CloudVmCluster-scanDnsName"></a>
The FQDN of the DNS record for the Single Client Access Name (SCAN) IP addresses that are associated with the VM cluster.
Type: String
Required: No

 ** scanDnsRecordId **   <a name="odb-Type-CloudVmCluster-scanDnsRecordId"></a>
The OCID of the DNS record for the SCAN IP addresses that are associated with the VM cluster.
Type: String
Required: No

 ** scanIpIds **   <a name="odb-Type-CloudVmCluster-scanIpIds"></a>
The OCID of the SCAN IP addresses that are associated with the VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** shape **   <a name="odb-Type-CloudVmCluster-shape"></a>
The hardware model name of the Exadata infrastructure that's running the VM cluster.
Type: String
Required: No

 ** sshPublicKeys **   <a name="odb-Type-CloudVmCluster-sshPublicKeys"></a>
The public key portion of one or more key pairs used for SSH access to the VM cluster.
Type: Array of strings
Required: No

 ** status **   <a name="odb-Type-CloudVmCluster-status"></a>
The current status of the VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-CloudVmCluster-statusReason"></a>
Additional information about the status of the VM cluster.
Type: String
Required: No

 ** storageSizeInGBs **   <a name="odb-Type-CloudVmCluster-storageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GB), that's allocated to the VM cluster.
Type: Integer
Required: No

 ** systemVersion **   <a name="odb-Type-CloudVmCluster-systemVersion"></a>
The operating system version of the image chosen for the VM cluster.
Type: String
Required: No

 ** timeZone **   <a name="odb-Type-CloudVmCluster-timeZone"></a>
The time zone of the VM cluster.
Type: String
Required: No

 ** vipIds **   <a name="odb-Type-CloudVmCluster-vipIds"></a>
The virtual IP (VIP) addresses that are associated with the VM cluster. Oracle's Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the VM cluster to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

## See Also
<a name="API_CloudVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CloudVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CloudVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CloudVmCluster)
