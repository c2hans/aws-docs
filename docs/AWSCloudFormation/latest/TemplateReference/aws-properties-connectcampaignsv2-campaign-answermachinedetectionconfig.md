---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign AnswerMachineDetectionConfig
<a name="aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig"></a>

Contains answering machine detection configuration.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig-syntax.json"></a>

```
{
  "[AwaitAnswerMachinePrompt](#cfn-connectcampaignsv2-campaign-answermachinedetectionconfig-awaitanswermachineprompt)" : {{Boolean}},
  "[EnableAnswerMachineDetection](#cfn-connectcampaignsv2-campaign-answermachinedetectionconfig-enableanswermachinedetection)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig-syntax.yaml"></a>

```
  [AwaitAnswerMachinePrompt](#cfn-connectcampaignsv2-campaign-answermachinedetectionconfig-awaitanswermachineprompt): {{Boolean}}
  [EnableAnswerMachineDetection](#cfn-connectcampaignsv2-campaign-answermachinedetectionconfig-enableanswermachinedetection): {{Boolean}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig-properties"></a>

`AwaitAnswerMachinePrompt`  <a name="cfn-connectcampaignsv2-campaign-answermachinedetectionconfig-awaitanswermachineprompt"></a>
Whether or not waiting for an answer machine prompt is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableAnswerMachineDetection`  <a name="cfn-connectcampaignsv2-campaign-answermachinedetectionconfig-enableanswermachinedetection"></a>
Enables answering machine detection.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
