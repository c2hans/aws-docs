---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dlm-lifecyclepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy
<a name="aws-resource-dlm-lifecyclepolicy"></a>

Specifies a lifecycle policy, which is used to automate operations on Amazon EBS resources.

The properties are required when you add a lifecycle policy and optional when you update a lifecycle policy.

## Syntax
<a name="aws-resource-dlm-lifecyclepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dlm-lifecyclepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::DLM::LifecyclePolicy",
  "Properties" : {
      "[CopyTags](#cfn-dlm-lifecyclepolicy-copytags)" : {{Boolean}},
      "[CreateInterval](#cfn-dlm-lifecyclepolicy-createinterval)" : {{Integer}},
      "[CrossRegionCopyTargets](#cfn-dlm-lifecyclepolicy-crossregioncopytargets)" : {{[ CrossRegionCopyTarget, ... ]}},
      "[DefaultPolicy](#cfn-dlm-lifecyclepolicy-defaultpolicy)" : {{String}},
      "[Description](#cfn-dlm-lifecyclepolicy-description)" : {{String}},
      "[Exclusions](#cfn-dlm-lifecyclepolicy-exclusions)" : {{Exclusions}},
      "[ExecutionRoleArn](#cfn-dlm-lifecyclepolicy-executionrolearn)" : {{String}},
      "[ExtendDeletion](#cfn-dlm-lifecyclepolicy-extenddeletion)" : {{Boolean}},
      "[PolicyDetails](#cfn-dlm-lifecyclepolicy-policydetails)" : {{PolicyDetails}},
      "[RetainInterval](#cfn-dlm-lifecyclepolicy-retaininterval)" : {{Integer}},
      "[State](#cfn-dlm-lifecyclepolicy-state)" : {{String}},
      "[Tags](#cfn-dlm-lifecyclepolicy-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-dlm-lifecyclepolicy-syntax.yaml"></a>

```
Type: AWS::DLM::LifecyclePolicy
Properties:
  [CopyTags](#cfn-dlm-lifecyclepolicy-copytags): {{Boolean}}
  [CreateInterval](#cfn-dlm-lifecyclepolicy-createinterval): {{Integer}}
  [CrossRegionCopyTargets](#cfn-dlm-lifecyclepolicy-crossregioncopytargets): {{
    - CrossRegionCopyTarget}}
  [DefaultPolicy](#cfn-dlm-lifecyclepolicy-defaultpolicy): {{String}}
  [Description](#cfn-dlm-lifecyclepolicy-description): {{String}}
  [Exclusions](#cfn-dlm-lifecyclepolicy-exclusions): {{
    Exclusions}}
  [ExecutionRoleArn](#cfn-dlm-lifecyclepolicy-executionrolearn): {{String}}
  [ExtendDeletion](#cfn-dlm-lifecyclepolicy-extenddeletion): {{Boolean}}
  [PolicyDetails](#cfn-dlm-lifecyclepolicy-policydetails): {{
    PolicyDetails}}
  [RetainInterval](#cfn-dlm-lifecyclepolicy-retaininterval): {{Integer}}
  [State](#cfn-dlm-lifecyclepolicy-state): {{String}}
  [Tags](#cfn-dlm-lifecyclepolicy-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-dlm-lifecyclepolicy-properties"></a>

`CopyTags`  <a name="cfn-dlm-lifecyclepolicy-copytags"></a>
**[Default policies only]** Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is `false`.
Default: false
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateInterval`  <a name="cfn-dlm-lifecyclepolicy-createinterval"></a>
**[Default policies only]** Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.
Default: 1
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossRegionCopyTargets`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopytargets"></a>
**[Default policies only]** Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.
*Required*: No
*Type*: Array of [CrossRegionCopyTarget](aws-properties-dlm-lifecyclepolicy-crossregioncopytarget.md)
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultPolicy`  <a name="cfn-dlm-lifecyclepolicy-defaultpolicy"></a>
**[Default policies only]** Specify the type of default policy to create.
+ To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify `VOLUME`.
+ To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify `INSTANCE`.
*Required*: No
*Type*: String
*Allowed values*: `VOLUME | INSTANCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-dlm-lifecyclepolicy-description"></a>
A description of the lifecycle policy. The characters ^[0-9A-Za-z \_-]\+$ are supported.
*Required*: Conditional
*Type*: String
*Pattern*: `[0-9A-Za-z _-]+`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exclusions`  <a name="cfn-dlm-lifecyclepolicy-exclusions"></a>
**[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.
*Required*: No
*Type*: [Exclusions](aws-properties-dlm-lifecyclepolicy-exclusions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-dlm-lifecyclepolicy-executionrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
*Required*: Conditional
*Type*: String
*Pattern*: `arn:aws(-[a-z]{1,4}){0,2}:iam::\d+:role/.*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExtendDeletion`  <a name="cfn-dlm-lifecyclepolicy-extenddeletion"></a>
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

`PolicyDetails`  <a name="cfn-dlm-lifecyclepolicy-policydetails"></a>
The configuration details of the lifecycle policy.
If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.
*Required*: Conditional
*Type*: [PolicyDetails](aws-properties-dlm-lifecyclepolicy-policydetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetainInterval`  <a name="cfn-dlm-lifecyclepolicy-retaininterval"></a>
**[Default policies only]** Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.
Default: 7
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-dlm-lifecyclepolicy-state"></a>
The activation state of the lifecycle policy.
*Required*: Conditional
*Type*: String
*Allowed values*: `ENABLED | DISABLED | ERROR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dlm-lifecyclepolicy-tags"></a>
The tags to apply to the lifecycle policy during creation.
*Required*: No
*Type*: Array of [Tag](aws-properties-dlm-lifecyclepolicy-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dlm-lifecyclepolicy-return-values"></a>

### Ref
<a name="aws-resource-dlm-lifecyclepolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the lifecycle policy.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dlm-lifecyclepolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-dlm-lifecyclepolicy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the lifecycle policy.

`PolicyId`  <a name="PolicyId-fn::getatt"></a>
The identifier of the lifecycle policy.

## Examples
<a name="aws-resource-dlm-lifecyclepolicy--examples"></a>

### Creating a Lifecycle Policy
<a name="aws-resource-dlm-lifecyclepolicy--examples--Creating_a_Lifecycle_Policy"></a>

The following example demonstrates how to create a basic snapshot lifecycle policy with a cross-Region copy rule.

#### JSON
<a name="aws-resource-dlm-lifecyclepolicy--examples--Creating_a_Lifecycle_Policy--json"></a>

```
{
    "Description": "Basic LifecyclePolicy",
    "Resources": {
        "BasicLifecyclePolicy": {
            "Type": "AWS::DLM::LifecyclePolicy",
            "Properties": {
                "Description": "Lifecycle Policy using CloudFormation",
                "State": "ENABLED",
                "ExecutionRoleArn": "arn:aws:iam::123456789012:role/service-role/AWSDataLifecycleManagerDefaultRole",
                "PolicyDetails": {
                    "ResourceTypes": [
                        "VOLUME"
                    ],
                    "TargetTags": [{
                        "Key": "costcenter",
                        "Value": "115"
                    }],
                    "Schedules": [{
                        "Name": "Daily Snapshots",
                        "TagsToAdd": [{
                            "Key": "type",
                            "Value": "DailySnapshot"
                        }],
                        "CreateRule": {
                            "Interval": 12,
                            "IntervalUnit": "HOURS",
                            "Times": [
                                "13:00"
                            ]
                        },
                        "RetainRule": {
                            "Count": 1
                        },
                        "CopyTags": true,
                        "CrossRegionCopyRules": [{
                            "Encrypted": false,
                            "Target": "us-east-1"
                        }]
                   }]
               }
           }
        }
    }
}
```

#### YAML
<a name="aws-resource-dlm-lifecyclepolicy--examples--Creating_a_Lifecycle_Policy--yaml"></a>

```
Description: Basic LifecyclePolicy
Resources:
  BasicLifecyclePolicy:
    Type: AWS::DLM::LifecyclePolicy
    Properties:
      Description: Lifecycle Policy using CloudFormation
      State: ENABLED
      ExecutionRoleArn: arn:aws:iam::123456789012:role/service-role/AWSDataLifecycleManagerDefaultRole
      PolicyDetails:
        ResourceTypes:
        - VOLUME
        TargetTags:
        - Key: costcenter
          Value: '115'
        Schedules:
        - Name: Daily Snapshots
          TagsToAdd:
          - Key: type
            Value: DailySnapshot
          CreateRule:
            Interval: 12
            IntervalUnit: HOURS
            Times:
            - '13:00'
          RetainRule:
            Count: 1
          CopyTags: true
          CrossRegionCopyRules:
          - Encrypted: false
            Target: us-east-1
```

## See also
<a name="aws-resource-dlm-lifecyclepolicy--seealso"></a>
+ [CreateLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CreateLifecyclePolicy.html) in the *Amazon Data Lifecycle Manager API Reference*
+ [Automating the Amazon EBS Snapshot Lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) in the *Amazon Elastic Compute Cloud User Guide*
