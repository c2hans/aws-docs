---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-uplinkechoconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config UplinkEchoConfig
<a name="aws-properties-groundstation-config-uplinkechoconfig"></a>

 Provides information about how AWS Ground Station should echo back uplink transmissions to a dataflow endpoint.

## Syntax
<a name="aws-properties-groundstation-config-uplinkechoconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-uplinkechoconfig-syntax.json"></a>

```
{
  "[AntennaUplinkConfigArn](#cfn-groundstation-config-uplinkechoconfig-antennauplinkconfigarn)" : {{String}},
  "[Enabled](#cfn-groundstation-config-uplinkechoconfig-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-groundstation-config-uplinkechoconfig-syntax.yaml"></a>

```
  [AntennaUplinkConfigArn](#cfn-groundstation-config-uplinkechoconfig-antennauplinkconfigarn): {{String}}
  [Enabled](#cfn-groundstation-config-uplinkechoconfig-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-groundstation-config-uplinkechoconfig-properties"></a>

`AntennaUplinkConfigArn`  <a name="cfn-groundstation-config-uplinkechoconfig-antennauplinkconfigarn"></a>
 Defines the ARN of the uplink config to echo back to a dataflow endpoint.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-groundstation-config-uplinkechoconfig-enabled"></a>
 Whether or not uplink echo is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-uplinkechoconfig--examples"></a>

### Create an UplinkEchoConfig
<a name="aws-properties-groundstation-config-uplinkechoconfig--examples--Create_an_UplinkEchoConfig"></a>

The following example creates a Ground Station `UplinkEchoConfig`

#### JSON
<a name="aws-properties-groundstation-config-uplinkechoconfig--examples--Create_an_UplinkEchoConfig--json"></a>

```
{
  "UplinkEchoConfig": {
    "AntennaUplinkConfigArn": "arn:aws:groundstation:us-east-2:012345678910:config/antenna-uplink/11111111-1111-1111-1111-111111111111",
    "Enabled": true
  }
}
```

#### YAML
<a name="aws-properties-groundstation-config-uplinkechoconfig--examples--Create_an_UplinkEchoConfig--yaml"></a>

```
UplinkEchoConfig:
  AntennaUplinkConfigArn: arn:aws:groundstation:us-east-2:012345678910:config/antenna-uplink/11111111-1111-1111-1111-111111111111
  Enabled: true
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
