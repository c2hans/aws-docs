---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationnfs-onpremconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationNFS OnPremConfig
<a name="aws-properties-datasync-locationnfs-onpremconfig"></a>

The AWS DataSync agents that can connect to your Network File System (NFS) file server.

## Syntax
<a name="aws-properties-datasync-locationnfs-onpremconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationnfs-onpremconfig-syntax.json"></a>

```
{
  "[AgentArns](#cfn-datasync-locationnfs-onpremconfig-agentarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-datasync-locationnfs-onpremconfig-syntax.yaml"></a>

```
  [AgentArns](#cfn-datasync-locationnfs-onpremconfig-agentarns): {{
    - String}}
```

## Properties
<a name="aws-properties-datasync-locationnfs-onpremconfig-properties"></a>

`AgentArns`  <a name="cfn-datasync-locationnfs-onpremconfig-agentarns"></a>
The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your NFS file server.
You can specify more than one agent. For more information, see [Using multiple DataSync agents](https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html#multiple-agents).
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
