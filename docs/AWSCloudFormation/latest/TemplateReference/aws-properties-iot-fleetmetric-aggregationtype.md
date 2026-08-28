---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-fleetmetric-aggregationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::FleetMetric AggregationType
<a name="aws-properties-iot-fleetmetric-aggregationtype"></a>

The type of aggregation queries.

## Syntax
<a name="aws-properties-iot-fleetmetric-aggregationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-fleetmetric-aggregationtype-syntax.json"></a>

```
{
  "[Name](#cfn-iot-fleetmetric-aggregationtype-name)" : {{String}},
  "[Values](#cfn-iot-fleetmetric-aggregationtype-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-fleetmetric-aggregationtype-syntax.yaml"></a>

```
  [Name](#cfn-iot-fleetmetric-aggregationtype-name): {{String}}
  [Values](#cfn-iot-fleetmetric-aggregationtype-values): {{
    - String}}
```

## Properties
<a name="aws-properties-iot-fleetmetric-aggregationtype-properties"></a>

`Name`  <a name="cfn-iot-fleetmetric-aggregationtype-name"></a>
The name of the aggregation type.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-iot-fleetmetric-aggregationtype-values"></a>
A list of the values of aggregation types.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
