---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-parsejson.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer ParseJSON
<a name="aws-properties-logs-transformer-parsejson"></a>

This processor parses log events that are in JSON format. It can extract JSON key-value pairs and place them under a destination that you specify.

Additionally, because you must have at least one parse-type processor in a transformer, you can use `ParseJSON` as that processor for JSON-format logs, so that you can also apply other processors, such as mutate processors, to these logs.

For more information about this processor including examples, see [ parseJSON](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseJSON) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-parsejson-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-parsejson-syntax.json"></a>

```
{
  "[Destination](#cfn-logs-transformer-parsejson-destination)" : {{String}},
  "[Source](#cfn-logs-transformer-parsejson-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-parsejson-syntax.yaml"></a>

```
  [Destination](#cfn-logs-transformer-parsejson-destination): {{String}}
  [Source](#cfn-logs-transformer-parsejson-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-parsejson-properties"></a>

`Destination`  <a name="cfn-logs-transformer-parsejson-destination"></a>
The location to put the parsed key value pair into. If you omit this parameter, it is placed under the root node.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-parsejson-source"></a>
Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, `store.book`
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
