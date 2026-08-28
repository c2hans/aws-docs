---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-instance-monthlytransfer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Instance MonthlyTransfer
<a name="aws-properties-lightsail-instance-monthlytransfer"></a>

`MonthlyTransfer` is a property of the [Networking](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html) property. It describes the amount of allocated monthly data transfer (in GB) for an instance.

## Syntax
<a name="aws-properties-lightsail-instance-monthlytransfer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-instance-monthlytransfer-syntax.json"></a>

```
{
  "[GbPerMonthAllocated](#cfn-lightsail-instance-monthlytransfer-gbpermonthallocated)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-instance-monthlytransfer-syntax.yaml"></a>

```
  [GbPerMonthAllocated](#cfn-lightsail-instance-monthlytransfer-gbpermonthallocated): {{String}}
```

## Properties
<a name="aws-properties-lightsail-instance-monthlytransfer-properties"></a>

`GbPerMonthAllocated`  <a name="cfn-lightsail-instance-monthlytransfer-gbpermonthallocated"></a>
The amount of allocated monthly data transfer (in GB) for an instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
