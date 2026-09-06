---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudVmClusterSummary.html
---

# CloudVmClusterSummary
<a name="API_CloudVmClusterSummary"></a>

Information about a VM cluster.

## Contents
<a name="API_CloudVmClusterSummary_Contents"></a>

 ** cloudVmClusterId **   <a name="odb-Type-CloudVmClusterSummary-cloudVmClusterId"></a>
The unique identifier of the VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** cloudExadataInfrastructureArn **   <a name="odb-Type-CloudVmClusterSummary-cloudExadataInfrastructureArn"></a>
The Amazon Resource Name (ARN) of the Exadata infrastructure that this VM cluster belongs to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** cloudExadataInfrastructureId **   <a name="odb-Type-CloudVmClusterSummary-cloudExadataInfrastructureId"></a>
The unique identifier of the Exadata infrastructure that this VM cluster belongs to.
Type: String
Required: No

 ** cloudVmClusterArn **   <a name="odb-Type-CloudVmClusterSummary-cloudVmClusterArn"></a>
The Amazon Resource Name (ARN) of the VM cluster.
Type: String
Required: No

 ** clusterName **   <a name="odb-Type-CloudVmClusterSummary-clusterName"></a>
The name of the Grid Infrastructure (GI) cluster.
Type: String
Required: No

 ** computeModel **   <a name="odb-Type-CloudVmClusterSummary-computeModel"></a>
The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** cpuCoreCount **   <a name="odb-Type-CloudVmClusterSummary-cpuCoreCount"></a>
The number of CPU cores enabled on the VM cluster.
Type: Integer
Required: No

 ** createdAt **   <a name="odb-Type-CloudVmClusterSummary-createdAt"></a>
The date and time when the VM cluster was created.
Type: Timestamp
Required: No

 ** dataCollectionOptions **   <a name="odb-Type-CloudVmClusterSummary-dataCollectionOptions"></a>
Information about the data collection options enabled for a VM cluster.
Type: [DataCollectionOptions](API_DataCollectionOptions.md) object
Required: No

 ** dataStorageSizeInTBs **   <a name="odb-Type-CloudVmClusterSummary-dataStorageSizeInTBs"></a>
The size of the data disk group, in terabytes (TB), that's allocated for the VM cluster.
Type: Double
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-CloudVmClusterSummary-dbNodeStorageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GB), that's allocated for the VM cluster.
Type: Integer
Required: No

 ** dbServers **   <a name="odb-Type-CloudVmClusterSummary-dbServers"></a>
The list of database servers for the VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** diskRedundancy **   <a name="odb-Type-CloudVmClusterSummary-diskRedundancy"></a>
The type of redundancy configured for the VM cluster. `NORMAL` is 2-way redundancy. `HIGH` is 3-way redundancy.
Type: String
Valid Values: `HIGH | NORMAL`
Required: No

 ** displayName **   <a name="odb-Type-CloudVmClusterSummary-displayName"></a>
The user-friendly name for the VM cluster.
Type: String
Required: No

 ** domain **   <a name="odb-Type-CloudVmClusterSummary-domain"></a>
The domain of the VM cluster.
Type: String
Required: No

 ** giVersion **   <a name="odb-Type-CloudVmClusterSummary-giVersion"></a>
The software version of the Oracle Grid Infrastructure (GI) for the VM cluster.
Type: String
Required: No

 ** hostname **   <a name="odb-Type-CloudVmClusterSummary-hostname"></a>
The host name for the VM cluster.
Type: String
Required: No

 ** iamRoles **   <a name="odb-Type-CloudVmClusterSummary-iamRoles"></a>
The AWS Identity and Access Management (IAM) service roles associated with the VM cluster in the summary information.
Type: Array of [IamRole](API_IamRole.md) objects
Required: No

 ** iormConfigCache **   <a name="odb-Type-CloudVmClusterSummary-iormConfigCache"></a>
The IORM settings of the Exadata DB system.
Type: [ExadataIormConfig](API_ExadataIormConfig.md) object
Required: No

 ** isLocalBackupEnabled **   <a name="odb-Type-CloudVmClusterSummary-isLocalBackupEnabled"></a>
Indicates whether database backups to local Exadata storage is enabled for the VM cluster.
Type: Boolean
Required: No

 ** isSparseDiskgroupEnabled **   <a name="odb-Type-CloudVmClusterSummary-isSparseDiskgroupEnabled"></a>
Indicates whether the VM cluster is configured with a sparse disk group.
Type: Boolean
Required: No

 ** lastUpdateHistoryEntryId **   <a name="odb-Type-CloudVmClusterSummary-lastUpdateHistoryEntryId"></a>
The Oracle Cloud ID (OCID) of the last maintenance update history entry.
Type: String
Required: No

 ** licenseModel **   <a name="odb-Type-CloudVmClusterSummary-licenseModel"></a>
The Oracle license model applied to the VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** listenerPort **   <a name="odb-Type-CloudVmClusterSummary-listenerPort"></a>
The port number configured for the listener on the VM cluster.
Type: Integer
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-CloudVmClusterSummary-memorySizeInGBs"></a>
The amount of memory, in gigabytes (GB), that's allocated for the VM cluster.
Type: Integer
Required: No

 ** nodeCount **   <a name="odb-Type-CloudVmClusterSummary-nodeCount"></a>
The number of nodes in the VM cluster.
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-CloudVmClusterSummary-ocid"></a>
The OCID of the VM cluster.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-CloudVmClusterSummary-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the VM cluster.
Type: String
Required: No

 ** ociUrl **   <a name="odb-Type-CloudVmClusterSummary-ociUrl"></a>
The HTTPS link to the VM cluster in OCI.
Type: String
Required: No

 ** odbNetworkArn **   <a name="odb-Type-CloudVmClusterSummary-odbNetworkArn"></a>
The Amazon Resource Name (ARN) of the ODB network associated with this VM cluster.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** odbNetworkId **   <a name="odb-Type-CloudVmClusterSummary-odbNetworkId"></a>
The unique identifier of the ODB network for the VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** percentProgress **   <a name="odb-Type-CloudVmClusterSummary-percentProgress"></a>
The amount of progress made on the current operation on the VM cluster, expressed as a percentage.
Type: Float
Required: No

 ** scanDnsName **   <a name="odb-Type-CloudVmClusterSummary-scanDnsName"></a>
The fully qualified domain name (FQDN) of the DNS record for the Single Client Access Name (SCAN) IP addresses that are associated with the VM cluster.
Type: String
Required: No

 ** scanDnsRecordId **   <a name="odb-Type-CloudVmClusterSummary-scanDnsRecordId"></a>
The OCID of the DNS record for the SCAN IP addresses that are associated with the VM cluster.
Type: String
Required: No

 ** scanIpIds **   <a name="odb-Type-CloudVmClusterSummary-scanIpIds"></a>
The OCID of the SCAN IP addresses that are associated with the VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** shape **   <a name="odb-Type-CloudVmClusterSummary-shape"></a>
The hardware model name of the Exadata infrastructure that's running the VM cluster.
Type: String
Required: No

 ** sshPublicKeys **   <a name="odb-Type-CloudVmClusterSummary-sshPublicKeys"></a>
The public key portion of one or more key pairs used for SSH access to the VM cluster.
Type: Array of strings
Required: No

 ** status **   <a name="odb-Type-CloudVmClusterSummary-status"></a>
The current status of the VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-CloudVmClusterSummary-statusReason"></a>
Additional information about the status of the VM cluster.
Type: String
Required: No

 ** storageSizeInGBs **   <a name="odb-Type-CloudVmClusterSummary-storageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GB), that's allocated to the VM cluster.
Type: Integer
Required: No

 ** systemVersion **   <a name="odb-Type-CloudVmClusterSummary-systemVersion"></a>
The operating system version of the image chosen for the VM cluster.
Type: String
Required: No

 ** timeZone **   <a name="odb-Type-CloudVmClusterSummary-timeZone"></a>
The time zone of the VM cluster.
Type: String
Required: No

 ** vipIds **   <a name="odb-Type-CloudVmClusterSummary-vipIds"></a>
The virtual IP (VIP) addresses that are associated with the VM cluster. Oracle's Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the VM cluster to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

## See Also
<a name="API_CloudVmClusterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CloudVmClusterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CloudVmClusterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CloudVmClusterSummary)
