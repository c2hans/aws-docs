---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-frequency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config Frequency
<a name="aws-properties-groundstation-config-frequency"></a>

 Defines a frequency.

## Syntax
<a name="aws-properties-groundstation-config-frequency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-frequency-syntax.json"></a>

```
{
  "[Units](#cfn-groundstation-config-frequency-units)" : {{String}},
  "[Value](#cfn-groundstation-config-frequency-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-groundstation-config-frequency-syntax.yaml"></a>

```
  [Units](#cfn-groundstation-config-frequency-units): {{String}}
  [Value](#cfn-groundstation-config-frequency-value): {{Number}}
```

## Properties
<a name="aws-properties-groundstation-config-frequency-properties"></a>

`Units`  <a name="cfn-groundstation-config-frequency-units"></a>
 The units of the frequency.
*Required*: No
*Type*: String
*Allowed values*: `GHz | MHz | kHz`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-groundstation-config-frequency-value"></a>
 The value of the frequency. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-frequency--examples"></a>

### Create a Frequency
<a name="aws-properties-groundstation-config-frequency--examples--Create_a_Frequency"></a>

The following example creates a Ground Station `Frequency`

#### JSON
<a name="aws-properties-groundstation-config-frequency--examples--Create_a_Frequency--json"></a>

```
{
  "CenterFrequency": {
    "Value": 7812,
    "Units": "MHz"
  },
}
```

#### YAML
<a name="aws-properties-groundstation-config-frequency--examples--Create_a_Frequency--yaml"></a>

```
CenterFrequency:
  Value: 7812
  Units: MHz
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
