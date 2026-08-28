---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule CloudtrailParameters
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters"></a>

 Parameters specific to AWS CloudTrail telemetry configuration.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-syntax.json"></a>

```
{
  "[AdvancedEventSelectors](#cfn-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-advancedeventselectors)" : {{[ AdvancedEventSelector, ... ]}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-syntax.yaml"></a>

```
  [AdvancedEventSelectors](#cfn-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-advancedeventselectors): {{
    - AdvancedEventSelector}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-properties"></a>

`AdvancedEventSelectors`  <a name="cfn-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-advancedeventselectors"></a>
 The advanced event selectors to use for filtering AWS CloudTrail events.
*Required*: Yes
*Type*: Array of [AdvancedEventSelector](aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
