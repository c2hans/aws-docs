---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_Parameters.html
---

# Parameters
<a name="API_Parameters"></a>

 **[Custom snapshot and AMI policies only]** Specifies optional parameters for snapshot and AMI policies. The set of valid parameters depends on the combination of policy type and target resource type.

If you choose to exclude boot volumes and you specify tags that consequently exclude all of the additional data volumes attached to an instance, then Amazon Data Lifecycle Manager will not create any snapshots for the affected instance, and it will emit a `SnapshotsCreateFailed` Amazon CloudWatch metric. For more information, see [Monitor your policies using Amazon CloudWatch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-dlm-cw-metrics.html).

## Contents
<a name="API_Parameters_Contents"></a>

 ** ExcludeBootVolume **   <a name="dlm-Type-Parameters-ExcludeBootVolume"></a>
 **[Custom snapshot policies that target instances only]** Indicates whether to exclude the root volume from multi-volume snapshot sets. The default is `false`. If you specify `true`, then the root volumes attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.
Type: Boolean
Required: No

 ** ExcludeDataVolumeTags **   <a name="dlm-Type-Parameters-ExcludeDataVolumeTags"></a>
 **[Custom snapshot policies that target instances only]** The tags used to identify data (non-root) volumes to exclude from multi-volume snapshot sets.
If you create a snapshot lifecycle policy that targets instances and you specify tags for this parameter, then data volumes with the specified tags that are attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** NoReboot **   <a name="dlm-Type-Parameters-NoReboot"></a>
 **[Custom AMI policies only]** Indicates whether targeted instances are rebooted when the lifecycle policy runs. `true` indicates that targeted instances are not rebooted when the policy runs. `false` indicates that target instances are rebooted when the policy runs. The default is `true` (instances are not rebooted).
Type: Boolean
Required: No

## See Also
<a name="API_Parameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/Parameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/Parameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/Parameters)
