---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connectoroperation-provisionedcapacitydescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::ConnectorOperation ProvisionedCapacityDescription
<a name="aws-properties-kafkaconnect-connectoroperation-provisionedcapacitydescription"></a>

The description of a connector's provisioned capacity.

## Syntax
<a name="aws-properties-kafkaconnect-connectoroperation-provisionedcapacitydescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connectoroperation-provisionedcapacitydescription-syntax.json"></a>

```
{
  "[McuCount](#cfn-kafkaconnect-connectoroperation-provisionedcapacitydescription-mcucount)" : {{Integer}},
  "[WorkerCount](#cfn-kafkaconnect-connectoroperation-provisionedcapacitydescription-workercount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connectoroperation-provisionedcapacitydescription-syntax.yaml"></a>

```
  [McuCount](#cfn-kafkaconnect-connectoroperation-provisionedcapacitydescription-mcucount): {{Integer}}
  [WorkerCount](#cfn-kafkaconnect-connectoroperation-provisionedcapacitydescription-workercount): {{Integer}}
```

## Properties
<a name="aws-properties-kafkaconnect-connectoroperation-provisionedcapacitydescription-properties"></a>

`McuCount`  <a name="cfn-kafkaconnect-connectoroperation-provisionedcapacitydescription-mcucount"></a>
The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkerCount`  <a name="cfn-kafkaconnect-connectoroperation-provisionedcapacitydescription-workercount"></a>
The number of workers that are allocated to the connector.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
