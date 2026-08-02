---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DbNode.html
---

# DbNode
<a name="API_DbNode"></a>

Information about a DB node.

## Contents
<a name="API_DbNode_Contents"></a>

 ** additionalDetails **   <a name="odb-Type-DbNode-additionalDetails"></a>
Additional information about the planned maintenance.
Type: String
Required: No

 ** backupIpId **   <a name="odb-Type-DbNode-backupIpId"></a>
The Oracle Cloud ID (OCID) of the backup IP address that's associated with the DB node.
Type: String
Required: No

 ** backupVnic2Id **   <a name="odb-Type-DbNode-backupVnic2Id"></a>
The OCID of the second backup VNIC.
Type: String
Required: No

 ** backupVnicId **   <a name="odb-Type-DbNode-backupVnicId"></a>
The OCID of the backup VNIC.
Type: String
Required: No

 ** cpuCoreCount **   <a name="odb-Type-DbNode-cpuCoreCount"></a>
Number of CPU cores enabled on the DB node.
Type: Integer
Required: No

 ** createdAt **   <a name="odb-Type-DbNode-createdAt"></a>
The date and time when the DB node was created.
Type: Timestamp
Required: No

 ** dbNodeArn **   <a name="odb-Type-DbNode-dbNodeArn"></a>
The Amazon Resource Name (ARN) of the DB node.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** dbNodeId **   <a name="odb-Type-DbNode-dbNodeId"></a>
The unique identifier of the DB node.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-DbNode-dbNodeStorageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GBs), that's allocated on the DB node.
Type: Integer
Required: No

 ** dbServerId **   <a name="odb-Type-DbNode-dbServerId"></a>
The unique identifier of the Db server that is associated with the DB node.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** dbSystemId **   <a name="odb-Type-DbNode-dbSystemId"></a>
The OCID of the DB system.
Type: String
Required: No

 ** faultDomain **   <a name="odb-Type-DbNode-faultDomain"></a>
The name of the fault domain the instance is contained in.
Type: String
Required: No

 ** floatingIpAddress **   <a name="odb-Type-DbNode-floatingIpAddress"></a>
The floating IP address assigned to the DB node.
Type: String
Required: No

 ** hostIpId **   <a name="odb-Type-DbNode-hostIpId"></a>
The OCID of the host IP address that's associated with the DB node.
Type: String
Required: No

 ** hostname **   <a name="odb-Type-DbNode-hostname"></a>
The host name for the DB node.
Type: String
Required: No

 ** maintenanceType **   <a name="odb-Type-DbNode-maintenanceType"></a>
The type of database node maintenance. Either `VMDB_REBOOT_MIGRATION` or `EXADBXS_REBOOT_MIGRATION`.
Type: String
Valid Values: `VMDB_REBOOT_MIGRATION`
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-DbNode-memorySizeInGBs"></a>
The allocated memory in GBs on the DB node.
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-DbNode-ocid"></a>
The OCID of the DB node.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-DbNode-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the DB node.
Type: String
Required: No

 ** privateIpAddress **   <a name="odb-Type-DbNode-privateIpAddress"></a>
The private IP address assigned to the DB node.
Type: String
Required: No

 ** softwareStorageSizeInGB **   <a name="odb-Type-DbNode-softwareStorageSizeInGB"></a>
The size (in GB) of the block storage volume allocation for the DB system.
Type: Integer
Required: No

 ** status **   <a name="odb-Type-DbNode-status"></a>
The current status of the DB node.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | STOPPING | STOPPED | STARTING`
Required: No

 ** statusReason **   <a name="odb-Type-DbNode-statusReason"></a>
Additional information about the status of the DB node.
Type: String
Required: No

 ** timeMaintenanceWindowEnd **   <a name="odb-Type-DbNode-timeMaintenanceWindowEnd"></a>
End date and time of maintenance window.
Type: String
Required: No

 ** timeMaintenanceWindowStart **   <a name="odb-Type-DbNode-timeMaintenanceWindowStart"></a>
Start date and time of maintenance window.
Type: String
Required: No

 ** totalCpuCoreCount **   <a name="odb-Type-DbNode-totalCpuCoreCount"></a>
The total number of CPU cores reserved on the DB node.
Type: Integer
Required: No

 ** vnic2Id **   <a name="odb-Type-DbNode-vnic2Id"></a>
The OCID of the second VNIC.
Type: String
Required: No

 ** vnicId **   <a name="odb-Type-DbNode-vnicId"></a>
The OCID of the VNIC.
Type: String
Required: No

## See Also
<a name="API_DbNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DbNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DbNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DbNode)
