---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSetEventDestination DimensionConfiguration
<a name="aws-properties-ses-configurationseteventdestination-dimensionconfiguration"></a>

An object that defines the dimension configuration to use when you send email events to Amazon CloudWatch.

## Syntax
<a name="aws-properties-ses-configurationseteventdestination-dimensionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationseteventdestination-dimensionconfiguration-syntax.json"></a>

```
{
  "[DefaultDimensionValue](#cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue)" : {{String}},
  "[DimensionName](#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname)" : {{String}},
  "[DimensionValueSource](#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-configurationseteventdestination-dimensionconfiguration-syntax.yaml"></a>

```
  [DefaultDimensionValue](#cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue): {{String}}
  [DimensionName](#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname): {{String}}
  [DimensionValueSource](#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource): {{String}}
```

## Properties
<a name="aws-properties-ses-configurationseteventdestination-dimensionconfiguration-properties"></a>

`DefaultDimensionValue`  <a name="cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue"></a>
The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:
+ Can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-), at signs (@), and periods (.).
+ It can contain no more than 255 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionName`  <a name="cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname"></a>
The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:
+ It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-).
+ It can contain no more than 255 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_:-]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionValueSource`  <a name="cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource"></a>
The location where the Amazon SES API v2 finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an `X-SES-MESSAGE-TAGS` header or a parameter to the `SendEmail` or `SendRawEmail` API, choose `messageTag`. To use your own email headers, choose `emailHeader`. To use link tags, choose `linkTag`.
*Required*: Yes
*Type*: String
*Allowed values*: `messageTag | emailHeader | linkTag`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
