---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connectoroperation-capacitydescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::ConnectorOperation CapacityDescription
<a name="aws-properties-kafkaconnect-connectoroperation-capacitydescription"></a>

A description of the connector's capacity.

## Syntax
<a name="aws-properties-kafkaconnect-connectoroperation-capacitydescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connectoroperation-capacitydescription-syntax.json"></a>

```
{
  "[ProvisionedCapacity](#cfn-kafkaconnect-connectoroperation-capacitydescription-provisionedcapacity)" : {{ProvisionedCapacityDescription}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connectoroperation-capacitydescription-syntax.yaml"></a>

```
  [ProvisionedCapacity](#cfn-kafkaconnect-connectoroperation-capacitydescription-provisionedcapacity): {{
    ProvisionedCapacityDescription}}
```

## Properties
<a name="aws-properties-kafkaconnect-connectoroperation-capacitydescription-properties"></a>

`ProvisionedCapacity`  <a name="cfn-kafkaconnect-connectoroperation-capacitydescription-provisionedcapacity"></a>
Describes a connector's provisioned capacity.
*Required*: No
*Type*: [ProvisionedCapacityDescription](aws-properties-kafkaconnect-connectoroperation-provisionedcapacitydescription.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
