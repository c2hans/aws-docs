---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-haclusterprometheusexporter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application HAClusterPrometheusExporter
<a name="aws-properties-applicationinsights-application-haclusterprometheusexporter"></a>

The `AWS::ApplicationInsights::Application HAClusterPrometheusExporter` property type defines the HA cluster Prometheus Exporter settings. For more information, see the [component configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config-sections.html#component-configuration-prometheus) in the CloudWatch Application Insights documentation.

## Syntax
<a name="aws-properties-applicationinsights-application-haclusterprometheusexporter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-haclusterprometheusexporter-syntax.json"></a>

```
{
  "[PrometheusPort](#cfn-applicationinsights-application-haclusterprometheusexporter-prometheusport)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-haclusterprometheusexporter-syntax.yaml"></a>

```
  [PrometheusPort](#cfn-applicationinsights-application-haclusterprometheusexporter-prometheusport): {{String}}
```

## Properties
<a name="aws-properties-applicationinsights-application-haclusterprometheusexporter-properties"></a>

`PrometheusPort`  <a name="cfn-applicationinsights-application-haclusterprometheusexporter-prometheusport"></a>
The target port to which Prometheus sends metrics. If not specified, the default port 9668 is used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
