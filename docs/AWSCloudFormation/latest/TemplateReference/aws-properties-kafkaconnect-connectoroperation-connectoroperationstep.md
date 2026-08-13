---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connectoroperation-connectoroperationstep.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::ConnectorOperation ConnectorOperationStep
<a name="aws-properties-kafkaconnect-connectoroperation-connectoroperationstep"></a>

Details of a step that is involved in a connector's operation.

## Syntax
<a name="aws-properties-kafkaconnect-connectoroperation-connectoroperationstep-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connectoroperation-connectoroperationstep-syntax.json"></a>

```
{
  "[StepState](#cfn-kafkaconnect-connectoroperation-connectoroperationstep-stepstate)" : {{String}},
  "[StepType](#cfn-kafkaconnect-connectoroperation-connectoroperationstep-steptype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connectoroperation-connectoroperationstep-syntax.yaml"></a>

```
  [StepState](#cfn-kafkaconnect-connectoroperation-connectoroperationstep-stepstate): {{String}}
  [StepType](#cfn-kafkaconnect-connectoroperation-connectoroperationstep-steptype): {{String}}
```

## Properties
<a name="aws-properties-kafkaconnect-connectoroperation-connectoroperationstep-properties"></a>

`StepState`  <a name="cfn-kafkaconnect-connectoroperation-connectoroperationstep-stepstate"></a>
The step state of the operation.
*Required*: No
*Type*: String
*Allowed values*: `PENDING | IN_PROGRESS | COMPLETED | FAILED | CANCELLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StepType`  <a name="cfn-kafkaconnect-connectoroperation-connectoroperationstep-steptype"></a>
The step type of the operation.
*Required*: No
*Type*: String
*Allowed values*: `INITIALIZE_UPDATE | FINALIZE_UPDATE | UPDATE_WORKER_SETTING | UPDATE_CONNECTOR_CONFIGURATION | VALIDATE_UPDATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
