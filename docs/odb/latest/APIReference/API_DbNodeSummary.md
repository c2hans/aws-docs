---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DbNodeSummary.html
---

# DbNodeSummary
<a name="API_DbNodeSummary"></a>

Information about a DB node.

## Contents
<a name="API_DbNodeSummary_Contents"></a>

 ** additionalDetails **   <a name="odb-Type-DbNodeSummary-additionalDetails"></a>
Additional information about the planned maintenance.
Type: String
Required: No

 ** backupIpId **   <a name="odb-Type-DbNodeSummary-backupIpId"></a>
The Oracle Cloud ID (OCID) of the backup IP address that's associated with the DB node.
Type: String
Required: No

 ** backupVnic2Id **   <a name="odb-Type-DbNodeSummary-backupVnic2Id"></a>
The OCID of the second backup virtual network interface card (VNIC) for the DB node.
Type: String
Required: No

 ** backupVnicId **   <a name="odb-Type-DbNodeSummary-backupVnicId"></a>
The OCID of the backup VNIC for the DB node.
Type: String
Required: No

 ** cpuCoreCount **   <a name="odb-Type-DbNodeSummary-cpuCoreCount"></a>
The number of CPU cores enabled on the DB node.
Type: Integer
Required: No

 ** createdAt **   <a name="odb-Type-DbNodeSummary-createdAt"></a>
The date and time when the DB node was created.
Type: Timestamp
Required: No

 ** dbNodeArn **   <a name="odb-Type-DbNodeSummary-dbNodeArn"></a>
The Amazon Resource Name (ARN) of the DB node.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** dbNodeId **   <a name="odb-Type-DbNodeSummary-dbNodeId"></a>
The unique identifier of the DB node.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-DbNodeSummary-dbNodeStorageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GB), that's allocated on the DB node.
Type: Integer
Required: No

 ** dbServerId **   <a name="odb-Type-DbNodeSummary-dbServerId"></a>
The unique identifier of the database server that's associated with the DB node.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** dbSystemId **   <a name="odb-Type-DbNodeSummary-dbSystemId"></a>
The OCID of the DB system.
Type: String
Required: No

 ** faultDomain **   <a name="odb-Type-DbNodeSummary-faultDomain"></a>
The name of the fault domain where the DB node is located.
Type: String
Required: No

 ** hostIpId **   <a name="odb-Type-DbNodeSummary-hostIpId"></a>
The OCID of the host IP address that's associated with the DB node.
Type: String
Required: No

 ** hostname **   <a name="odb-Type-DbNodeSummary-hostname"></a>
The host name for the DB node.
Type: String
Required: No

 ** maintenanceType **   <a name="odb-Type-DbNodeSummary-maintenanceType"></a>
The type of maintenance the DB node.
Type: String
Valid Values: `VMDB_REBOOT_MIGRATION`
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-DbNodeSummary-memorySizeInGBs"></a>
The amount of memory, in gigabytes (GB), that allocated on the DB node.
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-DbNodeSummary-ocid"></a>
The OCID of the DB node.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-DbNodeSummary-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the DB node.
Type: String
Required: No

 ** softwareStorageSizeInGB **   <a name="odb-Type-DbNodeSummary-softwareStorageSizeInGB"></a>
The size of the block storage volume, in gigabytes (GB), that's allocated for the DB system. This attribute applies only for virtual machine DB systems.
Type: Integer
Required: No

 ** status **   <a name="odb-Type-DbNodeSummary-status"></a>
The current status of the DB node.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | STOPPING | STOPPED | STARTING`
Required: No

 ** statusReason **   <a name="odb-Type-DbNodeSummary-statusReason"></a>
Additional information about the status of the DB node.
Type: String
Required: No

 ** timeMaintenanceWindowEnd **   <a name="odb-Type-DbNodeSummary-timeMaintenanceWindowEnd"></a>
The end date and time of the maintenance window.
Type: String
Required: No

 ** timeMaintenanceWindowStart **   <a name="odb-Type-DbNodeSummary-timeMaintenanceWindowStart"></a>
The start date and time of the maintenance window.
Type: String
Required: No

 ** totalCpuCoreCount **   <a name="odb-Type-DbNodeSummary-totalCpuCoreCount"></a>
The total number of CPU cores reserved on the DB node.
Type: Integer
Required: No

 ** vnic2Id **   <a name="odb-Type-DbNodeSummary-vnic2Id"></a>
The OCID of the second VNIC.
Type: String
Required: No

 ** vnicId **   <a name="odb-Type-DbNodeSummary-vnicId"></a>
The OCID of the VNIC.
Type: String
Required: No

## See Also
<a name="API_DbNodeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DbNodeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DbNodeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DbNodeSummary)
