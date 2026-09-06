---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-task-taskreportconfigdestinations3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::Task TaskReportConfigDestinationS3
<a name="aws-properties-datasync-task-taskreportconfigdestinations3"></a>

<a name="aws-properties-datasync-task-taskreportconfigdestinations3-description"></a>The `TaskReportConfigDestinationS3` property type specifies Property description not available. for an [AWS::DataSync::Task](aws-resource-datasync-task.md).

## Syntax
<a name="aws-properties-datasync-task-taskreportconfigdestinations3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-task-taskreportconfigdestinations3-syntax.json"></a>

```
{
  "[BucketAccessRoleArn](#cfn-datasync-task-taskreportconfigdestinations3-bucketaccessrolearn)" : {{String}},
  "[S3BucketArn](#cfn-datasync-task-taskreportconfigdestinations3-s3bucketarn)" : {{String}},
  "[Subdirectory](#cfn-datasync-task-taskreportconfigdestinations3-subdirectory)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-task-taskreportconfigdestinations3-syntax.yaml"></a>

```
  [BucketAccessRoleArn](#cfn-datasync-task-taskreportconfigdestinations3-bucketaccessrolearn): {{String}}
  [S3BucketArn](#cfn-datasync-task-taskreportconfigdestinations3-s3bucketarn): {{String}}
  [Subdirectory](#cfn-datasync-task-taskreportconfigdestinations3-subdirectory): {{String}}
```

## Properties
<a name="aws-properties-datasync-task-taskreportconfigdestinations3-properties"></a>

`BucketAccessRoleArn`  <a name="cfn-datasync-task-taskreportconfigdestinations3-bucketaccessrolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketArn`  <a name="cfn-datasync-task-taskreportconfigdestinations3-s3bucketarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):(s3|s3-outposts):[a-z\-0-9]*:[0-9]*:.*$`
*Maximum*: `156`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdirectory`  <a name="cfn-datasync-task-taskreportconfigdestinations3-subdirectory"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
