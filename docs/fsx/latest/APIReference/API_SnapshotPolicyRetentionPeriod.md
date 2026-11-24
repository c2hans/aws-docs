---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapshotPolicyRetentionPeriod.html
---

# SnapshotPolicyRetentionPeriod

The length of time that snapshots created by this schedule are locked. This setting applies only to volumes that have snapshot locking enabled.

## Contents
<a name="API_SnapshotPolicyRetentionPeriod_Contents"></a>

 ** Type **   <a name="FSx-Type-SnapshotPolicyRetentionPeriod-Type"></a>
The unit of time for the retention period. If you set it to `INFINITE`, the snapshots are retained forever.
Type: String
Valid Values: `SECONDS | MINUTES | HOURS | DAYS | MONTHS | YEARS | INFINITE`
Required: Yes

 ** Value **   <a name="FSx-Type-SnapshotPolicyRetentionPeriod-Value"></a>
Defines the amount of time for the retention period. You can't set a value for `INFINITE`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_SnapshotPolicyRetentionPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapshotPolicyRetentionPeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapshotPolicyRetentionPeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapshotPolicyRetentionPeriod)
