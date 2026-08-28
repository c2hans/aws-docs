---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-cluster-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::Cluster Endpoint
<a name="aws-properties-redshift-cluster-endpoint"></a>

Describes a connection endpoint.

## Syntax
<a name="aws-properties-redshift-cluster-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-cluster-endpoint-syntax.json"></a>

```
{
  "[Address](#cfn-redshift-cluster-endpoint-address)" : {{String}},
  "[Port](#cfn-redshift-cluster-endpoint-port)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-cluster-endpoint-syntax.yaml"></a>

```
  [Address](#cfn-redshift-cluster-endpoint-address): {{String}}
  [Port](#cfn-redshift-cluster-endpoint-port): {{String}}
```

## Properties
<a name="aws-properties-redshift-cluster-endpoint-properties"></a>

`Address`  <a name="cfn-redshift-cluster-endpoint-address"></a>
The DNS address of the cluster. This property is read only.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-redshift-cluster-endpoint-port"></a>
The port that the database engine is listening on. This property is read only.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
