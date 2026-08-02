---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DatabaseStandbySummary.html
---

# DatabaseStandbySummary
<a name="API_DatabaseStandbySummary"></a>

A summary of a standby Autonomous Database in an Oracle Data Guard configuration.

## Contents
<a name="API_DatabaseStandbySummary_Contents"></a>

 ** availabilityDomain **   <a name="odb-Type-DatabaseStandbySummary-availabilityDomain"></a>
The availability domain of the standby Autonomous Database.
Type: String
Required: No

 ** lagTimeInSeconds **   <a name="odb-Type-DatabaseStandbySummary-lagTimeInSeconds"></a>
The time lag, in seconds, between the standby database and the primary database.
Type: Integer
Required: No

 ** maintenanceTargetComponent **   <a name="odb-Type-DatabaseStandbySummary-maintenanceTargetComponent"></a>
The component on the standby Autonomous Database that the current maintenance is being applied to.
Type: String
Required: No

 ** status **   <a name="odb-Type-DatabaseStandbySummary-status"></a>
The current status of the standby Autonomous Database.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS | STOPPING | STOPPED | STARTING | UNAVAILABLE | RESTORE_IN_PROGRESS | RESTORE_FAILED | BACKUP_IN_PROGRESS | SCALE_IN_PROGRESS | AVAILABLE_NEEDS_ATTENTION | RESTARTING | RECREATING | ROLE_CHANGE_IN_PROGRESS | UPGRADING | INACCESSIBLE | STANDBY`
Required: No

 ** statusReason **   <a name="odb-Type-DatabaseStandbySummary-statusReason"></a>
Additional information about the current status of the standby Autonomous Database, if applicable.
Type: String
Required: No

 ** timeDataGuardRoleChanged **   <a name="odb-Type-DatabaseStandbySummary-timeDataGuardRoleChanged"></a>
The date and time when the Oracle Data Guard role of the standby database last changed.
Type: Timestamp
Required: No

 ** timeDisasterRecoveryRoleChanged **   <a name="odb-Type-DatabaseStandbySummary-timeDisasterRecoveryRoleChanged"></a>
The date and time when the disaster recovery role of the standby database last changed.
Type: Timestamp
Required: No

 ** timeMaintenanceBegin **   <a name="odb-Type-DatabaseStandbySummary-timeMaintenanceBegin"></a>
The date and time when the next maintenance of the standby database begins.
Type: Timestamp
Required: No

 ** timeMaintenanceEnd **   <a name="odb-Type-DatabaseStandbySummary-timeMaintenanceEnd"></a>
The date and time when the next maintenance of the standby database ends.
Type: Timestamp
Required: No

## See Also
<a name="API_DatabaseStandbySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DatabaseStandbySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DatabaseStandbySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DatabaseStandbySummary)
