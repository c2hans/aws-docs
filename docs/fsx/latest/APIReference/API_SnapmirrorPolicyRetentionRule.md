---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapmirrorPolicyRetentionRule.html
---

# SnapmirrorPolicyRetentionRule

Specifies a snapshot retention rule for an Amazon FSx for NetApp ONTAP SnapMirror policy.

## Contents
<a name="API_SnapmirrorPolicyRetentionRule_Contents"></a>

 ** Count **   <a name="FSx-Type-SnapmirrorPolicyRetentionRule-Count"></a>
The number of snapshots with the label to retain on the destination volume.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1019.
Required: Yes

 ** Label **   <a name="FSx-Type-SnapmirrorPolicyRetentionRule-Label"></a>
The SnapMirror label of the snapshots that the rule applies to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 31.
Required: Yes

 ** CreationSchedule **   <a name="FSx-Type-SnapmirrorPolicyRetentionRule-CreationSchedule"></a>
The name of the ONTAP schedule on which SnapMirror creates snapshots with the label directly on the destination volume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_:.-]{1,256}$`
Required: No

## See Also
<a name="API_SnapmirrorPolicyRetentionRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapmirrorPolicyRetentionRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapmirrorPolicyRetentionRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapmirrorPolicyRetentionRule)
