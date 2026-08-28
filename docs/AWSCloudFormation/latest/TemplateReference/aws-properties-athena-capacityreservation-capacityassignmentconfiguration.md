---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-capacityreservation-capacityassignmentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::CapacityReservation CapacityAssignmentConfiguration
<a name="aws-properties-athena-capacityreservation-capacityassignmentconfiguration"></a>

Assigns Athena workgroups (and hence their queries) to capacity reservations. A capacity reservation can have only one capacity assignment configuration, but the capacity assignment configuration can be made up of multiple individual assignments. Each assignment specifies how Athena queries can consume capacity from the capacity reservation that their workgroup is mapped to.

## Syntax
<a name="aws-properties-athena-capacityreservation-capacityassignmentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-capacityreservation-capacityassignmentconfiguration-syntax.json"></a>

```
{
  "[CapacityAssignments](#cfn-athena-capacityreservation-capacityassignmentconfiguration-capacityassignments)" : {{[ CapacityAssignment, ... ]}}
}
```

### YAML
<a name="aws-properties-athena-capacityreservation-capacityassignmentconfiguration-syntax.yaml"></a>

```
  [CapacityAssignments](#cfn-athena-capacityreservation-capacityassignmentconfiguration-capacityassignments): {{
    - CapacityAssignment}}
```

## Properties
<a name="aws-properties-athena-capacityreservation-capacityassignmentconfiguration-properties"></a>

`CapacityAssignments`  <a name="cfn-athena-capacityreservation-capacityassignmentconfiguration-capacityassignments"></a>
The list of assignments that make up the capacity assignment configuration.
*Required*: Yes
*Type*: Array of [CapacityAssignment](aws-properties-athena-capacityreservation-capacityassignment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
