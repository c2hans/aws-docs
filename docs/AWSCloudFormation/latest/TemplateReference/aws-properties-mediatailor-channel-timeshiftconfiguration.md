---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-channel-timeshiftconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Channel TimeShiftConfiguration
<a name="aws-properties-mediatailor-channel-timeshiftconfiguration"></a>

 The configuration for time-shifted viewing.

## Syntax
<a name="aws-properties-mediatailor-channel-timeshiftconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-channel-timeshiftconfiguration-syntax.json"></a>

```
{
  "[MaxTimeDelaySeconds](#cfn-mediatailor-channel-timeshiftconfiguration-maxtimedelayseconds)" : {{Number}}
}
```

### YAML
<a name="aws-properties-mediatailor-channel-timeshiftconfiguration-syntax.yaml"></a>

```
  [MaxTimeDelaySeconds](#cfn-mediatailor-channel-timeshiftconfiguration-maxtimedelayseconds): {{Number}}
```

## Properties
<a name="aws-properties-mediatailor-channel-timeshiftconfiguration-properties"></a>

`MaxTimeDelaySeconds`  <a name="cfn-mediatailor-channel-timeshiftconfiguration-maxtimedelayseconds"></a>
 The maximum time delay for time-shifted viewing. The minimum allowed maximum time delay is 0 seconds, and the maximum allowed maximum time delay is 21600 seconds (6 hours).
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
