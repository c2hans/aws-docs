---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmcontacts-contact-targets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Contact Targets
<a name="aws-properties-ssmcontacts-contact-targets"></a>

The contact or contact channel that's being engaged.

## Syntax
<a name="aws-properties-ssmcontacts-contact-targets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmcontacts-contact-targets-syntax.json"></a>

```
{
  "[ChannelTargetInfo](#cfn-ssmcontacts-contact-targets-channeltargetinfo)" : {{ChannelTargetInfo}},
  "[ContactTargetInfo](#cfn-ssmcontacts-contact-targets-contacttargetinfo)" : {{ContactTargetInfo}}
}
```

### YAML
<a name="aws-properties-ssmcontacts-contact-targets-syntax.yaml"></a>

```
  [ChannelTargetInfo](#cfn-ssmcontacts-contact-targets-channeltargetinfo): {{
    ChannelTargetInfo}}
  [ContactTargetInfo](#cfn-ssmcontacts-contact-targets-contacttargetinfo): {{
    ContactTargetInfo}}
```

## Properties
<a name="aws-properties-ssmcontacts-contact-targets-properties"></a>

`ChannelTargetInfo`  <a name="cfn-ssmcontacts-contact-targets-channeltargetinfo"></a>
Information about the contact channel that Incident Manager engages.
*Required*: No
*Type*: [ChannelTargetInfo](aws-properties-ssmcontacts-contact-channeltargetinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContactTargetInfo`  <a name="cfn-ssmcontacts-contact-targets-contacttargetinfo"></a>
The contact that Incident Manager is engaging during an incident.
*Required*: No
*Type*: [ContactTargetInfo](aws-properties-ssmcontacts-contact-contacttargetinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
