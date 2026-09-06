---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DisasterRecoveryConfiguration.html
---

# DisasterRecoveryConfiguration
<a name="API_DisasterRecoveryConfiguration"></a>

The disaster recovery configuration for an Autonomous Database.

## Contents
<a name="API_DisasterRecoveryConfiguration_Contents"></a>

 ** disasterRecoveryType **   <a name="odb-Type-DisasterRecoveryConfiguration-disasterRecoveryType"></a>
The type of disaster recovery configured for the Autonomous Database.
Type: String
Valid Values: `ADG | BACKUP_BASED`
Required: No

 ** isReplicateAutomaticBackups **   <a name="odb-Type-DisasterRecoveryConfiguration-isReplicateAutomaticBackups"></a>
Indicates whether automatic backups are replicated to the disaster recovery database.
Type: Boolean
Required: No

 ** isSnapshotStandby **   <a name="odb-Type-DisasterRecoveryConfiguration-isSnapshotStandby"></a>
Indicates whether the standby database is a snapshot standby.
Type: Boolean
Required: No

 ** timeSnapshotStandbyEnabledTill **   <a name="odb-Type-DisasterRecoveryConfiguration-timeSnapshotStandbyEnabledTill"></a>
The date and time until which the snapshot standby database remains enabled.
Type: Timestamp
Required: No

## See Also
<a name="API_DisasterRecoveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DisasterRecoveryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DisasterRecoveryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DisasterRecoveryConfiguration)
