---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule Filter
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-filter"></a>

 A single filter condition that specifies behavior, requirement, and matching conditions for WAF log records.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-filter-syntax.json"></a>

```
{
  "[Behavior](#cfn-observabilityadmin-organizationtelemetryrule-filter-behavior)" : {{String}},
  "[Conditions](#cfn-observabilityadmin-organizationtelemetryrule-filter-conditions)" : {{[ Condition, ... ]}},
  "[Requirement](#cfn-observabilityadmin-organizationtelemetryrule-filter-requirement)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-filter-syntax.yaml"></a>

```
  [Behavior](#cfn-observabilityadmin-organizationtelemetryrule-filter-behavior): {{String}}
  [Conditions](#cfn-observabilityadmin-organizationtelemetryrule-filter-conditions): {{
    - Condition}}
  [Requirement](#cfn-observabilityadmin-organizationtelemetryrule-filter-requirement): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-filter-properties"></a>

`Behavior`  <a name="cfn-observabilityadmin-organizationtelemetryrule-filter-behavior"></a>
 The action to take for log records matching this filter (KEEP or DROP).
*Required*: No
*Type*: String
*Allowed values*: `KEEP | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Conditions`  <a name="cfn-observabilityadmin-organizationtelemetryrule-filter-conditions"></a>
 The list of conditions that determine if a log record matches this filter.
*Required*: No
*Type*: Array of [Condition](aws-properties-observabilityadmin-organizationtelemetryrule-condition.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Requirement`  <a name="cfn-observabilityadmin-organizationtelemetryrule-filter-requirement"></a>
 Whether the log record must meet all conditions (MEETS\_ALL) or any condition (MEETS\_ANY) to match this filter.
*Required*: No
*Type*: String
*Allowed values*: `MEETS_ALL | MEETS_ANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
