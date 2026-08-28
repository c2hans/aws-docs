---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::InstanceStorageConfig KinesisStreamConfig
<a name="aws-properties-connect-instancestorageconfig-kinesisstreamconfig"></a>

Configuration information of a Kinesis data stream.

## Syntax
<a name="aws-properties-connect-instancestorageconfig-kinesisstreamconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-instancestorageconfig-kinesisstreamconfig-syntax.json"></a>

```
{
  "[StreamArn](#cfn-connect-instancestorageconfig-kinesisstreamconfig-streamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-instancestorageconfig-kinesisstreamconfig-syntax.yaml"></a>

```
  [StreamArn](#cfn-connect-instancestorageconfig-kinesisstreamconfig-streamarn): {{String}}
```

## Properties
<a name="aws-properties-connect-instancestorageconfig-kinesisstreamconfig-properties"></a>

`StreamArn`  <a name="cfn-connect-instancestorageconfig-kinesisstreamconfig-streamarn"></a>
The Amazon Resource Name (ARN) of the data stream.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:kinesis:[-a-z0-9]*:[0-9]{12}:stream/[-a-zA-Z0-9_.]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
