---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformitemenablementsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormItemEnablementSource

An enablement expression source item.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource-syntax.json"></a>

```json
{
  "[RefId](#cfn-connect-evaluationform-evaluationformitemenablementsource-refid)" : {{String}},
  "[Type](#cfn-connect-evaluationform-evaluationformitemenablementsource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource-syntax.yaml"></a>

```yaml
  [RefId](#cfn-connect-evaluationform-evaluationformitemenablementsource-refid): {{String}}
  [Type](#cfn-connect-evaluationform-evaluationformitemenablementsource-type): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementsource-properties"></a>

`RefId`  <a name="cfn-connect-evaluationform-evaluationformitemenablementsource-refid"></a>
A referenceId of the source item. Use when `Type` is `QUESTION_REF_ID`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,40}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-evaluationform-evaluationformitemenablementsource-type"></a>
A type of source item. Valid values:
+ `QUESTION_REF_ID` - The answer to another question in the evaluation form.
+ `CONTACT` - Data from the evaluated contact.
+ `EVALUATION_METADATA` - Metadata of the evaluation, such as the evaluation type.
+ `AI_METRICS` - Metrics about AI agents, AI sessions, and AI tools on the contact.
*Required*: Yes
*Type*: String
*Allowed values*: `QUESTION_REF_ID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
