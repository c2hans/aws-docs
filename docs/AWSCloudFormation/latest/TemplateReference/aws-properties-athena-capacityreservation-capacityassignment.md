---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-capacityreservation-capacityassignment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::CapacityReservation CapacityAssignment
<a name="aws-properties-athena-capacityreservation-capacityassignment"></a>

A mapping between one or more workgroups and a capacity reservation.

## Syntax
<a name="aws-properties-athena-capacityreservation-capacityassignment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-capacityreservation-capacityassignment-syntax.json"></a>

```
{
  "[WorkgroupNames](#cfn-athena-capacityreservation-capacityassignment-workgroupnames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-athena-capacityreservation-capacityassignment-syntax.yaml"></a>

```
  [WorkgroupNames](#cfn-athena-capacityreservation-capacityassignment-workgroupnames): {{
    - String}}
```

## Properties
<a name="aws-properties-athena-capacityreservation-capacityassignment-properties"></a>

`WorkgroupNames`  <a name="cfn-athena-capacityreservation-capacityassignment-workgroupnames"></a>
The list of workgroup names for the capacity assignment.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
