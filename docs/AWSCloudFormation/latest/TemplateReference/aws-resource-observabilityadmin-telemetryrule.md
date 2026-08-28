---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-telemetryrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule
<a name="aws-resource-observabilityadmin-telemetryrule"></a>

 Creates a telemetry rule that defines how telemetry should be configured for AWS resources in your account. The rule specifies which resources should have telemetry enabled and how that telemetry data should be collected based on resource type, telemetry type, and selection criteria.

## Syntax
<a name="aws-resource-observabilityadmin-telemetryrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-observabilityadmin-telemetryrule-syntax.json"></a>

```
{
  "Type" : "AWS::ObservabilityAdmin::TelemetryRule",
  "Properties" : {
      "[Rule](#cfn-observabilityadmin-telemetryrule-rule)" : {{TelemetryRule}},
      "[RuleName](#cfn-observabilityadmin-telemetryrule-rulename)" : {{String}},
      "[Tags](#cfn-observabilityadmin-telemetryrule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-observabilityadmin-telemetryrule-syntax.yaml"></a>

```
Type: AWS::ObservabilityAdmin::TelemetryRule
Properties:
  [Rule](#cfn-observabilityadmin-telemetryrule-rule): {{
    TelemetryRule}}
  [RuleName](#cfn-observabilityadmin-telemetryrule-rulename): {{String}}
  [Tags](#cfn-observabilityadmin-telemetryrule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-observabilityadmin-telemetryrule-properties"></a>

`Rule`  <a name="cfn-observabilityadmin-telemetryrule-rule"></a>
 Retrieves the details of a specific telemetry rule in your account.
*Required*: Yes
*Type*: [TelemetryRule](aws-properties-observabilityadmin-telemetryrule-telemetryrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-observabilityadmin-telemetryrule-rulename"></a>
 The name of the telemetry rule.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-observabilityadmin-telemetryrule-tags"></a>
 Lists all tags attached to the specified resource. Supports telemetry rule resources and telemetry pipeline resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-observabilityadmin-telemetryrule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-observabilityadmin-telemetryrule-return-values"></a>

### Ref
<a name="aws-resource-observabilityadmin-telemetryrule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-observabilityadmin-telemetryrule-return-values-fn--getatt"></a>

####
<a name="aws-resource-observabilityadmin-telemetryrule-return-values-fn--getatt-fn--getatt"></a>

`RegionStatuses`  <a name="RegionStatuses-fn::getatt"></a>
Property description not available.

`RuleArn`  <a name="RuleArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the telemetry rule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
