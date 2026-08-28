---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rum-appmonitor-customevents.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RUM::AppMonitor CustomEvents
<a name="aws-properties-rum-appmonitor-customevents"></a>

This structure specifies whether this app monitor allows the web client to define and send custom events.

## Syntax
<a name="aws-properties-rum-appmonitor-customevents-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rum-appmonitor-customevents-syntax.json"></a>

```
{
  "[Status](#cfn-rum-appmonitor-customevents-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-rum-appmonitor-customevents-syntax.yaml"></a>

```
  [Status](#cfn-rum-appmonitor-customevents-status): {{String}}
```

## Properties
<a name="aws-properties-rum-appmonitor-customevents-properties"></a>

`Status`  <a name="cfn-rum-appmonitor-customevents-status"></a>
Set this to `ENABLED` to allow the web client to send custom events for this app monitor.
Valid values are `ENABLED` and `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
