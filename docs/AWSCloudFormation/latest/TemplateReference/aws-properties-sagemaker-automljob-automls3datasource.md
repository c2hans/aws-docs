---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automls3datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLS3DataSource
<a name="aws-properties-sagemaker-automljob-automls3datasource"></a>

Describes the Amazon S3 data source.

## Syntax
<a name="aws-properties-sagemaker-automljob-automls3datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automls3datasource-syntax.json"></a>

```
{
  "[S3DataType](#cfn-sagemaker-automljob-automls3datasource-s3datatype)" : {{String}},
  "[S3Uri](#cfn-sagemaker-automljob-automls3datasource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automls3datasource-syntax.yaml"></a>

```
  [S3DataType](#cfn-sagemaker-automljob-automls3datasource-s3datatype): {{String}}
  [S3Uri](#cfn-sagemaker-automljob-automls3datasource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automls3datasource-properties"></a>

`S3DataType`  <a name="cfn-sagemaker-automljob-automls3datasource-s3datatype"></a>
The data type.
+ If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. SageMaker AI uses all objects that match the specified key name prefix for model training.

  The `S3Prefix` should have the following format:

   `s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER-OR-FILE`
+ If you choose `ManifestFile`, `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker AI to use for model training.

  A `ManifestFile` should have the format shown below:

   `[ {"prefix": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/DOC-EXAMPLE-PREFIX/"}, `

   `"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-1",`

   `"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-2",`

   `... "DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-N" ]`
+ If you choose `AugmentedManifestFile`, `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` is available for V2 API jobs only (for example, for jobs created by calling `CreateAutoMLJobV2`).

  Here is a minimal, single-record example of an `AugmentedManifestFile`:

   `{"source-ref": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/cats/cat.jpg",`

  `"label-metadata": {"class-name": "cat"` }

  For more information on `AugmentedManifestFile`, see [Provide Dataset Metadata to Training Jobs with an Augmented Manifest File](https://docs.aws.amazon.com/sagemaker/latest/dg/augmented-manifest.html).
*Required*: Yes
*Type*: String
*Allowed values*: `ManifestFile | S3Prefix | AugmentedManifestFile`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-sagemaker-automljob-automls3datasource-s3uri"></a>
The URL to the Amazon S3 data source. The Uri refers to the Amazon S3 prefix or ManifestFile depending on the data type.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
