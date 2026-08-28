---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-neptuneungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan NeptuneUngraceful
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful"></a>

Configuration for handling failures when performing operations on Neptune global databases.

## Syntax
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful-syntax.json"></a>

```
{
  "[Ungraceful](#cfn-arcregionswitch-plan-neptuneungraceful-ungraceful)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful-syntax.yaml"></a>

```
  [Ungraceful](#cfn-arcregionswitch-plan-neptuneungraceful-ungraceful): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful-properties"></a>

`Ungraceful`  <a name="cfn-arcregionswitch-plan-neptuneungraceful-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: String
*Allowed values*: `failover`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
