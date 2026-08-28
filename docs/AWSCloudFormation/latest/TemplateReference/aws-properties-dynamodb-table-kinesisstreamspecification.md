---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-kinesisstreamspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table KinesisStreamSpecification
<a name="aws-properties-dynamodb-table-kinesisstreamspecification"></a>

The Kinesis Data Streams configuration for the specified table.

## Syntax
<a name="aws-properties-dynamodb-table-kinesisstreamspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-kinesisstreamspecification-syntax.json"></a>

```
{
  "[ApproximateCreationDateTimePrecision](#cfn-dynamodb-table-kinesisstreamspecification-approximatecreationdatetimeprecision)" : {{String}},
  "[StreamArn](#cfn-dynamodb-table-kinesisstreamspecification-streamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-kinesisstreamspecification-syntax.yaml"></a>

```
  [ApproximateCreationDateTimePrecision](#cfn-dynamodb-table-kinesisstreamspecification-approximatecreationdatetimeprecision): {{String}}
  [StreamArn](#cfn-dynamodb-table-kinesisstreamspecification-streamarn): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-table-kinesisstreamspecification-properties"></a>

`ApproximateCreationDateTimePrecision`  <a name="cfn-dynamodb-table-kinesisstreamspecification-approximatecreationdatetimeprecision"></a>
The precision for the time and date that the stream was created.
*Required*: No
*Type*: String
*Allowed values*: `MICROSECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamArn`  <a name="cfn-dynamodb-table-kinesisstreamspecification-streamarn"></a>
The ARN for a specific Kinesis data stream.
Length Constraints: Minimum length of 37. Maximum length of 1024.
*Required*: Yes
*Type*: String
*Minimum*: `37`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-dynamodb-table-kinesisstreamspecification--seealso"></a>
+  [Change Data Capture for Kinesis Data Streams with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
