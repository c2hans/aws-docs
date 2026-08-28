---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-redshiftdatasetdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob RedshiftDatasetDefinition
<a name="aws-properties-sagemaker-processingjob-redshiftdatasetdefinition"></a>

Configuration for Redshift Dataset Definition input.

## Syntax
<a name="aws-properties-sagemaker-processingjob-redshiftdatasetdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-redshiftdatasetdefinition-syntax.json"></a>

```
{
  "[ClusterId](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-clusterid)" : {{String}},
  "[ClusterRoleArn](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-clusterrolearn)" : {{String}},
  "[Database](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-database)" : {{String}},
  "[DbUser](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-dbuser)" : {{String}},
  "[KmsKeyId](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-kmskeyid)" : {{String}},
  "[OutputCompression](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputcompression)" : {{String}},
  "[OutputFormat](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputformat)" : {{String}},
  "[OutputS3Uri](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputs3uri)" : {{String}},
  "[QueryString](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-querystring)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-redshiftdatasetdefinition-syntax.yaml"></a>

```
  [ClusterId](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-clusterid): {{String}}
  [ClusterRoleArn](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-clusterrolearn): {{String}}
  [Database](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-database): {{String}}
  [DbUser](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-dbuser): {{String}}
  [KmsKeyId](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-kmskeyid): {{String}}
  [OutputCompression](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputcompression): {{String}}
  [OutputFormat](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputformat): {{String}}
  [OutputS3Uri](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputs3uri): {{String}}
  [QueryString](#cfn-sagemaker-processingjob-redshiftdatasetdefinition-querystring): {{
    String}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-redshiftdatasetdefinition-properties"></a>

`ClusterId`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-clusterid"></a>
The Redshift cluster Identifier.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterRoleArn`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-clusterrolearn"></a>
The IAM role attached to your Redshift cluster that Amazon SageMaker uses to generate datasets.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Database`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-database"></a>
The name of the Redshift database used in Redshift query execution.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DbUser`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-dbuser"></a>
The database user name used in Redshift query execution.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data from a Redshift execution.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:/_-]*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputCompression`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputcompression"></a>
The compression used for Redshift query results.
*Required*: No
*Type*: String
*Allowed values*: `None | GZIP | SNAPPY | ZSTD | BZIP2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputFormat`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputformat"></a>
The data storage format for Redshift query results.
*Required*: Yes
*Type*: String
*Allowed values*: `PARQUET | CSV`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputS3Uri`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-outputs3uri"></a>
The location in Amazon S3 where the Redshift query results are stored.
*Required*: Yes
*Type*: String
*Pattern*: `(https|s3)://([^/]+)/?(.*)`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryString`  <a name="cfn-sagemaker-processingjob-redshiftdatasetdefinition-querystring"></a>
The SQL query statements to be executed.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]+`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
