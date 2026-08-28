---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy CrossRegionCopyRule
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyrule"></a>

**[Custom snapshot and AMI policies only]** Specifies a cross-Region copy rule for a snapshot and AMI policies.

**Note**
To specify a cross-Region copy action for event-based polices, use [CrossRegionCopyAction](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyAction.html).

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyrule-syntax.json"></a>

```
{
  "[CmkArn](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-cmkarn)" : {{String}},
  "[CopyTags](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-copytags)" : {{Boolean}},
  "[DeprecateRule](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-deprecaterule)" : {{CrossRegionCopyDeprecateRule}},
  "[Encrypted](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-encrypted)" : {{Boolean}},
  "[RetainRule](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-retainrule)" : {{CrossRegionCopyRetainRule}},
  "[Target](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-target)" : {{String}},
  "[TargetRegion](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-targetregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyrule-syntax.yaml"></a>

```
  [CmkArn](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-cmkarn): {{String}}
  [CopyTags](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-copytags): {{Boolean}}
  [DeprecateRule](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-deprecaterule): {{
    CrossRegionCopyDeprecateRule}}
  [Encrypted](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-encrypted): {{Boolean}}
  [RetainRule](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-retainrule): {{
    CrossRegionCopyRetainRule}}
  [Target](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-target): {{String}}
  [TargetRegion](#cfn-dlm-lifecyclepolicy-crossregioncopyrule-targetregion): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyrule-properties"></a>

`CmkArn`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyrule-cmkarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-[a-z]{1,4}){0,2}:kms:([a-z]+-){2,3}\d:\d+:key/.*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CopyTags`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyrule-copytags"></a>
Indicates whether to copy all user-defined tags from the source snapshot or AMI to the cross-Region copy.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeprecateRule`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyrule-deprecaterule"></a>
**[Custom AMI policies only]** The AMI deprecation rule for cross-Region AMI copies created by the rule.
*Required*: No
*Type*: [CrossRegionCopyDeprecateRule](aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Encrypted`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyrule-encrypted"></a>
To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetainRule`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyrule-retainrule"></a>
The retention rule that indicates how long the cross-Region snapshot or AMI copies are to be retained in the destination Region.
*Required*: No
*Type*: [CrossRegionCopyRetainRule](aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyrule-target"></a>
Use this parameter for snapshot policies only. For AMI policies, use **TargetRegion** instead.
**[Custom snapshot policies only]** The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.
*Required*: No
*Type*: String
*Pattern*: `^[\w:\-\/\*]+$`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRegion`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyrule-targetregion"></a>
Use this parameter for AMI policies only. For snapshot policies, use **Target** instead. For snapshot policies created before the **Target** parameter was introduced, this parameter indicates the target Region for snapshot copies.

**[Custom AMI policies only]** The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.
*Required*: No
*Type*: String
*Pattern*: `([a-z]+-){2,3}\d`
*Minimum*: `0`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
