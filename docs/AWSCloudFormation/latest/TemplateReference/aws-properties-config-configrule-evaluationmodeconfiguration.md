---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configrule-evaluationmodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigRule EvaluationModeConfiguration
<a name="aws-properties-config-configrule-evaluationmodeconfiguration"></a>

The configuration object for AWS Config rule evaluation mode. The supported valid values are Detective or Proactive.

## Syntax
<a name="aws-properties-config-configrule-evaluationmodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configrule-evaluationmodeconfiguration-syntax.json"></a>

```
{
  "[Mode](#cfn-config-configrule-evaluationmodeconfiguration-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-configrule-evaluationmodeconfiguration-syntax.yaml"></a>

```
  [Mode](#cfn-config-configrule-evaluationmodeconfiguration-mode): {{String}}
```

## Properties
<a name="aws-properties-config-configrule-evaluationmodeconfiguration-properties"></a>

`Mode`  <a name="cfn-config-configrule-evaluationmodeconfiguration-mode"></a>
The mode of an evaluation. The valid values are Detective or Proactive.
*Required*: No
*Type*: String
*Allowed values*: `DETECTIVE | PROACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
