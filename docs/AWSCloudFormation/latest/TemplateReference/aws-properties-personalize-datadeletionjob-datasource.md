---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-datadeletionjob-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::DataDeletionJob DataSource
<a name="aws-properties-personalize-datadeletionjob-datasource"></a>

Describes the data source that contains the data to upload to a dataset, or the list of records to delete from Amazon Personalize.

## Syntax
<a name="aws-properties-personalize-datadeletionjob-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-datadeletionjob-datasource-syntax.json"></a>

```
{
  "[DataLocation](#cfn-personalize-datadeletionjob-datasource-datalocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-datadeletionjob-datasource-syntax.yaml"></a>

```
  [DataLocation](#cfn-personalize-datadeletionjob-datasource-datalocation): {{String}}
```

## Properties
<a name="aws-properties-personalize-datadeletionjob-datasource-properties"></a>

`DataLocation`  <a name="cfn-personalize-datadeletionjob-datasource-datalocation"></a>
For dataset import jobs, the path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored. For data deletion jobs, the path to the Amazon S3 bucket that stores the list of records to delete.
 For example:
 `s3://bucket-name/folder-name/fileName.csv`
If your CSV files are in a folder in your Amazon S3 bucket and you want your import job or data deletion job to consider multiple files, you can specify the path to the folder. With a data deletion job, Amazon Personalize uses all files in the folder and any sub folder. Use the following syntax with a `/` after the folder name:
 `s3://bucket-name/folder-name/`
*Required*: No
*Type*: String
*Pattern*: `^(s3|http|https)://.+$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
