---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule SourceMetricsConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration"></a>

Configuration for selecting source metrics for centralization.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration-syntax.json"></a>

```
{
  "[MetricsSelectionCriteria](#cfn-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration-metricsselectioncriteria)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration-syntax.yaml"></a>

```
  [MetricsSelectionCriteria](#cfn-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration-metricsselectioncriteria): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration-properties"></a>

`MetricsSelectionCriteria`  <a name="cfn-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration-metricsselectioncriteria"></a>
The filter expression that selects which source metrics to centralize. Currently, only `*` (all metrics) is supported. Other values return a validation error.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
