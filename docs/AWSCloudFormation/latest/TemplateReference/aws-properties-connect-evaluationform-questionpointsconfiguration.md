---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-questionpointsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm QuestionPointsConfiguration
<a name="aws-properties-connect-evaluationform-questionpointsconfiguration"></a>

Information about the points configuration for a question.

## Syntax
<a name="aws-properties-connect-evaluationform-questionpointsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-questionpointsconfiguration-syntax.json"></a>

```
{
  "[IsBonus](#cfn-connect-evaluationform-questionpointsconfiguration-isbonus)" : {{Boolean}},
  "[MaxPointValue](#cfn-connect-evaluationform-questionpointsconfiguration-maxpointvalue)" : {{Integer}},
  "[MinPointValue](#cfn-connect-evaluationform-questionpointsconfiguration-minpointvalue)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-questionpointsconfiguration-syntax.yaml"></a>

```
  [IsBonus](#cfn-connect-evaluationform-questionpointsconfiguration-isbonus): {{Boolean}}
  [MaxPointValue](#cfn-connect-evaluationform-questionpointsconfiguration-maxpointvalue): {{Integer}}
  [MinPointValue](#cfn-connect-evaluationform-questionpointsconfiguration-minpointvalue): {{Integer}}
```

## Properties
<a name="aws-properties-connect-evaluationform-questionpointsconfiguration-properties"></a>

`IsBonus`  <a name="cfn-connect-evaluationform-questionpointsconfiguration-isbonus"></a>
The flag to mark the question as a bonus question.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxPointValue`  <a name="cfn-connect-evaluationform-questionpointsconfiguration-maxpointvalue"></a>
The maximum point value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinPointValue`  <a name="cfn-connect-evaluationform-questionpointsconfiguration-minpointvalue"></a>
The minimum point value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
