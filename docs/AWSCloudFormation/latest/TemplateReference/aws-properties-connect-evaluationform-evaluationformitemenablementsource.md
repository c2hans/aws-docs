---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformitemenablementsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormItemEnablementSource
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource"></a>

An enablement expression source item.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource-syntax.json"></a>

```
{
  "[RefId](#cfn-connect-evaluationform-evaluationformitemenablementsource-refid)" : {{String}},
  "[Type](#cfn-connect-evaluationform-evaluationformitemenablementsource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource-syntax.yaml"></a>

```
  [RefId](#cfn-connect-evaluationform-evaluationformitemenablementsource-refid): {{String}}
  [Type](#cfn-connect-evaluationform-evaluationformitemenablementsource-type): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource-properties"></a>

`RefId`  <a name="cfn-connect-evaluationform-evaluationformitemenablementsource-refid"></a>
A referenceId of the source item.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,40}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-evaluationform-evaluationformitemenablementsource-type"></a>
A type of source item.
*Required*: Yes
*Type*: String
*Allowed values*: `QUESTION_REF_ID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
