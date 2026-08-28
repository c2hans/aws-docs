---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-actioncondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule ActionCondition
<a name="aws-properties-observabilityadmin-telemetryrule-actioncondition"></a>

 Condition that matches based on the specific WAF action taken on the request.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-actioncondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-actioncondition-syntax.json"></a>

```
{
  "[Action](#cfn-observabilityadmin-telemetryrule-actioncondition-action)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-actioncondition-syntax.yaml"></a>

```
  [Action](#cfn-observabilityadmin-telemetryrule-actioncondition-action): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-actioncondition-properties"></a>

`Action`  <a name="cfn-observabilityadmin-telemetryrule-actioncondition-action"></a>
 The WAF action to match against (ALLOW, BLOCK, COUNT, CAPTCHA, CHALLENGE, EXCLUDED\_AS\_COUNT).
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | BLOCK | COUNT | CAPTCHA | CHALLENGE | EXCLUDED_AS_COUNT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
