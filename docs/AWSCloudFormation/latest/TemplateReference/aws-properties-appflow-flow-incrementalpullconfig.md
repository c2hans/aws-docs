---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-incrementalpullconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow IncrementalPullConfig
<a name="aws-properties-appflow-flow-incrementalpullconfig"></a>

 Specifies the configuration used when importing incremental records from the source.

## Syntax
<a name="aws-properties-appflow-flow-incrementalpullconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-incrementalpullconfig-syntax.json"></a>

```
{
  "[DatetimeTypeFieldName](#cfn-appflow-flow-incrementalpullconfig-datetimetypefieldname)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-incrementalpullconfig-syntax.yaml"></a>

```
  [DatetimeTypeFieldName](#cfn-appflow-flow-incrementalpullconfig-datetimetypefieldname): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-incrementalpullconfig-properties"></a>

`DatetimeTypeFieldName`  <a name="cfn-appflow-flow-incrementalpullconfig-datetimetypefieldname"></a>
 A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
