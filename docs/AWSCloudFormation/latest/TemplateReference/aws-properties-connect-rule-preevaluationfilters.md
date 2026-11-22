---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-preevaluationfilters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule PreEvaluationFilters

The pre-evaluation filters for a rule, that restrict a rule to be applied to only certain resources based on the resource's attributes, such as tags assigned to a contact. The pre-evaluation filters are applied even before rule conditions are evaluated and are used to enforce tag-based-access-control while applying rules.

## Syntax
<a name="aws-properties-connect-rule-preevaluationfilters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-preevaluationfilters-syntax.json"></a>

```json
{
  "[AndConditions](#cfn-connect-rule-preevaluationfilters-andconditions)" : {{[ PreEvaluationFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-rule-preevaluationfilters-syntax.yaml"></a>

```yaml
  [AndConditions](#cfn-connect-rule-preevaluationfilters-andconditions): {{
    - PreEvaluationFilter}}
```

## Properties
<a name="aws-properties-connect-rule-preevaluationfilters-properties"></a>

`AndConditions`  <a name="cfn-connect-rule-preevaluationfilters-andconditions"></a>
A list of conditions that the rule evaluates together using AND logic. All conditions must be met for the event to be evaluated by the rule.
*Required*: No
*Type*: Array of [PreEvaluationFilter](aws-properties-connect-rule-preevaluationfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
