---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceFailback.html
---

# RecoveryInstanceFailback
<a name="API_RecoveryInstanceFailback"></a>

An object representing failback related information of the Recovery Instance.

## Contents
<a name="API_RecoveryInstanceFailback_Contents"></a>

 ** agentLastSeenByServiceDateTime **   <a name="drs-Type-RecoveryInstanceFailback-agentLastSeenByServiceDateTime"></a>
The date and time the agent on the Recovery Instance was last seen by the service.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** elapsedReplicationDuration **   <a name="drs-Type-RecoveryInstanceFailback-elapsedReplicationDuration"></a>
The amount of time that the Recovery Instance has been replicating for.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** failbackClientID **   <a name="drs-Type-RecoveryInstanceFailback-failbackClientID"></a>
The ID of the failback client that this Recovery Instance is associated with.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** failbackClientLastSeenByServiceDateTime **   <a name="drs-Type-RecoveryInstanceFailback-failbackClientLastSeenByServiceDateTime"></a>
The date and time that the failback client was last seen by the service.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** failbackInitiationTime **   <a name="drs-Type-RecoveryInstanceFailback-failbackInitiationTime"></a>
The date and time that the failback initiation started.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** failbackJobID **   <a name="drs-Type-RecoveryInstanceFailback-failbackJobID"></a>
The Job ID of the last failback log for this Recovery Instance.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `drsjob-[0-9a-zA-Z]{17}`
Required: No

 ** failbackLaunchType **   <a name="drs-Type-RecoveryInstanceFailback-failbackLaunchType"></a>
The launch type (Recovery / Drill) of the last launch for the failback replication of this recovery instance.
Type: String
Valid Values: `RECOVERY | DRILL`
Required: No

 ** failbackToOriginalServer **   <a name="drs-Type-RecoveryInstanceFailback-failbackToOriginalServer"></a>
Whether we are failing back to the original Source Server for this Recovery Instance.
Type: Boolean
Required: No

 ** firstByteDateTime **   <a name="drs-Type-RecoveryInstanceFailback-firstByteDateTime"></a>
The date and time of the first byte that was replicated from the Recovery Instance.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** state **   <a name="drs-Type-RecoveryInstanceFailback-state"></a>
The state of the failback process that this Recovery Instance is in.
Type: String
Valid Values: `FAILBACK_NOT_STARTED | FAILBACK_IN_PROGRESS | FAILBACK_READY_FOR_LAUNCH | FAILBACK_COMPLETED | FAILBACK_ERROR | FAILBACK_NOT_READY_FOR_LAUNCH | FAILBACK_LAUNCH_STATE_NOT_AVAILABLE`
Required: No

## See Also
<a name="API_RecoveryInstanceFailback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryInstanceFailback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryInstanceFailback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryInstanceFailback)
