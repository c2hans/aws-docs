---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-filterrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket FilterRule
<a name="aws-properties-s3-bucket-filterrule"></a>

Specifies the Amazon S3 object key name to filter on. An object key name is the name assigned to an object in your Amazon S3 bucket. You specify whether to filter on the suffix or prefix of the object key name. A prefix is a specific string of characters at the beginning of an object key name, which you can use to organize objects. For example, you can start the key names of related objects with a prefix, such as `2023-` or `engineering/`. Then, you can use `FilterRule` to find objects in a bucket with key names that have the same prefix. A suffix is similar to a prefix, but it is at the end of the object key name instead of at the beginning.

## Syntax
<a name="aws-properties-s3-bucket-filterrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-filterrule-syntax.json"></a>

```
{
  "[Name](#cfn-s3-bucket-filterrule-name)" : {{String}},
  "[Value](#cfn-s3-bucket-filterrule-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-filterrule-syntax.yaml"></a>

```
  [Name](#cfn-s3-bucket-filterrule-name): {{String}}
  [Value](#cfn-s3-bucket-filterrule-value): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-filterrule-properties"></a>

`Name`  <a name="cfn-s3-bucket-filterrule-name"></a>
The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in the *Amazon S3 User Guide*.
*Required*: Yes
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-s3-bucket-filterrule-value"></a>
The value that the filter searches for in object key names.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
