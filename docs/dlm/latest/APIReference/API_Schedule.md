---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_Schedule.html
---

# Schedule
<a name="API_Schedule"></a>

 **[Custom snapshot and AMI policies only]** Specifies a schedule for a snapshot or AMI lifecycle policy.

## Contents
<a name="API_Schedule_Contents"></a>

 ** ArchiveRule **   <a name="dlm-Type-Schedule-ArchiveRule"></a>
 **[Custom snapshot policies that target volumes only]** The snapshot archiving rule for the schedule. When you specify an archiving rule, snapshots are automatically moved from the standard tier to the archive tier once the schedule's retention threshold is met. Snapshots are then retained in the archive tier for the archive retention period that you specify.
For more information about using snapshot archiving, see [Considerations for snapshot lifecycle policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-ami-policy.html#dlm-archive).
Type: [ArchiveRule](API_ArchiveRule.md) object
Required: No

 ** CopyTags **   <a name="dlm-Type-Schedule-CopyTags"></a>
Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.
Type: Boolean
Required: No

 ** CreateRule **   <a name="dlm-Type-Schedule-CreateRule"></a>
The creation rule.
Type: [CreateRule](API_CreateRule.md) object
Required: No

 ** CrossRegionCopyRules **   <a name="dlm-Type-Schedule-CrossRegionCopyRules"></a>
Specifies a rule for copying snapshots or AMIs across Regions.
You can't specify cross-Region copy rules for policies that create snapshots on an Outpost or in a Local Zone. If the policy creates snapshots in a Region, then snapshots can be copied to up to three Regions or Outposts.
Type: Array of [CrossRegionCopyRule](API_CrossRegionCopyRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** DeprecateRule **   <a name="dlm-Type-Schedule-DeprecateRule"></a>
 **[Custom AMI policies only]** The AMI deprecation rule for the schedule.
Type: [DeprecateRule](API_DeprecateRule.md) object
Required: No

 ** FastRestoreRule **   <a name="dlm-Type-Schedule-FastRestoreRule"></a>
 **[Custom snapshot policies only]** The rule for enabling fast snapshot restore.
Type: [FastRestoreRule](API_FastRestoreRule.md) object
Required: No

 ** Name **   <a name="dlm-Type-Schedule-Name"></a>
The name of the schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 120.
Pattern: `[0-9A-Za-z _-]+`
Required: No

 ** RetainRule **   <a name="dlm-Type-Schedule-RetainRule"></a>
The retention rule for snapshots or AMIs created by the policy.
Type: [RetainRule](API_RetainRule.md) object
Required: No

 ** ShareRules **   <a name="dlm-Type-Schedule-ShareRules"></a>
 **[Custom snapshot policies only]** The rule for sharing snapshots with other AWS accounts.
Type: Array of [ShareRule](API_ShareRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** TagsToAdd **   <a name="dlm-Type-Schedule-TagsToAdd"></a>
The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 45 items.
Required: No

 ** VariableTags **   <a name="dlm-Type-Schedule-VariableTags"></a>
 **[AMI policies and snapshot policies that target instances only]** A collection of key/value pairs with values determined dynamically when the policy is executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two following formats: `$(instance-id)` or `$(timestamp)`. Variable tags are only valid for EBS Snapshot Management – Instance policies.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 45 items.
Required: No

## See Also
<a name="API_Schedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/Schedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/Schedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/Schedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
