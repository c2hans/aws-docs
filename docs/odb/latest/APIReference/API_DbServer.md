---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DbServer.html
---

# DbServer
<a name="API_DbServer"></a>

Information about a database server.

## Contents
<a name="API_DbServer_Contents"></a>

 ** autonomousVirtualMachineIds **   <a name="odb-Type-DbServer-autonomousVirtualMachineIds"></a>
The list of unique identifiers for the Autonomous VMs associated with this database server.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** autonomousVmClusterIds **   <a name="odb-Type-DbServer-autonomousVmClusterIds"></a>
The list of identifiers for the Autonomous VM clusters associated with this database server.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** computeModel **   <a name="odb-Type-DbServer-computeModel"></a>
The compute model of the database server (ECPU or OCPU).
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** cpuCoreCount **   <a name="odb-Type-DbServer-cpuCoreCount"></a>
The number of CPU cores enabled on the database server.
Type: Integer
Required: No

 ** createdAt **   <a name="odb-Type-DbServer-createdAt"></a>
The date and time when the database server was created.
Type: Timestamp
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-DbServer-dbNodeStorageSizeInGBs"></a>
The allocated local node storage in GBs on the database server.
Type: Integer
Required: No

 ** dbServerId **   <a name="odb-Type-DbServer-dbServerId"></a>
The unique identifier for the database server.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** dbServerPatchingDetails **   <a name="odb-Type-DbServer-dbServerPatchingDetails"></a>
The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.
Type: [DbServerPatchingDetails](API_DbServerPatchingDetails.md) object
Required: No

 ** displayName **   <a name="odb-Type-DbServer-displayName"></a>
The user-friendly name of the database server.
Type: String
Required: No

 ** exadataInfrastructureId **   <a name="odb-Type-DbServer-exadataInfrastructureId"></a>
The ID of the Exadata infrastructure the database server belongs to.
Type: String
Required: No

 ** maxCpuCount **   <a name="odb-Type-DbServer-maxCpuCount"></a>
The total number of CPU cores available.
Type: Integer
Required: No

 ** maxDbNodeStorageInGBs **   <a name="odb-Type-DbServer-maxDbNodeStorageInGBs"></a>
The total local node storage available in GBs.
Type: Integer
Required: No

 ** maxMemoryInGBs **   <a name="odb-Type-DbServer-maxMemoryInGBs"></a>
The total memory available in GBs.
Type: Integer
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-DbServer-memorySizeInGBs"></a>
The allocated memory in GBs on the database server.
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-DbServer-ocid"></a>
The OCID of the database server.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-DbServer-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the database server.
Type: String
Required: No

 ** shape **   <a name="odb-Type-DbServer-shape"></a>
The shape of the database server. The shape determines the amount of CPU, storage, and memory resources available.
Type: String
Required: No

 ** status **   <a name="odb-Type-DbServer-status"></a>
The current status of the database server.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-DbServer-statusReason"></a>
Additional information about the current status of the database server.
Type: String
Required: No

 ** vmClusterIds **   <a name="odb-Type-DbServer-vmClusterIds"></a>
The OCID of the VM clusters that are associated with the database server.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

## See Also
<a name="API_DbServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DbServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DbServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DbServer)
