---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-metricattribution-s3datadestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::MetricAttribution S3DataDestination
<a name="aws-properties-personalize-metricattribution-s3datadestination"></a>

<a name="aws-properties-personalize-metricattribution-s3datadestination-description"></a>The `S3DataDestination` property type specifies Property description not available. for an [AWS::Personalize::MetricAttribution](aws-resource-personalize-metricattribution.md).

## Syntax
<a name="aws-properties-personalize-metricattribution-s3datadestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-metricattribution-s3datadestination-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-personalize-metricattribution-s3datadestination-kmskeyarn)" : {{String}},
  "[Path](#cfn-personalize-metricattribution-s3datadestination-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-metricattribution-s3datadestination-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-personalize-metricattribution-s3datadestination-kmskeyarn): {{String}}
  [Path](#cfn-personalize-metricattribution-s3datadestination-path): {{String}}
```

## Properties
<a name="aws-properties-personalize-metricattribution-s3datadestination-properties"></a>

`KmsKeyArn`  <a name="cfn-personalize-metricattribution-s3datadestination-kmskeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws.*:kms:.*:[0-9]{12}:key/`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-personalize-metricattribution-s3datadestination-path"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(s3|http|https)://.+$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
