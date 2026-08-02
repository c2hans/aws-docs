---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-slackconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association SlackConfiguration
<a name="aws-properties-devopsagent-association-slackconfiguration"></a>

Configuration for Slack workspace integration. Defines the workspace ID, workspace name, and transmission targets that specify which Slack channels receive notifications.

## Syntax
<a name="aws-properties-devopsagent-association-slackconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-slackconfiguration-syntax.json"></a>

```
{
  "[TransmissionTarget](#cfn-devopsagent-association-slackconfiguration-transmissiontarget)" : {{SlackTransmissionTarget}},
  "[WorkspaceId](#cfn-devopsagent-association-slackconfiguration-workspaceid)" : {{String}},
  "[WorkspaceName](#cfn-devopsagent-association-slackconfiguration-workspacename)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-slackconfiguration-syntax.yaml"></a>

```
  [TransmissionTarget](#cfn-devopsagent-association-slackconfiguration-transmissiontarget): {{
    SlackTransmissionTarget}}
  [WorkspaceId](#cfn-devopsagent-association-slackconfiguration-workspaceid): {{String}}
  [WorkspaceName](#cfn-devopsagent-association-slackconfiguration-workspacename): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-slackconfiguration-properties"></a>

`TransmissionTarget`  <a name="cfn-devopsagent-association-slackconfiguration-transmissiontarget"></a>
Transmission targets for agent notifications.
*Required*: Yes
*Type*: [SlackTransmissionTarget](aws-properties-devopsagent-association-slacktransmissiontarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceId`  <a name="cfn-devopsagent-association-slackconfiguration-workspaceid"></a>
The associated Slack workspace ID.
The ID must match the pattern `^[TE][A-Z0-9]+$`.
*Required*: Yes
*Type*: String
*Pattern*: `^[TE][A-Z0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceName`  <a name="cfn-devopsagent-association-slackconfiguration-workspacename"></a>
Associated Slack workspace name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
