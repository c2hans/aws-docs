---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryPlanExecutionSourceServer.html
---

# RecoveryPlanExecutionSourceServer
<a name="API_RecoveryPlanExecutionSourceServer"></a>

A source server with a specific recovery snapshot for plan execution.

## Contents
<a name="API_RecoveryPlanExecutionSourceServer_Contents"></a>

 ** recoverySnapshotID **   <a name="drs-Type-RecoveryPlanExecutionSourceServer-recoverySnapshotID"></a>
The ID of the recovery snapshot to use.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `pit-[0-9a-zA-Z]{17}`
Required: Yes

 ** sourceServerID **   <a name="drs-Type-RecoveryPlanExecutionSourceServer-sourceServerID"></a>
The ID of the source server.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## See Also
<a name="API_RecoveryPlanExecutionSourceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryPlanExecutionSourceServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryPlanExecutionSourceServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryPlanExecutionSourceServer)
