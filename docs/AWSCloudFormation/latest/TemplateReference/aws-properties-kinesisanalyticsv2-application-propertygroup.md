---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-propertygroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application PropertyGroup
<a name="aws-properties-kinesisanalyticsv2-application-propertygroup"></a>

Property key-value pairs passed into an application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-propertygroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-propertygroup-syntax.json"></a>

```
{
  "[PropertyGroupId](#cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid)" : {{String}},
  "[PropertyMap](#cfn-kinesisanalyticsv2-application-propertygroup-propertymap)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-propertygroup-syntax.yaml"></a>

```
  [PropertyGroupId](#cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid): {{String}}
  [PropertyMap](#cfn-kinesisanalyticsv2-application-propertygroup-propertymap): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-propertygroup-properties"></a>

`PropertyGroupId`  <a name="cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid"></a>
Describes the key of an application execution property key-value pair.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyMap`  <a name="cfn-kinesisanalyticsv2-application-propertygroup-propertymap"></a>
Describes the value of an application execution property key-value pair.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{1,2048}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-propertygroup--seealso"></a>
+ [PropertyGroup](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_PropertyGroup.html) in the *Amazon Kinesis Data Analytics API Reference*
