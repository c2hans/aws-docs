---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-automaticfailconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm AutomaticFailConfiguration
<a name="aws-properties-connect-evaluationform-automaticfailconfiguration"></a>

Information about automatic fail configuration for an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-automaticfailconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-automaticfailconfiguration-syntax.json"></a>

```
{
  "[TargetSection](#cfn-connect-evaluationform-automaticfailconfiguration-targetsection)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-automaticfailconfiguration-syntax.yaml"></a>

```
  [TargetSection](#cfn-connect-evaluationform-automaticfailconfiguration-targetsection): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-automaticfailconfiguration-properties"></a>

`TargetSection`  <a name="cfn-connect-evaluationform-automaticfailconfiguration-targetsection"></a>
The referenceId of the target section for auto failure.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,40}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
