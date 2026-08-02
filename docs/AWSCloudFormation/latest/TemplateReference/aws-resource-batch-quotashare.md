---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-quotashare.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::QuotaShare
<a name="aws-resource-batch-quotashare"></a>

Creates an AWS Batch quota share. Each quota share operates as a virtual queue with a configured compute capacity, resource sharing strategy, and borrow limits.

## Syntax
<a name="aws-resource-batch-quotashare-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-batch-quotashare-syntax.json"></a>

```
{
  "Type" : "AWS::Batch::QuotaShare",
  "Properties" : {
      "[CapacityLimits](#cfn-batch-quotashare-capacitylimits)" : {{[ QuotaShareCapacityLimit, ... ]}},
      "[JobQueue](#cfn-batch-quotashare-jobqueue)" : {{String}},
      "[PreemptionConfiguration](#cfn-batch-quotashare-preemptionconfiguration)" : {{QuotaSharePreemptionConfiguration}},
      "[QuotaShareName](#cfn-batch-quotashare-quotasharename)" : {{String}},
      "[ResourceSharingConfiguration](#cfn-batch-quotashare-resourcesharingconfiguration)" : {{QuotaShareResourceSharingConfiguration}},
      "[State](#cfn-batch-quotashare-state)" : {{String}},
      "[Tags](#cfn-batch-quotashare-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-batch-quotashare-syntax.yaml"></a>

```
Type: AWS::Batch::QuotaShare
Properties:
  [CapacityLimits](#cfn-batch-quotashare-capacitylimits): {{
    - QuotaShareCapacityLimit}}
  [JobQueue](#cfn-batch-quotashare-jobqueue): {{String}}
  [PreemptionConfiguration](#cfn-batch-quotashare-preemptionconfiguration): {{
    QuotaSharePreemptionConfiguration}}
  [QuotaShareName](#cfn-batch-quotashare-quotasharename): {{String}}
  [ResourceSharingConfiguration](#cfn-batch-quotashare-resourcesharingconfiguration): {{
    QuotaShareResourceSharingConfiguration}}
  [State](#cfn-batch-quotashare-state): {{String}}
  [Tags](#cfn-batch-quotashare-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-batch-quotashare-properties"></a>

`CapacityLimits`  <a name="cfn-batch-quotashare-capacitylimits"></a>
A list that specifies the quantity and type of compute capacity allocated to the quota share.
*Required*: Yes
*Type*: Array of [QuotaShareCapacityLimit](aws-properties-batch-quotashare-quotasharecapacitylimit.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobQueue`  <a name="cfn-batch-quotashare-jobqueue"></a>
The Amazon Resource Name (ARN) or name of the job queue associated with this quota share.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreemptionConfiguration`  <a name="cfn-batch-quotashare-preemptionconfiguration"></a>
Specifies the preemption behavior for jobs in a quota share.
*Required*: Yes
*Type*: [QuotaSharePreemptionConfiguration](aws-properties-batch-quotashare-quotasharepreemptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QuotaShareName`  <a name="cfn-batch-quotashare-quotasharename"></a>
The name of the quota share.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceSharingConfiguration`  <a name="cfn-batch-quotashare-resourcesharingconfiguration"></a>
Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.
*Required*: Yes
*Type*: [QuotaShareResourceSharingConfiguration](aws-properties-batch-quotashare-quotashareresourcesharingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-batch-quotashare-state"></a>
The state of the quota share.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-batch-quotashare-tags"></a>
The tags applied to the quota share. Each tag is a key-value pair. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-batch-quotashare-return-values"></a>

### Ref
<a name="aws-resource-batch-quotashare-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-batch-quotashare-return-values-fn--getatt"></a>

####
<a name="aws-resource-batch-quotashare-return-values-fn--getatt-fn--getatt"></a>

`QuotaShareArn`  <a name="QuotaShareArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the quota share.
