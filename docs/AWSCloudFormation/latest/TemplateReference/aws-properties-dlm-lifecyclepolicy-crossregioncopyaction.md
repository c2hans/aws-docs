---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy CrossRegionCopyAction
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyaction"></a>

**[Event-based policies only]** Specifies a cross-Region copy action for event-based policies.

**Note**
To specify a cross-Region copy rule for snapshot and AMI policies, use [CrossRegionCopyRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html).

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyaction-syntax.json"></a>

```
{
  "[EncryptionConfiguration](#cfn-dlm-lifecyclepolicy-crossregioncopyaction-encryptionconfiguration)" : {{EncryptionConfiguration}},
  "[RetainRule](#cfn-dlm-lifecyclepolicy-crossregioncopyaction-retainrule)" : {{CrossRegionCopyRetainRule}},
  "[Target](#cfn-dlm-lifecyclepolicy-crossregioncopyaction-target)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyaction-syntax.yaml"></a>

```
  [EncryptionConfiguration](#cfn-dlm-lifecyclepolicy-crossregioncopyaction-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [RetainRule](#cfn-dlm-lifecyclepolicy-crossregioncopyaction-retainrule): {{
    CrossRegionCopyRetainRule}}
  [Target](#cfn-dlm-lifecyclepolicy-crossregioncopyaction-target): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopyaction-properties"></a>

`EncryptionConfiguration`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyaction-encryptionconfiguration"></a>
The encryption settings for the copied snapshot.
*Required*: Yes
*Type*: [EncryptionConfiguration](aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetainRule`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyaction-retainrule"></a>
Specifies a retention rule for cross-Region snapshot copies created by snapshot or event-based policies, or cross-Region AMI copies created by AMI policies. After the retention period expires, the cross-Region copy is deleted.
*Required*: No
*Type*: [CrossRegionCopyRetainRule](aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopyaction-target"></a>
The target Region.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w:\-\/\*]+$`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
