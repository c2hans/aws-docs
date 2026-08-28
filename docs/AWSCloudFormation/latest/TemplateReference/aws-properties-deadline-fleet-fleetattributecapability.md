---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-fleetattributecapability.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet FleetAttributeCapability
<a name="aws-properties-deadline-fleet-fleetattributecapability"></a>

Defines the fleet's capability name, minimum, and maximum.

## Syntax
<a name="aws-properties-deadline-fleet-fleetattributecapability-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-fleetattributecapability-syntax.json"></a>

```
{
  "[Name](#cfn-deadline-fleet-fleetattributecapability-name)" : {{String}},
  "[Values](#cfn-deadline-fleet-fleetattributecapability-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-fleetattributecapability-syntax.yaml"></a>

```
  [Name](#cfn-deadline-fleet-fleetattributecapability-name): {{String}}
  [Values](#cfn-deadline-fleet-fleetattributecapability-values): {{
    - String}}
```

## Properties
<a name="aws-properties-deadline-fleet-fleetattributecapability-properties"></a>

`Name`  <a name="cfn-deadline-fleet-fleetattributecapability-name"></a>
The name of the fleet attribute capability for the worker.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z][a-zA-Z0-9]{0,63}:)?attr(\.[a-zA-Z][a-zA-Z0-9]{0,63})+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-deadline-fleet-fleetattributecapability-values"></a>
The number of fleet attribute capabilities.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
