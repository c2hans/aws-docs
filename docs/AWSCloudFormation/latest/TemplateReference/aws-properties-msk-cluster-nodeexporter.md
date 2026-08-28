---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-nodeexporter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster NodeExporter
<a name="aws-properties-msk-cluster-nodeexporter"></a>

Indicates whether you want to enable or disable the Node Exporter.

## Syntax
<a name="aws-properties-msk-cluster-nodeexporter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-nodeexporter-syntax.json"></a>

```
{
  "[EnabledInBroker](#cfn-msk-cluster-nodeexporter-enabledinbroker)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-cluster-nodeexporter-syntax.yaml"></a>

```
  [EnabledInBroker](#cfn-msk-cluster-nodeexporter-enabledinbroker): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-cluster-nodeexporter-properties"></a>

`EnabledInBroker`  <a name="cfn-msk-cluster-nodeexporter-enabledinbroker"></a>
Indicates whether you want to enable or disable the Node Exporter.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
