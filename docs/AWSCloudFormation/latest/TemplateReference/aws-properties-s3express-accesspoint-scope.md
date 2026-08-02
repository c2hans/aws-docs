---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-accesspoint-scope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::AccessPoint Scope
<a name="aws-properties-s3express-accesspoint-scope"></a>

You can use the access point scope to restrict access to specific prefixes, API operations, or a combination of both.

For more information, see [Manage the scope of your access points for directory buckets.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-manage-scope.html)

## Syntax
<a name="aws-properties-s3express-accesspoint-scope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-accesspoint-scope-syntax.json"></a>

```
{
  "[Permissions](#cfn-s3express-accesspoint-scope-permissions)" : {{[ String, ... ]}},
  "[Prefixes](#cfn-s3express-accesspoint-scope-prefixes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-s3express-accesspoint-scope-syntax.yaml"></a>

```
  [Permissions](#cfn-s3express-accesspoint-scope-permissions): {{
    - String}}
  [Prefixes](#cfn-s3express-accesspoint-scope-prefixes): {{
    - String}}
```

## Properties
<a name="aws-properties-s3express-accesspoint-scope-properties"></a>

`Permissions`  <a name="cfn-s3express-accesspoint-scope-permissions"></a>
You can include one or more API operations as permissions.
*Required*: No
*Type*: Array of String
*Allowed values*: `GetObject | GetObjectAttributes | ListMultipartUploadParts | ListBucket | ListBucketMultipartUploads | PutObject | DeleteObject | AbortMultipartUpload`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefixes`  <a name="cfn-s3express-accesspoint-scope-prefixes"></a>
You can specify any amount of prefixes, but the total length of characters of all prefixes must be less than 256 bytes in size.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
