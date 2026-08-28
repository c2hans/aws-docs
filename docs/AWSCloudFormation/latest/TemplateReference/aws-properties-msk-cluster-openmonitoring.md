---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-openmonitoring.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster OpenMonitoring
<a name="aws-properties-msk-cluster-openmonitoring"></a>

JMX and Node monitoring for the MSK cluster.

## Syntax
<a name="aws-properties-msk-cluster-openmonitoring-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-openmonitoring-syntax.json"></a>

```
{
  "[Prometheus](#cfn-msk-cluster-openmonitoring-prometheus)" : {{Prometheus}}
}
```

### YAML
<a name="aws-properties-msk-cluster-openmonitoring-syntax.yaml"></a>

```
  [Prometheus](#cfn-msk-cluster-openmonitoring-prometheus): {{
    Prometheus}}
```

## Properties
<a name="aws-properties-msk-cluster-openmonitoring-properties"></a>

`Prometheus`  <a name="cfn-msk-cluster-openmonitoring-prometheus"></a>
Prometheus exporter settings.
*Required*: Yes
*Type*: [Prometheus](aws-properties-msk-cluster-prometheus.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
