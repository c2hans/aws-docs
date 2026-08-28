---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-servicereportconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service ServiceReportConfiguration
<a name="aws-properties-resiliencehubv2-service-servicereportconfiguration"></a>

Configuration for automatic report generation on a Service.

## Syntax
<a name="aws-properties-resiliencehubv2-service-servicereportconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-servicereportconfiguration-syntax.json"></a>

```
{
  "[ReportOutput](#cfn-resiliencehubv2-service-servicereportconfiguration-reportoutput)" : {{[ ReportOutputConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-servicereportconfiguration-syntax.yaml"></a>

```
  [ReportOutput](#cfn-resiliencehubv2-service-servicereportconfiguration-reportoutput): {{
    - ReportOutputConfiguration}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-servicereportconfiguration-properties"></a>

`ReportOutput`  <a name="cfn-resiliencehubv2-service-servicereportconfiguration-reportoutput"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [ReportOutputConfiguration](aws-properties-resiliencehubv2-service-reportoutputconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
