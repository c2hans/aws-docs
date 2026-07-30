---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformitemenablementsourcevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormItemEnablementSourceValue
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsourcevalue"></a>

An enablement expression source value.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsourcevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsourcevalue-syntax.json"></a>

```
{
  "[RefId](#cfn-connect-evaluationform-evaluationformitemenablementsourcevalue-refid)" : {{String}},
  "[Type](#cfn-connect-evaluationform-evaluationformitemenablementsourcevalue-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsourcevalue-syntax.yaml"></a>

```
  [RefId](#cfn-connect-evaluationform-evaluationformitemenablementsourcevalue-refid): {{String}}
  [Type](#cfn-connect-evaluationform-evaluationformitemenablementsourcevalue-type): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsourcevalue-properties"></a>

`RefId`  <a name="cfn-connect-evaluationform-evaluationformitemenablementsourcevalue-refid"></a>
A referenceId of the source value.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,40}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-evaluationform-evaluationformitemenablementsourcevalue-type"></a>
A type of source item value.
*Required*: No
*Type*: String
*Allowed values*: `OPTION_REF_ID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
