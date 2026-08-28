---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule LoggingFilter
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter"></a>

 Configuration that determines which WAF log records to keep or drop based on specified conditions.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter-syntax.json"></a>

```
{
  "[DefaultBehavior](#cfn-observabilityadmin-organizationtelemetryrule-loggingfilter-defaultbehavior)" : {{String}},
  "[Filters](#cfn-observabilityadmin-organizationtelemetryrule-loggingfilter-filters)" : {{[ Filter, ... ]}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter-syntax.yaml"></a>

```
  [DefaultBehavior](#cfn-observabilityadmin-organizationtelemetryrule-loggingfilter-defaultbehavior): {{String}}
  [Filters](#cfn-observabilityadmin-organizationtelemetryrule-loggingfilter-filters): {{
    - Filter}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter-properties"></a>

`DefaultBehavior`  <a name="cfn-observabilityadmin-organizationtelemetryrule-loggingfilter-defaultbehavior"></a>
 The default action (KEEP or DROP) for log records that don't match any filter conditions.
*Required*: No
*Type*: String
*Allowed values*: `KEEP | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filters`  <a name="cfn-observabilityadmin-organizationtelemetryrule-loggingfilter-filters"></a>
 A list of filter conditions that determine log record handling behavior.
*Required*: No
*Type*: Array of [Filter](aws-properties-observabilityadmin-organizationtelemetryrule-filter.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
