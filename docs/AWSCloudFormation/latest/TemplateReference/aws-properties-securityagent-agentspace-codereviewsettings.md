---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-codereviewsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace CodeReviewSettings
<a name="aws-properties-securityagent-agentspace-codereviewsettings"></a>

The code review settings for an agent space, controlling which types of scanning are enabled.

## Syntax
<a name="aws-properties-securityagent-agentspace-codereviewsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-codereviewsettings-syntax.json"></a>

```
{
  "[ControlsScanning](#cfn-securityagent-agentspace-codereviewsettings-controlsscanning)" : {{Boolean}},
  "[GeneralPurposeScanning](#cfn-securityagent-agentspace-codereviewsettings-generalpurposescanning)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-codereviewsettings-syntax.yaml"></a>

```
  [ControlsScanning](#cfn-securityagent-agentspace-codereviewsettings-controlsscanning): {{Boolean}}
  [GeneralPurposeScanning](#cfn-securityagent-agentspace-codereviewsettings-generalpurposescanning): {{Boolean}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-codereviewsettings-properties"></a>

`ControlsScanning`  <a name="cfn-securityagent-agentspace-codereviewsettings-controlsscanning"></a>
Indicates whether controls scanning is enabled for code reviews.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GeneralPurposeScanning`  <a name="cfn-securityagent-agentspace-codereviewsettings-generalpurposescanning"></a>
Indicates whether general-purpose scanning is enabled for code reviews.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
