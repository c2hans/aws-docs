---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-organizationtelemetryrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule
<a name="aws-resource-observabilityadmin-organizationtelemetryrule"></a>

Retrieves the details of a specific organization centralization rule. This operation can only be called by the organization's management account or a delegated administrator account.

## Syntax
<a name="aws-resource-observabilityadmin-organizationtelemetryrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-observabilityadmin-organizationtelemetryrule-syntax.json"></a>

```
{
  "Type" : "AWS::ObservabilityAdmin::OrganizationTelemetryRule",
  "Properties" : {
      "[Rule](#cfn-observabilityadmin-organizationtelemetryrule-rule)" : {{TelemetryRule}},
      "[RuleName](#cfn-observabilityadmin-organizationtelemetryrule-rulename)" : {{String}},
      "[Tags](#cfn-observabilityadmin-organizationtelemetryrule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-observabilityadmin-organizationtelemetryrule-syntax.yaml"></a>

```
Type: AWS::ObservabilityAdmin::OrganizationTelemetryRule
Properties:
  [Rule](#cfn-observabilityadmin-organizationtelemetryrule-rule): {{
    TelemetryRule}}
  [RuleName](#cfn-observabilityadmin-organizationtelemetryrule-rulename): {{String}}
  [Tags](#cfn-observabilityadmin-organizationtelemetryrule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-observabilityadmin-organizationtelemetryrule-properties"></a>

`Rule`  <a name="cfn-observabilityadmin-organizationtelemetryrule-rule"></a>
 The name of the organization telemetry rule.
*Required*: Yes
*Type*: [TelemetryRule](aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-observabilityadmin-organizationtelemetryrule-rulename"></a>
The name of the organization centralization rule.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-observabilityadmin-organizationtelemetryrule-tags"></a>
 Lists all tags attached to the specified resource. Supports telemetry rule resources and telemetry pipeline resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-observabilityadmin-organizationtelemetryrule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-observabilityadmin-organizationtelemetryrule-return-values"></a>

### Ref
<a name="aws-resource-observabilityadmin-organizationtelemetryrule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-observabilityadmin-organizationtelemetryrule-return-values-fn--getatt"></a>

####
<a name="aws-resource-observabilityadmin-organizationtelemetryrule-return-values-fn--getatt-fn--getatt"></a>

`RegionStatuses`  <a name="RegionStatuses-fn::getatt"></a>
Property description not available.

`RuleArn`  <a name="RuleArn-fn::getatt"></a>
Property description not available.
