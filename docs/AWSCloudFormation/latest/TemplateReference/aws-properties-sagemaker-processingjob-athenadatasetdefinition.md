---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-athenadatasetdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob AthenaDatasetDefinition
<a name="aws-properties-sagemaker-processingjob-athenadatasetdefinition"></a>

Configuration for Athena Dataset Definition input.

## Syntax
<a name="aws-properties-sagemaker-processingjob-athenadatasetdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-athenadatasetdefinition-syntax.json"></a>

```
{
  "[Catalog](#cfn-sagemaker-processingjob-athenadatasetdefinition-catalog)" : {{String}},
  "[Database](#cfn-sagemaker-processingjob-athenadatasetdefinition-database)" : {{String}},
  "[KmsKeyId](#cfn-sagemaker-processingjob-athenadatasetdefinition-kmskeyid)" : {{String}},
  "[OutputCompression](#cfn-sagemaker-processingjob-athenadatasetdefinition-outputcompression)" : {{String}},
  "[OutputFormat](#cfn-sagemaker-processingjob-athenadatasetdefinition-outputformat)" : {{String}},
  "[OutputS3Uri](#cfn-sagemaker-processingjob-athenadatasetdefinition-outputs3uri)" : {{String}},
  "[QueryString](#cfn-sagemaker-processingjob-athenadatasetdefinition-querystring)" : {{String}},
  "[WorkGroup](#cfn-sagemaker-processingjob-athenadatasetdefinition-workgroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-athenadatasetdefinition-syntax.yaml"></a>

```
  [Catalog](#cfn-sagemaker-processingjob-athenadatasetdefinition-catalog): {{String}}
  [Database](#cfn-sagemaker-processingjob-athenadatasetdefinition-database): {{String}}
  [KmsKeyId](#cfn-sagemaker-processingjob-athenadatasetdefinition-kmskeyid): {{String}}
  [OutputCompression](#cfn-sagemaker-processingjob-athenadatasetdefinition-outputcompression): {{String}}
  [OutputFormat](#cfn-sagemaker-processingjob-athenadatasetdefinition-outputformat): {{String}}
  [OutputS3Uri](#cfn-sagemaker-processingjob-athenadatasetdefinition-outputs3uri): {{String}}
  [QueryString](#cfn-sagemaker-processingjob-athenadatasetdefinition-querystring): {{
    String}}
  [WorkGroup](#cfn-sagemaker-processingjob-athenadatasetdefinition-workgroup): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-athenadatasetdefinition-properties"></a>

`Catalog`  <a name="cfn-sagemaker-processingjob-athenadatasetdefinition-catalog"></a>
The name of the data catalog used in Athena query execution.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Database`  <a name="cfn-sagemaker-processingjob-athenadatasetdefinition-database"></a>
The name of the database used in the Athena query execution.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-sagemaker-processingjob-athenadatasetdefinition-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data generated from an Athena query execution.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:/_-]*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputCompression`  <a name="cfn-sagemaker-processingjob-athenadatasetdefinition-outputcompression"></a>
The compression used for Athena query results.
*Required*: No
*Type*: String
*Allowed values*: `GZIP | SNAPPY | ZLIB`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputFormat`  <a name="cfn-sagemaker-processingjob-athenadatasetdefinition-outputformat"></a>
The data storage format for Athena query results.
*Required*: Yes
*Type*: String
*Allowed values*: `PARQUET | AVRO | ORC | JSON | TEXTFILE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputS3Uri`  <a name="cfn-sagemaker-processingjob-athenadatasetdefinition-outputs3uri"></a>
The location in Amazon S3 where Athena query results are stored.
*Required*: Yes
*Type*: String
*Pattern*: `(https|s3)://([^/]+)/?(.*)`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryString`  <a name="cfn-sagemaker-processingjob-athenadatasetdefinition-querystring"></a>
The SQL query statements, to be executed.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]+`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkGroup`  <a name="cfn-sagemaker-processingjob-athenadatasetdefinition-workgroup"></a>
The name of the workgroup in which the Athena query is being started.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9._-]+`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
