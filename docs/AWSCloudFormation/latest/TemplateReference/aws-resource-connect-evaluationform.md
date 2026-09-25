---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-evaluationform.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm
<a name="aws-resource-connect-evaluationform"></a>

Creates an evaluation form for the specified Connect Customer instance.

## Syntax
<a name="aws-resource-connect-evaluationform-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-evaluationform-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::EvaluationForm",
  "Properties" : {
      "[AIVersion](#cfn-connect-evaluationform-aiversion)" : {{String}},
      "[AutoEvaluationConfiguration](#cfn-connect-evaluationform-autoevaluationconfiguration)" : {{AutoEvaluationConfiguration}},
      "[Description](#cfn-connect-evaluationform-description)" : {{String}},
      "[InstanceArn](#cfn-connect-evaluationform-instancearn)" : {{String}},
      "[Items](#cfn-connect-evaluationform-items)" : {{[ EvaluationFormBaseItem, ... ]}},
      "[LanguageConfiguration](#cfn-connect-evaluationform-languageconfiguration)" : {{EvaluationFormLanguageConfiguration}},
      "[ReviewConfiguration](#cfn-connect-evaluationform-reviewconfiguration)" : {{EvaluationReviewConfiguration}},
      "[ScoringStrategy](#cfn-connect-evaluationform-scoringstrategy)" : {{ScoringStrategy}},
      "[Status](#cfn-connect-evaluationform-status)" : {{String}},
      "[Tags](#cfn-connect-evaluationform-tags)" : {{[ Tag, ... ]}},
      "[TargetConfiguration](#cfn-connect-evaluationform-targetconfiguration)" : {{EvaluationFormTargetConfiguration}},
      "[Title](#cfn-connect-evaluationform-title)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-evaluationform-syntax.yaml"></a>

```
Type: AWS::Connect::EvaluationForm
Properties:
  [AIVersion](#cfn-connect-evaluationform-aiversion): {{String}}
  [AutoEvaluationConfiguration](#cfn-connect-evaluationform-autoevaluationconfiguration): {{
    AutoEvaluationConfiguration}}
  [Description](#cfn-connect-evaluationform-description): {{String}}
  [InstanceArn](#cfn-connect-evaluationform-instancearn): {{String}}
  [Items](#cfn-connect-evaluationform-items): {{
    - EvaluationFormBaseItem}}
  [LanguageConfiguration](#cfn-connect-evaluationform-languageconfiguration): {{
    EvaluationFormLanguageConfiguration}}
  [ReviewConfiguration](#cfn-connect-evaluationform-reviewconfiguration): {{
    EvaluationReviewConfiguration}}
  [ScoringStrategy](#cfn-connect-evaluationform-scoringstrategy): {{
    ScoringStrategy}}
  [Status](#cfn-connect-evaluationform-status): {{String}}
  [Tags](#cfn-connect-evaluationform-tags): {{
    - Tag}}
  [TargetConfiguration](#cfn-connect-evaluationform-targetconfiguration): {{
    EvaluationFormTargetConfiguration}}
  [Title](#cfn-connect-evaluationform-title): {{String}}
```

## Properties
<a name="aws-resource-connect-evaluationform-properties"></a>

`AIVersion`  <a name="cfn-connect-evaluationform-aiversion"></a>
The AI version to use for the evaluation form. This specifies which AI model version is used for automated evaluations.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoEvaluationConfiguration`  <a name="cfn-connect-evaluationform-autoevaluationconfiguration"></a>
The automatic evaluation configuration of an evaluation form.
*Required*: No
*Type*: [AutoEvaluationConfiguration](aws-properties-connect-evaluationform-autoevaluationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-evaluationform-description"></a>
The description of the evaluation form.
*Length Constraints*: Minimum length of 0. Maximum length of 1024.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-evaluationform-instancearn"></a>
The identifier of the Amazon Connect instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Items`  <a name="cfn-connect-evaluationform-items"></a>
Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.
*Minimum size*: 1
*Maximum size*: 100
*Required*: Yes
*Type*: Array of [EvaluationFormBaseItem](aws-properties-connect-evaluationform-evaluationformbaseitem.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LanguageConfiguration`  <a name="cfn-connect-evaluationform-languageconfiguration"></a>
Configuration for language settings of this evaluation form.
*Required*: No
*Type*: [EvaluationFormLanguageConfiguration](aws-properties-connect-evaluationform-evaluationformlanguageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReviewConfiguration`  <a name="cfn-connect-evaluationform-reviewconfiguration"></a>
Configuration for evaluation review settings of this evaluation form.
*Required*: No
*Type*: [EvaluationReviewConfiguration](aws-properties-connect-evaluationform-evaluationreviewconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScoringStrategy`  <a name="cfn-connect-evaluationform-scoringstrategy"></a>
A scoring strategy of the evaluation form.
*Required*: No
*Type*: [ScoringStrategy](aws-properties-connect-evaluationform-scoringstrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-connect-evaluationform-status"></a>
The status of the evaluation form.
*Allowed values*: `DRAFT` \| `ACTIVE`
*Required*: Yes
*Type*: String
*Allowed values*: `DRAFT | ACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-evaluationform-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-evaluationform-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetConfiguration`  <a name="cfn-connect-evaluationform-targetconfiguration"></a>
Configuration that specifies the target for this evaluation form.
*Required*: No
*Type*: [EvaluationFormTargetConfiguration](aws-properties-connect-evaluationform-evaluationformtargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-connect-evaluationform-title"></a>
A title of the evaluation form.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-evaluationform-return-values"></a>

### Ref
<a name="aws-resource-connect-evaluationform-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the evaluation form name. For example:

 `{ "Ref": "myEvaluationFormName" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-evaluationform-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-evaluationform-return-values-fn--getatt-fn--getatt"></a>

`EvaluationFormArn`  <a name="EvaluationFormArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the evaluation form.
