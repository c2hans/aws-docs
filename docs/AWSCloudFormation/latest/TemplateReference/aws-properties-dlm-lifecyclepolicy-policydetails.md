---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-policydetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy PolicyDetails
<a name="aws-properties-dlm-lifecyclepolicy-policydetails"></a>

Specifies the configuration of a lifecycle policy.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-policydetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-policydetails-syntax.json"></a>

```
{
  "[Actions](#cfn-dlm-lifecyclepolicy-policydetails-actions)" : {{[ Action, ... ]}},
  "[CopyTags](#cfn-dlm-lifecyclepolicy-policydetails-copytags)" : {{Boolean}},
  "[CreateInterval](#cfn-dlm-lifecyclepolicy-policydetails-createinterval)" : {{Integer}},
  "[CrossRegionCopyTargets](#cfn-dlm-lifecyclepolicy-policydetails-crossregioncopytargets)" : {{[ CrossRegionCopyTarget, ... ]}},
  "[EventSource](#cfn-dlm-lifecyclepolicy-policydetails-eventsource)" : {{EventSource}},
  "[Exclusions](#cfn-dlm-lifecyclepolicy-policydetails-exclusions)" : {{Exclusions}},
  "[ExtendDeletion](#cfn-dlm-lifecyclepolicy-policydetails-extenddeletion)" : {{Boolean}},
  "[Parameters](#cfn-dlm-lifecyclepolicy-policydetails-parameters)" : {{Parameters}},
  "[PolicyLanguage](#cfn-dlm-lifecyclepolicy-policydetails-policylanguage)" : {{String}},
  "[PolicyType](#cfn-dlm-lifecyclepolicy-policydetails-policytype)" : {{String}},
  "[ResourceLocations](#cfn-dlm-lifecyclepolicy-policydetails-resourcelocations)" : {{[ String, ... ]}},
  "[ResourceType](#cfn-dlm-lifecyclepolicy-policydetails-resourcetype)" : {{String}},
  "[ResourceTypes](#cfn-dlm-lifecyclepolicy-policydetails-resourcetypes)" : {{[ String, ... ]}},
  "[RetainInterval](#cfn-dlm-lifecyclepolicy-policydetails-retaininterval)" : {{Integer}},
  "[Schedules](#cfn-dlm-lifecyclepolicy-policydetails-schedules)" : {{[ Schedule, ... ]}},
  "[TargetTags](#cfn-dlm-lifecyclepolicy-policydetails-targettags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-policydetails-syntax.yaml"></a>

```
  [Actions](#cfn-dlm-lifecyclepolicy-policydetails-actions): {{
    - Action}}
  [CopyTags](#cfn-dlm-lifecyclepolicy-policydetails-copytags): {{Boolean}}
  [CreateInterval](#cfn-dlm-lifecyclepolicy-policydetails-createinterval): {{Integer}}
  [CrossRegionCopyTargets](#cfn-dlm-lifecyclepolicy-policydetails-crossregioncopytargets): {{
    - CrossRegionCopyTarget}}
  [EventSource](#cfn-dlm-lifecyclepolicy-policydetails-eventsource): {{
    EventSource}}
  [Exclusions](#cfn-dlm-lifecyclepolicy-policydetails-exclusions): {{
    Exclusions}}
  [ExtendDeletion](#cfn-dlm-lifecyclepolicy-policydetails-extenddeletion): {{Boolean}}
  [Parameters](#cfn-dlm-lifecyclepolicy-policydetails-parameters): {{
    Parameters}}
  [PolicyLanguage](#cfn-dlm-lifecyclepolicy-policydetails-policylanguage): {{String}}
  [PolicyType](#cfn-dlm-lifecyclepolicy-policydetails-policytype): {{String}}
  [ResourceLocations](#cfn-dlm-lifecyclepolicy-policydetails-resourcelocations): {{
    - String}}
  [ResourceType](#cfn-dlm-lifecyclepolicy-policydetails-resourcetype): {{String}}
  [ResourceTypes](#cfn-dlm-lifecyclepolicy-policydetails-resourcetypes): {{
    - String}}
  [RetainInterval](#cfn-dlm-lifecyclepolicy-policydetails-retaininterval): {{Integer}}
  [Schedules](#cfn-dlm-lifecyclepolicy-policydetails-schedules): {{
    - Schedule}}
  [TargetTags](#cfn-dlm-lifecyclepolicy-policydetails-targettags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-policydetails-properties"></a>

`Actions`  <a name="cfn-dlm-lifecyclepolicy-policydetails-actions"></a>
**[Event-based policies only]** The actions to be performed when the event-based policy is activated. You can specify only one action per policy.
*Required*: No
*Type*: Array of [Action](aws-properties-dlm-lifecyclepolicy-action.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CopyTags`  <a name="cfn-dlm-lifecyclepolicy-policydetails-copytags"></a>
**[Default policies only]** Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is `false`.
Default: false
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateInterval`  <a name="cfn-dlm-lifecyclepolicy-policydetails-createinterval"></a>
**[Default policies only]** Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.
Default: 1
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossRegionCopyTargets`  <a name="cfn-dlm-lifecyclepolicy-policydetails-crossregioncopytargets"></a>
**[Default policies only]** Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.
*Required*: No
*Type*: Array of [CrossRegionCopyTarget](aws-properties-dlm-lifecyclepolicy-crossregioncopytarget.md)
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventSource`  <a name="cfn-dlm-lifecyclepolicy-policydetails-eventsource"></a>
**[Event-based policies only]** The event that activates the event-based policy.
*Required*: No
*Type*: [EventSource](aws-properties-dlm-lifecyclepolicy-eventsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exclusions`  <a name="cfn-dlm-lifecyclepolicy-policydetails-exclusions"></a>
**[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.
*Required*: No
*Type*: [Exclusions](aws-properties-dlm-lifecyclepolicy-exclusions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExtendDeletion`  <a name="cfn-dlm-lifecyclepolicy-policydetails-extenddeletion"></a>
**[Default policies only]** Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.
By default (**ExtendDeletion=false**):
+ If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify `true`.
+ If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify `true`.
If you enable extended deletion (**ExtendDeletion=true**), you override both default behaviors simultaneously.
If you do not specify a value, the default is `false`.
Default: false
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-dlm-lifecyclepolicy-policydetails-parameters"></a>
**[Custom snapshot and AMI policies only]** A set of optional parameters for snapshot and AMI lifecycle policies.
If you are modifying a policy that was created or previously modified using the Amazon Data Lifecycle Manager console, then you must include this parameter and specify either the default values or the new values that you require. You can't omit this parameter or set its values to null.
*Required*: No
*Type*: [Parameters](aws-properties-dlm-lifecyclepolicy-parameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyLanguage`  <a name="cfn-dlm-lifecyclepolicy-policydetails-policylanguage"></a>
The type of policy to create. Specify one of the following:
+ `SIMPLIFIED` To create a default policy.
+ `STANDARD` To create a custom policy.
*Required*: No
*Type*: String
*Allowed values*: `SIMPLIFIED | STANDARD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyType`  <a name="cfn-dlm-lifecyclepolicy-policydetails-policytype"></a>
The type of policy. Specify `EBS_SNAPSHOT_MANAGEMENT` to create a lifecycle policy that manages the lifecycle of Amazon EBS snapshots. Specify `IMAGE_MANAGEMENT` to create a lifecycle policy that manages the lifecycle of EBS-backed AMIs. Specify `EVENT_BASED_POLICY ` to create an event-based policy that performs specific actions when a defined event occurs in your AWS account.
The default is `EBS_SNAPSHOT_MANAGEMENT`.
*Required*: No
*Type*: String
*Allowed values*: `EBS_SNAPSHOT_MANAGEMENT | IMAGE_MANAGEMENT | EVENT_BASED_POLICY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceLocations`  <a name="cfn-dlm-lifecyclepolicy-policydetails-resourcelocations"></a>
**[Custom snapshot and AMI policies only]** The location of the resources to backup.
+ If the source resources are located in a Region, specify `CLOUD`. In this case, the policy targets all resources of the specified type with matching target tags across all Availability Zones in the Region.
+ **[Custom snapshot policies only]** If the source resources are located in a Local Zone, specify `LOCAL_ZONE`. In this case, the policy targets all resources of the specified type with matching target tags across all Local Zones in the Region.
+ If the source resources are located on an Outpost in your account, specify `OUTPOST`. In this case, the policy targets all resources of the specified type with matching target tags across all of the Outposts in your account.

*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-dlm-lifecyclepolicy-policydetails-resourcetype"></a>
**[Default policies only]** Specify the type of default policy to create.
+ To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify `VOLUME`.
+ To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify `INSTANCE`.
*Required*: No
*Type*: String
*Allowed values*: `VOLUME | INSTANCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTypes`  <a name="cfn-dlm-lifecyclepolicy-policydetails-resourcetypes"></a>
**[Custom snapshot policies only]** The target resource type for snapshot and AMI lifecycle policies. Use `VOLUME `to create snapshots of individual volumes or use `INSTANCE` to create multi-volume snapshots from the volumes for an instance.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetainInterval`  <a name="cfn-dlm-lifecyclepolicy-policydetails-retaininterval"></a>
**[Default policies only]** Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.
Default: 7
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schedules`  <a name="cfn-dlm-lifecyclepolicy-policydetails-schedules"></a>
**[Custom snapshot and AMI policies only]** The schedules of policy-defined actions for snapshot and AMI lifecycle policies. A policy can have up to four schedules—one mandatory schedule and up to three optional schedules.
*Required*: No
*Type*: Array of [Schedule](aws-properties-dlm-lifecyclepolicy-schedule.md)
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetTags`  <a name="cfn-dlm-lifecyclepolicy-policydetails-targettags"></a>
**[Custom snapshot and AMI policies only]** The single tag that identifies targeted resources for this policy.
*Required*: No
*Type*: Array of [Tag](aws-properties-dlm-lifecyclepolicy-tag.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-dlm-lifecyclepolicy-policydetails--seealso"></a>
+ [PolicyDetails](https://docs.aws.amazon.com/dlm/latest/APIReference/API_PolicyDetails.html) in the *Amazon Data Lifecycle Manager API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
