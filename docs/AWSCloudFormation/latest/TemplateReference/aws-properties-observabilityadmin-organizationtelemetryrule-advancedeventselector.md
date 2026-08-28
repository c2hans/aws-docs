---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule AdvancedEventSelector
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector"></a>

Advanced event selectors let you create fine-grained selectors for management, data, and network activity events.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector-syntax.json"></a>

```
{
  "[FieldSelectors](#cfn-observabilityadmin-organizationtelemetryrule-advancedeventselector-fieldselectors)" : {{[ AdvancedFieldSelector, ... ]}},
  "[Name](#cfn-observabilityadmin-organizationtelemetryrule-advancedeventselector-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector-syntax.yaml"></a>

```
  [FieldSelectors](#cfn-observabilityadmin-organizationtelemetryrule-advancedeventselector-fieldselectors): {{
    - AdvancedFieldSelector}}
  [Name](#cfn-observabilityadmin-organizationtelemetryrule-advancedeventselector-name): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector-properties"></a>

`FieldSelectors`  <a name="cfn-observabilityadmin-organizationtelemetryrule-advancedeventselector-fieldselectors"></a>
Contains all selector statements in an advanced event selector.
*Required*: Yes
*Type*: Array of [AdvancedFieldSelector](aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-observabilityadmin-organizationtelemetryrule-advancedeventselector-name"></a>
An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
