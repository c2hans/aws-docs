---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3objectlambda-accesspoint-alias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3ObjectLambda::AccessPoint Alias
<a name="aws-properties-s3objectlambda-accesspoint-alias"></a>

The alias of an Object Lambda Access Point. For more information, see [How to use a bucket-style alias for your S3 bucket Object Lambda Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-use.html#ol-access-points-alias).

## Syntax
<a name="aws-properties-s3objectlambda-accesspoint-alias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3objectlambda-accesspoint-alias-syntax.json"></a>

```
{
  "[Status](#cfn-s3objectlambda-accesspoint-alias-status)" : {{String}},
  "[Value](#cfn-s3objectlambda-accesspoint-alias-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3objectlambda-accesspoint-alias-syntax.yaml"></a>

```
  [Status](#cfn-s3objectlambda-accesspoint-alias-status): {{String}}
  [Value](#cfn-s3objectlambda-accesspoint-alias-value): {{String}}
```

## Properties
<a name="aws-properties-s3objectlambda-accesspoint-alias-properties"></a>

`Status`  <a name="cfn-s3objectlambda-accesspoint-alias-status"></a>
The status of the Object Lambda Access Point alias. If the status is `PROVISIONING`, the Object Lambda Access Point is provisioning the alias and the alias is not ready for use yet. If the status is `READY`, the Object Lambda Access Point alias is successfully provisioned and ready for use.
*Required*: No
*Type*: String
*Pattern*: `^[A-Z]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-s3objectlambda-accesspoint-alias-value"></a>
The alias value of the Object Lambda Access Point.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9\-]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
