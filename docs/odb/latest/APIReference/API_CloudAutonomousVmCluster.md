---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudAutonomousVmCluster.html
---

# CloudAutonomousVmCluster
<a name="API_CloudAutonomousVmCluster"></a>

Information about an Autonomous VM cluster resource.

## Contents
<a name="API_CloudAutonomousVmCluster_Contents"></a>

 ** cloudAutonomousVmClusterId **   <a name="odb-Type-CloudAutonomousVmCluster-cloudAutonomousVmClusterId"></a>
The unique identifier of the Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** autonomousDataStoragePercentage **   <a name="odb-Type-CloudAutonomousVmCluster-autonomousDataStoragePercentage"></a>
The percentage of data storage currently in use for Autonomous Databases in the Autonomous VM cluster.
Type: Float
Required: No

 ** autonomousDataStorageSizeInTBs **   <a name="odb-Type-CloudAutonomousVmCluster-autonomousDataStorageSizeInTBs"></a>
The data storage size allocated for Autonomous Databases in the Autonomous VM cluster, in TB.
Type: Double
Required: No

 ** availableAutonomousDataStorageSizeInTBs **   <a name="odb-Type-CloudAutonomousVmCluster-availableAutonomousDataStorageSizeInTBs"></a>
The available data storage space for Autonomous Databases in the Autonomous VM cluster, in TB.
Type: Double
Required: No

 ** availableContainerDatabases **   <a name="odb-Type-CloudAutonomousVmCluster-availableContainerDatabases"></a>
The number of Autonomous CDBs that you can create with the currently available storage.
Type: Integer
Required: No

 ** availableCpus **   <a name="odb-Type-CloudAutonomousVmCluster-availableCpus"></a>
The number of CPU cores available for allocation to Autonomous Databases.
Type: Float
Required: No

 ** cloudAutonomousVmClusterArn **   <a name="odb-Type-CloudAutonomousVmCluster-cloudAutonomousVmClusterArn"></a>
The Amazon Resource Name (ARN) for the Autonomous VM cluster.
Type: String
Required: No

 ** cloudExadataInfrastructureArn **   <a name="odb-Type-CloudAutonomousVmCluster-cloudExadataInfrastructureArn"></a>
The Amazon Resource Name (ARN) of the Cloud Exadata Infrastructure containing this Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** cloudExadataInfrastructureId **   <a name="odb-Type-CloudAutonomousVmCluster-cloudExadataInfrastructureId"></a>
The unique identifier of the Cloud Exadata Infrastructure containing this Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** computeModel **   <a name="odb-Type-CloudAutonomousVmCluster-computeModel"></a>
The compute model of the Autonomous VM cluster: ECPU or OCPU.
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** cpuCoreCount **   <a name="odb-Type-CloudAutonomousVmCluster-cpuCoreCount"></a>
The total number of CPU cores in the Autonomous VM cluster.
Type: Integer
Required: No

 ** cpuCoreCountPerNode **   <a name="odb-Type-CloudAutonomousVmCluster-cpuCoreCountPerNode"></a>
The number of CPU cores enabled per node in the Autonomous VM cluster.
Type: Integer
Required: No

 ** cpuPercentage **   <a name="odb-Type-CloudAutonomousVmCluster-cpuPercentage"></a>
The percentage of total CPU cores currently in use in the Autonomous VM cluster.
Type: Float
Required: No

 ** createdAt **   <a name="odb-Type-CloudAutonomousVmCluster-createdAt"></a>
The date and time when the Autonomous VM cluster was created.
Type: Timestamp
Required: No

 ** dataStorageSizeInGBs **   <a name="odb-Type-CloudAutonomousVmCluster-dataStorageSizeInGBs"></a>
The total data storage allocated to the Autonomous VM cluster, in GB.
Type: Double
Required: No

 ** dataStorageSizeInTBs **   <a name="odb-Type-CloudAutonomousVmCluster-dataStorageSizeInTBs"></a>
The total data storage allocated to the Autonomous VM cluster, in TB.
Type: Double
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-CloudAutonomousVmCluster-dbNodeStorageSizeInGBs"></a>
The local node storage allocated to the Autonomous VM cluster, in gigabytes (GB).
Type: Integer
Required: No

 ** dbServers **   <a name="odb-Type-CloudAutonomousVmCluster-dbServers"></a>
The list of database servers associated with the Autonomous VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** description **   <a name="odb-Type-CloudAutonomousVmCluster-description"></a>
The user-provided description of the Autonomous VM cluster.
Type: String
Required: No

 ** displayName **   <a name="odb-Type-CloudAutonomousVmCluster-displayName"></a>
The display name of the Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** domain **   <a name="odb-Type-CloudAutonomousVmCluster-domain"></a>
The domain name for the Autonomous VM cluster.
Type: String
Required: No

 ** exadataStorageInTBsLowestScaledValue **   <a name="odb-Type-CloudAutonomousVmCluster-exadataStorageInTBsLowestScaledValue"></a>
The minimum value to which you can scale down the Exadata storage, in TB.
Type: Double
Required: No

 ** hostname **   <a name="odb-Type-CloudAutonomousVmCluster-hostname"></a>
The hostname for the Autonomous VM cluster.
Type: String
Required: No

 ** iamRoles **   <a name="odb-Type-CloudAutonomousVmCluster-iamRoles"></a>
The AWS Identity and Access Management (IAM) service roles associated with the Autonomous VM cluster.
Type: Array of [IamRole](API_IamRole.md) objects
Required: No

 ** isMtlsEnabledVmCluster **   <a name="odb-Type-CloudAutonomousVmCluster-isMtlsEnabledVmCluster"></a>
Indicates whether mutual TLS (mTLS) authentication is enabled for the Autonomous VM cluster.
Type: Boolean
Required: No

 ** licenseModel **   <a name="odb-Type-CloudAutonomousVmCluster-licenseModel"></a>
The Oracle license model that applies to the Autonomous VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** maintenanceWindow **   <a name="odb-Type-CloudAutonomousVmCluster-maintenanceWindow"></a>
The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
Type: [MaintenanceWindow](API_MaintenanceWindow.md) object
Required: No

 ** maxAcdsLowestScaledValue **   <a name="odb-Type-CloudAutonomousVmCluster-maxAcdsLowestScaledValue"></a>
The minimum value to which you can scale down the maximum number of Autonomous CDBs.
Type: Integer
Required: No

 ** memoryPerOracleComputeUnitInGBs **   <a name="odb-Type-CloudAutonomousVmCluster-memoryPerOracleComputeUnitInGBs"></a>
The amount of memory allocated per Oracle Compute Unit, in GB.
Type: Integer
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-CloudAutonomousVmCluster-memorySizeInGBs"></a>
The total amount of memory allocated to the Autonomous VM cluster, in gigabytes (GB).
Type: Integer
Required: No

 ** nodeCount **   <a name="odb-Type-CloudAutonomousVmCluster-nodeCount"></a>
The number of database server nodes in the Autonomous VM cluster.
Type: Integer
Required: No

 ** nonProvisionableAutonomousContainerDatabases **   <a name="odb-Type-CloudAutonomousVmCluster-nonProvisionableAutonomousContainerDatabases"></a>
The number of Autonomous CDBs that can't be provisioned because of resource constraints.
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-CloudAutonomousVmCluster-ocid"></a>
The Oracle Cloud Identifier (OCID) of the Autonomous VM cluster.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-CloudAutonomousVmCluster-ociResourceAnchorName"></a>
The name of the OCI resource anchor associated with this Autonomous VM cluster.
Type: String
Required: No

 ** ociUrl **   <a name="odb-Type-CloudAutonomousVmCluster-ociUrl"></a>
The URL for accessing the OCI console page for this Autonomous VM cluster.
Type: String
Required: No

 ** odbNetworkArn **   <a name="odb-Type-CloudAutonomousVmCluster-odbNetworkArn"></a>
The Amazon Resource Name (ARN) of the ODB network associated with this Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** odbNetworkId **   <a name="odb-Type-CloudAutonomousVmCluster-odbNetworkId"></a>
The unique identifier of the ODB network associated with this Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** percentProgress **   <a name="odb-Type-CloudAutonomousVmCluster-percentProgress"></a>
The progress of the current operation on the Autonomous VM cluster, as a percentage.
Type: Float
Required: No

 ** provisionableAutonomousContainerDatabases **   <a name="odb-Type-CloudAutonomousVmCluster-provisionableAutonomousContainerDatabases"></a>
The number of Autonomous CDBs that can be provisioned in the Autonomous VM cluster.
Type: Integer
Required: No

 ** provisionedAutonomousContainerDatabases **   <a name="odb-Type-CloudAutonomousVmCluster-provisionedAutonomousContainerDatabases"></a>
The number of Autonomous CDBs currently provisioned in the Autonomous VM cluster.
Type: Integer
Required: No

 ** provisionedCpus **   <a name="odb-Type-CloudAutonomousVmCluster-provisionedCpus"></a>
The number of CPU cores currently provisioned in the Autonomous VM cluster.
Type: Float
Required: No

 ** reclaimableCpus **   <a name="odb-Type-CloudAutonomousVmCluster-reclaimableCpus"></a>
The number of CPU cores that can be reclaimed from terminated or scaled-down Autonomous Databases.
Type: Float
Required: No

 ** reservedCpus **   <a name="odb-Type-CloudAutonomousVmCluster-reservedCpus"></a>
The number of CPU cores reserved for system operations and redundancy.
Type: Float
Required: No

 ** scanListenerPortNonTls **   <a name="odb-Type-CloudAutonomousVmCluster-scanListenerPortNonTls"></a>
The SCAN listener port for non-TLS (TCP) protocol. The default is 1521.
Type: Integer
Required: No

 ** scanListenerPortTls **   <a name="odb-Type-CloudAutonomousVmCluster-scanListenerPortTls"></a>
The SCAN listener port for TLS (TCP) protocol. The default is 2484.
Type: Integer
Required: No

 ** shape **   <a name="odb-Type-CloudAutonomousVmCluster-shape"></a>
The shape of the Exadata infrastructure for the Autonomous VM cluster.
Type: String
Required: No

 ** status **   <a name="odb-Type-CloudAutonomousVmCluster-status"></a>
The current state of the Autonomous VM cluster. Possible values include `CREATING`, `AVAILABLE`, `UPDATING`, `DELETING`, `DELETED`, `FAILED`.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-CloudAutonomousVmCluster-statusReason"></a>
Additional information about the current status of the Autonomous VM cluster.
Type: String
Required: No

 ** timeDatabaseSslCertificateExpires **   <a name="odb-Type-CloudAutonomousVmCluster-timeDatabaseSslCertificateExpires"></a>
The expiration date and time of the database SSL certificate.
Type: Timestamp
Required: No

 ** timeOrdsCertificateExpires **   <a name="odb-Type-CloudAutonomousVmCluster-timeOrdsCertificateExpires"></a>
The expiration date and time of the Oracle REST Data Services (ORDS) certificate.
Type: Timestamp
Required: No

 ** timeZone **   <a name="odb-Type-CloudAutonomousVmCluster-timeZone"></a>
The time zone of the Autonomous VM cluster.
Type: String
Required: No

 ** totalContainerDatabases **   <a name="odb-Type-CloudAutonomousVmCluster-totalContainerDatabases"></a>
The total number of Autonomous Container Databases that can be created with the allocated local storage.
Type: Integer
Required: No

## See Also
<a name="API_CloudAutonomousVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CloudAutonomousVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CloudAutonomousVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CloudAutonomousVmCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
