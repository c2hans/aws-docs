---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformlanguageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormLanguageConfiguration
<a name="aws-properties-connect-evaluationform-evaluationformlanguageconfiguration"></a>

Language configuration for an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformlanguageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformlanguageconfiguration-syntax.json"></a>

```
{
  "[FormLanguage](#cfn-connect-evaluationform-evaluationformlanguageconfiguration-formlanguage)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformlanguageconfiguration-syntax.yaml"></a>

```
  [FormLanguage](#cfn-connect-evaluationform-evaluationformlanguageconfiguration-formlanguage): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformlanguageconfiguration-properties"></a>

`FormLanguage`  <a name="cfn-connect-evaluationform-evaluationformlanguageconfiguration-formlanguage"></a>
The language for the evaluation form.
*Required*: No
*Type*: String
*Allowed values*: `de-DE | en-US | es-ES | fr-FR | it-IT | pt-BR | ja-JP | ko-KR | zh-CN | ms-MY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
