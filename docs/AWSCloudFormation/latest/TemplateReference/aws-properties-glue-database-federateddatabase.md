---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-database-federateddatabase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Database FederatedDatabase
<a name="aws-properties-glue-database-federateddatabase"></a>

A `FederatedDatabase` structure that references an entity outside the AWS Glue Data Catalog.

## Syntax
<a name="aws-properties-glue-database-federateddatabase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-database-federateddatabase-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-database-federateddatabase-connectionname)" : {{String}},
  "[Identifier](#cfn-glue-database-federateddatabase-identifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-database-federateddatabase-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-database-federateddatabase-connectionname): {{String}}
  [Identifier](#cfn-glue-database-federateddatabase-identifier): {{String}}
```

## Properties
<a name="aws-properties-glue-database-federateddatabase-properties"></a>

`ConnectionName`  <a name="cfn-glue-database-federateddatabase-connectionname"></a>
The name of the connection to the external metastore.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identifier`  <a name="cfn-glue-database-federateddatabase-identifier"></a>
A unique identifier for the federated database.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
