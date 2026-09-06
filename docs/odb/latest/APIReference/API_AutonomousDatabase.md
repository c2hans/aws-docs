---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousDatabase.html
---

# AutonomousDatabase
<a name="API_AutonomousDatabase"></a>

Information about an Autonomous Database.

## Contents
<a name="API_AutonomousDatabase_Contents"></a>

 ** actualUsedDataStorageSizeInTBs **   <a name="odb-Type-AutonomousDatabase-actualUsedDataStorageSizeInTBs"></a>
The actual amount of data storage currently in use by the Autonomous Database, in TB.
Type: Double
Required: No

 ** adminPasswordSourceSummary **   <a name="odb-Type-AutonomousDatabase-adminPasswordSourceSummary"></a>
The summary of the admin password source configuration for the Autonomous Database.
Type: [AdminPasswordSourceSummary](API_AdminPasswordSourceSummary.md) object
Required: No

 ** allocatedStorageSizeInTBs **   <a name="odb-Type-AutonomousDatabase-allocatedStorageSizeInTBs"></a>
The amount of storage currently allocated to the Autonomous Database, in TB.
Type: Double
Required: No

 ** allowlistedIps **   <a name="odb-Type-AutonomousDatabase-allowlistedIps"></a>
The list of IP addresses that are allowed to access the Autonomous Database.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** apexDetails **   <a name="odb-Type-AutonomousDatabase-apexDetails"></a>
The Oracle Application Express (APEX) details for the Autonomous Database.
Type: [AutonomousDatabaseApex](API_AutonomousDatabaseApex.md) object
Required: No

 ** autonomousDatabaseArn **   <a name="odb-Type-AutonomousDatabase-autonomousDatabaseArn"></a>
The Amazon Resource Name (ARN) of the Autonomous Database.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** autonomousDatabaseId **   <a name="odb-Type-AutonomousDatabase-autonomousDatabaseId"></a>
The unique identifier of the Autonomous Database.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** autonomousMaintenanceScheduleType **   <a name="odb-Type-AutonomousDatabase-autonomousMaintenanceScheduleType"></a>
The maintenance schedule type for the Autonomous Database.
Type: String
Valid Values: `EARLY | REGULAR`
Required: No

 ** autoRefreshFrequencyInSeconds **   <a name="odb-Type-AutonomousDatabase-autoRefreshFrequencyInSeconds"></a>
The frequency, in seconds, at which the refreshable clone Autonomous Database is automatically refreshed.
Type: Integer
Required: No

 ** autoRefreshPointLagInSeconds **   <a name="odb-Type-AutonomousDatabase-autoRefreshPointLagInSeconds"></a>
The time lag, in seconds, between the refreshable clone and its source Autonomous Database.
Type: Integer
Required: No

 ** availabilityZone **   <a name="odb-Type-AutonomousDatabase-availabilityZone"></a>
The Availability Zone where the Autonomous Database is located.
Type: String
Required: No

 ** availabilityZoneId **   <a name="odb-Type-AutonomousDatabase-availabilityZoneId"></a>
The unique identifier of the Availability Zone where the Autonomous Database is located.
Type: String
Required: No

 ** availableUpgradeVersions **   <a name="odb-Type-AutonomousDatabase-availableUpgradeVersions"></a>
The list of Oracle Database software versions to which the Autonomous Database can be upgraded.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** backupRetentionPeriodInDays **   <a name="odb-Type-AutonomousDatabase-backupRetentionPeriodInDays"></a>
The retention period, in days, for automatic backups of the Autonomous Database.
Type: Integer
Required: No

 ** byolComputeCountLimit **   <a name="odb-Type-AutonomousDatabase-byolComputeCountLimit"></a>
The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.
Type: Integer
Required: No

 ** characterSet **   <a name="odb-Type-AutonomousDatabase-characterSet"></a>
The character set of the Autonomous Database.
Type: String
Required: No

 ** cloneTableSpaceList **   <a name="odb-Type-AutonomousDatabase-cloneTableSpaceList"></a>
The list of tablespace identifiers to clone for the Autonomous Database.
Type: Array of integers
Required: No

 ** computeCount **   <a name="odb-Type-AutonomousDatabase-computeCount"></a>
The compute capacity, in number of Elastic CPUs (ECPUs) or Oracle CPUs (OCPUs), assigned to the Autonomous Database.
Type: Float
Required: No

 ** computeModel **   <a name="odb-Type-AutonomousDatabase-computeModel"></a>
The compute model of the Autonomous Database, either ECPU or OCPU.
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** connectionStringDetails **   <a name="odb-Type-AutonomousDatabase-connectionStringDetails"></a>
The connection string details for the Autonomous Database.
Type: [AutonomousDatabaseConnectionStrings](API_AutonomousDatabaseConnectionStrings.md) object
Required: No

 ** connectionUrls **   <a name="odb-Type-AutonomousDatabase-connectionUrls"></a>
The connection URLs for accessing tools and services for the Autonomous Database.
Type: [AutonomousDatabaseConnectionUrls](API_AutonomousDatabaseConnectionUrls.md) object
Required: No

 ** cpuCoreCount **   <a name="odb-Type-AutonomousDatabase-cpuCoreCount"></a>
The number of CPU cores allocated to the Autonomous Database.
Type: Integer
Required: No

 ** createdAt **   <a name="odb-Type-AutonomousDatabase-createdAt"></a>
The date and time when the Autonomous Database was created.
Type: Timestamp
Required: No

 ** customerContacts **   <a name="odb-Type-AutonomousDatabase-customerContacts"></a>
The list of customer contacts that receive operational notifications from Oracle for the Autonomous Database.
Type: Array of [CustomerContact](API_CustomerContact.md) objects
Required: No

 ** databaseEdition **   <a name="odb-Type-AutonomousDatabase-databaseEdition"></a>
The Oracle Database edition of the Autonomous Database.
Type: String
Valid Values: `STANDARD_EDITION | ENTERPRISE_EDITION`
Required: No

 ** databaseManagementStatus **   <a name="odb-Type-AutonomousDatabase-databaseManagementStatus"></a>
The status of Oracle Database Management for the Autonomous Database.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | NOT_ENABLED | FAILED_ENABLING | FAILED_DISABLING`
Required: No

 ** databaseType **   <a name="odb-Type-AutonomousDatabase-databaseType"></a>
The type of the Autonomous Database, either a regular database or a clone.
Type: String
Valid Values: `REGULAR | CLONE`
Required: No

 ** dataSafeStatus **   <a name="odb-Type-AutonomousDatabase-dataSafeStatus"></a>
The status of the Oracle Data Safe registration for the Autonomous Database.
Type: String
Valid Values: `REGISTERING | REGISTERED | DEREGISTERING | NOT_REGISTERED | FAILED`
Required: No

 ** dataStorageSizeInGBs **   <a name="odb-Type-AutonomousDatabase-dataStorageSizeInGBs"></a>
The size, in gigabytes (GB), of the data volume allocated for the Autonomous Database.
Type: Integer
Required: No

 ** dataStorageSizeInTBs **   <a name="odb-Type-AutonomousDatabase-dataStorageSizeInTBs"></a>
The size, in terabytes (TB), of the data volume allocated for the Autonomous Database.
Type: Double
Required: No

 ** dbName **   <a name="odb-Type-AutonomousDatabase-dbName"></a>
The name of the Autonomous Database.
Type: String
Required: No

 ** dbToolsDetails **   <a name="odb-Type-AutonomousDatabase-dbToolsDetails"></a>
The list of database management tools enabled for the Autonomous Database.
Type: Array of [DatabaseTool](API_DatabaseTool.md) objects
Required: No

 ** dbVersion **   <a name="odb-Type-AutonomousDatabase-dbVersion"></a>
The Oracle Database software version of the Autonomous Database.
Type: String
Required: No

 ** dbWorkload **   <a name="odb-Type-AutonomousDatabase-dbWorkload"></a>
The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.
Type: String
Valid Values: `OLTP | AJD | APEX | LH`
Required: No

 ** displayName **   <a name="odb-Type-AutonomousDatabase-displayName"></a>
The user-friendly name of the Autonomous Database.
Type: String
Required: No

 ** encryptionSummary **   <a name="odb-Type-AutonomousDatabase-encryptionSummary"></a>
The encryption configuration for the Autonomous Database.
Type: [EncryptionSummary](API_EncryptionSummary.md) object
Required: No

 ** failedDataRecoveryInSeconds **   <a name="odb-Type-AutonomousDatabase-failedDataRecoveryInSeconds"></a>
The amount of time, in seconds, that the data in the Autonomous Database is behind the data in the primary database.
Type: Integer
Required: No

 ** inMemoryAreaInGBs **   <a name="odb-Type-AutonomousDatabase-inMemoryAreaInGBs"></a>
The size of the in-memory area of the Autonomous Database, in GB.
Type: Integer
Required: No

 ** isAutoScalingEnabled **   <a name="odb-Type-AutonomousDatabase-isAutoScalingEnabled"></a>
Indicates whether automatic scaling of the compute resources is enabled for the Autonomous Database.
Type: Boolean
Required: No

 ** isAutoScalingForStorageEnabled **   <a name="odb-Type-AutonomousDatabase-isAutoScalingForStorageEnabled"></a>
Indicates whether automatic scaling of the storage is enabled for the Autonomous Database.
Type: Boolean
Required: No

 ** isBackupRetentionLocked **   <a name="odb-Type-AutonomousDatabase-isBackupRetentionLocked"></a>
Indicates whether the backup retention period of the Autonomous Database is locked.
Type: Boolean
Required: No

 ** isLocalDataGuardEnabled **   <a name="odb-Type-AutonomousDatabase-isLocalDataGuardEnabled"></a>
Indicates whether local Oracle Data Guard is enabled for the Autonomous Database.
Type: Boolean
Required: No

 ** isMtlsConnectionRequired **   <a name="odb-Type-AutonomousDatabase-isMtlsConnectionRequired"></a>
Indicates whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.
Type: Boolean
Required: No

 ** isReconnectCloneEnabled **   <a name="odb-Type-AutonomousDatabase-isReconnectCloneEnabled"></a>
Indicates whether reconnecting the refreshable clone to its source Autonomous Database is enabled.
Type: Boolean
Required: No

 ** isRefreshableClone **   <a name="odb-Type-AutonomousDatabase-isRefreshableClone"></a>
Indicates whether the Autonomous Database is a refreshable clone.
Type: Boolean
Required: No

 ** isRemoteDataGuardEnabled **   <a name="odb-Type-AutonomousDatabase-isRemoteDataGuardEnabled"></a>
Indicates whether remote Oracle Data Guard is enabled for the Autonomous Database.
Type: Boolean
Required: No

 ** licenseModel **   <a name="odb-Type-AutonomousDatabase-licenseModel"></a>
The Oracle license model that applies to the Autonomous Database.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** localAdgAutoFailoverMaxDataLossLimit **   <a name="odb-Type-AutonomousDatabase-localAdgAutoFailoverMaxDataLossLimit"></a>
The maximum data loss limit, in seconds, for automatic failover to the local Oracle Data Guard standby database.
Type: Integer
Required: No

 ** localDisasterRecoveryType **   <a name="odb-Type-AutonomousDatabase-localDisasterRecoveryType"></a>
The type of local disaster recovery configured for the Autonomous Database.
Type: String
Valid Values: `ADG | BACKUP_BASED`
Required: No

 ** localStandbyDb **   <a name="odb-Type-AutonomousDatabase-localStandbyDb"></a>
The details of the local standby Autonomous Database in an Oracle Data Guard configuration.
Type: [DatabaseStandbySummary](API_DatabaseStandbySummary.md) object
Required: No

 ** longTermBackupSchedule **   <a name="odb-Type-AutonomousDatabase-longTermBackupSchedule"></a>
The long-term backup schedule for the Autonomous Database.
Type: [LongTermBackupSchedule](API_LongTermBackupSchedule.md) object
Required: No

 ** maintenanceTargetComponent **   <a name="odb-Type-AutonomousDatabase-maintenanceTargetComponent"></a>
The component on the Autonomous Database that the current maintenance is being applied to.
Type: String
Required: No

 ** memoryPerOracleComputeUnitInGBs **   <a name="odb-Type-AutonomousDatabase-memoryPerOracleComputeUnitInGBs"></a>
The amount of memory allocated per Oracle Compute Unit, in GB.
Type: Integer
Required: No

 ** ncharacterSet **   <a name="odb-Type-AutonomousDatabase-ncharacterSet"></a>
The national character set of the Autonomous Database.
Type: String
Required: No

 ** netServicesArchitecture **   <a name="odb-Type-AutonomousDatabase-netServicesArchitecture"></a>
The Oracle Net Services architecture of the Autonomous Database, either dedicated or shared.
Type: String
Valid Values: `DEDICATED | SHARED`
Required: No

 ** nextLongTermBackupTimeStamp **   <a name="odb-Type-AutonomousDatabase-nextLongTermBackupTimeStamp"></a>
The date and time of the next scheduled long-term backup of the Autonomous Database.
Type: Timestamp
Required: No

 ** ocid **   <a name="odb-Type-AutonomousDatabase-ocid"></a>
The Oracle Cloud Identifier (OCID) of the Autonomous Database.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-AutonomousDatabase-ociResourceAnchorName"></a>
The name of the Oracle Cloud Infrastructure (OCI) resource anchor associated with the Autonomous Database.
Type: String
Required: No

 ** ociUrl **   <a name="odb-Type-AutonomousDatabase-ociUrl"></a>
The URL for accessing the OCI console page for the Autonomous Database.
Type: String
Required: No

 ** odbNetworkArn **   <a name="odb-Type-AutonomousDatabase-odbNetworkArn"></a>
The Amazon Resource Name (ARN) of the ODB network associated with the Autonomous Database.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** odbNetworkId **   <a name="odb-Type-AutonomousDatabase-odbNetworkId"></a>
The unique identifier of the ODB network associated with the Autonomous Database.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** openMode **   <a name="odb-Type-AutonomousDatabase-openMode"></a>
The mode in which the Autonomous Database is open, either read-only or read/write.
Type: String
Valid Values: `READ_ONLY | READ_WRITE`
Required: No

 ** operationsInsightsStatus **   <a name="odb-Type-AutonomousDatabase-operationsInsightsStatus"></a>
The status of Oracle Operations Insights for the Autonomous Database.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | NOT_ENABLED | FAILED_ENABLING | FAILED_DISABLING`
Required: No

 ** peerDbIds **   <a name="odb-Type-AutonomousDatabase-peerDbIds"></a>
The list of unique identifiers of the peer Autonomous Databases.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** percentProgress **   <a name="odb-Type-AutonomousDatabase-percentProgress"></a>
The progress of the current operation on the Autonomous Database, as a percentage.
Type: Float
Required: No

 ** permissionLevel **   <a name="odb-Type-AutonomousDatabase-permissionLevel"></a>
The permission level of the Autonomous Database.
Type: String
Valid Values: `RESTRICTED | UNRESTRICTED`
Required: No

 ** privateEndpoint **   <a name="odb-Type-AutonomousDatabase-privateEndpoint"></a>
The private endpoint for the Autonomous Database.
Type: String
Required: No

 ** privateEndpointIp **   <a name="odb-Type-AutonomousDatabase-privateEndpointIp"></a>
The private endpoint IP address for the Autonomous Database.
Type: String
Required: No

 ** privateEndpointLabel **   <a name="odb-Type-AutonomousDatabase-privateEndpointLabel"></a>
The private endpoint label for the Autonomous Database.
Type: String
Required: No

 ** provisionableCpus **   <a name="odb-Type-AutonomousDatabase-provisionableCpus"></a>
The list of CPU core counts that you can provision for the Autonomous Database.
Type: Array of integers
Required: No

 ** refreshableMode **   <a name="odb-Type-AutonomousDatabase-refreshableMode"></a>
The refresh mode of the refreshable clone Autonomous Database.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** refreshableStatus **   <a name="odb-Type-AutonomousDatabase-refreshableStatus"></a>
The refresh status of the refreshable clone Autonomous Database.
Type: String
Valid Values: `REFRESHING | NOT_REFRESHING`
Required: No

 ** remoteDisasterRecoveryConfiguration **   <a name="odb-Type-AutonomousDatabase-remoteDisasterRecoveryConfiguration"></a>
The configuration of the remote disaster recovery for the Autonomous Database.
Type: [DisasterRecoveryConfiguration](API_DisasterRecoveryConfiguration.md) object
Required: No

 ** resourcePoolLeaderId **   <a name="odb-Type-AutonomousDatabase-resourcePoolLeaderId"></a>
The unique identifier of the resource pool leader Autonomous Database.
Type: String
Required: No

 ** resourcePoolSummary **   <a name="odb-Type-AutonomousDatabase-resourcePoolSummary"></a>
The configuration of the resource pool for the Autonomous Database.
Type: [ResourcePoolSummary](API_ResourcePoolSummary.md) object
Required: No

 ** role **   <a name="odb-Type-AutonomousDatabase-role"></a>
The Oracle Data Guard role of the Autonomous Database.
Type: String
Valid Values: `PRIMARY | STANDBY | DISABLED_STANDBY | BACKUP_COPY | SNAPSHOT_STANDBY`
Required: No

 ** scheduledOperations **   <a name="odb-Type-AutonomousDatabase-scheduledOperations"></a>
The list of scheduled start and stop times for the Autonomous Database.
Type: Array of [ScheduledOperationDetails](API_ScheduledOperationDetails.md) objects
Required: No

 ** serviceConsoleUrl **   <a name="odb-Type-AutonomousDatabase-serviceConsoleUrl"></a>
The URL for accessing the Oracle service console for the Autonomous Database.
Type: String
Required: No

 ** sourceId **   <a name="odb-Type-AutonomousDatabase-sourceId"></a>
The unique identifier of the source from which the Autonomous Database was created.
Type: String
Required: No

 ** sqlWebDeveloperUrl **   <a name="odb-Type-AutonomousDatabase-sqlWebDeveloperUrl"></a>
The URL for accessing Oracle SQL Developer Web for the Autonomous Database.
Type: String
Required: No

 ** standbyAllowlistedIps **   <a name="odb-Type-AutonomousDatabase-standbyAllowlistedIps"></a>
The list of IP addresses that are allowed to access the standby Autonomous Database.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** standbyAllowlistedIpsSource **   <a name="odb-Type-AutonomousDatabase-standbyAllowlistedIpsSource"></a>
The source of the allowlisted IP addresses for the standby Autonomous Database.
Type: String
Valid Values: `PRIMARY | SEPARATE | NOT_APPLICABLE`
Required: No

 ** standbyDb **   <a name="odb-Type-AutonomousDatabase-standbyDb"></a>
The details of the standby Autonomous Database in a cross-Region Oracle Data Guard configuration.
Type: [DatabaseStandbySummary](API_DatabaseStandbySummary.md) object
Required: No

 ** status **   <a name="odb-Type-AutonomousDatabase-status"></a>
The current status of the Autonomous Database.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS | STOPPING | STOPPED | STARTING | UNAVAILABLE | RESTORE_IN_PROGRESS | RESTORE_FAILED | BACKUP_IN_PROGRESS | SCALE_IN_PROGRESS | AVAILABLE_NEEDS_ATTENTION | RESTARTING | RECREATING | ROLE_CHANGE_IN_PROGRESS | UPGRADING | INACCESSIBLE | STANDBY`
Required: No

 ** statusReason **   <a name="odb-Type-AutonomousDatabase-statusReason"></a>
Additional information about the current status of the Autonomous Database, if applicable.
Type: String
Required: No

 ** timeDataGuardRoleChanged **   <a name="odb-Type-AutonomousDatabase-timeDataGuardRoleChanged"></a>
The date and time when the Oracle Data Guard role of the Autonomous Database last changed.
Type: Timestamp
Required: No

 ** timeDeletionOfFreeAutonomousDatabase **   <a name="odb-Type-AutonomousDatabase-timeDeletionOfFreeAutonomousDatabase"></a>
The date and time when the inactive Always Free Autonomous Database is scheduled to be automatically deleted.
Type: Timestamp
Required: No

 ** timeDisasterRecoveryRoleChanged **   <a name="odb-Type-AutonomousDatabase-timeDisasterRecoveryRoleChanged"></a>
The date and time when the disaster recovery role of the Autonomous Database last changed.
Type: Timestamp
Required: No

 ** timeLocalDataGuardEnabled **   <a name="odb-Type-AutonomousDatabase-timeLocalDataGuardEnabled"></a>
The date and time when local Oracle Data Guard was enabled for the Autonomous Database.
Type: Timestamp
Required: No

 ** timeMaintenanceBegin **   <a name="odb-Type-AutonomousDatabase-timeMaintenanceBegin"></a>
The date and time when the next maintenance of the Autonomous Database begins.
Type: Timestamp
Required: No

 ** timeMaintenanceEnd **   <a name="odb-Type-AutonomousDatabase-timeMaintenanceEnd"></a>
The date and time when the next maintenance of the Autonomous Database ends.
Type: Timestamp
Required: No

 ** timeOfAutoRefreshStart **   <a name="odb-Type-AutonomousDatabase-timeOfAutoRefreshStart"></a>
The date and time at which the automatic refresh of the refreshable clone Autonomous Database starts.
Type: Timestamp
Required: No

 ** timeOfLastBackup **   <a name="odb-Type-AutonomousDatabase-timeOfLastBackup"></a>
The date and time of the last backup of the Autonomous Database.
Type: Timestamp
Required: No

 ** timeOfLastFailover **   <a name="odb-Type-AutonomousDatabase-timeOfLastFailover"></a>
The date and time of the last failover operation for the Autonomous Database.
Type: Timestamp
Required: No

 ** timeOfLastRefresh **   <a name="odb-Type-AutonomousDatabase-timeOfLastRefresh"></a>
The date and time of the last refresh of the refreshable clone Autonomous Database.
Type: Timestamp
Required: No

 ** timeOfLastRefreshPoint **   <a name="odb-Type-AutonomousDatabase-timeOfLastRefreshPoint"></a>
The date and time as of which the data in the refreshable clone Autonomous Database is current.
Type: Timestamp
Required: No

 ** timeOfLastSwitchover **   <a name="odb-Type-AutonomousDatabase-timeOfLastSwitchover"></a>
The date and time of the last switchover operation for the Autonomous Database.
Type: Timestamp
Required: No

 ** timeOfNextRefresh **   <a name="odb-Type-AutonomousDatabase-timeOfNextRefresh"></a>
The date and time of the next scheduled refresh of the refreshable clone Autonomous Database.
Type: Timestamp
Required: No

 ** timeReclamationOfFreeAutonomousDatabase **   <a name="odb-Type-AutonomousDatabase-timeReclamationOfFreeAutonomousDatabase"></a>
The date and time when the Always Free Autonomous Database is scheduled to be stopped because of inactivity.
Type: Timestamp
Required: No

 ** timeUndeleted **   <a name="odb-Type-AutonomousDatabase-timeUndeleted"></a>
The date and time when the Autonomous Database was restored after deletion.
Type: Timestamp
Required: No

 ** timeUntilReconnectCloneEnabled **   <a name="odb-Type-AutonomousDatabase-timeUntilReconnectCloneEnabled"></a>
The date and time until which reconnecting the refreshable clone to its source Autonomous Database is allowed.
Type: Timestamp
Required: No

 ** totalBackupStorageSizeInGBs **   <a name="odb-Type-AutonomousDatabase-totalBackupStorageSizeInGBs"></a>
The total amount of backup storage used by the Autonomous Database, in GB.
Type: Double
Required: No

 ** usedDataStorageSizeInGBs **   <a name="odb-Type-AutonomousDatabase-usedDataStorageSizeInGBs"></a>
The amount of data storage currently in use by the Autonomous Database, in GB.
Type: Integer
Required: No

 ** usedDataStorageSizeInTBs **   <a name="odb-Type-AutonomousDatabase-usedDataStorageSizeInTBs"></a>
The amount of data storage currently in use by the Autonomous Database, in TB.
Type: Double
Required: No

## See Also
<a name="API_AutonomousDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AutonomousDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AutonomousDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AutonomousDatabase)
