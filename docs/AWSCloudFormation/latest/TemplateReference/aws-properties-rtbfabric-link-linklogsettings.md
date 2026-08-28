---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-linklogsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link LinkLogSettings
<a name="aws-properties-rtbfabric-link-linklogsettings"></a>

Describes the settings for a link log.

## Syntax
<a name="aws-properties-rtbfabric-link-linklogsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-linklogsettings-syntax.json"></a>

```
{
  "[ApplicationLogs](#cfn-rtbfabric-link-linklogsettings-applicationlogs)" : {{ApplicationLogs}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-linklogsettings-syntax.yaml"></a>

```
  [ApplicationLogs](#cfn-rtbfabric-link-linklogsettings-applicationlogs): {{
    ApplicationLogs}}
```

## Properties
<a name="aws-properties-rtbfabric-link-linklogsettings-properties"></a>

`ApplicationLogs`  <a name="cfn-rtbfabric-link-linklogsettings-applicationlogs"></a>
Describes the configuration of a link application log.
*Required*: Yes
*Type*: [ApplicationLogs](aws-properties-rtbfabric-link-applicationlogs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
