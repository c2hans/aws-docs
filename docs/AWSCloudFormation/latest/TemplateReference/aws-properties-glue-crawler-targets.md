---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-targets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler Targets
<a name="aws-properties-glue-crawler-targets"></a>

Specifies data stores to crawl.

## Syntax
<a name="aws-properties-glue-crawler-targets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-targets-syntax.json"></a>

```
{
  "[CatalogTargets](#cfn-glue-crawler-targets-catalogtargets)" : {{[ CatalogTarget, ... ]}},
  "[DeltaTargets](#cfn-glue-crawler-targets-deltatargets)" : {{[ DeltaTarget, ... ]}},
  "[DynamoDBTargets](#cfn-glue-crawler-targets-dynamodbtargets)" : {{[ DynamoDBTarget, ... ]}},
  "[HudiTargets](#cfn-glue-crawler-targets-huditargets)" : {{[ HudiTarget, ... ]}},
  "[IcebergTargets](#cfn-glue-crawler-targets-icebergtargets)" : {{[ IcebergTarget, ... ]}},
  "[JdbcTargets](#cfn-glue-crawler-targets-jdbctargets)" : {{[ JdbcTarget, ... ]}},
  "[MongoDBTargets](#cfn-glue-crawler-targets-mongodbtargets)" : {{[ MongoDBTarget, ... ]}},
  "[S3Targets](#cfn-glue-crawler-targets-s3targets)" : {{[ S3Target, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-crawler-targets-syntax.yaml"></a>

```
  [CatalogTargets](#cfn-glue-crawler-targets-catalogtargets): {{
    - CatalogTarget}}
  [DeltaTargets](#cfn-glue-crawler-targets-deltatargets): {{
    - DeltaTarget}}
  [DynamoDBTargets](#cfn-glue-crawler-targets-dynamodbtargets): {{
    - DynamoDBTarget}}
  [HudiTargets](#cfn-glue-crawler-targets-huditargets): {{
    - HudiTarget}}
  [IcebergTargets](#cfn-glue-crawler-targets-icebergtargets): {{
    - IcebergTarget}}
  [JdbcTargets](#cfn-glue-crawler-targets-jdbctargets): {{
    - JdbcTarget}}
  [MongoDBTargets](#cfn-glue-crawler-targets-mongodbtargets): {{
    - MongoDBTarget}}
  [S3Targets](#cfn-glue-crawler-targets-s3targets): {{
    - S3Target}}
```

## Properties
<a name="aws-properties-glue-crawler-targets-properties"></a>

`CatalogTargets`  <a name="cfn-glue-crawler-targets-catalogtargets"></a>
Specifies AWS Glue Data Catalog targets.
*Required*: No
*Type*: Array of [CatalogTarget](aws-properties-glue-crawler-catalogtarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeltaTargets`  <a name="cfn-glue-crawler-targets-deltatargets"></a>
Specifies an array of Delta data store targets.
*Required*: No
*Type*: Array of [DeltaTarget](aws-properties-glue-crawler-deltatarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DynamoDBTargets`  <a name="cfn-glue-crawler-targets-dynamodbtargets"></a>
Specifies Amazon DynamoDB targets.
*Required*: No
*Type*: Array of [DynamoDBTarget](aws-properties-glue-crawler-dynamodbtarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HudiTargets`  <a name="cfn-glue-crawler-targets-huditargets"></a>
Property description not available.
*Required*: No
*Type*: Array of [HudiTarget](aws-properties-glue-crawler-huditarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IcebergTargets`  <a name="cfn-glue-crawler-targets-icebergtargets"></a>
Specifies Apache Iceberg data store targets.
*Required*: No
*Type*: Array of [IcebergTarget](aws-properties-glue-crawler-icebergtarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JdbcTargets`  <a name="cfn-glue-crawler-targets-jdbctargets"></a>
Specifies JDBC targets.
*Required*: No
*Type*: Array of [JdbcTarget](aws-properties-glue-crawler-jdbctarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MongoDBTargets`  <a name="cfn-glue-crawler-targets-mongodbtargets"></a>
A list of Mongo DB targets.
*Required*: No
*Type*: Array of [MongoDBTarget](aws-properties-glue-crawler-mongodbtarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Targets`  <a name="cfn-glue-crawler-targets-s3targets"></a>
Specifies Amazon Simple Storage Service (Amazon S3) targets.
*Required*: No
*Type*: Array of [S3Target](aws-properties-glue-crawler-s3target.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
