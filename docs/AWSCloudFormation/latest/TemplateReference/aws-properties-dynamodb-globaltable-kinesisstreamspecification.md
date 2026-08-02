---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-kinesisstreamspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable KinesisStreamSpecification
<a name="aws-properties-dynamodb-globaltable-kinesisstreamspecification"></a>

The Kinesis Data Streams configuration for the specified global table replica.

## Syntax
<a name="aws-properties-dynamodb-globaltable-kinesisstreamspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-kinesisstreamspecification-syntax.json"></a>

```
{
  "[ApproximateCreationDateTimePrecision](#cfn-dynamodb-globaltable-kinesisstreamspecification-approximatecreationdatetimeprecision)" : {{String}},
  "[StreamArn](#cfn-dynamodb-globaltable-kinesisstreamspecification-streamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-kinesisstreamspecification-syntax.yaml"></a>

```
  [ApproximateCreationDateTimePrecision](#cfn-dynamodb-globaltable-kinesisstreamspecification-approximatecreationdatetimeprecision): {{String}}
  [StreamArn](#cfn-dynamodb-globaltable-kinesisstreamspecification-streamarn): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-kinesisstreamspecification-properties"></a>

`ApproximateCreationDateTimePrecision`  <a name="cfn-dynamodb-globaltable-kinesisstreamspecification-approximatecreationdatetimeprecision"></a>
The precision for the time and date that the stream was created.
*Required*: No
*Type*: String
*Allowed values*: `MICROSECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamArn`  <a name="cfn-dynamodb-globaltable-kinesisstreamspecification-streamarn"></a>
The ARN for a specific Kinesis data stream.
*Required*: Yes
*Type*: String
*Minimum*: `37`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
