---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-questionoptionpointsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm QuestionOptionPointsConfiguration
<a name="aws-properties-connect-evaluationform-questionoptionpointsconfiguration"></a>

Information about the points configuration for an answer option.

## Syntax
<a name="aws-properties-connect-evaluationform-questionoptionpointsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-questionoptionpointsconfiguration-syntax.json"></a>

```
{
  "[IsBonus](#cfn-connect-evaluationform-questionoptionpointsconfiguration-isbonus)" : {{Boolean}},
  "[PointValue](#cfn-connect-evaluationform-questionoptionpointsconfiguration-pointvalue)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-questionoptionpointsconfiguration-syntax.yaml"></a>

```
  [IsBonus](#cfn-connect-evaluationform-questionoptionpointsconfiguration-isbonus): {{Boolean}}
  [PointValue](#cfn-connect-evaluationform-questionoptionpointsconfiguration-pointvalue): {{Integer}}
```

## Properties
<a name="aws-properties-connect-evaluationform-questionoptionpointsconfiguration-properties"></a>

`IsBonus`  <a name="cfn-connect-evaluationform-questionoptionpointsconfiguration-isbonus"></a>
The flag to mark the option as a bonus option.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PointValue`  <a name="cfn-connect-evaluationform-questionoptionpointsconfiguration-pointvalue"></a>
The point value assigned to the answer option.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
