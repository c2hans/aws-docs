---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_PolicyDetails.html
---

# PolicyDetails
<a name="API_PolicyDetails"></a>

Specifies the configuration of a lifecycle policy.

## Contents
<a name="API_PolicyDetails_Contents"></a>

 ** Actions **   <a name="dlm-Type-PolicyDetails-Actions"></a>
 **[Event-based policies only]** The actions to be performed when the event-based policy is activated. You can specify only one action per policy.
Type: Array of [Action](API_Action.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** CopyTags **   <a name="dlm-Type-PolicyDetails-CopyTags"></a>
 **[Default policies only]** Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is `false`.
Default: false
Type: Boolean
Required: No

 ** CreateInterval **   <a name="dlm-Type-PolicyDetails-CreateInterval"></a>
 **[Default policies only]** Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.
Default: 1
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** CrossRegionCopyTargets **   <a name="dlm-Type-PolicyDetails-CrossRegionCopyTargets"></a>
 **[Default policies only]** Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.
Type: Array of [CrossRegionCopyTarget](API_CrossRegionCopyTarget.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** EventSource **   <a name="dlm-Type-PolicyDetails-EventSource"></a>
 **[Event-based policies only]** The event that activates the event-based policy.
Type: [EventSource](API_EventSource.md) object
Required: No

 ** Exclusions **   <a name="dlm-Type-PolicyDetails-Exclusions"></a>
 **[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.
Type: [Exclusions](API_Exclusions.md) object
Required: No

 ** ExtendDeletion **   <a name="dlm-Type-PolicyDetails-ExtendDeletion"></a>
 **[Default policies only]** Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.
By default (**ExtendDeletion=false**):
+ If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify `true`.
+ If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify `true`.
If you enable extended deletion (**ExtendDeletion=true**), you override both default behaviors simultaneously.
If you do not specify a value, the default is `false`.
Default: false
Type: Boolean
Required: No

 ** Parameters **   <a name="dlm-Type-PolicyDetails-Parameters"></a>
 **[Custom snapshot and AMI policies only]** A set of optional parameters for snapshot and AMI lifecycle policies.
If you are modifying a policy that was created or previously modified using the Amazon Data Lifecycle Manager console, then you must include this parameter and specify either the default values or the new values that you require. You can't omit this parameter or set its values to null.
Type: [Parameters](API_Parameters.md) object
Required: No

 ** PolicyLanguage **   <a name="dlm-Type-PolicyDetails-PolicyLanguage"></a>
The type of policy to create. Specify one of the following:
+  `SIMPLIFIED` To create a default policy.
+  `STANDARD` To create a custom policy.
Type: String
Valid Values: `SIMPLIFIED | STANDARD`
Required: No

 ** PolicyType **   <a name="dlm-Type-PolicyDetails-PolicyType"></a>
The type of policy. Specify `EBS_SNAPSHOT_MANAGEMENT` to create a lifecycle policy that manages the lifecycle of Amazon EBS snapshots. Specify `IMAGE_MANAGEMENT` to create a lifecycle policy that manages the lifecycle of EBS-backed AMIs. Specify `EVENT_BASED_POLICY ` to create an event-based policy that performs specific actions when a defined event occurs in your AWS account.
The default is `EBS_SNAPSHOT_MANAGEMENT`.
Type: String
Valid Values: `EBS_SNAPSHOT_MANAGEMENT | IMAGE_MANAGEMENT | EVENT_BASED_POLICY`
Required: No

 ** ResourceLocations **   <a name="dlm-Type-PolicyDetails-ResourceLocations"></a>
 **[Custom snapshot and AMI policies only]** The location of the resources to backup.
+ If the source resources are located in a Region, specify `CLOUD`. In this case, the policy targets all resources of the specified type with matching target tags across all Availability Zones in the Region.
+  **[Custom snapshot policies only]** If the source resources are located in a Local Zone, specify `LOCAL_ZONE`. In this case, the policy targets all resources of the specified type with matching target tags across all Local Zones in the Region.
+ If the source resources are located on an Outpost in your account, specify `OUTPOST`. In this case, the policy targets all resources of the specified type with matching target tags across all of the Outposts in your account.

Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `CLOUD | OUTPOST | LOCAL_ZONE`
Required: No

 ** ResourceType **   <a name="dlm-Type-PolicyDetails-ResourceType"></a>
 **[Default policies only]** Specify the type of default policy to create.
+ To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify `VOLUME`.
+ To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify `INSTANCE`.
Type: String
Valid Values: `VOLUME | INSTANCE`
Required: No

 ** ResourceTypes **   <a name="dlm-Type-PolicyDetails-ResourceTypes"></a>
 **[Custom snapshot policies only]** The target resource type for snapshot and AMI lifecycle policies. Use `VOLUME `to create snapshots of individual volumes or use `INSTANCE` to create multi-volume snapshots from the volumes for an instance.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `VOLUME | INSTANCE`
Required: No

 ** RetainInterval **   <a name="dlm-Type-PolicyDetails-RetainInterval"></a>
 **[Default policies only]** Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.
Default: 7
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Schedules **   <a name="dlm-Type-PolicyDetails-Schedules"></a>
 **[Custom snapshot and AMI policies only]** The schedules of policy-defined actions for snapshot and AMI lifecycle policies. A policy can have up to four schedules—one mandatory schedule and up to three optional schedules.
Type: Array of [Schedule](API_Schedule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** TargetTags **   <a name="dlm-Type-PolicyDetails-TargetTags"></a>
 **[Custom snapshot and AMI policies only]** The single tag that identifies targeted resources for this policy.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_PolicyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/PolicyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/PolicyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/PolicyDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
