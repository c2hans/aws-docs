---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbcluster-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBCluster Endpoint
<a name="aws-properties-rds-dbcluster-endpoint"></a>

The `Endpoint` return value specifies the connection endpoint for the primary instance of the DB cluster.

## Syntax
<a name="aws-properties-rds-dbcluster-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbcluster-endpoint-syntax.json"></a>

```
{
  "[Address](#cfn-rds-dbcluster-endpoint-address)" : {{String}},
  "[Port](#cfn-rds-dbcluster-endpoint-port)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbcluster-endpoint-syntax.yaml"></a>

```
  [Address](#cfn-rds-dbcluster-endpoint-address): {{String}}
  [Port](#cfn-rds-dbcluster-endpoint-port): {{String}}
```

## Properties
<a name="aws-properties-rds-dbcluster-endpoint-properties"></a>

`Address`  <a name="cfn-rds-dbcluster-endpoint-address"></a>
Specifies the connection endpoint for the primary instance of the DB cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-rds-dbcluster-endpoint-port"></a>
Specifies the port that the database engine is listening on.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
