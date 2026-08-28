---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-federatedcatalog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog FederatedCatalog
<a name="aws-properties-glue-catalog-federatedcatalog"></a>

A catalog that points to an entity outside the AWS Glue Data Catalog.

## Syntax
<a name="aws-properties-glue-catalog-federatedcatalog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-federatedcatalog-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-catalog-federatedcatalog-connectionname)" : {{String}},
  "[Identifier](#cfn-glue-catalog-federatedcatalog-identifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-federatedcatalog-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-catalog-federatedcatalog-connectionname): {{String}}
  [Identifier](#cfn-glue-catalog-federatedcatalog-identifier): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-federatedcatalog-properties"></a>

`ConnectionName`  <a name="cfn-glue-catalog-federatedcatalog-connectionname"></a>
The name of the connection to an external data source, for example a Redshift-federated catalog.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identifier`  <a name="cfn-glue-catalog-federatedcatalog-identifier"></a>
A unique identifier for the federated catalog.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
