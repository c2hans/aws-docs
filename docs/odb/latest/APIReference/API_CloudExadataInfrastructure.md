---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudExadataInfrastructure.html
---

# CloudExadataInfrastructure
<a name="API_CloudExadataInfrastructure"></a>

Information about an Exadata infrastructure.

## Contents
<a name="API_CloudExadataInfrastructure_Contents"></a>

 ** cloudExadataInfrastructureId **   <a name="odb-Type-CloudExadataInfrastructure-cloudExadataInfrastructureId"></a>
The unique identifier for the Exadata infrastructure.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** activatedStorageCount **   <a name="odb-Type-CloudExadataInfrastructure-activatedStorageCount"></a>
The number of storage servers requested for the Exadata infrastructure.
Type: Integer
Required: No

 ** additionalStorageCount **   <a name="odb-Type-CloudExadataInfrastructure-additionalStorageCount"></a>
The number of storage servers requested for the Exadata infrastructure.
Type: Integer
Required: No

 ** availabilityZone **   <a name="odb-Type-CloudExadataInfrastructure-availabilityZone"></a>
The name of the Availability Zone (AZ) where the Exadata infrastructure is located.
Type: String
Required: No

 ** availabilityZoneId **   <a name="odb-Type-CloudExadataInfrastructure-availabilityZoneId"></a>
The AZ ID of the AZ where the Exadata infrastructure is located.
Type: String
Required: No

 ** availableStorageSizeInGBs **   <a name="odb-Type-CloudExadataInfrastructure-availableStorageSizeInGBs"></a>
The amount of available storage, in gigabytes (GB), for the Exadata infrastructure.
Type: Integer
Required: No

 ** cloudExadataInfrastructureArn **   <a name="odb-Type-CloudExadataInfrastructure-cloudExadataInfrastructureArn"></a>
The Amazon Resource Name (ARN) for the Exadata infrastructure.
Type: String
Required: No

 ** computeCount **   <a name="odb-Type-CloudExadataInfrastructure-computeCount"></a>
The number of database servers for the Exadata infrastructure.
Type: Integer
Required: No

 ** computeModel **   <a name="odb-Type-CloudExadataInfrastructure-computeModel"></a>
The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** cpuCount **   <a name="odb-Type-CloudExadataInfrastructure-cpuCount"></a>
The total number of CPU cores that are allocated to the Exadata infrastructure.
Type: Integer
Required: No

 ** createdAt **   <a name="odb-Type-CloudExadataInfrastructure-createdAt"></a>
The date and time when the Exadata infrastructure was created.
Type: Timestamp
Required: No

 ** customerContactsToSendToOCI **   <a name="odb-Type-CloudExadataInfrastructure-customerContactsToSendToOCI"></a>
The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.
Type: Array of [CustomerContact](API_CustomerContact.md) objects
Required: No

 ** databaseServerType **   <a name="odb-Type-CloudExadataInfrastructure-databaseServerType"></a>
The database server model type of the Exadata infrastructure. For the list of valid model names, use the `ListDbSystemShapes` operation.
Type: String
Required: No

 ** dataStorageSizeInTBs **   <a name="odb-Type-CloudExadataInfrastructure-dataStorageSizeInTBs"></a>
The size of the Exadata infrastructure's data disk group, in terabytes (TB).
Type: Double
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-CloudExadataInfrastructure-dbNodeStorageSizeInGBs"></a>
The size of the Exadata infrastructure's local node storage, in gigabytes (GB).
Type: Integer
Required: No

 ** dbServerVersion **   <a name="odb-Type-CloudExadataInfrastructure-dbServerVersion"></a>
The software version of the database servers (dom0) in the Exadata infrastructure.
Type: String
Required: No

 ** displayName **   <a name="odb-Type-CloudExadataInfrastructure-displayName"></a>
The user-friendly name for the Exadata infrastructure.
Type: String
Required: No

 ** lastMaintenanceRunId **   <a name="odb-Type-CloudExadataInfrastructure-lastMaintenanceRunId"></a>
The Oracle Cloud Identifier (OCID) of the last maintenance run for the Exadata infrastructure.
Type: String
Required: No

 ** maintenanceWindow **   <a name="odb-Type-CloudExadataInfrastructure-maintenanceWindow"></a>
The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
Type: [MaintenanceWindow](API_MaintenanceWindow.md) object
Required: No

 ** maxCpuCount **   <a name="odb-Type-CloudExadataInfrastructure-maxCpuCount"></a>
The total number of CPU cores available on the Exadata infrastructure.
Type: Integer
Required: No

 ** maxDataStorageInTBs **   <a name="odb-Type-CloudExadataInfrastructure-maxDataStorageInTBs"></a>
The total amount of data disk group storage, in terabytes (TB), that's available on the Exadata infrastructure.
Type: Double
Required: No

 ** maxDbNodeStorageSizeInGBs **   <a name="odb-Type-CloudExadataInfrastructure-maxDbNodeStorageSizeInGBs"></a>
The total amount of local node storage, in gigabytes (GB), that's available on the Exadata infrastructure.
Type: Integer
Required: No

 ** maxMemoryInGBs **   <a name="odb-Type-CloudExadataInfrastructure-maxMemoryInGBs"></a>
The total amount of memory, in gigabytes (GB), that's available on the Exadata infrastructure.
Type: Integer
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-CloudExadataInfrastructure-memorySizeInGBs"></a>
The amount of memory, in gigabytes (GB), that's allocated on the Exadata infrastructure.
Type: Integer
Required: No

 ** monthlyDbServerVersion **   <a name="odb-Type-CloudExadataInfrastructure-monthlyDbServerVersion"></a>
The monthly software version of the database servers installed on the Exadata infrastructure.
Type: String
Required: No

 ** monthlyStorageServerVersion **   <a name="odb-Type-CloudExadataInfrastructure-monthlyStorageServerVersion"></a>
The monthly software version of the storage servers installed on the Exadata infrastructure.
Type: String
Required: No

 ** nextMaintenanceRunId **   <a name="odb-Type-CloudExadataInfrastructure-nextMaintenanceRunId"></a>
The OCID of the next maintenance run for the Exadata infrastructure.
Type: String
Required: No

 ** ocid **   <a name="odb-Type-CloudExadataInfrastructure-ocid"></a>
The OCID of the Exadata infrastructure.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-CloudExadataInfrastructure-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the Exadata infrastructure.
Type: String
Required: No

 ** ociUrl **   <a name="odb-Type-CloudExadataInfrastructure-ociUrl"></a>
The HTTPS link to the Exadata infrastructure in OCI.
Type: String
Required: No

 ** percentProgress **   <a name="odb-Type-CloudExadataInfrastructure-percentProgress"></a>
The amount of progress made on the current operation on the Exadata infrastructure, expressed as a percentage.
Type: Float
Required: No

 ** shape **   <a name="odb-Type-CloudExadataInfrastructure-shape"></a>
The model name of the Exadata infrastructure.
Type: String
Required: No

 ** status **   <a name="odb-Type-CloudExadataInfrastructure-status"></a>
The current status of the Exadata infrastructure.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-CloudExadataInfrastructure-statusReason"></a>
Additional information about the status of the Exadata infrastructure.
Type: String
Required: No

 ** storageCount **   <a name="odb-Type-CloudExadataInfrastructure-storageCount"></a>
The number of storage servers that are activated for the Exadata infrastructure.
Type: Integer
Required: No

 ** storageServerType **   <a name="odb-Type-CloudExadataInfrastructure-storageServerType"></a>
The storage server model type of the Exadata infrastructure. For the list of valid model names, use the `ListDbSystemShapes` operation.
Type: String
Required: No

 ** storageServerVersion **   <a name="odb-Type-CloudExadataInfrastructure-storageServerVersion"></a>
The software version of the storage servers on the Exadata infrastructure.
Type: String
Required: No

 ** totalStorageSizeInGBs **   <a name="odb-Type-CloudExadataInfrastructure-totalStorageSizeInGBs"></a>
The total amount of storage, in gigabytes (GB), on the the Exadata infrastructure.
Type: Integer
Required: No

## See Also
<a name="API_CloudExadataInfrastructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CloudExadataInfrastructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CloudExadataInfrastructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CloudExadataInfrastructure)
