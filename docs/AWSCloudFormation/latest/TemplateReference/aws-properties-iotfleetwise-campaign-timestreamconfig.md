---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-timestreamconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign TimestreamConfig
<a name="aws-properties-iotfleetwise-campaign-timestreamconfig"></a>

The Amazon Timestream table where the AWS IoT FleetWise campaign sends data. Timestream stores and organizes data to optimize query processing time and to reduce storage costs. For more information, see [Data modeling](https://docs.aws.amazon.com/timestream/latest/developerguide/data-modeling.html) in the *Amazon Timestream Developer Guide*.

## Syntax
<a name="aws-properties-iotfleetwise-campaign-timestreamconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-timestreamconfig-syntax.json"></a>

```
{
  "[ExecutionRoleArn](#cfn-iotfleetwise-campaign-timestreamconfig-executionrolearn)" : {{String}},
  "[TimestreamTableArn](#cfn-iotfleetwise-campaign-timestreamconfig-timestreamtablearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-timestreamconfig-syntax.yaml"></a>

```
  [ExecutionRoleArn](#cfn-iotfleetwise-campaign-timestreamconfig-executionrolearn): {{String}}
  [TimestreamTableArn](#cfn-iotfleetwise-campaign-timestreamconfig-timestreamtablearn): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-timestreamconfig-properties"></a>

`ExecutionRoleArn`  <a name="cfn-iotfleetwise-campaign-timestreamconfig-executionrolearn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants AWS IoT FleetWise permission to deliver data to the Amazon Timestream table.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimestreamTableArn`  <a name="cfn-iotfleetwise-campaign-timestreamconfig-timestreamtablearn"></a>
The Amazon Resource Name (ARN) of the Amazon Timestream table.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):timestream:[a-zA-Z0-9-]+:[0-9]{12}:database\/[a-zA-Z0-9_.-]+\/table\/[a-zA-Z0-9_.-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
