---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule Condition
<a name="aws-properties-observabilityadmin-telemetryrule-condition"></a>

 A single condition that can match based on WAF rule action or label name.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-condition-syntax.json"></a>

```
{
  "[ActionCondition](#cfn-observabilityadmin-telemetryrule-condition-actioncondition)" : {{ActionCondition}},
  "[LabelNameCondition](#cfn-observabilityadmin-telemetryrule-condition-labelnamecondition)" : {{LabelNameCondition}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-condition-syntax.yaml"></a>

```
  [ActionCondition](#cfn-observabilityadmin-telemetryrule-condition-actioncondition): {{
    ActionCondition}}
  [LabelNameCondition](#cfn-observabilityadmin-telemetryrule-condition-labelnamecondition): {{
    LabelNameCondition}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-condition-properties"></a>

`ActionCondition`  <a name="cfn-observabilityadmin-telemetryrule-condition-actioncondition"></a>
 Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.).
*Required*: No
*Type*: [ActionCondition](aws-properties-observabilityadmin-telemetryrule-actioncondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LabelNameCondition`  <a name="cfn-observabilityadmin-telemetryrule-condition-labelnamecondition"></a>
 Matches log records based on WAF rule labels applied to the request.
*Required*: No
*Type*: [LabelNameCondition](aws-properties-observabilityadmin-telemetryrule-labelnamecondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
