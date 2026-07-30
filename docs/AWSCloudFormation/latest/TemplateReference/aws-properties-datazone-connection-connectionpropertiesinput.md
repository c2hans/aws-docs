---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-connectionpropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection ConnectionPropertiesInput
<a name="aws-properties-datazone-connection-connectionpropertiesinput"></a>

The properties of a connection.

## Syntax
<a name="aws-properties-datazone-connection-connectionpropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-connectionpropertiesinput-syntax.json"></a>

```
{
  "[AmazonQProperties](#cfn-datazone-connection-connectionpropertiesinput-amazonqproperties)" : {{AmazonQPropertiesInput}},
  "[AthenaProperties](#cfn-datazone-connection-connectionpropertiesinput-athenaproperties)" : {{AthenaPropertiesInput}},
  "[GlueProperties](#cfn-datazone-connection-connectionpropertiesinput-glueproperties)" : {{GluePropertiesInput}},
  "[HyperPodProperties](#cfn-datazone-connection-connectionpropertiesinput-hyperpodproperties)" : {{HyperPodPropertiesInput}},
  "[IamProperties](#cfn-datazone-connection-connectionpropertiesinput-iamproperties)" : {{IamPropertiesInput}},
  "[LakehouseProperties](#cfn-datazone-connection-connectionpropertiesinput-lakehouseproperties)" : {{LakehousePropertiesInput}},
  "[MlflowProperties](#cfn-datazone-connection-connectionpropertiesinput-mlflowproperties)" : {{MlflowPropertiesInput}},
  "[RedshiftProperties](#cfn-datazone-connection-connectionpropertiesinput-redshiftproperties)" : {{RedshiftPropertiesInput}},
  "[S3Properties](#cfn-datazone-connection-connectionpropertiesinput-s3properties)" : {{S3PropertiesInput}},
  "[SparkEmrProperties](#cfn-datazone-connection-connectionpropertiesinput-sparkemrproperties)" : {{SparkEmrPropertiesInput}},
  "[SparkGlueProperties](#cfn-datazone-connection-connectionpropertiesinput-sparkglueproperties)" : {{SparkGluePropertiesInput}},
  "[WorkflowsMwaaProperties](#cfn-datazone-connection-connectionpropertiesinput-workflowsmwaaproperties)" : {{WorkflowsMwaaPropertiesInput}},
  "[WorkflowsServerlessProperties](#cfn-datazone-connection-connectionpropertiesinput-workflowsserverlessproperties)" : {{Json}}
}
```

### YAML
<a name="aws-properties-datazone-connection-connectionpropertiesinput-syntax.yaml"></a>

```
  [AmazonQProperties](#cfn-datazone-connection-connectionpropertiesinput-amazonqproperties): {{
    AmazonQPropertiesInput}}
  [AthenaProperties](#cfn-datazone-connection-connectionpropertiesinput-athenaproperties): {{
    AthenaPropertiesInput}}
  [GlueProperties](#cfn-datazone-connection-connectionpropertiesinput-glueproperties): {{
    GluePropertiesInput}}
  [HyperPodProperties](#cfn-datazone-connection-connectionpropertiesinput-hyperpodproperties): {{
    HyperPodPropertiesInput}}
  [IamProperties](#cfn-datazone-connection-connectionpropertiesinput-iamproperties): {{
    IamPropertiesInput}}
  [LakehouseProperties](#cfn-datazone-connection-connectionpropertiesinput-lakehouseproperties): {{
    LakehousePropertiesInput}}
  [MlflowProperties](#cfn-datazone-connection-connectionpropertiesinput-mlflowproperties): {{
    MlflowPropertiesInput}}
  [RedshiftProperties](#cfn-datazone-connection-connectionpropertiesinput-redshiftproperties): {{
    RedshiftPropertiesInput}}
  [S3Properties](#cfn-datazone-connection-connectionpropertiesinput-s3properties): {{
    S3PropertiesInput}}
  [SparkEmrProperties](#cfn-datazone-connection-connectionpropertiesinput-sparkemrproperties): {{
    SparkEmrPropertiesInput}}
  [SparkGlueProperties](#cfn-datazone-connection-connectionpropertiesinput-sparkglueproperties): {{
    SparkGluePropertiesInput}}
  [WorkflowsMwaaProperties](#cfn-datazone-connection-connectionpropertiesinput-workflowsmwaaproperties): {{
    WorkflowsMwaaPropertiesInput}}
  [WorkflowsServerlessProperties](#cfn-datazone-connection-connectionpropertiesinput-workflowsserverlessproperties): {{Json}}
```

## Properties
<a name="aws-properties-datazone-connection-connectionpropertiesinput-properties"></a>

`AmazonQProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-amazonqproperties"></a>
The Amazon Q properties of the connection.
*Required*: No
*Type*: [AmazonQPropertiesInput](aws-properties-datazone-connection-amazonqpropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AthenaProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-athenaproperties"></a>
The Amazon Athena properties of a connection.
*Required*: No
*Type*: [AthenaPropertiesInput](aws-properties-datazone-connection-athenapropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlueProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-glueproperties"></a>
The AWS Glue properties of a connection.
*Required*: No
*Type*: [GluePropertiesInput](aws-properties-datazone-connection-gluepropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HyperPodProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-hyperpodproperties"></a>
The hyper pod properties of a connection.
*Required*: No
*Type*: [HyperPodPropertiesInput](aws-properties-datazone-connection-hyperpodpropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-iamproperties"></a>
The IAM properties of a connection.
*Required*: No
*Type*: [IamPropertiesInput](aws-properties-datazone-connection-iampropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LakehouseProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-lakehouseproperties"></a>
Property description not available.
*Required*: No
*Type*: [LakehousePropertiesInput](aws-properties-datazone-connection-lakehousepropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MlflowProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-mlflowproperties"></a>
The MLflow properties of a connection.
*Required*: No
*Type*: [MlflowPropertiesInput](aws-properties-datazone-connection-mlflowpropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-redshiftproperties"></a>
The Amazon Redshift properties of a connection.
*Required*: No
*Type*: [RedshiftPropertiesInput](aws-properties-datazone-connection-redshiftpropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Properties`  <a name="cfn-datazone-connection-connectionpropertiesinput-s3properties"></a>
The Amazon S3 properties of a connection.
*Required*: No
*Type*: [S3PropertiesInput](aws-properties-datazone-connection-s3propertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SparkEmrProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-sparkemrproperties"></a>
The Spark EMR properties of a connection.
*Required*: No
*Type*: [SparkEmrPropertiesInput](aws-properties-datazone-connection-sparkemrpropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SparkGlueProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-sparkglueproperties"></a>
The Spark AWS Glue properties of a connection.
*Required*: No
*Type*: [SparkGluePropertiesInput](aws-properties-datazone-connection-sparkgluepropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowsMwaaProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-workflowsmwaaproperties"></a>
The Amazon MWAA properties of a connection.
*Required*: No
*Type*: [WorkflowsMwaaPropertiesInput](aws-properties-datazone-connection-workflowsmwaapropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowsServerlessProperties`  <a name="cfn-datazone-connection-connectionpropertiesinput-workflowsserverlessproperties"></a>
The MWAA serverless properties of a connection.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
