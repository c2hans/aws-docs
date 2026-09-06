---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformtargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormTargetConfiguration
<a name="aws-properties-connect-evaluationform-evaluationformtargetconfiguration"></a>

Configuration that specifies the target for an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformtargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformtargetconfiguration-syntax.json"></a>

```
{
  "[ContactInteractionType](#cfn-connect-evaluationform-evaluationformtargetconfiguration-contactinteractiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformtargetconfiguration-syntax.yaml"></a>

```
  [ContactInteractionType](#cfn-connect-evaluationform-evaluationformtargetconfiguration-contactinteractiontype): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformtargetconfiguration-properties"></a>

`ContactInteractionType`  <a name="cfn-connect-evaluationform-evaluationformtargetconfiguration-contactinteractiontype"></a>
The contact interaction type for this evaluation form.
*Required*: Yes
*Type*: String
*Allowed values*: `AGENT | AUTOMATED | CUSTOMER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
