---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-personalize-datadeletionjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::DataDeletionJob
<a name="aws-resource-personalize-datadeletionjob"></a>

Describes a job that deletes all references to specific users from an Amazon Personalize dataset group in batches. For information about creating a data deletion job, see [Deleting users](https://docs.aws.amazon.com/personalize/latest/dg/delete-records.html).

## Syntax
<a name="aws-resource-personalize-datadeletionjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-personalize-datadeletionjob-syntax.json"></a>

```
{
  "Type" : "AWS::Personalize::DataDeletionJob",
  "Properties" : {
      "[DatasetGroupArn](#cfn-personalize-datadeletionjob-datasetgrouparn)" : {{String}},
      "[DataSource](#cfn-personalize-datadeletionjob-datasource)" : {{DataSource}},
      "[JobName](#cfn-personalize-datadeletionjob-jobname)" : {{String}},
      "[RoleArn](#cfn-personalize-datadeletionjob-rolearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-personalize-datadeletionjob-syntax.yaml"></a>

```
Type: AWS::Personalize::DataDeletionJob
Properties:
  [DatasetGroupArn](#cfn-personalize-datadeletionjob-datasetgrouparn): {{String}}
  [DataSource](#cfn-personalize-datadeletionjob-datasource): {{
    DataSource}}
  [JobName](#cfn-personalize-datadeletionjob-jobname): {{String}}
  [RoleArn](#cfn-personalize-datadeletionjob-rolearn): {{String}}
```

## Properties
<a name="aws-resource-personalize-datadeletionjob-properties"></a>

`DatasetGroupArn`  <a name="cfn-personalize-datadeletionjob-datasetgrouparn"></a>
The Amazon Resource Name (ARN) of the dataset group the job deletes records from.
*Required*: No
*Type*: String
*Pattern*: `^arn:([a-z\d-]+):personalize:.*:.*:.+$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSource`  <a name="cfn-personalize-datadeletionjob-datasource"></a>
Describes the data source that contains the data to upload to a dataset, or the list of records to delete from Amazon Personalize.
*Required*: No
*Type*: [DataSource](aws-properties-personalize-datadeletionjob-datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobName`  <a name="cfn-personalize-datadeletionjob-jobname"></a>
The name of the data deletion job.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-personalize-datadeletionjob-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3 data source.
*Required*: No
*Type*: String
*Pattern*: `^arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-personalize-datadeletionjob-return-values"></a>

### Ref
<a name="aws-resource-personalize-datadeletionjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-personalize-datadeletionjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-personalize-datadeletionjob-return-values-fn--getatt-fn--getatt"></a>

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The creation date and time (in Unix time) of the data deletion job.

`DataDeletionJobArn`  <a name="DataDeletionJobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the data deletion job.

`LastUpdatedDateTime`  <a name="LastUpdatedDateTime-fn::getatt"></a>
The date and time (in Unix time) the data deletion job was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The status of the data deletion job.
A data deletion job can have one of the following statuses:
+ PENDING > IN\_PROGRESS > COMPLETED -or- FAILED
