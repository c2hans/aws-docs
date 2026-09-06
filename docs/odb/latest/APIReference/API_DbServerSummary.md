---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DbServerSummary.html
---

# DbServerSummary
<a name="API_DbServerSummary"></a>

Information about a database server.

## Contents
<a name="API_DbServerSummary_Contents"></a>

 ** autonomousVirtualMachineIds **   <a name="odb-Type-DbServerSummary-autonomousVirtualMachineIds"></a>
A list of unique identifiers for the Autonomous VMs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** autonomousVmClusterIds **   <a name="odb-Type-DbServerSummary-autonomousVmClusterIds"></a>
A list of identifiers for the Autonomous VM clusters.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** computeModel **   <a name="odb-Type-DbServerSummary-computeModel"></a>
The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** cpuCoreCount **   <a name="odb-Type-DbServerSummary-cpuCoreCount"></a>
The number of CPU cores enabled on the database server.
Type: Integer
Required: No

 ** createdAt **   <a name="odb-Type-DbServerSummary-createdAt"></a>
The date and time when the database server was created.
Type: Timestamp
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-DbServerSummary-dbNodeStorageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GB), that's allocated on the database server.
Type: Integer
Required: No

 ** dbServerId **   <a name="odb-Type-DbServerSummary-dbServerId"></a>
The unique identifier of the database server.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** dbServerPatchingDetails **   <a name="odb-Type-DbServerSummary-dbServerPatchingDetails"></a>
The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.
Type: [DbServerPatchingDetails](API_DbServerPatchingDetails.md) object
Required: No

 ** displayName **   <a name="odb-Type-DbServerSummary-displayName"></a>
The user-friendly name of the database server. The name doesn't need to be unique.
Type: String
Required: No

 ** exadataInfrastructureId **   <a name="odb-Type-DbServerSummary-exadataInfrastructureId"></a>
The ID of the Exadata infrastructure that hosts the database server.
Type: String
Required: No

 ** maxCpuCount **   <a name="odb-Type-DbServerSummary-maxCpuCount"></a>
The total number of CPU cores available on the database server.
Type: Integer
Required: No

 ** maxDbNodeStorageInGBs **   <a name="odb-Type-DbServerSummary-maxDbNodeStorageInGBs"></a>
The total amount of local node storage, in gigabytes (GB), that's available on the database server.
Type: Integer
Required: No

 ** maxMemoryInGBs **   <a name="odb-Type-DbServerSummary-maxMemoryInGBs"></a>
The total amount of memory, in gigabytes (GB), that's available on the database server.
Type: Integer
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-DbServerSummary-memorySizeInGBs"></a>
The amount of memory, in gigabytes (GB), that's allocated on the database server.
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-DbServerSummary-ocid"></a>
The OCID of the database server.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-DbServerSummary-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the database server.
Type: String
Required: No

 ** shape **   <a name="odb-Type-DbServerSummary-shape"></a>
The hardware system model of the Exadata infrastructure that the database server is hosted on. The shape determines the amount of CPU, storage, and memory resources available.
Type: String
Required: No

 ** status **   <a name="odb-Type-DbServerSummary-status"></a>
The current status of the database server.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-DbServerSummary-statusReason"></a>
Additional information about the status of the database server.
Type: String
Required: No

 ** vmClusterIds **   <a name="odb-Type-DbServerSummary-vmClusterIds"></a>
The IDs of the VM clusters that are associated with the database server.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

## See Also
<a name="API_DbServerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DbServerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DbServerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DbServerSummary)
