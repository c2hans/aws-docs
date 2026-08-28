---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-securityprofile-metricvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SecurityProfile MetricValue
<a name="aws-properties-iot-securityprofile-metricvalue"></a>

The value to be compared with the `metric`.

## Syntax
<a name="aws-properties-iot-securityprofile-metricvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-securityprofile-metricvalue-syntax.json"></a>

```
{
  "[Cidrs](#cfn-iot-securityprofile-metricvalue-cidrs)" : {{[ String, ... ]}},
  "[Count](#cfn-iot-securityprofile-metricvalue-count)" : {{String}},
  "[Number](#cfn-iot-securityprofile-metricvalue-number)" : {{Number}},
  "[Numbers](#cfn-iot-securityprofile-metricvalue-numbers)" : {{[ Number, ... ]}},
  "[Ports](#cfn-iot-securityprofile-metricvalue-ports)" : {{[ Integer, ... ]}},
  "[Strings](#cfn-iot-securityprofile-metricvalue-strings)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-securityprofile-metricvalue-syntax.yaml"></a>

```
  [Cidrs](#cfn-iot-securityprofile-metricvalue-cidrs): {{
    - String}}
  [Count](#cfn-iot-securityprofile-metricvalue-count): {{String}}
  [Number](#cfn-iot-securityprofile-metricvalue-number): {{
    Number}}
  [Numbers](#cfn-iot-securityprofile-metricvalue-numbers): {{
    - Number}}
  [Ports](#cfn-iot-securityprofile-metricvalue-ports): {{
    - Integer}}
  [Strings](#cfn-iot-securityprofile-metricvalue-strings): {{
    - String}}
```

## Properties
<a name="aws-properties-iot-securityprofile-metricvalue-properties"></a>

`Cidrs`  <a name="cfn-iot-securityprofile-metricvalue-cidrs"></a>
If the `comparisonOperator` calls for a set of CIDRs, use this to specify that set to be compared with the `metric`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Count`  <a name="cfn-iot-securityprofile-metricvalue-count"></a>
If the `comparisonOperator` calls for a numeric value, use this to specify that numeric value to be compared with the `metric`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Number`  <a name="cfn-iot-securityprofile-metricvalue-number"></a>
The numeric values of a metric.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Numbers`  <a name="cfn-iot-securityprofile-metricvalue-numbers"></a>
The numeric value of a metric.
*Required*: No
*Type*: Array of Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ports`  <a name="cfn-iot-securityprofile-metricvalue-ports"></a>
If the `comparisonOperator` calls for a set of ports, use this to specify that set to be compared with the `metric`.
*Required*: No
*Type*: Array of Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strings`  <a name="cfn-iot-securityprofile-metricvalue-strings"></a>
The string values of a metric.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
