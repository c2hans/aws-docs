---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-redshiftclusterstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource RedshiftClusterStorage
<a name="aws-properties-datazone-datasource-redshiftclusterstorage"></a>

The details of the Amazon Redshift cluster storage.

## Syntax
<a name="aws-properties-datazone-datasource-redshiftclusterstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-redshiftclusterstorage-syntax.json"></a>

```
{
  "[ClusterName](#cfn-datazone-datasource-redshiftclusterstorage-clustername)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-redshiftclusterstorage-syntax.yaml"></a>

```
  [ClusterName](#cfn-datazone-datasource-redshiftclusterstorage-clustername): {{String}}
```

## Properties
<a name="aws-properties-datazone-datasource-redshiftclusterstorage-properties"></a>

`ClusterName`  <a name="cfn-datazone-datasource-redshiftclusterstorage-clustername"></a>
The name of an Amazon Redshift cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z].[a-z0-9\-]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
