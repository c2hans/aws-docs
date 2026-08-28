---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-eirp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config Eirp
<a name="aws-properties-groundstation-config-eirp"></a>

 Defines an equivalent isotropically radiated power (EIRP).

## Syntax
<a name="aws-properties-groundstation-config-eirp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-eirp-syntax.json"></a>

```
{
  "[Units](#cfn-groundstation-config-eirp-units)" : {{String}},
  "[Value](#cfn-groundstation-config-eirp-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-groundstation-config-eirp-syntax.yaml"></a>

```
  [Units](#cfn-groundstation-config-eirp-units): {{String}}
  [Value](#cfn-groundstation-config-eirp-value): {{Number}}
```

## Properties
<a name="aws-properties-groundstation-config-eirp-properties"></a>

`Units`  <a name="cfn-groundstation-config-eirp-units"></a>
 The units of the EIRP.
*Required*: No
*Type*: String
*Allowed values*: `dBW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-groundstation-config-eirp-value"></a>
 The value of the EIRP. Valid values are between 20.0 to 50.0 dBW.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-eirp--examples"></a>

### Create an EIRP
<a name="aws-properties-groundstation-config-eirp--examples--Create_an_EIRP"></a>

The following example creates a Ground Station `EIRP`

#### JSON
<a name="aws-properties-groundstation-config-eirp--examples--Create_an_EIRP--json"></a>

```
{
  "TargetEirp": {
    "Value": 20,
    "Units": "dBW"
  }
}
```

#### YAML
<a name="aws-properties-groundstation-config-eirp--examples--Create_an_EIRP--yaml"></a>

```
TargetEirp:
  Value: 20.0
  Units: dBW
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
