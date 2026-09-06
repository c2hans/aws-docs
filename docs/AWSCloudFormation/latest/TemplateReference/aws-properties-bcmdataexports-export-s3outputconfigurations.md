---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bcmdataexports-export-s3outputconfigurations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Export S3OutputConfigurations
<a name="aws-properties-bcmdataexports-export-s3outputconfigurations"></a>

The compression type, file format, and overwrite preference for the data export.

## Syntax
<a name="aws-properties-bcmdataexports-export-s3outputconfigurations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bcmdataexports-export-s3outputconfigurations-syntax.json"></a>

```
{
  "[Compression](#cfn-bcmdataexports-export-s3outputconfigurations-compression)" : {{String}},
  "[Format](#cfn-bcmdataexports-export-s3outputconfigurations-format)" : {{String}},
  "[OutputType](#cfn-bcmdataexports-export-s3outputconfigurations-outputtype)" : {{String}},
  "[Overwrite](#cfn-bcmdataexports-export-s3outputconfigurations-overwrite)" : {{String}}
}
```

### YAML
<a name="aws-properties-bcmdataexports-export-s3outputconfigurations-syntax.yaml"></a>

```
  [Compression](#cfn-bcmdataexports-export-s3outputconfigurations-compression): {{String}}
  [Format](#cfn-bcmdataexports-export-s3outputconfigurations-format): {{String}}
  [OutputType](#cfn-bcmdataexports-export-s3outputconfigurations-outputtype): {{String}}
  [Overwrite](#cfn-bcmdataexports-export-s3outputconfigurations-overwrite): {{String}}
```

## Properties
<a name="aws-properties-bcmdataexports-export-s3outputconfigurations-properties"></a>

`Compression`  <a name="cfn-bcmdataexports-export-s3outputconfigurations-compression"></a>
The compression type for the data export.
*Required*: Yes
*Type*: String
*Allowed values*: `GZIP | PARQUET | ZIP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-bcmdataexports-export-s3outputconfigurations-format"></a>
The file format for the data export.
*Required*: Yes
*Type*: String
*Allowed values*: `TEXT_OR_CSV | PARQUET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputType`  <a name="cfn-bcmdataexports-export-s3outputconfigurations-outputtype"></a>
The output type for the data export.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOM | ATHENA | REDSHIFT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Overwrite`  <a name="cfn-bcmdataexports-export-s3outputconfigurations-overwrite"></a>
The rule to follow when generating a version of the data export file. You have the choice to overwrite the previous version or to be delivered in addition to the previous versions. Overwriting exports can save on Amazon S3 storage costs. Creating new export versions allows you to track the changes in cost and usage data over time.
*Required*: Yes
*Type*: String
*Allowed values*: `CREATE_NEW_REPORT | OVERWRITE_REPORT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
