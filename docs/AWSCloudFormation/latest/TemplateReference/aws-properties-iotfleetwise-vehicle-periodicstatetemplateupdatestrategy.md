---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Vehicle PeriodicStateTemplateUpdateStrategy
<a name="aws-properties-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy"></a>

Vehicles associated with the state template will stream telemetry data during a specified time period.

## Syntax
<a name="aws-properties-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy-syntax.json"></a>

```
{
  "[StateTemplateUpdateRate](#cfn-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy-statetemplateupdaterate)" : {{TimePeriod}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy-syntax.yaml"></a>

```
  [StateTemplateUpdateRate](#cfn-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy-statetemplateupdaterate): {{
    TimePeriod}}
```

## Properties
<a name="aws-properties-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy-properties"></a>

`StateTemplateUpdateRate`  <a name="cfn-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy-statetemplateupdaterate"></a>
Property description not available.
*Required*: Yes
*Type*: [TimePeriod](aws-properties-iotfleetwise-vehicle-timeperiod.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
