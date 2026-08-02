---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule ActionCondition
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition"></a>

 Condition that matches based on the specific WAF action taken on the request.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition-syntax.json"></a>

```
{
  "[Action](#cfn-observabilityadmin-organizationtelemetryrule-actioncondition-action)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition-syntax.yaml"></a>

```
  [Action](#cfn-observabilityadmin-organizationtelemetryrule-actioncondition-action): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition-properties"></a>

`Action`  <a name="cfn-observabilityadmin-organizationtelemetryrule-actioncondition-action"></a>
 The WAF action to match against (ALLOW, BLOCK, COUNT, CAPTCHA, CHALLENGE, EXCLUDED\_AS\_COUNT).
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | BLOCK | COUNT | CAPTCHA | CHALLENGE | EXCLUDED_AS_COUNT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
