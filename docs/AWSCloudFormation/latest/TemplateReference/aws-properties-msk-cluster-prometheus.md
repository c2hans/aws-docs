---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-prometheus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster Prometheus
<a name="aws-properties-msk-cluster-prometheus"></a>

Prometheus settings for open monitoring.

## Syntax
<a name="aws-properties-msk-cluster-prometheus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-prometheus-syntax.json"></a>

```
{
  "[JmxExporter](#cfn-msk-cluster-prometheus-jmxexporter)" : {{JmxExporter}},
  "[NodeExporter](#cfn-msk-cluster-prometheus-nodeexporter)" : {{NodeExporter}}
}
```

### YAML
<a name="aws-properties-msk-cluster-prometheus-syntax.yaml"></a>

```
  [JmxExporter](#cfn-msk-cluster-prometheus-jmxexporter): {{
    JmxExporter}}
  [NodeExporter](#cfn-msk-cluster-prometheus-nodeexporter): {{
    NodeExporter}}
```

## Properties
<a name="aws-properties-msk-cluster-prometheus-properties"></a>

`JmxExporter`  <a name="cfn-msk-cluster-prometheus-jmxexporter"></a>
Indicates whether you want to enable or disable the JMX Exporter.
*Required*: No
*Type*: [JmxExporter](aws-properties-msk-cluster-jmxexporter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeExporter`  <a name="cfn-msk-cluster-prometheus-nodeexporter"></a>
Indicates whether you want to enable or disable the Node Exporter.
*Required*: No
*Type*: [NodeExporter](aws-properties-msk-cluster-nodeexporter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
