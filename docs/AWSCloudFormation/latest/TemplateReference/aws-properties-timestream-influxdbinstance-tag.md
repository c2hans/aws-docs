---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-influxdbinstance-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBInstance Tag
<a name="aws-properties-timestream-influxdbinstance-tag"></a>

 A tag is a label that you assign to a Timestream for InfluxDB resource. Each tag consists of a key and an optional value, both of which you define. With tags, you can categorize databases and/or tables, for example, by purpose, owner, or environment.

## Syntax
<a name="aws-properties-timestream-influxdbinstance-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-influxdbinstance-tag-syntax.json"></a>

```
{
  "[Key](#cfn-timestream-influxdbinstance-tag-key)" : {{String}},
  "[Value](#cfn-timestream-influxdbinstance-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-influxdbinstance-tag-syntax.yaml"></a>

```
  [Key](#cfn-timestream-influxdbinstance-tag-key): {{String}}
  [Value](#cfn-timestream-influxdbinstance-tag-value): {{String}}
```

## Properties
<a name="aws-properties-timestream-influxdbinstance-tag-properties"></a>

`Key`  <a name="cfn-timestream-influxdbinstance-tag-key"></a>
 The key of the tag. Tag keys are case sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-timestream-influxdbinstance-tag-value"></a>
 The value of the tag. Tag values are case-sensitive and can be null.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
