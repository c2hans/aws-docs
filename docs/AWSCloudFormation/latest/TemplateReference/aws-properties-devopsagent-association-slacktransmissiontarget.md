---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-slacktransmissiontarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association SlackTransmissionTarget
<a name="aws-properties-devopsagent-association-slacktransmissiontarget"></a>

Defines the Slack channels where different types of agent notifications will be sent.

## Syntax
<a name="aws-properties-devopsagent-association-slacktransmissiontarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-slacktransmissiontarget-syntax.json"></a>

```
{
  "[IncidentResponseTarget](#cfn-devopsagent-association-slacktransmissiontarget-incidentresponsetarget)" : {{SlackChannel}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-slacktransmissiontarget-syntax.yaml"></a>

```
  [IncidentResponseTarget](#cfn-devopsagent-association-slacktransmissiontarget-incidentresponsetarget): {{
    SlackChannel}}
```

## Properties
<a name="aws-properties-devopsagent-association-slacktransmissiontarget-properties"></a>

`IncidentResponseTarget`  <a name="cfn-devopsagent-association-slacktransmissiontarget-incidentresponsetarget"></a>
Destination for AWS DevOps Agent Incident Response.
*Required*: Yes
*Type*: [SlackChannel](aws-properties-devopsagent-association-slackchannel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
