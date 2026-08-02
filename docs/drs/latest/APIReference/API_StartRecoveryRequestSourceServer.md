---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_StartRecoveryRequestSourceServer.html
---

# StartRecoveryRequestSourceServer
<a name="API_StartRecoveryRequestSourceServer"></a>

An object representing the Source Server to recover.

## Contents
<a name="API_StartRecoveryRequestSourceServer_Contents"></a>

 ** sourceServerID **   <a name="drs-Type-StartRecoveryRequestSourceServer-sourceServerID"></a>
The ID of the Source Server you want to recover.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** recoverySnapshotID **   <a name="drs-Type-StartRecoveryRequestSourceServer-recoverySnapshotID"></a>
The ID of a Recovery Snapshot we want to recover from. Omit this field to launch from the latest data by taking an on-demand snapshot.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `pit-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_StartRecoveryRequestSourceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/StartRecoveryRequestSourceServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/StartRecoveryRequestSourceServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/StartRecoveryRequestSourceServer)
