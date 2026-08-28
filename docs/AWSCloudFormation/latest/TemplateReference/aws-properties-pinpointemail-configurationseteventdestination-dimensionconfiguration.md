---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PinpointEmail::ConfigurationSetEventDestination DimensionConfiguration
<a name="aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration"></a>

An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

## Syntax
<a name="aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration-syntax.json"></a>

```
{
  "[DefaultDimensionValue](#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue)" : {{String}},
  "[DimensionName](#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionname)" : {{String}},
  "[DimensionValueSource](#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration-syntax.yaml"></a>

```
  [DefaultDimensionValue](#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue): {{String}}
  [DimensionName](#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionname): {{String}}
  [DimensionValueSource](#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource): {{String}}
```

## Properties
<a name="aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration-properties"></a>

`DefaultDimensionValue`  <a name="cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue"></a>
The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:
+ It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-).
+ It can contain no more than 256 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionName`  <a name="cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionname"></a>
The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:
+ It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-).
+ It can contain no more than 256 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionValueSource`  <a name="cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource"></a>
The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. Acceptable values: `MESSAGE_TAG`, `EMAIL_HEADER`, and `LINK_TAG`.
If you want Amazon Pinpoint to use the message tags that you specify using an `X-SES-MESSAGE-TAGS` header or a parameter to the `SendEmail` API, choose `MESSAGE_TAG`. If you want Amazon Pinpoint to use your own email headers, choose `EMAIL_HEADER`. If you want Amazon Pinpoint to use tags that are specified in your links, choose `LINK_TAG`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
