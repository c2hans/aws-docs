---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBInstance
<a name="aws-resource-rds-dbinstance"></a>

The `AWS::RDS::DBInstance` resource creates an Amazon DB instance. The new DB instance can be an RDS DB instance, or it can be a DB instance in an Aurora DB cluster.

For more information about creating an RDS DB instance, see [Creating an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) in the *Amazon RDS User Guide*.

For more information about creating a DB instance in an Aurora DB cluster, see [ Creating an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the *Amazon Aurora User Guide*.

If you import an existing DB instance, and the template configuration doesn't match the actual configuration of the DB instance, AWS CloudFormation applies the changes in the template during the import operation.

**Important**
If a DB instance is deleted or replaced during an update, AWS CloudFormation deletes all automated snapshots. However, it retains manual DB snapshots. During an update that requires replacement, you can apply a stack policy to prevent DB instances from being replaced. For more information, see [Prevent Updates to Stack Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html).

 **Updating DB instances**

When properties labeled "*Update requires:*[Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)" are updated, AWS CloudFormation first creates a replacement DB instance, then changes references from other dependent resources to point to the replacement DB instance, and finally deletes the old DB instance.

**Important**
We highly recommend that you take a snapshot of the database before updating the stack. If you don't, you lose the data when AWS CloudFormation replaces your DB instance. To preserve your data, perform the following procedure:
Deactivate any applications that are using the DB instance so that there's no activity on the DB instance.
Create a snapshot of the DB instance. For more information, see [Creating a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html).
If you want to restore your instance using a DB snapshot, modify the updated template with your DB instance changes and add the `DBSnapshotIdentifier` property with the ID of the DB snapshot that you want to use.
After you restore a DB instance with a `DBSnapshotIdentifier` property, you can delete the `DBSnapshotIdentifier` property. When you specify this property for an update, the DB instance is not restored from the DB snapshot again, and the data in the database is not changed. If you specify a different `DBSnapshotIdentifier` value, a new DB instance is restored from the specified snapshot, and the original DB instance is deleted.
Update the stack.

For more information about updating other properties of this resource, see ` [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) `. For more information about updating stacks, see [AWS CloudFormation Stacks Updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html).

 **Deleting DB instances**

For DB instances that are part of an Aurora DB cluster, you can set a deletion policy for your DB instance to control how AWS CloudFormation handles the DB instance when the stack is deleted. For Amazon RDS DB instances, you can choose to *retain* the DB instance, to *delete* the DB instance, or to *create a snapshot* of the DB instance. The default AWS CloudFormation behavior depends on the `DBClusterIdentifier` property:

1. For `AWS::RDS::DBInstance` resources that don't specify the `DBClusterIdentifier` property, AWS CloudFormation saves a snapshot of the DB instance.

1.  For `AWS::RDS::DBInstance` resources that do specify the `DBClusterIdentifier` property, AWS CloudFormation deletes the DB instance.

 For more information, see [DeletionPolicy Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

## Syntax
<a name="aws-resource-rds-dbinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbinstance-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBInstance",
  "Properties" : {
      "[AdditionalStorageVolumes](#cfn-rds-dbinstance-additionalstoragevolumes)" : {{[ AdditionalStorageVolume, ... ]}},
      "[AllocatedStorage](#cfn-rds-dbinstance-allocatedstorage)" : {{String}},
      "[AllowMajorVersionUpgrade](#cfn-rds-dbinstance-allowmajorversionupgrade)" : {{Boolean}},
      "[ApplyImmediately](#cfn-rds-dbinstance-applyimmediately)" : {{Boolean}},
      "[AssociatedRoles](#cfn-rds-dbinstance-associatedroles)" : {{[ DBInstanceRole, ... ]}},
      "[AutomaticBackupReplicationKmsKeyId](#cfn-rds-dbinstance-automaticbackupreplicationkmskeyid)" : {{String}},
      "[AutomaticBackupReplicationRegion](#cfn-rds-dbinstance-automaticbackupreplicationregion)" : {{String}},
      "[AutomaticBackupReplicationRetentionPeriod](#cfn-rds-dbinstance-automaticbackupreplicationretentionperiod)" : {{Integer}},
      "[AutoMinorVersionUpgrade](#cfn-rds-dbinstance-autominorversionupgrade)" : {{Boolean}},
      "[AvailabilityZone](#cfn-rds-dbinstance-availabilityzone)" : {{String}},
      "[BackupRetentionPeriod](#cfn-rds-dbinstance-backupretentionperiod)" : {{Integer}},
      "[BackupTarget](#cfn-rds-dbinstance-backuptarget)" : {{String}},
      "[CACertificateIdentifier](#cfn-rds-dbinstance-cacertificateidentifier)" : {{String}},
      "[CertificateRotationRestart](#cfn-rds-dbinstance-certificaterotationrestart)" : {{Boolean}},
      "[CharacterSetName](#cfn-rds-dbinstance-charactersetname)" : {{String}},
      "[CopyTagsToSnapshot](#cfn-rds-dbinstance-copytagstosnapshot)" : {{Boolean}},
      "[CustomIAMInstanceProfile](#cfn-rds-dbinstance-customiaminstanceprofile)" : {{String}},
      "[DatabaseInsightsMode](#cfn-rds-dbinstance-databaseinsightsmode)" : {{String}},
      "[DBClusterIdentifier](#cfn-rds-dbinstance-dbclusteridentifier)" : {{String}},
      "[DBClusterSnapshotIdentifier](#cfn-rds-dbinstance-dbclustersnapshotidentifier)" : {{String}},
      "[DBInstanceClass](#cfn-rds-dbinstance-dbinstanceclass)" : {{String}},
      "[DBInstanceIdentifier](#cfn-rds-dbinstance-dbinstanceidentifier)" : {{String}},
      "[DBName](#cfn-rds-dbinstance-dbname)" : {{String}},
      "[DBParameterGroupName](#cfn-rds-dbinstance-dbparametergroupname)" : {{String}},
      "[DBSecurityGroups](#cfn-rds-dbinstance-dbsecuritygroups)" : {{[ String, ... ]}},
      "[DBSnapshotIdentifier](#cfn-rds-dbinstance-dbsnapshotidentifier)" : {{String}},
      "[DBSubnetGroupName](#cfn-rds-dbinstance-dbsubnetgroupname)" : {{String}},
      "[DBSystemId](#cfn-rds-dbinstance-dbsystemid)" : {{String}},
      "[DedicatedLogVolume](#cfn-rds-dbinstance-dedicatedlogvolume)" : {{Boolean}},
      "[DeleteAutomatedBackups](#cfn-rds-dbinstance-deleteautomatedbackups)" : {{Boolean}},
      "[DeletionProtection](#cfn-rds-dbinstance-deletionprotection)" : {{Boolean}},
      "[Domain](#cfn-rds-dbinstance-domain)" : {{String}},
      "[DomainAuthSecretArn](#cfn-rds-dbinstance-domainauthsecretarn)" : {{String}},
      "[DomainDnsIps](#cfn-rds-dbinstance-domaindnsips)" : {{[ String, ... ]}},
      "[DomainFqdn](#cfn-rds-dbinstance-domainfqdn)" : {{String}},
      "[DomainIAMRoleName](#cfn-rds-dbinstance-domainiamrolename)" : {{String}},
      "[DomainOu](#cfn-rds-dbinstance-domainou)" : {{String}},
      "[EnableCloudwatchLogsExports](#cfn-rds-dbinstance-enablecloudwatchlogsexports)" : {{[ String, ... ]}},
      "[EnableIAMDatabaseAuthentication](#cfn-rds-dbinstance-enableiamdatabaseauthentication)" : {{Boolean}},
      "[EnablePerformanceInsights](#cfn-rds-dbinstance-enableperformanceinsights)" : {{Boolean}},
      "[Engine](#cfn-rds-dbinstance-engine)" : {{String}},
      "[EngineLifecycleSupport](#cfn-rds-dbinstance-enginelifecyclesupport)" : {{String}},
      "[EngineVersion](#cfn-rds-dbinstance-engineversion)" : {{String}},
      "[Iops](#cfn-rds-dbinstance-iops)" : {{Integer}},
      "[KmsKeyId](#cfn-rds-dbinstance-kmskeyid)" : {{String}},
      "[LicenseModel](#cfn-rds-dbinstance-licensemodel)" : {{String}},
      "[ManageMasterUserPassword](#cfn-rds-dbinstance-managemasteruserpassword)" : {{Boolean}},
      "[MasterUserAuthenticationType](#cfn-rds-dbinstance-masteruserauthenticationtype)" : {{String}},
      "[MasterUsername](#cfn-rds-dbinstance-masterusername)" : {{String}},
      "[MasterUserPassword](#cfn-rds-dbinstance-masteruserpassword)" : {{String}},
      "[MasterUserSecret](#cfn-rds-dbinstance-masterusersecret)" : {{MasterUserSecret}},
      "[MaxAllocatedStorage](#cfn-rds-dbinstance-maxallocatedstorage)" : {{Integer}},
      "[MonitoringInterval](#cfn-rds-dbinstance-monitoringinterval)" : {{Integer}},
      "[MonitoringRoleArn](#cfn-rds-dbinstance-monitoringrolearn)" : {{String}},
      "[MultiAZ](#cfn-rds-dbinstance-multiaz)" : {{Boolean}},
      "[NcharCharacterSetName](#cfn-rds-dbinstance-ncharcharactersetname)" : {{String}},
      "[NetworkType](#cfn-rds-dbinstance-networktype)" : {{String}},
      "[OptionGroupName](#cfn-rds-dbinstance-optiongroupname)" : {{String}},
      "[PerformanceInsightsKMSKeyId](#cfn-rds-dbinstance-performanceinsightskmskeyid)" : {{String}},
      "[PerformanceInsightsRetentionPeriod](#cfn-rds-dbinstance-performanceinsightsretentionperiod)" : {{Integer}},
      "[Port](#cfn-rds-dbinstance-port)" : {{String}},
      "[PreferredBackupWindow](#cfn-rds-dbinstance-preferredbackupwindow)" : {{String}},
      "[PreferredMaintenanceWindow](#cfn-rds-dbinstance-preferredmaintenancewindow)" : {{String}},
      "[ProcessorFeatures](#cfn-rds-dbinstance-processorfeatures)" : {{[ ProcessorFeature, ... ]}},
      "[PromotionTier](#cfn-rds-dbinstance-promotiontier)" : {{Integer}},
      "[PubliclyAccessible](#cfn-rds-dbinstance-publiclyaccessible)" : {{Boolean}},
      "[ReplicaMode](#cfn-rds-dbinstance-replicamode)" : {{String}},
      "[RestoreTime](#cfn-rds-dbinstance-restoretime)" : {{String}},
      "[SourceDBClusterIdentifier](#cfn-rds-dbinstance-sourcedbclusteridentifier)" : {{String}},
      "[SourceDBInstanceAutomatedBackupsArn](#cfn-rds-dbinstance-sourcedbinstanceautomatedbackupsarn)" : {{String}},
      "[SourceDBInstanceIdentifier](#cfn-rds-dbinstance-sourcedbinstanceidentifier)" : {{String}},
      "[SourceDbiResourceId](#cfn-rds-dbinstance-sourcedbiresourceid)" : {{String}},
      "[SourceRegion](#cfn-rds-dbinstance-sourceregion)" : {{String}},
      "[StorageEncrypted](#cfn-rds-dbinstance-storageencrypted)" : {{Boolean}},
      "[StorageThroughput](#cfn-rds-dbinstance-storagethroughput)" : {{Integer}},
      "[StorageType](#cfn-rds-dbinstance-storagetype)" : {{String}},
      "[Tags](#cfn-rds-dbinstance-tags)" : {{[ Tag, ... ]}},
      "[Timezone](#cfn-rds-dbinstance-timezone)" : {{String}},
      "[UseDefaultProcessorFeatures](#cfn-rds-dbinstance-usedefaultprocessorfeatures)" : {{Boolean}},
      "[UseLatestRestorableTime](#cfn-rds-dbinstance-uselatestrestorabletime)" : {{Boolean}},
      "[VPCSecurityGroups](#cfn-rds-dbinstance-vpcsecuritygroups)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbinstance-syntax.yaml"></a>

```
Type: AWS::RDS::DBInstance
Properties:
  [AdditionalStorageVolumes](#cfn-rds-dbinstance-additionalstoragevolumes): {{
    - AdditionalStorageVolume}}
  [AllocatedStorage](#cfn-rds-dbinstance-allocatedstorage): {{String}}
  [AllowMajorVersionUpgrade](#cfn-rds-dbinstance-allowmajorversionupgrade): {{Boolean}}
  [ApplyImmediately](#cfn-rds-dbinstance-applyimmediately): {{Boolean}}
  [AssociatedRoles](#cfn-rds-dbinstance-associatedroles): {{
    - DBInstanceRole}}
  [AutomaticBackupReplicationKmsKeyId](#cfn-rds-dbinstance-automaticbackupreplicationkmskeyid): {{String}}
  [AutomaticBackupReplicationRegion](#cfn-rds-dbinstance-automaticbackupreplicationregion): {{String}}
  [AutomaticBackupReplicationRetentionPeriod](#cfn-rds-dbinstance-automaticbackupreplicationretentionperiod): {{Integer}}
  [AutoMinorVersionUpgrade](#cfn-rds-dbinstance-autominorversionupgrade): {{Boolean}}
  [AvailabilityZone](#cfn-rds-dbinstance-availabilityzone): {{String}}
  [BackupRetentionPeriod](#cfn-rds-dbinstance-backupretentionperiod): {{Integer}}
  [BackupTarget](#cfn-rds-dbinstance-backuptarget): {{String}}
  [CACertificateIdentifier](#cfn-rds-dbinstance-cacertificateidentifier): {{String}}
  [CertificateRotationRestart](#cfn-rds-dbinstance-certificaterotationrestart): {{Boolean}}
  [CharacterSetName](#cfn-rds-dbinstance-charactersetname): {{String}}
  [CopyTagsToSnapshot](#cfn-rds-dbinstance-copytagstosnapshot): {{Boolean}}
  [CustomIAMInstanceProfile](#cfn-rds-dbinstance-customiaminstanceprofile): {{String}}
  [DatabaseInsightsMode](#cfn-rds-dbinstance-databaseinsightsmode): {{String}}
  [DBClusterIdentifier](#cfn-rds-dbinstance-dbclusteridentifier): {{String}}
  [DBClusterSnapshotIdentifier](#cfn-rds-dbinstance-dbclustersnapshotidentifier): {{String}}
  [DBInstanceClass](#cfn-rds-dbinstance-dbinstanceclass): {{String}}
  [DBInstanceIdentifier](#cfn-rds-dbinstance-dbinstanceidentifier): {{String}}
  [DBName](#cfn-rds-dbinstance-dbname): {{String}}
  [DBParameterGroupName](#cfn-rds-dbinstance-dbparametergroupname): {{String}}
  [DBSecurityGroups](#cfn-rds-dbinstance-dbsecuritygroups): {{
    - String}}
  [DBSnapshotIdentifier](#cfn-rds-dbinstance-dbsnapshotidentifier): {{String}}
  [DBSubnetGroupName](#cfn-rds-dbinstance-dbsubnetgroupname): {{String}}
  [DBSystemId](#cfn-rds-dbinstance-dbsystemid): {{String}}
  [DedicatedLogVolume](#cfn-rds-dbinstance-dedicatedlogvolume): {{Boolean}}
  [DeleteAutomatedBackups](#cfn-rds-dbinstance-deleteautomatedbackups): {{Boolean}}
  [DeletionProtection](#cfn-rds-dbinstance-deletionprotection): {{Boolean}}
  [Domain](#cfn-rds-dbinstance-domain): {{String}}
  [DomainAuthSecretArn](#cfn-rds-dbinstance-domainauthsecretarn): {{String}}
  [DomainDnsIps](#cfn-rds-dbinstance-domaindnsips): {{
    - String}}
  [DomainFqdn](#cfn-rds-dbinstance-domainfqdn): {{String}}
  [DomainIAMRoleName](#cfn-rds-dbinstance-domainiamrolename): {{String}}
  [DomainOu](#cfn-rds-dbinstance-domainou): {{String}}
  [EnableCloudwatchLogsExports](#cfn-rds-dbinstance-enablecloudwatchlogsexports): {{
    - String}}
  [EnableIAMDatabaseAuthentication](#cfn-rds-dbinstance-enableiamdatabaseauthentication): {{Boolean}}
  [EnablePerformanceInsights](#cfn-rds-dbinstance-enableperformanceinsights): {{Boolean}}
  [Engine](#cfn-rds-dbinstance-engine): {{String}}
  [EngineLifecycleSupport](#cfn-rds-dbinstance-enginelifecyclesupport): {{String}}
  [EngineVersion](#cfn-rds-dbinstance-engineversion): {{String}}
  [Iops](#cfn-rds-dbinstance-iops): {{Integer}}
  [KmsKeyId](#cfn-rds-dbinstance-kmskeyid): {{String}}
  [LicenseModel](#cfn-rds-dbinstance-licensemodel): {{String}}
  [ManageMasterUserPassword](#cfn-rds-dbinstance-managemasteruserpassword): {{Boolean}}
  [MasterUserAuthenticationType](#cfn-rds-dbinstance-masteruserauthenticationtype): {{String}}
  [MasterUsername](#cfn-rds-dbinstance-masterusername): {{String}}
  [MasterUserPassword](#cfn-rds-dbinstance-masteruserpassword): {{String}}
  [MasterUserSecret](#cfn-rds-dbinstance-masterusersecret): {{
    MasterUserSecret}}
  [MaxAllocatedStorage](#cfn-rds-dbinstance-maxallocatedstorage): {{Integer}}
  [MonitoringInterval](#cfn-rds-dbinstance-monitoringinterval): {{Integer}}
  [MonitoringRoleArn](#cfn-rds-dbinstance-monitoringrolearn): {{String}}
  [MultiAZ](#cfn-rds-dbinstance-multiaz): {{Boolean}}
  [NcharCharacterSetName](#cfn-rds-dbinstance-ncharcharactersetname): {{String}}
  [NetworkType](#cfn-rds-dbinstance-networktype): {{String}}
  [OptionGroupName](#cfn-rds-dbinstance-optiongroupname): {{String}}
  [PerformanceInsightsKMSKeyId](#cfn-rds-dbinstance-performanceinsightskmskeyid): {{String}}
  [PerformanceInsightsRetentionPeriod](#cfn-rds-dbinstance-performanceinsightsretentionperiod): {{Integer}}
  [Port](#cfn-rds-dbinstance-port): {{String}}
  [PreferredBackupWindow](#cfn-rds-dbinstance-preferredbackupwindow): {{String}}
  [PreferredMaintenanceWindow](#cfn-rds-dbinstance-preferredmaintenancewindow): {{String}}
  [ProcessorFeatures](#cfn-rds-dbinstance-processorfeatures): {{
    - ProcessorFeature}}
  [PromotionTier](#cfn-rds-dbinstance-promotiontier): {{Integer}}
  [PubliclyAccessible](#cfn-rds-dbinstance-publiclyaccessible): {{Boolean}}
  [ReplicaMode](#cfn-rds-dbinstance-replicamode): {{String}}
  [RestoreTime](#cfn-rds-dbinstance-restoretime): {{String}}
  [SourceDBClusterIdentifier](#cfn-rds-dbinstance-sourcedbclusteridentifier): {{String}}
  [SourceDBInstanceAutomatedBackupsArn](#cfn-rds-dbinstance-sourcedbinstanceautomatedbackupsarn): {{String}}
  [SourceDBInstanceIdentifier](#cfn-rds-dbinstance-sourcedbinstanceidentifier): {{String}}
  [SourceDbiResourceId](#cfn-rds-dbinstance-sourcedbiresourceid): {{String}}
  [SourceRegion](#cfn-rds-dbinstance-sourceregion): {{String}}
  [StorageEncrypted](#cfn-rds-dbinstance-storageencrypted): {{Boolean}}
  [StorageThroughput](#cfn-rds-dbinstance-storagethroughput): {{Integer}}
  [StorageType](#cfn-rds-dbinstance-storagetype): {{String}}
  [Tags](#cfn-rds-dbinstance-tags): {{
    - Tag}}
  [Timezone](#cfn-rds-dbinstance-timezone): {{String}}
  [UseDefaultProcessorFeatures](#cfn-rds-dbinstance-usedefaultprocessorfeatures): {{Boolean}}
  [UseLatestRestorableTime](#cfn-rds-dbinstance-uselatestrestorabletime): {{Boolean}}
  [VPCSecurityGroups](#cfn-rds-dbinstance-vpcsecuritygroups): {{
    - String}}
```

## Properties
<a name="aws-resource-rds-dbinstance-properties"></a>

`AdditionalStorageVolumes`  <a name="cfn-rds-dbinstance-additionalstoragevolumes"></a>
The additional storage volumes associated with the DB instance. RDS supports additional storage volumes for RDS for Oracle and RDS for SQL Server.
*Required*: No
*Type*: Array of [AdditionalStorageVolume](aws-properties-rds-dbinstance-additionalstoragevolume.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllocatedStorage`  <a name="cfn-rds-dbinstance-allocatedstorage"></a>
The amount of storage in gibibytes (GiB) to be initially allocated for the database instance.
If any value is set in the `Iops` parameter, `AllocatedStorage` must be at least 100 GiB, which corresponds to the minimum Iops value of 1,000. If you increase the `Iops` value (in 1,000 IOPS increments), then you must also increase the `AllocatedStorage` value (in 100-GiB increments).
 **Amazon Aurora**
Not applicable. Aurora cluster volumes automatically grow as the amount of data in your database increases, though you are only charged for the space that you use in an Aurora cluster volume.
 **Db2**
Constraints to the amount of storage for each storage type are the following:
+ General Purpose (SSD) storage (gp3): Must be an integer from 20 to 64000.
+ Provisioned IOPS storage (io1): Must be an integer from 100 to 64000.
 **MySQL**
Constraints to the amount of storage for each storage type are the following:
+ General Purpose (SSD) storage (gp2): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1): Must be an integer from 100 to 65536.
+ Magnetic storage (standard): Must be an integer from 5 to 3072.
 **MariaDB**
Constraints to the amount of storage for each storage type are the following:
+ General Purpose (SSD) storage (gp2): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1): Must be an integer from 100 to 65536.
+ Magnetic storage (standard): Must be an integer from 5 to 3072.
 **PostgreSQL**
Constraints to the amount of storage for each storage type are the following:
+ General Purpose (SSD) storage (gp2): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1): Must be an integer from 100 to 65536.
+ Magnetic storage (standard): Must be an integer from 5 to 3072.
 **Oracle**
Constraints to the amount of storage for each storage type are the following:
+ General Purpose (SSD) storage (gp2): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1): Must be an integer from 100 to 65536.
+ Magnetic storage (standard): Must be an integer from 10 to 3072.
 **SQL Server**
Constraints to the amount of storage for each storage type are the following:
+ General Purpose (SSD) storage (gp2):
  + Enterprise and Standard editions: Must be an integer from 20 to 16384.
  + Web and Express editions: Must be an integer from 20 to 16384.
+ Provisioned IOPS storage (io1):
  + Enterprise and Standard editions: Must be an integer from 20 to 16384.
  + Web and Express editions: Must be an integer from 20 to 16384.
+ Magnetic storage (standard):
  + Enterprise and Standard editions: Must be an integer from 20 to 1024.
  + Web and Express editions: Must be an integer from 20 to 1024.
*Required*: Conditional
*Type*: String
*Pattern*: `^[0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowMajorVersionUpgrade`  <a name="cfn-rds-dbinstance-allowmajorversionupgrade"></a>
A value that indicates whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.
Constraints: Major version upgrades must be allowed when specifying a value for the `EngineVersion` parameter that is a different major version than the DB instance's current version.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplyImmediately`  <a name="cfn-rds-dbinstance-applyimmediately"></a>
Specifies whether changes to the DB instance and any pending modifications are applied immediately, regardless of the `PreferredMaintenanceWindow` setting. If set to `false`, changes are applied during the next maintenance window. Until RDS applies the changes, the DB instance remains in a drift state. As a result, the configuration doesn't fully reflect the requested modifications and temporarily diverges from the intended state.
In addition to the settings described in [Modifying a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html), this property also determines whether the DB instance reboots when a static parameter is modified in the associated DB parameter group.
Default: `true`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociatedRoles`  <a name="cfn-rds-dbinstance-associatedroles"></a>
 The AWS Identity and Access Management (IAM) roles associated with the DB instance.
 **Amazon Aurora**
Not applicable. The associated roles are managed by the DB cluster.
*Required*: No
*Type*: Array of [DBInstanceRole](aws-properties-rds-dbinstance-dbinstancerole.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomaticBackupReplicationKmsKeyId`  <a name="cfn-rds-dbinstance-automaticbackupreplicationkmskeyid"></a>
The AWS KMS key identifier for encryption of the replicated automated backups. The KMS key ID is the Amazon Resource Name (ARN) for the KMS encryption key in the destination AWS Region, for example, `arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomaticBackupReplicationRegion`  <a name="cfn-rds-dbinstance-automaticbackupreplicationregion"></a>
The AWS Region associated with the automated backup.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomaticBackupReplicationRetentionPeriod`  <a name="cfn-rds-dbinstance-automaticbackupreplicationretentionperiod"></a>
The retention period for automated backups in a different AWS Region. Use this parameter to set a unique retention period that only applies to cross-Region automated backups. To enable automated backups in a different Region, specify a positive value for the `AutomaticBackupReplicationRegion` parameter.
If not specified, this parameter defaults to the value of the `BackupRetentionPeriod` parameter. The maximum allowed value is 35.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoMinorVersionUpgrade`  <a name="cfn-rds-dbinstance-autominorversionupgrade"></a>
A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`AvailabilityZone`  <a name="cfn-rds-dbinstance-availabilityzone"></a>
The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones, see [Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).
For Amazon Aurora, each Aurora DB cluster hosts copies of its storage in three separate Availability Zones. Specify one of these Availability Zones. Aurora automatically chooses an appropriate Availability Zone if you don't specify one.
Default: A random, system-chosen Availability Zone in the endpoint's AWS Region.
Constraints:
+ The `AvailabilityZone` parameter can't be specified if the DB instance is a Multi-AZ deployment.
+ The specified Availability Zone must be in the same AWS Region as the current endpoint.
Example: `us-east-1d`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`BackupRetentionPeriod`  <a name="cfn-rds-dbinstance-backupretentionperiod"></a>
The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
 **Amazon Aurora**
Not applicable. The retention period for automated backups is managed by the DB cluster.
Default: 1
Constraints:
+ Must be a value from 0 to 35
+ Can't be set to 0 if the DB instance is a source to read replicas
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`BackupTarget`  <a name="cfn-rds-dbinstance-backuptarget"></a>
The location for storing automated backups and manual snapshots.
Valid Values:
+ `local` (Dedicated Local Zone)
+ `outposts` (AWS Outposts)
+ `region` (AWS Region)
Default: `region`
For more information, see [Working with Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CACertificateIdentifier`  <a name="cfn-rds-dbinstance-cacertificateidentifier"></a>
The identifier of the CA certificate for this DB instance.
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateRotationRestart`  <a name="cfn-rds-dbinstance-certificaterotationrestart"></a>
Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.
By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.
Set this parameter only if you are *not* using SSL/TLS to connect to the DB instance.
If you are using SSL/TLS to connect to the DB instance, follow the appropriate instructions for your DB engine to rotate your SSL/TLS certificate:
+ For more information about rotating your SSL/TLS certificate for RDS DB engines, see [ Rotating Your SSL/TLS Certificate.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html) in the *Amazon RDS User Guide.*
+ For more information about rotating your SSL/TLS certificate for Aurora DB engines, see [ Rotating Your SSL/TLS Certificate](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html) in the *Amazon Aurora User Guide*.
This setting doesn't apply to RDS Custom DB instances.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CharacterSetName`  <a name="cfn-rds-dbinstance-charactersetname"></a>
For supported engines, indicates that the DB instance should be associated with the specified character set.
 **Amazon Aurora**
Not applicable. The character set is managed by the DB cluster. For more information, see [AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CopyTagsToSnapshot`  <a name="cfn-rds-dbinstance-copytagstosnapshot"></a>
Specifies whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
This setting doesn't apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomIAMInstanceProfile`  <a name="cfn-rds-dbinstance-customiaminstanceprofile"></a>
The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance.
This setting is required for RDS Custom.
Constraints:
+ The profile must exist in your account.
+ The profile must have an IAM role that Amazon EC2 has permissions to assume.
+ The instance profile name and the associated IAM role name must start with the prefix `AWSRDSCustom`.
For the list of permissions required for the IAM role, see [ Configure IAM and your VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseInsightsMode`  <a name="cfn-rds-dbinstance-databaseinsightsmode"></a>
The mode of Database Insights to enable for the DB instance.
Aurora DB instances inherit this value from the DB cluster, so you can't change this value.
*Required*: No
*Type*: String
*Allowed values*: `standard | advanced`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBClusterIdentifier`  <a name="cfn-rds-dbinstance-dbclusteridentifier"></a>
The identifier of the DB cluster that this DB instance will belong to.
This setting doesn't apply to RDS Custom DB instances.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBClusterSnapshotIdentifier`  <a name="cfn-rds-dbinstance-dbclustersnapshotidentifier"></a>
The identifier for the Multi-AZ DB cluster snapshot to restore from.
For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.
Constraints:
+ Must match the identifier of an existing Multi-AZ DB cluster snapshot.
+ Can't be specified when `DBSnapshotIdentifier` is specified.
+ Must be specified when `DBSnapshotIdentifier` isn't specified.
+ If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the `DBClusterSnapshotIdentifier` must be the ARN of the shared snapshot.
+ Can't be the identifier of an Aurora DB cluster snapshot.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DBInstanceClass`  <a name="cfn-rds-dbinstance-dbinstanceclass"></a>
The compute and memory capacity of the DB instance, for example `db.m5.large`. Not all DB instance classes are available in all AWS Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide* or [Aurora DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) in the *Amazon Aurora User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DBInstanceIdentifier`  <a name="cfn-rds-dbinstance-dbinstanceidentifier"></a>
A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance. For more information, see [Name Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
For information about constraints that apply to DB instance identifiers, see [Naming constraints in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.Constraints) in the *Amazon RDS User Guide*.
If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
*Required*: No
*Type*: String
*Pattern*: `^$|^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBName`  <a name="cfn-rds-dbinstance-dbname"></a>
The meaning of this parameter differs according to the database engine you use.
If you specify the ` [ DBSnapshotIdentifier](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsnapshotidentifier) ` property, this property only applies to RDS for Oracle.
 **Amazon Aurora**
Not applicable. The database name is managed by the DB cluster.
 **Db2**
The name of the database to create when the DB instance is created. If this parameter isn't specified, no database is created in the DB instance.
Constraints:
+ Must contain 1 to 64 letters or numbers.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
+ Can't be a word reserved by the specified database engine.
 **MySQL**
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance.
Constraints:
+ Must contain 1 to 64 letters or numbers.
+ Can't be a word reserved by the specified database engine
 **MariaDB**
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance.
Constraints:
+ Must contain 1 to 64 letters or numbers.
+ Can't be a word reserved by the specified database engine
 **PostgreSQL**
The name of the database to create when the DB instance is created. If this parameter is not specified, the default `postgres` database is created in the DB instance.
Constraints:
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
+ Must contain 1 to 63 characters.
+ Can't be a word reserved by the specified database engine
 **Oracle**
The Oracle System ID (SID) of the created DB instance. If you specify `null`, the default value `ORCL` is used. You can't specify the string NULL, or any other reserved word, for `DBName`.
Default: `ORCL`
Constraints:
+ Can't be longer than 8 characters
 **SQL Server**
Not applicable. Must be null.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBParameterGroupName`  <a name="cfn-rds-dbinstance-dbparametergroupname"></a>
The name of an existing DB parameter group or a reference to an [AWS::RDS::DBParameterGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html) resource created in the template.
To list all of the available DB parameter group names, use the following command:
 `aws rds describe-db-parameter-groups --query "DBParameterGroups[].DBParameterGroupName" --output text`
If any of the data members of the referenced parameter group are changed during an update, the DB instance might need to be restarted, which causes some interruption. If the parameter group contains static parameters, whether they were changed or not, an update triggers a reboot.
If you don't specify a value for `DBParameterGroupName` property, the default DB parameter group for the specified engine and engine version is used.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DBSecurityGroups`  <a name="cfn-rds-dbinstance-dbsecuritygroups"></a>
A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.
 If you set DBSecurityGroups, you must not set VPCSecurityGroups, and vice versa. Also, note that the DBSecurityGroups property exists only for backwards compatibility with older regions and is no longer recommended for providing security information to an RDS DB instance. Instead, use VPCSecurityGroups.
If you specify this property, AWS CloudFormation sends only the following properties (if specified) to Amazon RDS during create operations:
+  `AllocatedStorage`
+  `AutoMinorVersionUpgrade`
+  `AvailabilityZone`
+  `BackupRetentionPeriod`
+  `CharacterSetName`
+  `DBInstanceClass`
+  `DBName`
+  `DBParameterGroupName`
+  `DBSecurityGroups`
+  `DBSubnetGroupName`
+  `Engine`
+  `EngineVersion`
+  `Iops`
+  `LicenseModel`
+  `MasterUsername`
+  `MasterUserPassword`
+  `MultiAZ`
+  `OptionGroupName`
+  `PreferredBackupWindow`
+  `PreferredMaintenanceWindow`
All other properties are ignored. Specify a virtual private cloud (VPC) security group if you want to submit other properties, such as `StorageType`, `StorageEncrypted`, or `KmsKeyId`. If you're already using the `DBSecurityGroups` property, you can't use these other properties by updating your DB instance to use a VPC security group. You must recreate the DB instance.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBSnapshotIdentifier`  <a name="cfn-rds-dbinstance-dbsnapshotidentifier"></a>
The name or Amazon Resource Name (ARN) of the DB snapshot that's used to restore the DB instance. If you're restoring from a shared manual DB snapshot, you must specify the ARN of the snapshot.
By specifying this property, you can create a DB instance from the specified DB snapshot. If the `DBSnapshotIdentifier` property is an empty string or the `AWS::RDS::DBInstance` declaration has no `DBSnapshotIdentifier` property, AWS CloudFormation creates a new database. If the property contains a value (other than an empty string), AWS CloudFormation creates a database from the specified snapshot. If a snapshot with the specified name doesn't exist, AWS CloudFormation can't create the database and it rolls back the stack.
Some DB instance properties aren't valid when you restore from a snapshot, such as the `MasterUsername` and `MasterUserPassword` properties, and the point-in-time recovery properties `RestoreTime` and `UseLatestRestorableTime`. For information about the properties that you can specify, see the [`RestoreDBInstanceFromDBSnapshot`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html) action in the *Amazon RDS API Reference*.
When you specify the same `DBSnapshotIdentifier` property value for an update, the DB instance is not restored from the DB snapshot again, and the data in the database is not changed. If you specify a different `DBSnapshotIdentifier` value, a new DB instance is restored from the specified snapshot, and the original DB instance is deleted.
If you specify the `DBSnapshotIdentifier` property to restore a DB instance (as opposed to specifying it for DB instance updates), then don't specify the following properties:
+  `CharacterSetName`
+  `DBClusterIdentifier`
+  `DBName`
+  `KmsKeyId`
+  `MasterUsername`
+  `MasterUserPassword`
+  `PromotionTier`
+  `SourceDBInstanceIdentifier`
+  `SourceRegion`
+ `StorageEncrypted` (for an unencrypted snapshot)
+  `Timezone`
 **Amazon Aurora**
Not applicable. Snapshot restore is managed by the DB cluster.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DBSubnetGroupName`  <a name="cfn-rds-dbinstance-dbsubnetgroupname"></a>
A DB subnet group to associate with the DB instance. If you update this value, the new subnet group must be a subnet group in a new VPC.
If you don't specify a DB subnet group, RDS uses the default DB subnet group if one exists. If a default DB subnet group does not exist, and you don't specify a `DBSubnetGroupName`, the DB instance fails to launch.
For more information about using Amazon RDS in a VPC, see [Amazon VPC and Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html) in the *Amazon RDS User Guide*.
This setting doesn't apply to Amazon Aurora DB instances. The DB subnet group is managed by the DB cluster. If specified, the setting must match the DB cluster setting.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBSystemId`  <a name="cfn-rds-dbinstance-dbsystemid"></a>
The Oracle system identifier (SID), which is the name of the Oracle database instance that manages your database files. In this context, the term "Oracle database instance" refers exclusively to the system global area (SGA) and Oracle background processes. If you don't specify a SID, the value defaults to `RDSCDB`. The Oracle SID is also the name of your CDB.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DedicatedLogVolume`  <a name="cfn-rds-dbinstance-dedicatedlogvolume"></a>
Indicates whether the DB instance has a dedicated log volume (DLV) enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeleteAutomatedBackups`  <a name="cfn-rds-dbinstance-deleteautomatedbackups"></a>
A value that indicates whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.
 **Amazon Aurora**
Not applicable. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can't be recovered. Manual DB cluster snapshots of the DB cluster are not deleted.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtection`  <a name="cfn-rds-dbinstance-deletionprotection"></a>
Specifies whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see [ Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).
This setting doesn't apply to Amazon Aurora DB instances. You can enable or disable deletion protection for the DB cluster. For more information, see `CreateDBCluster`. DB instances in a DB cluster can be deleted even when deletion protection is enabled for the DB cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-rds-dbinstance-domain"></a>
The Active Directory directory ID to create the DB instance in. Currently, only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.
For more information, see [ Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html) in the *Amazon RDS User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainAuthSecretArn`  <a name="cfn-rds-dbinstance-domainauthsecretarn"></a>
The ARN for the Secrets Manager secret with the credentials for the user joining the domain.
Example: `arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DomainDnsIps`  <a name="cfn-rds-dbinstance-domaindnsips"></a>
The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.
Constraints:
+ Two IP addresses must be provided. If there isn't a secondary domain controller, use the IP address of the primary domain controller for both entries in the list.
Example: `123.124.125.126,234.235.236.237`
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DomainFqdn`  <a name="cfn-rds-dbinstance-domainfqdn"></a>
The fully qualified domain name (FQDN) of an Active Directory domain.
Constraints:
+ Can't be longer than 64 characters.
Example: `mymanagedADtest.mymanagedAD.mydomain`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DomainIAMRoleName`  <a name="cfn-rds-dbinstance-domainiamrolename"></a>
The name of the IAM role to use when making API calls to the Directory Service.
This setting doesn't apply to the following DB instances:
+ Amazon Aurora (The domain is managed by the DB cluster.)
+ RDS Custom
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainOu`  <a name="cfn-rds-dbinstance-domainou"></a>
The Active Directory organizational unit for your DB instance to join.
Constraints:
+ Must be in the distinguished name format.
+ Can't be longer than 64 characters.
Example: `OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EnableCloudwatchLogsExports`  <a name="cfn-rds-dbinstance-enablecloudwatchlogsexports"></a>
The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see [Publishing Database Logs to Amazon CloudWatch Logs ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Relational Database Service User Guide*.
 **Amazon Aurora**
Not applicable. CloudWatch Logs exports are managed by the DB cluster.
 **Db2**
Valid values: `diag.log`, `notify.log`
 **MariaDB**
Valid values: `audit`, `error`, `general`, `slowquery`
 **Microsoft SQL Server**
Valid values: `agent`, `error`
 **MySQL**
Valid values: `audit`, `error`, `general`, `slowquery`
 **Oracle**
Valid values: `alert`, `audit`, `listener`, `trace`, `oemagent`
 **PostgreSQL**
Valid values: `postgresql`, `upgrade`
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableIAMDatabaseAuthentication`  <a name="cfn-rds-dbinstance-enableiamdatabaseauthentication"></a>
A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
This property is supported for RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL. For more information, see [ IAM Database Authentication for MariaDB, MySQL, and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide.*
 **Amazon Aurora**
Not applicable. Mapping AWS IAM accounts to database accounts is managed by the DB cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnablePerformanceInsights`  <a name="cfn-rds-dbinstance-enableperformanceinsights"></a>
Specifies whether to enable Performance Insights for the DB instance. For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide*.
This setting doesn't apply to RDS Custom DB instances.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-rds-dbinstance-engine"></a>
The name of the database engine to use for this DB instance. Not every database engine is available in every AWS Region.
This property is required when creating a DB instance.
You can convert an Oracle database from the non-CDB architecture to the container database (CDB) architecture by updating the `Engine` value in your templates from `oracle-ee` to `oracle-ee-cdb` or from `oracle-se2` to `oracle-se2-cdb`. Converting to the CDB architecture requires an interruption.
Valid Values:
+ `aurora-mysql` (for Aurora MySQL DB instances)
+ `aurora-postgresql` (for Aurora PostgreSQL DB instances)
+ `custom-oracle-ee` (for RDS Custom for Oracle DB instances)
+ `custom-oracle-ee-cdb` (for RDS Custom for Oracle DB instances)
+ `custom-sqlserver-ee` (for RDS Custom for SQL Server DB instances)
+ `custom-sqlserver-se` (for RDS Custom for SQL Server DB instances)
+ `custom-sqlserver-web` (for RDS Custom for SQL Server DB instances)
+  `db2-ae`
+  `db2-se`
+  `mariadb`
+  `mysql`
+  `oracle-ee`
+  `oracle-ee-cdb`
+  `oracle-se2`
+  `oracle-se2-cdb`
+  `postgres`
+  `sqlserver-ee`
+  `sqlserver-se`
+  `sqlserver-ex`
+  `sqlserver-web`
*Required*: Conditional
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EngineLifecycleSupport`  <a name="cfn-rds-dbinstance-enginelifecyclesupport"></a>
The lifecycle type for this DB instance.
By default, this value is set to `open-source-rds-extended-support`, which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled`. In this case, creating the DB instance will fail if the DB major version is past its end of standard support date.
This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the engine lifecycle support is managed by the DB cluster.
You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see [Amazon RDS Extended Support with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide*.
Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`
Default: `open-source-rds-extended-support`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EngineVersion`  <a name="cfn-rds-dbinstance-engineversion"></a>
The version number of the database engine to use.
For a list of valid engine versions, use the `DescribeDBEngineVersions` action.
The following are the database engines and links to information about the major and minor versions that are available with Amazon RDS. Not every database engine is available for every AWS Region.
 **Amazon Aurora**
Not applicable. The version number of the database engine to be used by the DB instance is managed by the DB cluster.
 **Db2**
See [Amazon RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Db2.html#Db2.Concepts.VersionMgmt) in the *Amazon RDS User Guide.*
 **MariaDB**
See [MariaDB on Amazon RDS Versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html#MariaDB.Concepts.VersionMgmt) in the *Amazon RDS User Guide.*
 **Microsoft SQL Server**
See [Microsoft SQL Server Versions on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.VersionSupport) in the *Amazon RDS User Guide.*
 **MySQL**
See [MySQL on Amazon RDS Versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt) in the *Amazon RDS User Guide.*
 **Oracle**
See [Oracle Database Engine Release Notes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.PatchComposition.html) in the *Amazon RDS User Guide.*
 **PostgreSQL**
See [Supported PostgreSQL Database Versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts.General.DBVersions) in the *Amazon RDS User Guide.*
If you specify a version prefix rather than a full version number, AWS CloudFormation uses prefix matching during drift detection.
For example, `"8.0"` for MySQL or `"16"` for PostgreSQL matches any version that starts with that prefix.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Iops`  <a name="cfn-rds-dbinstance-iops"></a>
The number of I/O operations per second (IOPS) that the database provisions. The value must be equal to or greater than 1000.
If you specify this property, you must follow the range of allowed ratios of your requested IOPS rate to the amount of storage that you allocate (IOPS to allocated storage). For example, you can provision an Oracle database instance with 1000 IOPS and 200 GiB of storage (a ratio of 5:1), or specify 2000 IOPS with 200 GiB of storage (a ratio of 10:1). For more information, see [Amazon RDS Provisioned IOPS Storage to Improve Performance](https://docs.aws.amazon.com/AmazonRDS/latest/DeveloperGuide/CHAP_Storage.html#USER_PIOPS) in the *Amazon RDS User Guide*.
If you specify `io1` for the `StorageType` property, then you must also specify the `Iops` property.
Constraints:
+ For RDS for Db2, MariaDB, MySQL, Oracle, and PostgreSQL - Must be a multiple between .5 and 50 of the storage amount for the DB instance.
+ For RDS for SQL Server - Must be a multiple between 1 and 50 of the storage amount for the DB instance.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-rds-dbinstance-kmskeyid"></a>
The ARN of the AWS KMS key that's used to encrypt the DB instance, such as `arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef`. If you enable the StorageEncrypted property but don't specify this property, AWS CloudFormation uses the default KMS key. If you specify this property, you must set the StorageEncrypted property to true.
If you specify the `SourceDBInstanceIdentifier` or `SourceDbiResourceId` property, don't specify this property. The value is inherited from the source DB instance, and if the DB instance is encrypted, the specified `KmsKeyId` property is used. However, if the source DB instance is in a different AWS Region, you must specify a KMS key ID.
If you specify the `SourceDBInstanceAutomatedBackupsArn` property, don't specify this property. The value is inherited from the source DB instance automated backup, and if the automated backup is encrypted, the specified `KmsKeyId` property is used.
If you create an encrypted read replica in a different AWS Region, then you must specify a KMS key for the destination AWS Region. KMS encryption keys are specific to the region that they're created in, and you can't use encryption keys from one region in another region.
If you specify the `DBSnapshotIdentifier` property, don't specify this property. The `StorageEncrypted` property value is inherited from the snapshot. If the DB instance is encrypted, the specified `KmsKeyId` property is also inherited from the snapshot.
If you specify `DBSecurityGroups`, AWS CloudFormation ignores this property. To specify both a security group and this property, you must use a VPC security group. For more information about Amazon RDS and VPC, see [Using Amazon RDS with Amazon VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html) in the *Amazon RDS User Guide*.
 **Amazon Aurora**
Not applicable. The KMS key identifier is managed by the DB cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LicenseModel`  <a name="cfn-rds-dbinstance-licensemodel"></a>
License model information for this DB instance.
 Valid Values:
+ Aurora MySQL - `general-public-license`
+ Aurora PostgreSQL - `postgresql-license`
+ RDS for Db2 - `bring-your-own-license`. For more information about RDS for Db2 licensing, see [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html) in the *Amazon RDS User Guide.*
+ RDS for MariaDB - `general-public-license`
+ RDS for Microsoft SQL Server - `license-included` or `bring-your-own-media`
+ RDS for MySQL - `general-public-license`
+ RDS for Oracle - `bring-your-own-license` or `license-included`
+ RDS for PostgreSQL - `postgresql-license`
If you've specified `DBSecurityGroups` and then you update the license model, AWS CloudFormation replaces the underlying DB instance. This will incur some interruptions to database availability.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManageMasterUserPassword`  <a name="cfn-rds-dbinstance-managemasteruserpassword"></a>
Specifies whether to manage the master user password with AWS Secrets Manager.
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*
Constraints:
+ Can't manage the master user password with AWS Secrets Manager if `MasterUserPassword` is specified.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterUserAuthenticationType`  <a name="cfn-rds-dbinstance-masteruserauthenticationtype"></a>
Specifies the authentication type for the master user. With IAM master user authentication, you can configure the master DB user with IAM database authentication when you create a DB instance.
You can specify one of the following values:
+ `password` - Use standard database authentication with a password.
+ `iam-db-auth` - Use IAM database authentication for the master user.
This option is only valid for RDS for MySQL, RDS for MariaDB, RDS for PostgreSQL, Aurora MySQL, and Aurora PostgreSQL engines.
*Required*: No
*Type*: String
*Allowed values*: `password | iam-db-auth`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterUsername`  <a name="cfn-rds-dbinstance-masterusername"></a>
The master user name for the DB instance.
If you specify the `SourceDBInstanceIdentifier` or `DBSnapshotIdentifier` property, don't specify this property. The value is inherited from the source DB instance or snapshot.
When migrating a self-managed Db2 database, we recommend that you use the same master username as your self-managed Db2 instance name.
 **Amazon Aurora**
Not applicable. The name for the master user is managed by the DB cluster.
 **RDS for Db2**
Constraints:
+ Must be 1 to 16 letters or numbers.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
 **RDS for MariaDB**
Constraints:
+ Must be 1 to 16 letters or numbers.
+ Can't be a reserved word for the chosen database engine.
 **RDS for Microsoft SQL Server**
Constraints:
+ Must be 1 to 128 letters or numbers.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
 **RDS for MySQL**
Constraints:
+ Must be 1 to 16 letters or numbers.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
 **RDS for Oracle**
Constraints:
+ Must be 1 to 30 letters or numbers.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
 **RDS for PostgreSQL**
Constraints:
+ Must be 1 to 63 letters or numbers.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,127}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MasterUserPassword`  <a name="cfn-rds-dbinstance-masteruserpassword"></a>
The password for the master user. The password can include any printable ASCII character except "/", """, or "@".
 **Amazon Aurora**
Not applicable. The password for the master user is managed by the DB cluster.
 **RDS for Db2**
Must contain from 8 to 255 characters.
 **RDS for MariaDB**
Constraints: Must contain from 8 to 41 characters.
 **RDS for Microsoft SQL Server**
Constraints: Must contain from 8 to 128 characters.
 **RDS for MySQL**
Constraints: Must contain from 8 to 41 characters.
 **RDS for Oracle**
Constraints: Must contain from 8 to 30 characters.
 **RDS for PostgreSQL**
Constraints: Must contain from 8 to 128 characters.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterUserSecret`  <a name="cfn-rds-dbinstance-masterusersecret"></a>
The secret managed by RDS in AWS Secrets Manager for the master user password.
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*
*Required*: No
*Type*: [MasterUserSecret](aws-properties-rds-dbinstance-masterusersecret.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAllocatedStorage`  <a name="cfn-rds-dbinstance-maxallocatedstorage"></a>
The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.
For more information about this setting, including limitations that apply to it, see [ Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) in the *Amazon RDS User Guide*.
This setting doesn't apply to the following DB instances:
+ Amazon Aurora (Storage is managed by the DB cluster.)
+ RDS Custom
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MonitoringInterval`  <a name="cfn-rds-dbinstance-monitoringinterval"></a>
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify `0`.
If `MonitoringRoleArn` is specified, then you must set `MonitoringInterval` to a value other than `0`.
This setting doesn't apply to RDS Custom DB instances.
Valid Values: `0 | 1 | 5 | 10 | 15 | 30 | 60`
Default: `0`
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MonitoringRoleArn`  <a name="cfn-rds-dbinstance-monitoringrolearn"></a>
The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess`. For information on creating a monitoring role, see [Setting Up and Enabling Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling) in the *Amazon RDS User Guide*.
If `MonitoringInterval` is set to a value other than `0`, then you must supply a `MonitoringRoleArn` value.
This setting doesn't apply to RDS Custom DB instances.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiAZ`  <a name="cfn-rds-dbinstance-multiaz"></a>
Specifies whether the DB instance is a Multi-AZ deployment. You can't set the `AvailabilityZone` parameter if the DB instance is a Multi-AZ deployment.
This setting doesn't apply to Amazon Aurora because the DB instance Availability Zones (AZs) are managed by the DB cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`NcharCharacterSetName`  <a name="cfn-rds-dbinstance-ncharcharactersetname"></a>
The name of the NCHAR character set for the Oracle DB instance.
This setting doesn't apply to RDS Custom DB instances.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkType`  <a name="cfn-rds-dbinstance-networktype"></a>
The network type of the DB instance.
Valid values:
+  `IPV4`
+  `DUAL`
The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and IPv6 protocols (`DUAL`).
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptionGroupName`  <a name="cfn-rds-dbinstance-optiongroupname"></a>
Indicates that the DB instance should be associated with the specified option group.
Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group. Also, that option group can't be removed from a DB instance once it is associated with a DB instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerformanceInsightsKMSKeyId`  <a name="cfn-rds-dbinstance-performanceinsightskmskeyid"></a>
The AWS KMS key identifier for encryption of Performance Insights data.
The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.
If you do not specify a value for `PerformanceInsightsKMSKeyId`, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.
**Update behavior:** Once Performance Insights is enabled with a KMS key, you cannot change to a different physical KMS key without replacing the DB instance. However, the following updates do not require replacement:
+ Enabling or disabling Performance Insights using the `EnablePerformanceInsights` property
+ Changing between different identifier formats (key ARN, key ID, alias ARN, alias name) of the same physical KMS key
+ Removing the `PerformanceInsightsKMSKeyId` property from your template
**Drift behavior:** If you specify `PerformanceInsightsKMSKeyId` while `EnablePerformanceInsights` is set to `false`, CloudFormation will report drift. This occurs because the RDS API does not allow setting a KMS key when Performance Insights is disabled. CloudFormation ignores the `PerformanceInsightsKMSKeyId` value during instance creation to avoid API errors, resulting in a mismatch between your template and the actual instance configuration.
To avoid drift, omit both `EnablePerformanceInsights` and `PerformanceInsightsKMSKeyId` during initial instance creation, then set both properties together when you're ready to enable Performance Insights.
For information about enabling Performance Insights, see [ EnablePerformanceInsights](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-enableperformanceinsights).
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PerformanceInsightsRetentionPeriod`  <a name="cfn-rds-dbinstance-performanceinsightsretentionperiod"></a>
The number of days to retain Performance Insights data. When creating a DB instance without enabling Performance Insights, you can't specify the parameter `PerformanceInsightsRetentionPeriod`.
This setting doesn't apply to RDS Custom DB instances.
Valid Values:
+  `7`
+ *month* \* 31, where *month* is a number of months from 1-23. Examples: `93` (3 months \* 31), `341` (11 months \* 31), `589` (19 months \* 31)
+  `731`
Default: `7` days
If you specify a retention period that isn't valid, such as `94`, Amazon RDS returns an error.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-rds-dbinstance-port"></a>
The port number on which the database accepts connections.
This setting doesn't apply to Aurora DB instances. The port number is managed by the cluster.
Valid Values: `1150-65535`
Default:
+ RDS for Db2 - `50000`
+ RDS for MariaDB - `3306`
+ RDS for Microsoft SQL Server - `1433`
+ RDS for MySQL - `3306`
+ RDS for Oracle - `1521`
+ RDS for PostgreSQL - `5432`
Constraints:
+ For RDS for Microsoft SQL Server, the value can't be `1234`, `1434`, `3260`, `3343`, `3389`, `47001`, or `49152-49156`.
*Required*: No
*Type*: String
*Pattern*: `^\d*$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PreferredBackupWindow`  <a name="cfn-rds-dbinstance-preferredbackupwindow"></a>
 The daily time range during which automated backups are created if automated backups are enabled, using the `BackupRetentionPeriod` parameter. For more information, see [ Backup Window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) in the *Amazon RDS User Guide.*
Constraints:
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
 **Amazon Aurora**
Not applicable. The daily time range for creating automated backups is managed by the DB cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredMaintenanceWindow`  <a name="cfn-rds-dbinstance-preferredmaintenancewindow"></a>
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
Format: `ddd:hh24:mi-ddd:hh24:mi`
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see [Maintaining a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow) in the *Amazon RDS User Guide.*
This property applies when AWS CloudFormation initially creates the DB instance. If you use AWS CloudFormation to update the DB instance, those updates are applied immediately.
Constraints: Minimum 30-minute window.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ProcessorFeatures`  <a name="cfn-rds-dbinstance-processorfeatures"></a>
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.
*Required*: No
*Type*: Array of [ProcessorFeature](aws-properties-rds-dbinstance-processorfeature.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromotionTier`  <a name="cfn-rds-dbinstance-promotiontier"></a>
The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see [ Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide*.
This setting doesn't apply to RDS Custom DB instances.
Default: `1`
Valid Values: `0 - 15`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-rds-dbinstance-publiclyaccessible"></a>
Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.
The default behavior value depends on your VPC setup and the database subnet group. For more information, see the `PubliclyAccessible` parameter in the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) in the *Amazon RDS API Reference*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicaMode`  <a name="cfn-rds-dbinstance-replicamode"></a>
The open mode of an Oracle read replica. For more information, see [Working with Oracle Read Replicas for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the *Amazon RDS User Guide*.
This setting is only supported in RDS for Oracle.
Default: `open-read-only`
Valid Values: `open-read-only` or `mounted`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestoreTime`  <a name="cfn-rds-dbinstance-restoretime"></a>
The date and time to restore from. This parameter applies to point-in-time recovery. For more information, see [Restoring a DB instance to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html) in the in the *Amazon RDS User Guide*.
Constraints:
+ Must be a time in Universal Coordinated Time (UTC) format.
+ Must be before the latest restorable time for the DB instance.
+ Can't be specified if the `UseLatestRestorableTime` parameter is enabled.
Example: `2009-09-07T23:45:00Z`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SourceDBClusterIdentifier`  <a name="cfn-rds-dbinstance-sourcedbclusteridentifier"></a>
The identifier of the Multi-AZ DB cluster that will act as the source for the read replica. Each DB cluster can have up to 15 read replicas.
Constraints:
+ Must be the identifier of an existing Multi-AZ DB cluster.
+ Can't be specified if the `SourceDBInstanceIdentifier` parameter is also specified.
+ The specified DB cluster must have automatic backups enabled, that is, its backup retention period must be greater than 0.
+ The source DB cluster must be in the same AWS Region as the read replica. Cross-Region replication isn't supported.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SourceDBInstanceAutomatedBackupsArn`  <a name="cfn-rds-dbinstance-sourcedbinstanceautomatedbackupsarn"></a>
The Amazon Resource Name (ARN) of the replicated automated backups from which to restore, for example, `arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE`.
This setting doesn't apply to RDS Custom.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SourceDBInstanceIdentifier`  <a name="cfn-rds-dbinstance-sourcedbinstanceidentifier"></a>
If you want to create a read replica DB instance, specify the ID of the source DB instance. Each DB instance can have a limited number of read replicas. For more information, see [Working with Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/DeveloperGuide/USER_ReadRepl.html) in the *Amazon RDS User Guide*.
For information about constraints that apply to DB instance identifiers, see [Naming constraints in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.Constraints) in the *Amazon RDS User Guide*.
The `SourceDBInstanceIdentifier` property determines whether a DB instance is a read replica. If you remove the `SourceDBInstanceIdentifier` property from your template and then update your stack, AWS CloudFormation promotes the read replica to a standalone DB instance.
If you specify the `UseLatestRestorableTime` or `RestoreTime` properties in conjunction with the `SourceDBInstanceIdentifier` property, RDS restores the DB instance to the requested point in time, thereby creating a new DB instance.
+ If you specify a source DB instance that uses VPC security groups, we recommend that you specify the `VPCSecurityGroups` property. If you don't specify the property, the read replica inherits the value of the `VPCSecurityGroups` property from the source DB when you create the replica. However, if you update the stack, AWS CloudFormation reverts the replica's `VPCSecurityGroups` property to the default value because it's not defined in the stack's template. This change might cause unexpected issues.
+ Read replicas don't support deletion policies. AWS CloudFormation ignores any deletion policy that's associated with a read replica.
+ If you specify `SourceDBInstanceIdentifier`, don't specify the `DBSnapshotIdentifier` property. You can't create a read replica from a snapshot.
+ Don't set the `BackupRetentionPeriod`, `DBName`, `MasterUsername`, `MasterUserPassword`, and `PreferredBackupWindow` properties. The database attributes are inherited from the source DB instance, and backups are disabled for read replicas.
+ If the source DB instance is in a different region than the read replica, specify the source region in `SourceRegion`, and specify an ARN for a valid DB instance in `SourceDBInstanceIdentifier`. For more information, see [ Constructing a Amazon RDS Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#USER_Tagging.ARN) in the *Amazon RDS User Guide*.
+ For DB instances in Amazon Aurora clusters, don't specify this property. Amazon RDS automatically assigns writer and reader DB instances.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SourceDbiResourceId`  <a name="cfn-rds-dbinstance-sourcedbiresourceid"></a>
The resource ID of the source DB instance from which to restore.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SourceRegion`  <a name="cfn-rds-dbinstance-sourceregion"></a>
The ID of the region that contains the source DB instance for the read replica.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageEncrypted`  <a name="cfn-rds-dbinstance-storageencrypted"></a>
A value that indicates whether the DB instance is encrypted. By default, it isn't encrypted.
If you specify the `KmsKeyId` property, then you must enable encryption.
If you specify the `SourceDBInstanceIdentifier` or `SourceDbiResourceId` property, don't specify this property. The value is inherited from the source DB instance, and if the DB instance is encrypted, the specified `KmsKeyId` property is used.
If you specify the `SourceDBInstanceAutomatedBackupsArn` property, don't specify this property. The value is inherited from the source DB instance automated backup.
If you specify `DBSnapshotIdentifier` property, don't specify this property. The value is inherited from the snapshot.
 **Amazon Aurora**
Not applicable. The encryption for DB instances is managed by the DB cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageThroughput`  <a name="cfn-rds-dbinstance-storagethroughput"></a>
Specifies the storage throughput value, in mebibyte per second (MiBps), for the DB instance. This setting applies only to the `gp3` storage type.
This setting doesn't apply to RDS Custom or Amazon Aurora.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageType`  <a name="cfn-rds-dbinstance-storagetype"></a>
The storage type to associate with the DB instance.
If you specify `io1`, `io2`, or `gp3`, you must also include a value for the `Iops` parameter.
This setting doesn't apply to Amazon Aurora DB instances. Storage is managed by the DB cluster.
Valid Values: `gp2 | gp3 | io1 | io2 | standard`
Default: `io1`, if the `Iops` parameter is specified. Otherwise, `gp3`.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-rds-dbinstance-tags"></a>
Tags to assign to the DB instance.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-dbinstance-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-rds-dbinstance-timezone"></a>
The time zone of the DB instance. The time zone parameter is currently supported only by [RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-time-zone) and [RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UseDefaultProcessorFeatures`  <a name="cfn-rds-dbinstance-usedefaultprocessorfeatures"></a>
Specifies whether the DB instance class of the DB instance uses its default processor features.
This setting doesn't apply to RDS Custom DB instances.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseLatestRestorableTime`  <a name="cfn-rds-dbinstance-uselatestrestorabletime"></a>
Specifies whether the DB instance is restored from the latest backup time. By default, the DB instance isn't restored from the latest backup time. This parameter applies to point-in-time recovery. For more information, see [Restoring a DB instance to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html) in the in the *Amazon RDS User Guide*.
Constraints:
+ Can't be specified if the `RestoreTime` parameter is provided.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`VPCSecurityGroups`  <a name="cfn-rds-dbinstance-vpcsecuritygroups"></a>
A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html) resources created in the template.
If you plan to update the resource, don't specify VPC security groups in a shared VPC.
 If you set `VPCSecurityGroups`, you must not set [`DBSecurityGroups`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsecuritygroups), and vice versa.
You can migrate a DB instance in your stack from an RDS DB security group to a VPC security group, but keep the following in mind:
+ You can't revert to using an RDS security group after you establish a VPC security group membership.
+ When you migrate your DB instance to VPC security groups, if your stack update rolls back because the DB instance update fails or because an update fails in another AWS CloudFormation resource, the rollback fails because it can't revert to an RDS security group.
+ To use the properties that are available when you use a VPC security group, you must recreate the DB instance. If you don't, AWS CloudFormation submits only the property values that are listed in the [`DBSecurityGroups`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsecuritygroups) property.
To avoid this situation, migrate your DB instance to using VPC security groups only when that is the only change in your stack template.
 **Amazon Aurora**
Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. If specified, the setting must match the DB cluster setting.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-dbinstance-return-values"></a>

### Ref
<a name="aws-resource-rds-dbinstance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DB instance name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-dbinstance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rds-dbinstance-return-values-fn--getatt-fn--getatt"></a>

`AutomaticRestartTime`  <a name="AutomaticRestartTime-fn::getatt"></a>
The time when a stopped DB instance is restarted automatically.

`CertificateDetails.CAIdentifier`  <a name="CertificateDetails.CAIdentifier-fn::getatt"></a>
The CA identifier of the CA certificate used for the DB instance's server certificate.

`CertificateDetails.ValidTill`  <a name="CertificateDetails.ValidTill-fn::getatt"></a>
The expiration date of the DB instance’s server certificate.

`DBInstanceArn`  <a name="DBInstanceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the DB instance.

`DBInstanceStatus`  <a name="DBInstanceStatus-fn::getatt"></a>
The current state of this DB instance.

`DbiResourceId`  <a name="DbiResourceId-fn::getatt"></a>
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

`DBSystemId`  <a name="DBSystemId-fn::getatt"></a>
The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB.
This setting is valid for RDS Custom only.

`Endpoint.Address`  <a name="Endpoint.Address-fn::getatt"></a>
The connection endpoint for the database. For example: `mystack-mydb-1apw1j4phylrk.cg034hpkmmjt.us-east-2.rds.amazonaws.com`
For Aurora Serverless DB clusters, the connection endpoint only applies to the DB cluster.

`Endpoint.HostedZoneId`  <a name="Endpoint.HostedZoneId-fn::getatt"></a>
The ID that Amazon Route 53 assigns when you create a hosted zone.

`Endpoint.Port`  <a name="Endpoint.Port-fn::getatt"></a>
The port number on which the database accepts connections. For example: `3306`

`InstanceCreateTime`  <a name="InstanceCreateTime-fn::getatt"></a>
The date and time when the DB instance was created.

`IsStorageConfigUpgradeAvailable`  <a name="IsStorageConfigUpgradeAvailable-fn::getatt"></a>
Indicates whether an upgrade is recommended for the storage file system configuration on the DB instance.

`LatestRestorableTime`  <a name="LatestRestorableTime-fn::getatt"></a>
The latest time to which a database in this DB instance can be restored with point-in-time restore.

`ListenerEndpoint.Address`  <a name="ListenerEndpoint.Address-fn::getatt"></a>
 The connection endpoint for the database. For example: `mystack-mydb-1apw1j4phylrk.cg034hpkmmjt.us-east-2.rds.amazonaws.com`

`ListenerEndpoint.HostedZoneId`  <a name="ListenerEndpoint.HostedZoneId-fn::getatt"></a>
 The ID of the hosted zone in that is associated with the database endpoint.

`ListenerEndpoint.Port`  <a name="ListenerEndpoint.Port-fn::getatt"></a>
The port number on which the database accepts connections.
This setting doesn't apply to Aurora DB instances. The port number is managed by the cluster.
Valid Values: `1150-65535`
Default:
+ RDS for Db2 - `50000`
+ RDS for MariaDB - `3306`
+ RDS for Microsoft SQL Server - `1433`
+ RDS for MySQL - `3306`
+ RDS for Oracle - `1521`
+ RDS for PostgreSQL - `5432`
Constraints:
+ For RDS for Microsoft SQL Server, the value can't be `1234`, `1434`, `3260`, `3343`, `3389`, `47001`, or `49152-49156`.

`MasterUserSecret.SecretArn`  <a name="MasterUserSecret.SecretArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the secret. This parameter is a return value that you can retrieve using the `Fn::GetAtt` intrinsic function. For more information, see [Return values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#aws-resource-rds-dbinstance-return-values).

`PercentProgress`  <a name="PercentProgress-fn::getatt"></a>
The progress of the storage optimization operation as a percentage.

`ReadReplicaDBClusterIdentifiers`  <a name="ReadReplicaDBClusterIdentifiers-fn::getatt"></a>
The identifiers of Aurora DB clusters to which the RDS DB instance is replicated as a read replica.

`ReadReplicaDBInstanceIdentifiers`  <a name="ReadReplicaDBInstanceIdentifiers-fn::getatt"></a>
The identifiers of the read replicas associated with this DB instance.

`ResumeFullAutomationModeTime`  <a name="ResumeFullAutomationModeTime-fn::getatt"></a>
The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation. The minimum value is 60 (default). The maximum value is 1,440.

`SecondaryAvailabilityZone`  <a name="SecondaryAvailabilityZone-fn::getatt"></a>
If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.

`StatusInfos`  <a name="StatusInfos-fn::getatt"></a>
The status of a read replica. If the DB instance isn't a read replica, the value is blank.

## Remarks
<a name="aws-resource-rds-dbinstance--remarks"></a>

 *DB instance creation modes*

This section outlines the modes for creating RDS DB instances—empty database, read replica, restore from snapshot, and point-in-time recovery. In the console, API, or CLI, each mode corresponds to a distinct API or command. In CloudFormation, however, the mode is determined by the following parameter combinations.
+ **Empty database** - Creates a new, empty DB instance.

  To create an empty database, *don't* specify any of the following properties:
  +  `RestoreTime`
  +  `UseLatestRestorableTime`
  +  `SourceDBInstanceAutomatedBackupsArn`
  +  `SourceDbiResourceId`
  +  `SourceDBInstanceIdentifier`
  +  `SourceDBClusterIdentifier`
  +  `DBSnapshotIdentifier`
+ **Read replica** - Creates a replica of an existing DB instance to replicate data asynchronously.

  To create a read replica, specify the `SourceDBInstanceIdentifier` property or the `SourceDBClusterIdentifier` property *without* the following properties:
  +  `RestoreTime`
  +  `UseLatestRestorableTime`
  +  `SourceDBInstanceAutomatedBackupsArn`
  +  `SourceDbiResourceId`
  +  `DBSnapshotIdentifier`
+ **Restore from snapshot** - Restores the DB instance from the specified snapshot. Cannot be used with a point-in-time recovery.

  To restore a DB instance from a snapshot, specify the `DBSnapshotIdentifier` property *without* the following properties:
  +  `RestoreTime`
  +  `UseLatestRestorableTime`
  +  `SourceDbiResourceId`
  +  `SourceDBInstanceAutomatedBackupsArn`
  +  `SourceDBInstanceIdentifier`
  +  `SourceDBClusterIdentifier`
+ **Point-in-time recovery** - Recovers the DB instance to a specific point in time. Requires identifying the source and the recovery time. Cannot be used with a snapshot.

  To restore a DB instance to a specified time, include any of the following properties:
  +  `SourceDBInstanceIdentifier`
  +  `SourceDbiResourceId`
  +  `SourceDBInstanceAutomatedBackupsArn`

  with *either* the `RestoreTime` property or the `UseLatestRestorableTime` property.

## Examples
<a name="aws-resource-rds-dbinstance--examples"></a>

**Topics**
+ [Creating a DB instance with Enhanced Monitoring enabled](#aws-resource-rds-dbinstance--examples--Creating_a_DB_instance_with_Enhanced_Monitoring_enabled)
+ [Creating a cross-region encrypted read replica](#aws-resource-rds-dbinstance--examples--Creating_a_cross-region_encrypted_read_replica)
+ [Setting a AWS region for the backup replication of a DB instance](#aws-resource-rds-dbinstance--examples--Setting_a_region_for_the_backup_replication_of_a_DB_instance)
+ [Creating an Amazon RDS Custom DB instance](#aws-resource-rds-dbinstance--examples--Creating_an_Amazon_RDS_Custom_DB_instance)
+ [Deploying RDS Custom for Oracle with single and multiple Availability Zones](#aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones)
+ [Creating a Secrets Manager secret for a master password](#aws-resource-rds-dbinstance--examples--Creating_a_Secrets_Manager_secret_for_a_master_password)
+ [Creating a DB instance with self-managed Active Directory domain](#aws-resource-rds-dbinstance--examples--Creating_a_DB_instance_with_self-managed_Active_Directory_domain)

### Creating a DB instance with Enhanced Monitoring enabled
<a name="aws-resource-rds-dbinstance--examples--Creating_a_DB_instance_with_Enhanced_Monitoring_enabled"></a>

The following example creates an Amazon RDS MySQL DB instance with Enhanced Monitoring enabled. The IAM role for Enhanced Monitoring specified in `MonitoringRoleArn` must exist before you run this example. For more information, see [ Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html) in the *Amazon RDS User Guide*.

#### JSON
<a name="aws-resource-rds-dbinstance--examples--Creating_a_DB_instance_with_Enhanced_Monitoring_enabled--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation Sample Template for creating an Amazon RDS DB instance: Sample template showing how to create a DB instance with Enhanced Monitoring enabled. **WARNING** This template creates an RDS DB instance. You will be billed for the AWS resources used if you create a stack from this template.",
    "Parameters": {
        "DBInstanceID": {
            "Default": "mydbinstance",
            "Description": "My database instance",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "63",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "Must begin with a letter and must not end with a hyphen or contain two consecutive hyphens."
        },
        "DBName": {
            "Default": "mydb",
            "Description": "My database",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "64",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "Must begin with a letter and contain only alphanumeric characters."
        },
        "DBInstanceClass": {
            "Default": "db.m5.large",
            "Description": "DB instance class",
            "Type": "String",
            "ConstraintDescription": "Must select a valid DB instance type."
        },
        "DBAllocatedStorage": {
            "Default": "50",
            "Description": "The size of the database (GiB)",
            "Type": "Number",
            "MinValue": "20",
            "MaxValue": "65536",
            "ConstraintDescription": "must be between 20 and 65536 GiB."
        },
        "DBUsername": {
            "NoEcho": "true",
            "Description": "Username for MySQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "DBPassword": {
            "NoEcho": "true",
            "Description": "Password MySQL database access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        }
    },
    "Resources": {
        "MyDB": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "DBInstanceIdentifier": {
                    "Ref": "DBInstanceID"
                },
                "DBName": {
                    "Ref": "DBName"
                },
                "DBInstanceClass": {
                    "Ref": "DBInstanceClass"
                },
                "AllocatedStorage": {
                    "Ref": "DBAllocatedStorage"
                },
                "Engine": "MySQL",
                "EngineVersion": "8.0.33",
                "MasterUsername": {
                    "Ref": "DBUsername"
                },
                "MasterUserPassword": {
                    "Ref": "DBPassword"
                },
                "MonitoringInterval": 60,
                "MonitoringRoleArn": "arn:aws:iam::1233456789012:role/rds-monitoring-role"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbinstance--examples--Creating_a_DB_instance_with_Enhanced_Monitoring_enabled--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: >-
  Description": "AWS CloudFormation Sample Template for creating an Amazon RDS DB instance:
  Sample template showing how to create a DB instance with Enhanced Monitoring enabled.
  **WARNING** This template creates an RDS DB instance. You will be billed for the AWS
  resources used if you create a stack from this template.
Parameters:
  DBInstanceID:
    Default: mydbinstance
    Description: My database instance
    Type: String
    MinLength: '1'
    MaxLength: '63'
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: >-
      Must begin with a letter and must not end with a hyphen or contain two
      consecutive hyphens.
  DBName:
    Default: mydb
    Description: My database
    Type: String
    MinLength: '1'
    MaxLength: '64'
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: Must begin with a letter and contain only alphanumeric characters.
  DBInstanceClass:
    Default: db.m5.large
    Description: DB instance class
    Type: String
    ConstraintDescription: Must select a valid DB instance type.
  DBAllocatedStorage:
    Default: '50'
    Description: The size of the database (GiB)
    Type: Number
    MinValue: '20'
    MaxValue: '65536'
    ConstraintDescription: must be between 20 and 65536 GiB.
  DBUsername:
    NoEcho: 'true'
    Description: Username for MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  DBPassword:
    NoEcho: 'true'
    Description: Password MySQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  MyDB:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      DBInstanceIdentifier: !Ref DBInstanceID
      DBName: !Ref DBName
      DBInstanceClass: !Ref DBInstanceClass
      AllocatedStorage: !Ref DBAllocatedStorage
      Engine: MySQL
      EngineVersion: "8.0.33"
      MasterUsername: !Ref DBUsername
      MasterUserPassword: !Ref DBPassword
      MonitoringInterval: 60
      MonitoringRoleArn: 'arn:aws:iam::123456789012:role/rds-monitoring-role'
```

### Creating a cross-region encrypted read replica
<a name="aws-resource-rds-dbinstance--examples--Creating_a_cross-region_encrypted_read_replica"></a>

The following example creates an encrypted read replica from a cross-region source DB instance.

#### JSON
<a name="aws-resource-rds-dbinstance--examples--Creating_a_cross-region_encrypted_read_replica--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "RDS Storage Encrypted",
    "Parameters": {
        "SourceDBInstanceIdentifier": {
            "Type": "String"
        },
        "DBInstanceType": {
            "Type": "String"
        },
        "SourceRegion": {
            "Type": "String"
        }
    },
    "Resources": {
        "MyKey": {
            "Type": "AWS::KMS::Key",
            "Properties": {
                "KeyPolicy": {
                    "Version": "2012-10-17",
                    "Id": "key-default-1",
                    "Statement": [
                        {
                            "Sid": "Enable IAM User Permissions",
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "arn:aws:iam::",
                                            {
                                                "Ref": "AWS::AccountId"
                                            },
                                            ":root"
                                        ]
                                    ]
                                }
                            },
                            "Action": "kms:*",
                            "Resource": "*"
                        }
                    ]
                }
            }
        },
        "MyDBSmall": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "DBInstanceClass": {
                    "Ref": "DBInstanceType"
                },
                "SourceDBInstanceIdentifier": {
                    "Ref": "SourceDBInstanceIdentifier"
                },
                "SourceRegion": {
                    "Ref": "SourceRegion"
                },
                "KmsKeyId": {
                    "Ref": "MyKey"
                }
            }
        }
    },
    "Outputs": {
        "InstanceId": {
            "Description": "InstanceId of the newly created RDS Instance",
            "Value": {
                "Ref": "MyDBSmall"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbinstance--examples--Creating_a_cross-region_encrypted_read_replica--yaml"></a>

```
---
AWSTemplateFormatVersion: 2010-09-09
Description: RDS Storage Encrypted
Parameters:
  SourceDBInstanceIdentifier:
    Type: String
  DBInstanceType:
    Type: String
  SourceRegion:
    Type: String
Resources:
  MyKey:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Version: 2012-10-17
        Id: key-default-1
        Statement:
          - Sid: Enable IAM User Permissions
            Effect: Allow
            Principal:
              AWS: !Join
                - ""
                - - "arn:aws:iam::"
                  - !Ref "AWS::AccountId"
                  - ":root"
            Action: "kms:*"
            Resource: "*"
  MyDBSmall:
    Type: AWS::RDS::DBInstance
    Properties:
      DBInstanceClass: !Ref DBInstanceType
      SourceDBInstanceIdentifier: !Ref SourceDBInstanceIdentifier
      SourceRegion: !Ref SourceRegion
      KmsKeyId: !Ref MyKey
Outputs:
  InstanceId:
    Description: InstanceId of the newly created RDS Instance
    Value: !Ref MyDBSmall
```

### Setting a AWS region for the backup replication of a DB instance
<a name="aws-resource-rds-dbinstance--examples--Setting_a_region_for_the_backup_replication_of_a_DB_instance"></a>

The following example defines the destination region for automated backup replication of a DB instance. In this example the DB instance backup will be replicated to `ap-northeast-1` region.

#### JSON
<a name="aws-resource-rds-dbinstance--examples--Setting_a_region_for_the_backup_replication_of_a_DB_instance--json"></a>

```
{
    "Resources": {
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "AllocatedStorage": "100",
                "AutomaticBackupReplicationRegion": "ap-northeast-1",
                "BackupRetentionPeriod": 1,
                "DBInstanceClass": "db.t3.micro",
                "Engine": "postgres",
                "Iops": 1000,
                "MasterUserPassword": "masterpassword",
                "MasterUsername": "masteruser",
                "StorageType": "IO1"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbinstance--examples--Setting_a_region_for_the_backup_replication_of_a_DB_instance--yaml"></a>

```
Resources:
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      AllocatedStorage: '100'
      AutomaticBackupReplicationRegion: ap-northeast-1
      BackupRetentionPeriod: 1
      DBInstanceClass: db.t3.micro
      Engine: postgres
      Iops: 1000
      MasterUserPassword: masterpassword
      MasterUsername: masteruser
      StorageType: IO1
```

### Creating an Amazon RDS Custom DB instance
<a name="aws-resource-rds-dbinstance--examples--Creating_an_Amazon_RDS_Custom_DB_instance"></a>

This example creates an Amazon RDS Custom DB instance. Amazon RDS Custom allows you as a database administrator to access and customize your database environment and operating system. With this access, you can configure settings, install patches, and enable native features to meet the dependent application's requirements. With RDS Custom, you can run your database workload using the AWS Management Console or AWS CLI. For more information, see [Working with Amazon RDS Custom](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html) in the *Amazon RDS User Guide*.

#### JSON
<a name="aws-resource-rds-dbinstance--examples--Creating_an_Amazon_RDS_Custom_DB_instance--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "AllocatedStorage": {
            "Type": "String"
        },
        "CustomIAMInstanceProfile": {
            "Type": "String"
        },
        "DBInstanceIdentifier": {
            "Type": "String"
        },
        "DBInstanceClass": {
            "Type": "String"
        },
        "DBName": {
            "Type": "String"
        },
        "DBSubnetGroupName": {
            "Type": "String"
        },
        "Engine": {
            "Type": "String"
        },
        "EngineVersion": {
            "Type": "String"
        },
        "KMSKeyId": {
            "Type": "String"
        },
        "LicenseModel": {
            "Type": "String"
        },
        "MasterUsername": {
            "Type": "String"
        },
        "MasterUserPassword": {
            "Type": "String",
            "NoEcho": true
        }
    },
    "Resources": {
        "RDSDBInstance": {
            "Properties": {
                "AllocatedStorage": {
                    "Ref": "AllocatedStorage"
                },
                "AutoMinorVersionUpgrade": false,
                "CustomIAMInstanceProfile": {
                    "Ref": "CustomIAMInstanceProfile"
                },
                "DBInstanceClass": {
                    "Ref": "DBInstanceClass"
                },
                "DBSubnetGroupName": {
                    "Ref": "DBSubnetGroupName"
                },
                "Engine": {
                    "Ref": "Engine"
                },
                "EngineVersion": {
                    "Ref": "EngineVersion"
                },
                "LicenseModel": {
                    "Ref": "LicenseModel"
                },
                "KmsKeyId": {
                    "Ref": "KMSKeyId"
                },
                "MasterUsername": {
                    "Ref": "MasterUsername"
                },
                "MasterUserPassword": {
                    "Ref": "MasterUserPassword"
                }
            },
            "Type": "AWS::RDS::DBInstance"
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbinstance--examples--Creating_an_Amazon_RDS_Custom_DB_instance--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  AllocatedStorage:
    Type: String
  CustomIAMInstanceProfile:
    Type: String
  DBInstanceIdentifier:
    Type: String
  DBInstanceClass:
    Type: String
  DBName:
    Type: String
  DBSubnetGroupName:
    Type: String
  Engine:
    Type: String
  EngineVersion:
    Type: String
  KMSKeyId:
    Type: String
  LicenseModel:
    Type: String
  MasterUsername:
    Type: String
  MasterUserPassword:
    Type: String
    NoEcho: true
Resources:
  RDSDBInstance:
    Properties:
      AllocatedStorage: !Ref AllocatedStorage
      AutoMinorVersionUpgrade: false
      CustomIAMInstanceProfile: !Ref CustomIAMInstanceProfile
      DBInstanceClass: !Ref DBInstanceClass
      DBSubnetGroupName: !Ref DBSubnetGroupName
      Engine: !Ref Engine
      EngineVersion: !Ref EngineVersion
      LicenseModel: !Ref LicenseModel
      KmsKeyId: !Ref KMSKeyId
      MasterUsername: !Ref MasterUsername
      MasterUserPassword: !Ref MasterUserPassword
    Type: 'AWS::RDS::DBInstance'
```

### Deploying RDS Custom for Oracle with single and multiple Availability Zones
<a name="aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones"></a>

These examples deploy RDS Custom for Oracle with single and multi-AZ support. The prerequisites template creates the required infrastructure, and the second template creates Custom Engine Versions (CEVs) as well as both single-AZ and multi-AZ RDS Custom for Oracle instances. For more information, see [Deploying RDS Custom for Oracle with CloudFormation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-multiaz-deployment.html) in the *Amazon RDS User Guide*.

#### JSON
<a name="aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "CloudFormation Template for the Pre-reqs of RDS Custom for Oracle",

    "Resources": {
        "RDSVPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "EnableDnsSupport": "true",
                "EnableDnsHostnames": "true",
                "CidrBlock": "10.20.0.0/16",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": {
                            "Fn::Join": [
                                "-",
                                [
                                    {
                                        "Ref": "AWS::StackName"
                                    },
                                    "RDSVPC"
                                ]
                            ]
                        }
                    }
                ]
            }
        },
        "Subnet1": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "CidrBlock": "10.20.1.0/24",
                "AvailabilityZone": {
                    "Fn::Select": [
                        0,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                },
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": {
                            "Fn::Join": [
                                "-",
                                [
                                    {
                                        "Ref": "AWS::StackName"
                                    },
                                    "Subnet1"
                                ]
                            ]
                        }
                    }
                ]
            }
        },
        "Subnet2": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "CidrBlock": "10.20.2.0/24",
                "AvailabilityZone": {
                    "Fn::Select": [
                        1,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                },
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": {
                            "Fn::Join": [
                                "-",
                                [
                                    {
                                        "Ref": "AWS::StackName"
                                    },
                                    "Subnet2"
                                ]
                            ]
                        }
                    }
                ]
            }
        },
        "Subnet3": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "CidrBlock": "10.20.3.0/24",
                "AvailabilityZone": {
                    "Fn::Select": [
                        2,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                },
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": {
                            "Fn::Join": [
                                "-",
                                [
                                    {
                                        "Ref": "AWS::StackName"
                                    },
                                    "Subnet3"
                                ]
                            ]
                        }
                    }
                ]
            }
        },
        "Subnet4": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "CidrBlock": "10.20.4.0/24",
                "AvailabilityZone": {
                    "Fn::Select": [
                        2,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                },
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": {
                            "Fn::Join": [
                                "-",
                                [
                                    {
                                        "Ref": "AWS::StackName"
                                    },
                                    "Subnet4"
                                ]
                            ]
                        }
                    }
                ]
            }
        },
        "InternetGateway": {
            "Type": "AWS::EC2::InternetGateway",
            "Properties": {
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": {
                            "Fn::Join": [
                                "-",
                                [
                                    {
                                        "Ref": "AWS::StackName"
                                    },
                                    "InternetGateway"
                                ]
                            ]
                        }
                    }
                ]
            }
        },
        "AttachGateway": {
            "Type": "AWS::EC2::VPCGatewayAttachment",
            "Properties": {
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "InternetGatewayId": {
                    "Ref": "InternetGateway"
                }
            }
        },
        "RouteTablePvt": {
            "Type": "AWS::EC2::RouteTable",
            "Properties": {
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": {
                            "Fn::Join": [
                                "-",
                                [
                                    {
                                        "Ref": "AWS::StackName"
                                    },
                                    "RouteTablePvt"
                                ]
                            ]
                        }
                    }
                ]
            }
        },
        "RouteTablePub": {
            "Type": "AWS::EC2::RouteTable",
            "Properties": {
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": {
                            "Fn::Join": [
                                "-",
                                [
                                    {
                                        "Ref": "AWS::StackName"
                                    },
                                    "RouteTablePub"
                                ]
                            ]
                        }
                    }
                ]
            }
        },
        "RoutePub": {
            "Type": "AWS::EC2::Route",
            "DependsOn": "AttachGateway",
            "Properties": {
                "RouteTableId": {
                    "Ref": "RouteTablePub"
                },
                "DestinationCidrBlock": "0.0.0.0/0",
                "GatewayId": {
                    "Ref": "InternetGateway"
                }
            }
        },
        "Subnet1RouteTableAssociation": {
            "Type": "AWS::EC2::SubnetRouteTableAssociation",
            "Properties": {
                "SubnetId": {
                    "Ref": "Subnet1"
                },
                "RouteTableId": {
                    "Ref": "RouteTablePvt"
                }
            }
        },
        "Subnet2RouteTableAssociation": {
            "Type": "AWS::EC2::SubnetRouteTableAssociation",
            "Properties": {
                "SubnetId": {
                    "Ref": "Subnet2"
                },
                "RouteTableId": {
                    "Ref": "RouteTablePvt"
                }
            }
        },
        "Subnet3RouteTableAssociation": {
            "Type": "AWS::EC2::SubnetRouteTableAssociation",
            "Properties": {
                "SubnetId": {
                    "Ref": "Subnet3"
                },
                "RouteTableId": {
                    "Ref": "RouteTablePvt"
                }
            }
        },
        "Subnet4RouteTableAssociation": {
            "Type": "AWS::EC2::SubnetRouteTableAssociation",
            "Properties": {
                "SubnetId": {
                    "Ref": "Subnet4"
                },
                "RouteTableId": {
                    "Ref": "RouteTablePub"
                }
            }
        },
        "RDSSG": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Security Group for RDS Oracle Custom instances",
                "GroupName": "rds-custom-db-sg",
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": "0",
                        "ToPort": "65535",
                        "CidrIp": "10.20.0.0/16",
                        "Description": "Allows all traffic from within the same VPC"
                    }
                ],
                "SecurityGroupEgress": [
                    {
                        "IpProtocol": -1,
                        "CidrIp": "0.0.0.0/0",
                        "Description": "Allows outbound communication"
                    }
                ],
                "VpcId": {
                    "Ref": "RDSVPC"
                }
            }
        },
        "VPCESG": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Security Group for VPC Endpoints",
                "GroupName": "rds-custom-vpce-sg",
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": "443",
                        "ToPort": "443",
                        "CidrIp": "10.20.0.0/16",
                        "Description": "Allows SSM access from the RDS Oracle DB instance"
                    }
                ],
                "SecurityGroupEgress": [
                    {
                        "IpProtocol": -1,
                        "CidrIp": "0.0.0.0/0",
                        "Description": "Allows outbound communication"
                    }
                ],
                "VpcId": {
                    "Ref": "RDSVPC"
                }
            }
        },
        "DBSubnetGroup": {
            "Type": "AWS::RDS::DBSubnetGroup",
            "Properties": {
                "DBSubnetGroupName": "rds-custom-private",
                "DBSubnetGroupDescription": "RDS Custom Private Network",
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ]
            }
        },
        "vpceS3": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "RouteTableIds": [
                    {
                        "Ref": "RouteTablePvt"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.s3"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                }
            }
        },
        "vpceEC2": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.ec2"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "vpceEC2Messages": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.ec2messages"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "vpceMonitoring": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.monitoring"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "vpceSSM": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.ssm"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "vpceSSMMessages": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.ssmmessages"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "vpceLogs": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.logs"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "vpceEvents": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.events"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "vpceSecretsManager": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.secretsmanager"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "vpceSQS": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "Subnet1"
                    },
                    {
                        "Ref": "Subnet2"
                    },
                    {
                        "Ref": "Subnet3"
                    }
                ],
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.sqs"
                },
                "VpcId": {
                    "Ref": "RDSVPC"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "VPCESG"
                    }
                ]
            }
        },
        "KMSKey": {
            "Type": "AWS::KMS::Key",
            "Properties": {
                "Description": "Symmetric key for the CEV",
                "Enabled": true,
                "EnableKeyRotation": false,
                "KeyPolicy": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Id": "key-default-1",
                    "Statement": {
                        "Sid": "Enable IAM policies",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": {
                                "Fn::Join": [
                                    ":",
                                    [
                                        "arn",
                                        {
                                            "Ref": "AWS::Partition"
                                        },
                                        "iam:",
                                        {
                                            "Ref": "AWS::AccountId"
                                        },
                                        "root"
                                    ]
                                ]
                            }
                        },
                        "Action": "kms:*",
                        "Resource": "*"
                    }
                },
                "KeySpec": "SYMMETRIC_DEFAULT",
                "KeyUsage": "ENCRYPT_DECRYPT",
                "MultiRegion": false
            }
        },
        "KMSKeyAlias": {
            "Type": "AWS::KMS::Alias",
            "Properties": {
                "AliasName": "alias/rds-custom",
                "TargetKeyId": {
                    "Ref": "KMSKey"
                }
            }
        },
        "RDSCustomInstanceServiceRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "RoleName": {
                    "Fn::Sub": "AWSRDSCustomInstanceRole-${AWS::Region}"
                },
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Action": "sts:AssumeRole",
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "ec2.amazonaws.com"
                            }
                        }
                    ]
                },
                "Path": "/",
                "Policies": [
                    {
                        "PolicyName": "AWSRDSCustomEc2InstanceRolePolicy",
                        "PolicyDocument": {
                            "Version": "2012-10-17"		 	 	 ,
                            "Statement": [
                                {
                                    "Sid": "1",
                                    "Effect": "Allow",
                                    "Action": [
                                        "ssm:DescribeAssociation",
                                        "ssm:GetDeployablePatchSnapshotForInstance",
                                        "ssm:GetDocument",
                                        "ssm:DescribeDocument",
                                        "ssm:GetManifest",
                                        "ssm:GetParameter",
                                        "ssm:GetParameters",
                                        "ssm:ListAssociations",
                                        "ssm:ListInstanceAssociations",
                                        "ssm:PutInventory",
                                        "ssm:PutComplianceItems",
                                        "ssm:PutConfigurePackageResult",
                                        "ssm:UpdateAssociationStatus",
                                        "ssm:UpdateInstanceAssociationStatus",
                                        "ssm:UpdateInstanceInformation",
                                        "ssm:GetConnectionStatus",
                                        "ssm:DescribeInstanceInformation",
                                        "ssmmessages:CreateControlChannel",
                                        "ssmmessages:CreateDataChannel",
                                        "ssmmessages:OpenControlChannel",
                                        "ssmmessages:OpenDataChannel"
                                    ],
                                    "Resource": [
                                        "*"
                                    ]
                                },
                                {
                                    "Sid": "2",
                                    "Effect": "Allow",
                                    "Action": [
                                        "ec2messages:AcknowledgeMessage",
                                        "ec2messages:DeleteMessage",
                                        "ec2messages:FailMessage",
                                        "ec2messages:GetEndpoint",
                                        "ec2messages:GetMessages",
                                        "ec2messages:SendReply"
                                    ],
                                    "Resource": [
                                        "*"
                                    ]
                                },
                                {
                                    "Sid": "3",
                                    "Effect": "Allow",
                                    "Action": [
                                        "logs:PutRetentionPolicy",
                                        "logs:PutLogEvents",
                                        "logs:DescribeLogStreams",
                                        "logs:DescribeLogGroups",
                                        "logs:CreateLogStream",
                                        "logs:CreateLogGroup"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:rds-custom-instance*"
                                        }
                                    ]
                                },
                                {
                                    "Sid": "4",
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:putObject",
                                        "s3:getObject",
                                        "s3:getObjectVersion"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:s3:::do-not-delete-rds-custom-*/*"
                                        }
                                    ]
                                },
                                {
                                    "Sid": "5",
                                    "Effect": "Allow",
                                    "Action": [
                                        "cloudwatch:PutMetricData"
                                    ],
                                    "Resource": [
                                        "*"
                                    ],
                                    "Condition": {
                                        "StringEquals": {
                                            "cloudwatch:namespace": [
                                                "RDSCustomForOracle/Agent"
                                            ]
                                        }
                                    }
                                },
                                {
                                    "Sid": "6",
                                    "Effect": "Allow",
                                    "Action": [
                                        "events:PutEvents"
                                    ],
                                    "Resource": [
                                        "*"
                                    ]
                                },
                                {
                                    "Sid": "7",
                                    "Effect": "Allow",
                                    "Action": [
                                        "secretsmanager:GetSecretValue",
                                        "secretsmanager:DescribeSecret"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:do-not-delete-rds-custom-*"
                                        },
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:rds-custom!oracle-do-not-delete-*"
                                        }
                                    ]
                                },
                                {
                                    "Sid": "8",
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:ListBucketVersions"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:s3:::do-not-delete-rds-custom-*"
                                        }
                                    ]
                                },
                                {
                                    "Sid": "9",
                                    "Effect": "Allow",
                                    "Action": "ec2:CreateSnapshots",
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:ec2:*:*:instance/*"
                                        },
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:ec2:*:*:volume/*"
                                        }
                                    ],
                                    "Condition": {
                                        "StringEquals": {
                                            "ec2:ResourceTag/AWSRDSCustom": "custom-oracle"
                                        }
                                    }
                                },
                                {
                                    "Sid": "10",
                                    "Effect": "Allow",
                                    "Action": "ec2:CreateSnapshots",
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:ec2:*::snapshot/*"
                                        }
                                    ]
                                },
                                {
                                    "Sid": "11",
                                    "Effect": "Allow",
                                    "Action": [
                                        "kms:Decrypt",
                                        "kms:GenerateDataKey"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::GetAtt": [
                                                "KMSKey",
                                                "Arn"
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "Sid": "12",
                                    "Effect": "Allow",
                                    "Action": "ec2:CreateTags",
                                    "Resource": "*",
                                    "Condition": {
                                        "StringLike": {
                                            "ec2:CreateAction": [
                                                "CreateSnapshots"
                                            ]
                                        }
                                    }
                                },
                                {
                                    "Sid": "13",
                                    "Effect": "Allow",
                                    "Action": [
                                        "sqs:SendMessage",
                                        "sqs:ReceiveMessage",
                                        "sqs:DeleteMessage",
                                        "sqs:GetQueueUrl"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:sqs:${AWS::Region}:${AWS::AccountId}:do-not-delete-rds-custom-*"
                                        }
                                    ],
                                    "Condition": {
                                        "StringLike": {
                                            "aws:ResourceTag/AWSRDSCustom": "custom-oracle"
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "RDSCustomInstanceProfile": {
            "Type": "AWS::IAM::InstanceProfile",
            "Properties": {
                "InstanceProfileName": "AWSRDSCustomInstanceProfileForRdsCustomInstance",
                "Path": "/",
                "Roles": [
                    {
                        "Ref": "RDSCustomInstanceServiceRole"
                    }
                ]
            }
        },
        "PublicSubnetParameter": {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Description": "The subnet ID of the public subnet",
                "Name": "PublicSubnetParameter",
                "Type": "String",
                "Value": {
                    "Ref": "Subnet4"
                }
            }
        },
        "RDSSGParameter": {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Description": "The security group ID of the RDSSG",
                "Name": "RDSSGParameter",
                "Type": "String",
                "Value": {
                    "Fn::GetAtt": [
                        "RDSSG",
                        "GroupId"
                    ]
                }
            }
        },
        "RDSKMSParameter": {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Description": "KMS Key",
                "Name": "KMSParameter",
                "Type": "String",
                "Value": {
                    "Fn::GetAtt": [
                        "KMSKey",
                        "KeyId"
                    ]
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones--yaml"></a>

```
# AWSTemplateFormatVersion: 2010-09-09
# RDS Custom for AWS RDS Oracle
# 06/15/2025  created by Sharath Chandra Kampili

AWSTemplateFormatVersion: '2010-09-09'
Description: CloudFormation Template for the pre-reqs of RDS Custom for Oracle

Resources:
  RDSVPC:
    Type: AWS::EC2::VPC
    Properties:
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
      CidrBlock: 10.20.0.0/16
      Tags:
      - Key: Name
        Value:
          Fn::Join:
          - "-"
          - - !Ref AWS::StackName
            - RDSVPC
  Subnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref RDSVPC
      CidrBlock: 10.20.1.0/24
      AvailabilityZone: !Select [0, !GetAZs ]
      Tags:
      - Key: Name
        Value:
          Fn::Join:
          - "-"
          - - !Ref AWS::StackName
            - Subnet1
  Subnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref RDSVPC
      CidrBlock: 10.20.2.0/24
      AvailabilityZone: !Select [1, !GetAZs ]
      Tags:
      - Key: Name
        Value:
          Fn::Join:
          - "-"
          - - !Ref AWS::StackName
            - Subnet2
  Subnet3:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref RDSVPC
      CidrBlock: 10.20.3.0/24
      AvailabilityZone: !Select [2, !GetAZs ]
      Tags:
      - Key: Name
        Value:
          Fn::Join:
          - "-"
          - - !Ref AWS::StackName
            - Subnet3
  Subnet4:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref RDSVPC
      CidrBlock: 10.20.4.0/24
      AvailabilityZone: !Select [2, !GetAZs ]
      Tags:
      - Key: Name
        Value:
          Fn::Join:
          - "-"
          - - !Ref AWS::StackName
            - Subnet4

  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
      - Key: Name
        Value:
          Fn::Join:
          - "-"
          - - !Ref AWS::StackName
            - InternetGateway
  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref RDSVPC
      InternetGatewayId: !Ref InternetGateway

  RouteTablePvt:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref RDSVPC
      Tags:
      - Key: Name
        Value:
          Fn::Join:
          - "-"
          - - !Ref AWS::StackName
            - RouteTablePvt
  RouteTablePub:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref RDSVPC
      Tags:
      - Key: Name
        Value:
          Fn::Join:
          - "-"
          - - !Ref AWS::StackName
            - RouteTablePub
  RoutePub:
    Type: AWS::EC2::Route
    DependsOn: AttachGateway
    Properties:
      RouteTableId: !Ref RouteTablePub
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway

  Subnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref Subnet1
      RouteTableId: !Ref RouteTablePvt
  Subnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref Subnet2
      RouteTableId: !Ref RouteTablePvt
  Subnet3RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref Subnet3
      RouteTableId: !Ref RouteTablePvt
  Subnet4RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref Subnet4
      RouteTableId: !Ref RouteTablePub

  RDSSG:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Security Group for RDS Oracle Custom instances
      GroupName: rds-custom-db-sg
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '0'
          ToPort: '65535'
          CidrIp: 10.20.0.0/16
          Description: Allows all traffic from within the same VPC
      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0
          Description: Allows outbound communication
      VpcId: !Ref RDSVPC
  VPCESG:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Security Group for VPC Endpoints
      GroupName: rds-custom-vpce-sg
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '443'
          ToPort: '443'
          CidrIp: 10.20.0.0/16
          Description: Allows SSM access from the RDS Oracle DB instance
      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0
          Description: Allows outbound communication
      VpcId: !Ref RDSVPC

  DBSubnetGroup:
    Type: AWS::RDS::DBSubnetGroup
    Properties:
      DBSubnetGroupName: rds-custom-private
      DBSubnetGroupDescription: RDS Custom Private Network
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
  vpceS3:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      RouteTableIds:
      - Ref: RouteTablePvt
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.s3
      VpcId: !Ref RDSVPC
  vpceEC2:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.ec2
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  vpceEC2Messages:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.ec2messages
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  vpceMonitoring:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.monitoring
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  vpceSSM:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.ssm
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  vpceSSMMessages:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.ssmmessages
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  vpceLogs:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.logs
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  vpceEvents:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.events
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  vpceSecretsManager:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.secretsmanager
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  vpceSQS:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref Subnet1
      - !Ref Subnet2
      - !Ref Subnet3
      ServiceName:
        Fn::Sub: com.amazonaws.${AWS::Region}.sqs
      VpcId: !Ref RDSVPC
      SecurityGroupIds:
      - !Ref VPCESG
  KMSKey:
    Type: "AWS::KMS::Key"
    Properties:
      Description: "Symmetric key for the CEV"
      Enabled: true
      EnableKeyRotation: false
      KeyPolicy:
        Version: "2012-10-17"
        Id: "key-default-1"
        Statement:
          Sid: "Enable IAM policies"
          Effect: "Allow"
          Principal:
            AWS: !Join [ ':', [ 'arn', !Ref AWS::Partition, 'iam:', !Ref AWS::AccountId, 'root' ] ]
          Action: kms:*
          Resource: '*'
      KeySpec: "SYMMETRIC_DEFAULT"
      KeyUsage: "ENCRYPT_DECRYPT"
      MultiRegion: false
  KMSKeyAlias:
    Type: AWS::KMS::Alias
    Properties:
      AliasName: 'alias/rds-custom'
      TargetKeyId: !Ref KMSKey
  RDSCustomInstanceServiceRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName:
        Fn::Sub: AWSRDSCustomInstanceRole-${AWS::Region}
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
      Path: /
      Policies:
        - PolicyName: AWSRDSCustomEc2InstanceRolePolicy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Sid: '1'
                Effect: Allow
                Action:
                  - ssm:DescribeAssociation
                  - ssm:GetDeployablePatchSnapshotForInstance
                  - ssm:GetDocument
                  - ssm:DescribeDocument
                  - ssm:GetManifest
                  - ssm:GetParameter
                  - ssm:GetParameters
                  - ssm:ListAssociations
                  - ssm:ListInstanceAssociations
                  - ssm:PutInventory
                  - ssm:PutComplianceItems
                  - ssm:PutConfigurePackageResult
                  - ssm:UpdateAssociationStatus
                  - ssm:UpdateInstanceAssociationStatus
                  - ssm:UpdateInstanceInformation
                  - ssm:GetConnectionStatus
                  - ssm:DescribeInstanceInformation
                  - ssmmessages:CreateControlChannel
                  - ssmmessages:CreateDataChannel
                  - ssmmessages:OpenControlChannel
                  - ssmmessages:OpenDataChannel
                Resource:
                  - '*'
              - Sid: '2'
                Effect: Allow
                Action:
                  - ec2messages:AcknowledgeMessage
                  - ec2messages:DeleteMessage
                  - ec2messages:FailMessage
                  - ec2messages:GetEndpoint
                  - ec2messages:GetMessages
                  - ec2messages:SendReply
                Resource:
                  - '*'
              - Sid: '3'
                Effect: Allow
                Action:
                  - logs:PutRetentionPolicy
                  - logs:PutLogEvents
                  - logs:DescribeLogStreams
                  - logs:DescribeLogGroups
                  - logs:CreateLogStream
                  - logs:CreateLogGroup
                Resource:
                  - Fn::Sub: >-
                      arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:rds-custom-instance*
              - Sid: '4'
                Effect: Allow
                Action:
                  - s3:putObject
                  - s3:getObject
                  - s3:getObjectVersion
                Resource:
                  - Fn::Sub: >-
                      arn:${AWS::Partition}:s3:::do-not-delete-rds-custom-*/*
              - Sid: '5'
                Effect: Allow
                Action:
                  - cloudwatch:PutMetricData
                Resource:
                  - '*'
                Condition:
                  StringEquals:
                    cloudwatch:namespace:
                      - RDSCustomForOracle/Agent
              - Sid: '6'
                Effect: Allow
                Action:
                  - events:PutEvents
                Resource:
                  - '*'
              - Sid: '7'
                Effect: Allow
                Action:
                  - secretsmanager:GetSecretValue
                  - secretsmanager:DescribeSecret
                Resource:
                  - Fn::Sub: arn:${AWS::Partition}:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:do-not-delete-rds-custom-*
                  - Fn::Sub: arn:${AWS::Partition}:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:rds-custom!oracle-do-not-delete-*
              - Sid: '8'
                Effect: Allow
                Action:
                  - s3:ListBucketVersions
                Resource:
                  - Fn::Sub: >-
                      arn:${AWS::Partition}:s3:::do-not-delete-rds-custom-*
              - Sid: '9'
                Effect: Allow
                Action: ec2:CreateSnapshots
                Resource:
                  - Fn::Sub: arn:${AWS::Partition}:ec2:*:*:instance/*
                  - Fn::Sub: arn:${AWS::Partition}:ec2:*:*:volume/*
                Condition:
                  StringEquals:
                    ec2:ResourceTag/AWSRDSCustom: custom-oracle
              - Sid: '10'
                Effect: Allow
                Action: ec2:CreateSnapshots
                Resource:
                  - Fn::Sub: arn:${AWS::Partition}:ec2:*::snapshot/*
              - Sid: '11'
                Effect: Allow
                Action:
                  - kms:Decrypt
                  - kms:GenerateDataKey
                Resource:
                  - !GetAtt KMSKey.Arn
              - Sid: '12'
                Effect: Allow
                Action: ec2:CreateTags
                Resource: '*'
                Condition:
                  StringLike:
                    ec2:CreateAction:
                      - CreateSnapshots
              - Sid: '13'
                Effect: Allow
                Action:
                  - sqs:SendMessage
                  - sqs:ReceiveMessage
                  - sqs:DeleteMessage
                  - sqs:GetQueueUrl
                Resource:
                  - Fn::Sub: arn:${AWS::Partition}:sqs:${AWS::Region}:${AWS::AccountId}:do-not-delete-rds-custom-*
                Condition:
                  StringLike:
                    aws:ResourceTag/AWSRDSCustom: custom-oracle

  RDSCustomInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      InstanceProfileName: 'AWSRDSCustomInstanceProfileForRdsCustomInstance'
      Path: /
      Roles:
        - !Ref RDSCustomInstanceServiceRole

  PublicSubnetParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Description: The subnet ID of the public subnet
      Name: PublicSubnetParameter
      Type: String
      Value: !Ref Subnet4
  RDSSGParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Description: The security group ID of the RDSSG
      Name: RDSSGParameter
      Type: String
      Value: !GetAtt RDSSG.GroupId
  RDSKMSParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Description: KMS Key
      Name: KMSParameter
      Type: String
      Value: !GetAtt KMSKey.KeyId
```

#### JSON
<a name="aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "CloudFormation Template for the RDS Custom for Oracle",
    "Parameters": {
        "BucketName": {
            "Type": "String",
            "MinLength": 3,
            "MaxLength": 63,
            "AllowedPattern": "[a-zA-Z0-9.-]*",
            "Description": "S3 bucket name containing Oracle installation files"
        },
        "CEVS3Prefix": {
            "Type": "String",
            "Default": "oracle_cev"
        },
        "RDSSG": {
            "Type": "AWS::SSM::Parameter::Value<String>",
            "Default": "RDSSGParameter"
        },
        "KMSParameter": {
            "Type": "AWS::SSM::Parameter::Value<String>",
            "Default": "KMSParameter"
        },
        "CEVCreation": {
            "Description": "Please select the option \"yes\" for creating the CEV , if not leave it default for creating one for you",
            "Type": "String",
            "Default": "Yes"
        },
        "DBInstanceIdentifier": {
            "Description": "RDS Instance Name for Single AZ",
            "Type": "String",
            "Default": "rds-custom"
        }
    },
    "Conditions": {
        "ShouldAddCEV": {
            "Fn::Equals": [
                {
                    "Ref": "CEVCreation"
                },
                "Yes"
            ]
        }
    },
    "Resources": {
        "SSMExecutionRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "RoleName": {
                    "Fn::Join": [
                        "-",
                        [
                            "SSM-Execution-Role",
                            {
                                "Fn::Select": [
                                    4,
                                    {
                                        "Fn::Split": [
                                            "-",
                                            {
                                                "Fn::Select": [
                                                    2,
                                                    {
                                                        "Fn::Split": [
                                                            "/",
                                                            {
                                                                "Ref": "AWS::StackId"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Fn::Sub": "${AWS::Region}"
                            }
                        ]
                    ]
                },
                "ManagedPolicyArns": [
                    {
                        "Fn::Sub": "arn:${AWS::Partition}:iam::aws:policy/service-role/AmazonSSMAutomationRole"
                    },
                    "arn:aws:iam::aws:policy/AmazonRDSFullAccess",
                    "arn:aws:iam::aws:policy/AmazonEC2FullAccess",
                    "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
                ],
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "ec2.amazonaws.com",
                                    "ssm.amazonaws.com"
                                ]
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                }
            }
        },
        "EC2Role": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "Path": "/",
                "RoleName": {
                    "Fn::Join": [
                        "-",
                        [
                            "EC2-Role",
                            {
                                "Fn::Select": [
                                    4,
                                    {
                                        "Fn::Split": [
                                            "-",
                                            {
                                                "Fn::Select": [
                                                    2,
                                                    {
                                                        "Fn::Split": [
                                                            "/",
                                                            {
                                                                "Ref": "AWS::StackId"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Fn::Sub": "${AWS::Region}"
                            }
                        ]
                    ]
                },
                "AssumeRolePolicyDocument": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"ec2.amazonaws.com\"},\"Action\":\"sts:AssumeRole\"}]}",
                "MaxSessionDuration": 43200,
                "ManagedPolicyArns": [
                    "arn:aws:iam::aws:policy/AmazonRDSFullAccess",
                    "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore",
                    "arn:aws:iam::aws:policy/IAMReadOnlyAccess"
                ],
                "Description": "Allows Lambda functions to call AWS services on your behalf.",
                "Policies": [
                    {
                        "PolicyName": {
                            "Fn::Join": [
                                "-",
                                [
                                    "cev-policy-1",
                                    {
                                        "Fn::Select": [
                                            4,
                                            {
                                                "Fn::Split": [
                                                    "-",
                                                    {
                                                        "Fn::Select": [
                                                            2,
                                                            {
                                                                "Fn::Split": [
                                                                    "/",
                                                                    {
                                                                        "Ref": "AWS::StackId"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "Fn::Sub": "${AWS::Region}"
                                    }
                                ]
                            ]
                        },
                        "PolicyDocument": {
                            "Version": "2012-10-17"		 	 	 ,
                            "Statement": [
                                {
                                    "Sid": "CreateKmsGrant",
                                    "Effect": "Allow",
                                    "Action": [
                                        "kms:DescribeKey",
                                        "kms:CreateGrant"
                                    ],
                                    "Resource": "*"
                                },
                                {
                                    "Sid": "CreateS3Bucket",
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:CreateBucket",
                                        "s3:PutBucketPolicy",
                                        "s3:PutBucketObjectLockConfiguration",
                                        "s3:PutBucketVersioning"
                                    ],
                                    "Resource": "arn:aws:s3:::do-not-delete-rds-custom-*"
                                },
                                {
                                    "Sid": "AccessToS3MediaBucket",
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:GetObjectAcl",
                                        "s3:GetObject",
                                        "s3:GetObjectTagging",
                                        "s3:ListBucket"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:s3:::${BucketName}"
                                        },
                                        {
                                           "Fn::Sub": "arn:${AWS::Partition}:s3:::${BucketName}/*"
                                        }
                                    ]
                                },
                                {
                                    "Sid": "PermissionForByom",
                                    "Effect": "Allow",
                                    "Action": [
                                        "mediaimport:CreateDatabaseBinarySnapshot"
                                    ],
                                    "Resource": "*"
                                },
                                {
                                    "Sid": "CreateServiceLinkedRole",
                                    "Effect": "Allow",
                                    "Action": [
                                        "iam:CreateServiceLinkedRole"
                                    ],
                                    "Resource": "arn:aws:iam::*:role/aws-service-role/custom.rds.amazonaws.com/AWSServiceRoleForRDSCustom"
                                }
                            ]
                        }
                    },
                    {
                        "PolicyName": {
                            "Fn::Join": [
                                "-",
                                [
                                    "cev-policy-2",
                                    {
                                        "Fn::Select": [
                                            4,
                                            {
                                                "Fn::Split": [
                                                    "-",
                                                    {
                                                        "Fn::Select": [
                                                            2,
                                                            {
                                                                "Fn::Split": [
                                                                    "/",
                                                                    {
                                                                        "Ref": "AWS::StackId"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "Fn::Sub": "${AWS::Region}"
                                    }
                                ]
                            ]
                        },
                        "PolicyDocument": {
                            "Version": "2012-10-17"		 	 	 ,
                            "Statement": [
                                {
                                    "Sid": "ValidateIamRole",
                                    "Effect": "Allow",
                                    "Action": "iam:SimulatePrincipalPolicy",
                                    "Resource": "*"
                                },
                                {
                                    "Sid": "CreateCloudTrail",
                                    "Effect": "Allow",
                                    "Action": [
                                        "cloudtrail:CreateTrail",
                                        "cloudtrail:StartLogging"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:cloudtrail:*:*:trail/do-not-delete-rds-custom-*"
                                        }
                                    ]
                                },
                                {
                                    "Sid": "CreateCloudWatchLogStreamAndPushEvents",
                                    "Effect": "Allow",
                                    "Action": [
                                        "logs:CreateLogStream",
                                        "logs:CreateLogGroup",
                                        "logs:DescribeLogStreams",
                                        "logs:GetLogEvents",
                                        "logs:PutLogEvents"
                                    ],
                                    "Resource": "*"
                                },
                                {
                                    "Sid": "IAMPassRole",
                                    "Effect": "Allow",
                                    "Action": [
                                        "iam:PassRole"
                                    ],
                                    "Resource": "arn:aws:iam::*:role/AWSRDSCustomInstanceRole*"
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "CEVWaithandle": {
            "Condition": "ShouldAddCEV",
            "DependsOn": "CustomOracleJanPatch",
            "Type": "AWS::CloudFormation::WaitConditionHandle"
        },
        "WaitHandle": {
            "Type": "AWS::CloudFormation::WaitConditionHandle"
        },
        "WaitCondition": {
            "Type": "AWS::CloudFormation::WaitCondition",
            "Properties": {
                "Handle": {
                    "Fn::If": [
                        "ShouldAddCEV",
                        {
                            "Ref": "CEVWaithandle"
                        },
                        {
                            "Ref": "WaitHandle"
                        }
                    ]
                },
                "Timeout": "1",
                "Count": 0
            }
        },
        "RDSCustomSecret": {
            "Type": "AWS::SecretsManager::Secret",
            "Properties": {
                "Name": {
                    "Fn::Sub": "${AWS::StackName}-rds-custom-secret"
                },
                "Description": "RDS Custom Oracle Admin Password",
                "GenerateSecretString": {
                    "SecretStringTemplate": "{\"username\": \"oraadmin\"}",
                    "GenerateStringKey": "password",
                    "PasswordLength": 16,
                    "ExcludeCharacters": "\"@/\\"
                }
            }
        },
        "CustomOracleJanPatch": {
            "DependsOn": "SSMExecutionRole",
            "Condition": "ShouldAddCEV",
            "Type": "AWS::RDS::CustomDBEngineVersion",
            "Properties": {
                "DatabaseInstallationFilesS3BucketName": {
                    "Ref": "BucketName"
                },
                "DatabaseInstallationFilesS3Prefix": {
                    "Ref": "CEVS3Prefix"
                },
                "Description": "CEV for RDS custom for Oracle",
                "Engine": "custom-oracle-ee",
                "EngineVersion": "19.18-rdscustom-oracle-jan23psu-cev",
                "KMSKeyId": {
                    "Ref": "KMSParameter"
                },
                "Manifest": "{\"mediaImportTemplateVersion\":\"2020-08-14\",\"databaseInstallationFileNames\":[\"V982063-01.zip\"],\"opatchFileNames\":[\"p6880880_190000_Linux-x86-64.zip\"],\"psuRuPatchFileNames\": [\"p34765931_190000_Linux-x86-64.zip\",\"p34786990_190000_Linux-x86-64.zip\"],\"otherPatchFileNames\": [\"p35099667_190000_Linux-x86-64.zip\",\"p35099674_190000_Generic.zip\",\"p28730253_190000_Linux-x86-64.zip\",\"p29213893_1918000DBRU_Generic.zip\",\"p33125873_1918000DBRU_Linux-x86-64.zip\",\"p35012866_1918000DBRU_Linux-x86-64.zip\"]}"
            }
        },
        "CustomOracleAprCOHMTPatch": {
            "DependsOn": "SSMExecutionRole",
            "Condition": "ShouldAddCEV",
            "Type": "AWS::RDS::CustomDBEngineVersion",
            "Properties": {
                "DatabaseInstallationFilesS3BucketName": {
                    "Ref": "BucketName"
                },
                "DatabaseInstallationFilesS3Prefix": {
                    "Ref": "CEVS3Prefix"
                },
                "Description": "CEV for RDS custom for Oracle",
                "Engine": "custom-oracle-ee-cdb",
                "EngineVersion": "19.19-custom-oracle-home-mt",
                "KMSKeyId": {
                    "Ref": "KMSParameter"
                },
                "Manifest": "{\"mediaImportTemplateVersion\":\"2020-08-14\",\"databaseInstallationFileNames\":[\"V982063-01.zip\"],\"opatchFileNames\":[\"p6880880_190000_Linux-x86-64.zip\"],\"psuRuPatchFileNames\": [\"p35042068_190000_Linux-x86-64.zip\",\"p35050341_190000_Linux-x86-64.zip\"],\"otherPatchFileNames\": [\"p28730253_190000_Linux-x86-64.zip\",\"p29213893_1919000DBRU_Generic.zip\",\"p33125873_1919000DBRU_Linux-x86-64.zip\",\"p35220732_190000_Linux-x86-64.zip\",\"p35239280_190000_Generic.zip\"],\"installationParameters\": { \"unixGroupName\": \"dba\",\"unixGroupId\": 65789,\"unixUname\": \"oracle\",\"unixUid\": 6758,\"oracleHome\": \"/opt/oracle/product/19.19/dbhome_1\",\"oracleBase\": \"/opt/oracle\"}}"
            }
        },
        "CustomOracleAprPatch": {
            "DependsOn": "SSMExecutionRole",
            "Condition": "ShouldAddCEV",
            "Type": "AWS::RDS::CustomDBEngineVersion",
            "Properties": {
                "DatabaseInstallationFilesS3BucketName": {
                    "Ref": "BucketName"
                },
                "DatabaseInstallationFilesS3Prefix": {
                    "Ref": "CEVS3Prefix"
                },
                "Description": "CEV for RDS custom for Oracle",
                "Engine": "custom-oracle-ee",
                "EngineVersion": "19.19-rdscustom-oracle-apr23psu-cev",
                "KMSKeyId": {
                    "Ref": "KMSParameter"
                },
                "Manifest": "{\"mediaImportTemplateVersion\":\"2020-08-14\",\"databaseInstallationFileNames\":[\"V982063-01.zip\"],\"opatchFileNames\":[\"p6880880_190000_Linux-x86-64.zip\"],\"psuRuPatchFileNames\": [\"p35042068_190000_Linux-x86-64.zip\",\"p35050341_190000_Linux-x86-64.zip\"],\"otherPatchFileNames\": [\"p28730253_190000_Linux-x86-64.zip\",\"p29213893_1919000DBRU_Generic.zip\",\"p33125873_1919000DBRU_Linux-x86-64.zip\",\"p35220732_190000_Linux-x86-64.zip\",\"p35239280_190000_Generic.zip\"]}"
            }
        },
        "RDSDBInstance": {
            "DependsOn": "WaitCondition",
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "AllocatedStorage": 40,
                "DBInstanceIdentifier": {
                    "Fn::Sub": "${DBInstanceIdentifier}-saz"
                },
                "AutoMinorVersionUpgrade": false,
                "CustomIAMInstanceProfile": "AWSRDSCustomInstanceProfileForRdsCustomInstance",
                "DBInstanceClass": "db.m5.large",
                "DBSubnetGroupName": "rds-custom-private",
                "Engine": "custom-oracle-ee",
                "EngineVersion": "19.18-rdscustom-oracle-jan23psu-cev",
                "KmsKeyId": {
                    "Ref": "KMSParameter"
                },
                "MasterUsername": {
                    "Fn::Sub": "{{resolve:secretsmanager:${RDSCustomSecret}:SecretString:username}}"
                },
                "MasterUserPassword": {
                    "Fn::Sub": "{{resolve:secretsmanager:${RDSCustomSecret}:SecretString:password}}"
                },
                "StorageEncrypted": "true",
                "VPCSecurityGroups": [
                    {
                        "Ref": "RDSSG"
                    }
                ],
                "DBName": "ORCL",
                "PreferredBackupWindow": "03:00-04:00",
                "PreferredMaintenanceWindow": "Mon:05:00-Mon:06:00",
                "PubliclyAccessible": false
            }
        },
        "HARDSDBInstance": {
            "DependsOn": "WaitCondition",
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "AllocatedStorage": 40,
                "DBInstanceIdentifier": {
                    "Fn::Sub": "${DBInstanceIdentifier}-maz"
                },
                "AutoMinorVersionUpgrade": false,
                "CustomIAMInstanceProfile": "AWSRDSCustomInstanceProfileForRdsCustomInstance",
                "DBInstanceClass": "db.m5.large",
                "DBSubnetGroupName": "rds-custom-private",
                "Engine": "custom-oracle-ee",
                "EngineVersion": "19.19-rdscustom-oracle-apr23psu-cev",
                "KmsKeyId": {
                    "Ref": "KMSParameter"
                },
                "MasterUsername": {
                    "Fn::Sub": "{{resolve:secretsmanager:${RDSCustomSecret}:SecretString:username}}"
                },
                "MasterUserPassword": {
                    "Fn::Sub": "{{resolve:secretsmanager:${RDSCustomSecret}:SecretString:password}}"
                },
                "StorageEncrypted": "true",
                "MultiAZ": "true",
                "VPCSecurityGroups": [
                    {
                        "Ref": "RDSSG"
                    }
                ],
                "DBName": "ORCL",
                "PreferredBackupWindow": "03:00-04:00",
                "PreferredMaintenanceWindow": "Mon:05:00-Mon:06:00",
                "PubliclyAccessible": false
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones--yaml"></a>

```
# AWSTemplateFormatVersion: 2010-09-09
# RDS Custom for AWS RDS Oracle
# 06/15/2025 created by Sharath Chandra Kampili

AWSTemplateFormatVersion: '2010-09-09'
Description: CloudFormation Template for the RDS Custom for Oracle

Parameters:
  BucketName:
    Type: "String"
    MinLength: 3
    MaxLength: 63
    AllowedPattern: ^[a-z0-9][a-z0-9.-]*[a-z0-9]$
    Description: "S3 bucket name (must be between 3 and 63 characters)"
  CEVS3Prefix:
    Type: "String"
    Default: "oracle_cev"
  RDSSG:
    Type: 'AWS::SSM::Parameter::Value<String>'
    Default: RDSSGParameter
  KMSParameter:
    Type: 'AWS::SSM::Parameter::Value<String>'
    Default: KMSParameter
  CEVCreation:
    Description: Please select the option "yes" for creating the CEV , if not leave it default for creating one for you
    Type: String
    Default: "Yes"
  DBInstanceIdentifier:
    Description: RDS Instance Name for Single AZ
    Type: String
    Default: "rds-custom"

Conditions:
  ShouldAddCEV: !Equals [ !Ref CEVCreation, "Yes" ]

Resources:

  SSMExecutionRole:
    Type : AWS::IAM::Role
    Properties:
      RoleName: !Join ['-', ['SSM-Execution-Role', !Select [4, !Split ['-', !Select [2, !Split ['/', !Ref AWS::StackId]]]],!Sub "${AWS::Region}"]]
      ManagedPolicyArns:
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/service-role/AmazonSSMAutomationRole'
        - arn:aws:iam::aws:policy/AmazonRDSFullAccess
        - arn:aws:iam::aws:policy/AmazonEC2FullAccess
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
        - Effect: "Allow"
          Principal:
            Service:
            - "ec2.amazonaws.com"
            - "ssm.amazonaws.com"
          Action: "sts:AssumeRole"

  RDSSecret:
    Type: 'AWS::SecretsManager::Secret'
    Properties:
      Name: !Sub '${AWS::StackName}-rds-credentials'
      Description: 'RDS Custom Oracle database credentials'
      GenerateSecretString:
        SecretStringTemplate: '{"username": "oraadmin"}'
        GenerateStringKey: "password"
        PasswordLength: 16
        ExcludeCharacters: '"@/\\'

  EC2Role:
    Type: "AWS::IAM::Role"
    Properties:
      Path: "/"
      RoleName: !Join ['-', ['EC2-Role', !Select [4, !Split ['-', !Select [2, !Split ['/', !Ref AWS::StackId]]]],!Sub "${AWS::Region}"]]
      AssumeRolePolicyDocument: '{"Version": "2012-10-17"		 	 	 ,"Statement":[{"Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},"Action":"sts:AssumeRole"}]}'
      MaxSessionDuration: 43200
      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/AmazonRDSFullAccess"
        - "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
        - "arn:aws:iam::aws:policy/IAMReadOnlyAccess"
      Description: "Allows Lambda functions to call AWS services on your behalf."
      Policies:
        - PolicyName: !Join ['-', ['cev-policy-1', !Select [4, !Split ['-', !Select [2, !Split ['/', !Ref AWS::StackId]]]],!Sub "${AWS::Region}"]]
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Sid: 'CreateKmsGrant'
              Effect: 'Allow'
              Action:
              - 'kms:DescribeKey'
              - 'kms:CreateGrant'
              Resource: '*'
            - Sid: 'CreateS3Bucket'
              Effect: 'Allow'
              Action:
              - 's3:CreateBucket'
              - 's3:PutBucketPolicy'
              - 's3:PutBucketObjectLockConfiguration'
              - 's3:PutBucketVersioning'
              Resource: "arn:aws:s3:::do-not-delete-rds-custom-*"
            - Sid: 'AccessToS3MediaBucket'
              Effect: 'Allow'
              Action:
              - 's3:GetObjectAcl'
              - 's3:GetObject'
              - 's3:GetObjectTagging'
              - 's3:ListBucket'
              Resource:
              - !Sub 'arn:${AWS::Partition}:s3:::${BucketName}'
              - !Sub 'arn:${AWS::Partition}:s3:::${BucketName}/*'
            - Sid: 'PermissionForByom'
              Effect: 'Allow'
              Action:
              - 'mediaimport:CreateDatabaseBinarySnapshot'
              Resource: "*"
            - Sid: 'CreateServiceLinkedRole'
              Effect: 'Allow'
              Action:
              - 'iam:CreateServiceLinkedRole'
              Resource: "arn:aws:iam::*:role/aws-service-role/custom.rds.amazonaws.com/AWSServiceRoleForRDSCustom"
        - PolicyName: !Join ['-', ['cev-policy-2', !Select [4, !Split ['-', !Select [2, !Split ['/', !Ref AWS::StackId]]]],!Sub "${AWS::Region}"]]
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Sid: 'ValidateIamRole'
              Effect: 'Allow'
              Action: 'iam:SimulatePrincipalPolicy'
              Resource: '*'
            - Sid: 'CreateCloudTrail'
              Effect: 'Allow'
              Action:
                - 'cloudtrail:CreateTrail'
                - 'cloudtrail:StartLogging'
              Resource:
                  - Fn::Sub: >-
                      arn:${AWS::Partition}:cloudtrail:*:*:trail/do-not-delete-rds-custom-*
            - Sid: 'CreateCloudWatchLogStreamAndPushEvents'
              Effect: 'Allow'
              Action:
                - 'logs:CreateLogStream'
                - 'logs:CreateLogGroup'
                - 'logs:DescribeLogStreams'
                - 'logs:GetLogEvents'
                - 'logs:PutLogEvents'
              Resource: '*'
            - Sid: 'IAMPassRole'
              Effect: 'Allow'
              Action:
                - 'iam:PassRole'
              Resource: arn:aws:iam::*:role/AWSRDSCustomInstanceRole*
            - Sid: 'SecretsManagerAccess'
              Effect: 'Allow'
              Action:
                - 'secretsmanager:GetSecretValue'
                - 'secretsmanager:DescribeSecret'
              Resource: !Ref RDSSecret

  CEVWaithandle:
    Condition: ShouldAddCEV
    DependsOn: CustomOracleJanPatch
    Type: "AWS::CloudFormation::WaitConditionHandle"

  WaitHandle:
    Type: "AWS::CloudFormation::WaitConditionHandle"

  WaitCondition:
    Type: "AWS::CloudFormation::WaitCondition"
    Properties:
      Handle: !If [ShouldAddCEV, !Ref CEVWaithandle , !Ref WaitHandle ]
      Timeout: "1"
      Count: 0

  CustomOracleJanPatch:
    DependsOn: SSMExecutionRole
    Condition: ShouldAddCEV
    Type: AWS::RDS::CustomDBEngineVersion
    Properties:
      DatabaseInstallationFilesS3BucketName: !Ref BucketName
      DatabaseInstallationFilesS3Prefix: !Ref CEVS3Prefix
      Description: CEV for RDS custom for Oracle
      Engine: custom-oracle-ee
      EngineVersion: 19.18-rdscustom-oracle-jan23psu-cev
      KMSKeyId: !Ref KMSParameter
      Manifest: '{"mediaImportTemplateVersion":"2020-08-14","databaseInstallationFileNames":["V982063-01.zip"],"opatchFileNames":["p6880880_190000_Linux-x86-64.zip"],"psuRuPatchFileNames": ["p34765931_190000_Linux-x86-64.zip","p34786990_190000_Linux-x86-64.zip"],"otherPatchFileNames": ["p35099667_190000_Linux-x86-64.zip","p35099674_190000_Generic.zip","p28730253_190000_Linux-x86-64.zip","p29213893_1918000DBRU_Generic.zip","p33125873_1918000DBRU_Linux-x86-64.zip","p35012866_1918000DBRU_Linux-x86-64.zip"]}'

  CustomOracleAprCOHMTPatch:
    DependsOn: SSMExecutionRole
    Condition: ShouldAddCEV
    Type: AWS::RDS::CustomDBEngineVersion
    Properties:
      DatabaseInstallationFilesS3BucketName:  !Ref BucketName
      DatabaseInstallationFilesS3Prefix: !Ref CEVS3Prefix
      Description: CEV for RDS custom for Oracle
      Engine: custom-oracle-ee-cdb
      EngineVersion: 19.19-custom-oracle-home-mt
      KMSKeyId: !Ref KMSParameter
      Manifest: '{"mediaImportTemplateVersion":"2020-08-14","databaseInstallationFileNames":["V982063-01.zip"],"opatchFileNames":["p6880880_190000_Linux-x86-64.zip"],"psuRuPatchFileNames": ["p35042068_190000_Linux-x86-64.zip","p35050341_190000_Linux-x86-64.zip"],"otherPatchFileNames": ["p28730253_190000_Linux-x86-64.zip","p29213893_1919000DBRU_Generic.zip","p33125873_1919000DBRU_Linux-x86-64.zip","p35220732_190000_Linux-x86-64.zip","p35239280_190000_Generic.zip"],"installationParameters": { "unixGroupName": "dba","unixGroupId": 65789,"unixUname": "oracle","unixUid": 6758,"oracleHome": "/opt/oracle/product/19.19/dbhome_1","oracleBase": "/opt/oracle"}}'

  CustomOracleAprPatch:
    DependsOn: SSMExecutionRole
    Condition: ShouldAddCEV
    Type: AWS::RDS::CustomDBEngineVersion
    Properties:
      DatabaseInstallationFilesS3BucketName:  !Ref BucketName
      DatabaseInstallationFilesS3Prefix: !Ref CEVS3Prefix
      Description: CEV for RDS custom for Oracle
      Engine: custom-oracle-ee
      EngineVersion: 19.19-rdscustom-oracle-apr23psu-cev
      KMSKeyId: !Ref KMSParameter
      Manifest: '{"mediaImportTemplateVersion":"2020-08-14","databaseInstallationFileNames":["V982063-01.zip"],"opatchFileNames":["p6880880_190000_Linux-x86-64.zip"],"psuRuPatchFileNames": ["p35042068_190000_Linux-x86-64.zip","p35050341_190000_Linux-x86-64.zip"],"otherPatchFileNames": ["p28730253_190000_Linux-x86-64.zip","p29213893_1919000DBRU_Generic.zip","p33125873_1919000DBRU_Linux-x86-64.zip","p35220732_190000_Linux-x86-64.zip","p35239280_190000_Generic.zip"]}'

  RDSDBInstance:
    DependsOn: WaitCondition
    Type: AWS::RDS::DBInstance
    Properties:
      AllocatedStorage: 40
      DBInstanceIdentifier: !Sub '${DBInstanceIdentifier}-saz'
      AutoMinorVersionUpgrade: false
      CustomIAMInstanceProfile: AWSRDSCustomInstanceProfileForRdsCustomInstance
      DBInstanceClass: db.m5.large
      DBSubnetGroupName: rds-custom-private
      Engine: custom-oracle-ee
      EngineVersion: 19.18-rdscustom-oracle-jan23psu-cev
      KmsKeyId: !Ref KMSParameter
      MasterUsername: !Sub '{{resolve:secretsmanager:${RDSSecret}:SecretString:username}}'
      MasterUserPassword: !Sub '{{resolve:secretsmanager:${RDSSecret}:SecretString:password}}'
      StorageEncrypted: 'true'
      VPCSecurityGroups:
        - !Ref RDSSG
      DBName: ORCL
      PreferredBackupWindow: '03:00-04:00'
      PreferredMaintenanceWindow: 'Mon:05:00-Mon:06:00'
      PubliclyAccessible: false

  HARDSDBInstance:
    DependsOn: WaitCondition
    Type: AWS::RDS::DBInstance
    Properties:
      AllocatedStorage: 40
      DBInstanceIdentifier: !Sub '${DBInstanceIdentifier}-maz'
      AutoMinorVersionUpgrade: false
      CustomIAMInstanceProfile: AWSRDSCustomInstanceProfileForRdsCustomInstance
      DBInstanceClass: db.m5.large
      DBSubnetGroupName: rds-custom-private
      Engine: custom-oracle-ee
      EngineVersion: 19.19-rdscustom-oracle-apr23psu-cev
      KmsKeyId: !Ref KMSParameter
      MasterUsername: !Sub '{{resolve:secretsmanager:${RDSSecret}:SecretString:username}}'
      MasterUserPassword: !Sub '{{resolve:secretsmanager:${RDSSecret}:SecretString:password}}'
      StorageEncrypted: 'true'
      MultiAZ: 'true'
      VPCSecurityGroups:
        - !Ref RDSSG
      DBName: ORCL
      PreferredBackupWindow: '03:00-04:00'
      PreferredMaintenanceWindow: 'Mon:05:00-Mon:06:00'
      PubliclyAccessible: false
```

### Creating a Secrets Manager secret for a master password
<a name="aws-resource-rds-dbinstance--examples--Creating_a_Secrets_Manager_secret_for_a_master_password"></a>

The following example creates an AWS::RDS::DBInstance resource with a managed master user and password. The secret used to authenticate the DB instance is shown in the `Secret` stack output. You can remove this output if you don't need to pass the value to another CloudFormation stack.

For more information about managing passwords with Secrets Manager, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide*.

#### JSON
<a name="aws-resource-rds-dbinstance--examples--Creating_a_Secrets_Manager_secret_for_a_master_password--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "A sample template",
    "Resources": {
        "MyInstance": {
            "Properties": {
                "MasterUsername": "masteruser",
                "DBInstanceClass": "db.t3.micro",
                "Engine": "mysql",
                "AllocatedStorage": 5,
                "AutoMinorVersionUpgrade": false,
                "ManageMasterUserPassword": true,
                "MasterUserSecret": {
                    "KmsKeyId": {
                        "Ref": "KMSKey"
                    }
                }
            },
            "Type": "AWS::RDS::DBInstance"
        },
        "KMSKey": {
            "Type": "AWS::KMS::Key",
            "Properties": {
                "Description": "Manual test KMS key",
                "EnableKeyRotation": true,
                "KeyPolicy": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Id": {
                        "Ref": "AWS::StackName"
                    },
                    "Statement": [
                        {
                            "Sid": "Allow administration of the key",
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Sub": "arn:${AWS::Partition}:iam::${AWS::AccountId}:root"
                                }
                            },
                            "Action": [
                                "kms:*"
                            ],
                            "Resource": "*"
                        }
                    ]
                }
            }
        }
    },
    "Outputs": {
        "Secret": {
            "Value": {
                "Fn::GetAtt": "MyInstance.MasterUserSecret.SecretArn"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbinstance--examples--Creating_a_Secrets_Manager_secret_for_a_master_password--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  MyInstance:
    Properties:
      MasterUsername: "masteruser"
      DBInstanceClass: "db.t3.micro"
      Engine: "mysql"
      AllocatedStorage: 5
      AutoMinorVersionUpgrade: false
      ManageMasterUserPassword: true
      MasterUserSecret:
        KmsKeyId: !Ref KMSKey
    Type: "AWS::RDS::DBInstance"
  KMSKey:
    Type: 'AWS::KMS::Key'
    Properties:
      Description: Manual test KMS key
      EnableKeyRotation: True
      KeyPolicy:
        Version: "2012-10-17"
        Id: !Ref "AWS::StackName"
        Statement:
          - Sid: "Allow administration of the key"
            Effect: "Allow"
            Principal:
              AWS:
                Fn::Sub: 'arn:${AWS::Partition}:iam::${AWS::AccountId}:root'
            Action:
              - "kms:*"
            Resource: "*"

Outputs:
  Secret:
    Value:
      Fn::GetAtt: MyInstance.MasterUserSecret.SecretArn
```

### Creating a DB instance with self-managed Active Directory domain
<a name="aws-resource-rds-dbinstance--examples--Creating_a_DB_instance_with_self-managed_Active_Directory_domain"></a>

The following example creates a AWS CloudFormation stack with the AWS::RDS::DBInstance resource with Active Directory domain.

#### JSON
<a name="aws-resource-rds-dbinstance--examples--Creating_a_DB_instance_with_self-managed_Active_Directory_domain--json"></a>

```
{
    "Resources":
    {
        "RDSDBInstance":
        {
            "Type": "AWS::RDS::DBInstance",
            "Properties":
            {
                "AllocatedStorage": { "Ref" : "DBAllocatedStorage" },
                "DBInstanceClass": { "Ref" : "DBClass" },
                "DBSubnetGroupName": { "Ref" : "MyDBSubnetGroup" },
                "Engine": "sqlserver-ee",
                "LicenseModel": "license-included",
                "MasterUsername"    : { "Ref" : "DBUsername" },
                "MasterUserPassword": { "Ref" : "DBPassword" },
                "DomainAuthSecretArn": { "Ref" : "DomainSecretArn" },
                "DomainDnsIps":
                [
                    "10.0.0.1",
                    "10.0.0.2"
                ],
                "DomainFqdn": { "Ref" : "MyDomainFqdn" },
                "DomainOu": { "Ref" : "MyDomainOu" }
            },
            "UpdateReplacePolicy": "Delete",
            "DeletionPolicy": "Delete"
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbinstance--examples--Creating_a_DB_instance_with_self-managed_Active_Directory_domain--yaml"></a>

```
Resources:
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      AllocatedStorage: !Ref DBAllocatedStorage
      DBInstanceClass: !Ref DBClass
      DBSubnetGroupName: !Ref MyDBSubnetGroup
      Engine: sqlserver-ee
      LicenseModel: license-included
      MasterUsername: !Ref DBUsername
      MasterUserPassword: !Ref DBPassword
      DomainAuthSecretArn: !Ref DomainSecretArn
      DomainDnsIps:
        - 10.0.0.1
        - 10.0.0.2
      DomainFqdn: !Ref MyDomainFqdn
      DomainOu: !Ref MyDomainOu
    UpdateReplacePolicy: Delete
    DeletionPolicy: Delete
```
