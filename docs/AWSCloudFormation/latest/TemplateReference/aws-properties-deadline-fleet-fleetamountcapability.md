---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-fleetamountcapability.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet FleetAmountCapability
<a name="aws-properties-deadline-fleet-fleetamountcapability"></a>

The fleet amount and attribute capabilities.

## Syntax
<a name="aws-properties-deadline-fleet-fleetamountcapability-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-fleetamountcapability-syntax.json"></a>

```
{
  "[Max](#cfn-deadline-fleet-fleetamountcapability-max)" : {{Number}},
  "[Min](#cfn-deadline-fleet-fleetamountcapability-min)" : {{Number}},
  "[Name](#cfn-deadline-fleet-fleetamountcapability-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-fleetamountcapability-syntax.yaml"></a>

```
  [Max](#cfn-deadline-fleet-fleetamountcapability-max): {{Number}}
  [Min](#cfn-deadline-fleet-fleetamountcapability-min): {{Number}}
  [Name](#cfn-deadline-fleet-fleetamountcapability-name): {{String}}
```

## Properties
<a name="aws-properties-deadline-fleet-fleetamountcapability-properties"></a>

`Max`  <a name="cfn-deadline-fleet-fleetamountcapability-max"></a>
The maximum amount of the fleet worker capability.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-deadline-fleet-fleetamountcapability-min"></a>
The minimum amount of fleet worker capability.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-deadline-fleet-fleetamountcapability-name"></a>
The name of the fleet capability.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z][a-zA-Z0-9]{0,63}:)?amount(\.[a-zA-Z][a-zA-Z0-9]{0,63})+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
