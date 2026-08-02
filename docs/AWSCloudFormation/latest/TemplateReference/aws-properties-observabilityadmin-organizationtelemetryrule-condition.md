---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule Condition
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-condition"></a>

 A single condition that can match based on WAF rule action or label name.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-condition-syntax.json"></a>

```
{
  "[ActionCondition](#cfn-observabilityadmin-organizationtelemetryrule-condition-actioncondition)" : {{ActionCondition}},
  "[LabelNameCondition](#cfn-observabilityadmin-organizationtelemetryrule-condition-labelnamecondition)" : {{LabelNameCondition}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-condition-syntax.yaml"></a>

```
  [ActionCondition](#cfn-observabilityadmin-organizationtelemetryrule-condition-actioncondition): {{
    ActionCondition}}
  [LabelNameCondition](#cfn-observabilityadmin-organizationtelemetryrule-condition-labelnamecondition): {{
    LabelNameCondition}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-condition-properties"></a>

`ActionCondition`  <a name="cfn-observabilityadmin-organizationtelemetryrule-condition-actioncondition"></a>
 Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.).
*Required*: No
*Type*: [ActionCondition](aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LabelNameCondition`  <a name="cfn-observabilityadmin-organizationtelemetryrule-condition-labelnamecondition"></a>
 Matches log records based on WAF rule labels applied to the request.
*Required*: No
*Type*: [LabelNameCondition](aws-properties-observabilityadmin-organizationtelemetryrule-labelnamecondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
