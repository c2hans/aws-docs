---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate ExperimentTemplateStopCondition
<a name="aws-properties-fis-experimenttemplate-experimenttemplatestopcondition"></a>

Specifies a stop condition for an experiment template.

For more information, see [Stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html) in the *AWS Fault Injection Service User Guide*.

## Syntax
<a name="aws-properties-fis-experimenttemplate-experimenttemplatestopcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-experimenttemplatestopcondition-syntax.json"></a>

```
{
  "[Source](#cfn-fis-experimenttemplate-experimenttemplatestopcondition-source)" : {{String}},
  "[Value](#cfn-fis-experimenttemplate-experimenttemplatestopcondition-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-experimenttemplatestopcondition-syntax.yaml"></a>

```
  [Source](#cfn-fis-experimenttemplate-experimenttemplatestopcondition-source): {{String}}
  [Value](#cfn-fis-experimenttemplate-experimenttemplatestopcondition-value): {{String}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-experimenttemplatestopcondition-properties"></a>

`Source`  <a name="cfn-fis-experimenttemplate-experimenttemplatestopcondition-source"></a>
The source for the stop condition.
*Required*: Yes
*Type*: String
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-fis-experimenttemplate-experimenttemplatestopcondition-value"></a>
The Amazon Resource Name (ARN) of the CloudWatch alarm, if applicable.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
