---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-instance-networking.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Instance Networking
<a name="aws-properties-lightsail-instance-networking"></a>

`Networking` is a property of the [AWS::Lightsail::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html) resource. It describes the public ports and the monthly amount of data transfer allocated for the instance.

## Syntax
<a name="aws-properties-lightsail-instance-networking-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-instance-networking-syntax.json"></a>

```
{
  "[MonthlyTransfer](#cfn-lightsail-instance-networking-monthlytransfer)" : {{MonthlyTransfer}},
  "[Ports](#cfn-lightsail-instance-networking-ports)" : {{[ Port, ... ]}}
}
```

### YAML
<a name="aws-properties-lightsail-instance-networking-syntax.yaml"></a>

```
  [MonthlyTransfer](#cfn-lightsail-instance-networking-monthlytransfer): {{
    MonthlyTransfer}}
  [Ports](#cfn-lightsail-instance-networking-ports): {{
    - Port}}
```

## Properties
<a name="aws-properties-lightsail-instance-networking-properties"></a>

`MonthlyTransfer`  <a name="cfn-lightsail-instance-networking-monthlytransfer"></a>
The monthly amount of data transfer, in GB, allocated for the instance
*Required*: No
*Type*: [MonthlyTransfer](aws-properties-lightsail-instance-monthlytransfer.md)
*Update requires*: Updates are not supported.

`Ports`  <a name="cfn-lightsail-instance-networking-ports"></a>
An array of ports to open on the instance.
*Required*: Yes
*Type*: Array of [Port](aws-properties-lightsail-instance-port.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
