---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoverySnapshot.html
---

# RecoverySnapshot
<a name="API_RecoverySnapshot"></a>

A snapshot of a Source Server used during recovery.

## Contents
<a name="API_RecoverySnapshot_Contents"></a>

 ** expectedTimestamp **   <a name="drs-Type-RecoverySnapshot-expectedTimestamp"></a>
The timestamp of when we expect the snapshot to be taken.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: Yes

 ** snapshotID **   <a name="drs-Type-RecoverySnapshot-snapshotID"></a>
The ID of the Recovery Snapshot.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `pit-[0-9a-zA-Z]{17}`
Required: Yes

 ** sourceServerID **   <a name="drs-Type-RecoverySnapshot-sourceServerID"></a>
The ID of the Source Server that the snapshot was taken for.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** ebsSnapshots **   <a name="drs-Type-RecoverySnapshot-ebsSnapshots"></a>
A list of EBS snapshots.
Type: Array of strings
Pattern: `snap-[0-9a-zA-Z]{17}`
Required: No

 ** timestamp **   <a name="drs-Type-RecoverySnapshot-timestamp"></a>
The actual timestamp that the snapshot was taken.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

## See Also
<a name="API_RecoverySnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoverySnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoverySnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoverySnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
