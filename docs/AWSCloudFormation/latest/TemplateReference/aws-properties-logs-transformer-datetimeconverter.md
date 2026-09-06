---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-datetimeconverter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer DateTimeConverter
<a name="aws-properties-logs-transformer-datetimeconverter"></a>

This processor converts a datetime string into a format that you specify.

For more information about this processor including examples, see [ datetimeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-datetimeConverter) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-datetimeconverter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-datetimeconverter-syntax.json"></a>

```
{
  "[Locale](#cfn-logs-transformer-datetimeconverter-locale)" : {{String}},
  "[MatchPatterns](#cfn-logs-transformer-datetimeconverter-matchpatterns)" : {{[ String, ... ]}},
  "[Source](#cfn-logs-transformer-datetimeconverter-source)" : {{String}},
  "[SourceTimezone](#cfn-logs-transformer-datetimeconverter-sourcetimezone)" : {{String}},
  "[Target](#cfn-logs-transformer-datetimeconverter-target)" : {{String}},
  "[TargetFormat](#cfn-logs-transformer-datetimeconverter-targetformat)" : {{String}},
  "[TargetTimezone](#cfn-logs-transformer-datetimeconverter-targettimezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-datetimeconverter-syntax.yaml"></a>

```
  [Locale](#cfn-logs-transformer-datetimeconverter-locale): {{String}}
  [MatchPatterns](#cfn-logs-transformer-datetimeconverter-matchpatterns): {{
    - String}}
  [Source](#cfn-logs-transformer-datetimeconverter-source): {{String}}
  [SourceTimezone](#cfn-logs-transformer-datetimeconverter-sourcetimezone): {{String}}
  [Target](#cfn-logs-transformer-datetimeconverter-target): {{String}}
  [TargetFormat](#cfn-logs-transformer-datetimeconverter-targetformat): {{String}}
  [TargetTimezone](#cfn-logs-transformer-datetimeconverter-targettimezone): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-datetimeconverter-properties"></a>

`Locale`  <a name="cfn-logs-transformer-datetimeconverter-locale"></a>
The locale of the source field. If you omit this, the default of `locale.ROOT` is used.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchPatterns`  <a name="cfn-logs-transformer-datetimeconverter-matchpatterns"></a>
A list of patterns to match against the `source` field.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-datetimeconverter-source"></a>
The key to apply the date conversion to.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTimezone`  <a name="cfn-logs-transformer-datetimeconverter-sourcetimezone"></a>
The time zone of the source field. If you omit this, the default used is the UTC zone.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-logs-transformer-datetimeconverter-target"></a>
The JSON field to store the result in.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetFormat`  <a name="cfn-logs-transformer-datetimeconverter-targetformat"></a>
The datetime format to use for the converted data in the target field.
If you omit this, the default of ` yyyy-MM-dd'T'HH:mm:ss.SSS'Z` is used.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetTimezone`  <a name="cfn-logs-transformer-datetimeconverter-targettimezone"></a>
The time zone of the target field. If you omit this, the default used is the UTC zone.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
