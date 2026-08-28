---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-linkapplicationlogsampling.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link LinkApplicationLogSampling
<a name="aws-properties-rtbfabric-link-linkapplicationlogsampling"></a>

Describes a link application log sample.

## Syntax
<a name="aws-properties-rtbfabric-link-linkapplicationlogsampling-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-linkapplicationlogsampling-syntax.json"></a>

```
{
  "[ErrorLog](#cfn-rtbfabric-link-linkapplicationlogsampling-errorlog)" : {{Number}},
  "[FilterLog](#cfn-rtbfabric-link-linkapplicationlogsampling-filterlog)" : {{Number}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-linkapplicationlogsampling-syntax.yaml"></a>

```
  [ErrorLog](#cfn-rtbfabric-link-linkapplicationlogsampling-errorlog): {{Number}}
  [FilterLog](#cfn-rtbfabric-link-linkapplicationlogsampling-filterlog): {{Number}}
```

## Properties
<a name="aws-properties-rtbfabric-link-linkapplicationlogsampling-properties"></a>

`ErrorLog`  <a name="cfn-rtbfabric-link-linkapplicationlogsampling-errorlog"></a>
An error log entry.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterLog`  <a name="cfn-rtbfabric-link-linkapplicationlogsampling-filterlog"></a>
A filter log entry.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
