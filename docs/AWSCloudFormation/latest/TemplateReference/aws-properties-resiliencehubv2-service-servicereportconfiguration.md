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
