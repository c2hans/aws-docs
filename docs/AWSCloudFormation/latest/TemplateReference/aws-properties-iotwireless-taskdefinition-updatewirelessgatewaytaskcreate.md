---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::TaskDefinition UpdateWirelessGatewayTaskCreate
<a name="aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate"></a>

UpdateWirelessGatewayTaskCreate object.

## Syntax
<a name="aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-syntax.json"></a>

```
{
  "[LoRaWAN](#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan)" : {{LoRaWANUpdateGatewayTaskCreate}},
  "[UpdateDataRole](#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole)" : {{String}},
  "[UpdateDataSource](#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-syntax.yaml"></a>

```
  [LoRaWAN](#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan): {{
    LoRaWANUpdateGatewayTaskCreate}}
  [UpdateDataRole](#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole): {{String}}
  [UpdateDataSource](#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-properties"></a>

`LoRaWAN`  <a name="cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan"></a>
The properties that relate to the LoRaWAN wireless gateway.
*Required*: No
*Type*: [LoRaWANUpdateGatewayTaskCreate](aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateDataRole`  <a name="cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole"></a>
The IAM role used to read data from the S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateDataSource`  <a name="cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource"></a>
The link to the S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
