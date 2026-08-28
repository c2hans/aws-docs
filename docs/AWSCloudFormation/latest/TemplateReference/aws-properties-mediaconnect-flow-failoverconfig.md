---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-failoverconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow FailoverConfig
<a name="aws-properties-mediaconnect-flow-failoverconfig"></a>

 The settings for source failover.

## Syntax
<a name="aws-properties-mediaconnect-flow-failoverconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-failoverconfig-syntax.json"></a>

```
{
  "[FailoverMode](#cfn-mediaconnect-flow-failoverconfig-failovermode)" : {{String}},
  "[RecoveryWindow](#cfn-mediaconnect-flow-failoverconfig-recoverywindow)" : {{Integer}},
  "[SourcePriority](#cfn-mediaconnect-flow-failoverconfig-sourcepriority)" : {{SourcePriority}},
  "[State](#cfn-mediaconnect-flow-failoverconfig-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-failoverconfig-syntax.yaml"></a>

```
  [FailoverMode](#cfn-mediaconnect-flow-failoverconfig-failovermode): {{String}}
  [RecoveryWindow](#cfn-mediaconnect-flow-failoverconfig-recoverywindow): {{Integer}}
  [SourcePriority](#cfn-mediaconnect-flow-failoverconfig-sourcepriority): {{
    SourcePriority}}
  [State](#cfn-mediaconnect-flow-failoverconfig-state): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-failoverconfig-properties"></a>

`FailoverMode`  <a name="cfn-mediaconnect-flow-failoverconfig-failovermode"></a>
The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams. The string for this property must be entered as MERGE or FAILOVER. No other string entry is valid.
*Required*: No
*Type*: String
*Allowed values*: `MERGE | FAILOVER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryWindow`  <a name="cfn-mediaconnect-flow-failoverconfig-recoverywindow"></a>
 Search window time to look for dash-7 packets.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePriority`  <a name="cfn-mediaconnect-flow-failoverconfig-sourcepriority"></a>
 The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.
*Required*: No
*Type*: [SourcePriority](aws-properties-mediaconnect-flow-sourcepriority.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-mediaconnect-flow-failoverconfig-state"></a>
The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
