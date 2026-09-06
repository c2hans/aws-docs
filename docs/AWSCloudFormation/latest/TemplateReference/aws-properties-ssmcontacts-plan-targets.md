---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmcontacts-plan-targets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Plan Targets
<a name="aws-properties-ssmcontacts-plan-targets"></a>

The contact or contact channel that's being engaged.

## Syntax
<a name="aws-properties-ssmcontacts-plan-targets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmcontacts-plan-targets-syntax.json"></a>

```
{
  "[ChannelTargetInfo](#cfn-ssmcontacts-plan-targets-channeltargetinfo)" : {{ChannelTargetInfo}},
  "[ContactTargetInfo](#cfn-ssmcontacts-plan-targets-contacttargetinfo)" : {{ContactTargetInfo}}
}
```

### YAML
<a name="aws-properties-ssmcontacts-plan-targets-syntax.yaml"></a>

```
  [ChannelTargetInfo](#cfn-ssmcontacts-plan-targets-channeltargetinfo): {{
    ChannelTargetInfo}}
  [ContactTargetInfo](#cfn-ssmcontacts-plan-targets-contacttargetinfo): {{
    ContactTargetInfo}}
```

## Properties
<a name="aws-properties-ssmcontacts-plan-targets-properties"></a>

`ChannelTargetInfo`  <a name="cfn-ssmcontacts-plan-targets-channeltargetinfo"></a>
Information about the contact channel that Incident Manager engages.
*Required*: No
*Type*: [ChannelTargetInfo](aws-properties-ssmcontacts-plan-channeltargetinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContactTargetInfo`  <a name="cfn-ssmcontacts-plan-targets-contacttargetinfo"></a>
Information about the contact that Incident Manager engages.
*Required*: No
*Type*: [ContactTargetInfo](aws-properties-ssmcontacts-plan-contacttargetinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
