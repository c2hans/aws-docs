---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-frequencybandwidth.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config FrequencyBandwidth
<a name="aws-properties-groundstation-config-frequencybandwidth"></a>

 Defines a bandwidth.

## Syntax
<a name="aws-properties-groundstation-config-frequencybandwidth-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-frequencybandwidth-syntax.json"></a>

```
{
  "[Units](#cfn-groundstation-config-frequencybandwidth-units)" : {{String}},
  "[Value](#cfn-groundstation-config-frequencybandwidth-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-groundstation-config-frequencybandwidth-syntax.yaml"></a>

```
  [Units](#cfn-groundstation-config-frequencybandwidth-units): {{String}}
  [Value](#cfn-groundstation-config-frequencybandwidth-value): {{Number}}
```

## Properties
<a name="aws-properties-groundstation-config-frequencybandwidth-properties"></a>

`Units`  <a name="cfn-groundstation-config-frequencybandwidth-units"></a>
 The units of the bandwidth.
*Required*: No
*Type*: String
*Allowed values*: `GHz | MHz | kHz`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-groundstation-config-frequencybandwidth-value"></a>
 The value of the bandwidth. AWS Ground Station currently has the following bandwidth limitations:
+ For `AntennaDownlinkDemodDecodeconfig`, valid values are between 125 kHz to 650 MHz.
+ For `AntennaDownlinkconfig`, valid values are between 10 kHz to 54 MHz.
+ For `AntennaUplinkConfig`, valid values are between 10 kHz to 54 MHz.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-frequencybandwidth--examples"></a>

### Create a Bandwidth
<a name="aws-properties-groundstation-config-frequencybandwidth--examples--Create_a_Bandwidth"></a>

The following example creates a Ground Station `Bandwidth`

#### JSON
<a name="aws-properties-groundstation-config-frequencybandwidth--examples--Create_a_Bandwidth--json"></a>

```
{
  "Bandwidth": {
    "Value": 30,
    "Units": "MHz"
  },
}
```

#### YAML
<a name="aws-properties-groundstation-config-frequencybandwidth--examples--Create_a_Bandwidth--yaml"></a>

```
Bandwidth:
  Value: 30
  Units: MHz
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
