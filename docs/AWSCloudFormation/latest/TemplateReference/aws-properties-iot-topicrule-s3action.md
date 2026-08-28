---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-s3action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule S3Action
<a name="aws-properties-iot-topicrule-s3action"></a>

Describes an action to write data to an Amazon S3 bucket.

## Syntax
<a name="aws-properties-iot-topicrule-s3action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-s3action-syntax.json"></a>

```
{
  "[BucketName](#cfn-iot-topicrule-s3action-bucketname)" : {{String}},
  "[CannedAcl](#cfn-iot-topicrule-s3action-cannedacl)" : {{String}},
  "[Key](#cfn-iot-topicrule-s3action-key)" : {{String}},
  "[RoleArn](#cfn-iot-topicrule-s3action-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-s3action-syntax.yaml"></a>

```
  [BucketName](#cfn-iot-topicrule-s3action-bucketname): {{String}}
  [CannedAcl](#cfn-iot-topicrule-s3action-cannedacl): {{String}}
  [Key](#cfn-iot-topicrule-s3action-key): {{String}}
  [RoleArn](#cfn-iot-topicrule-s3action-rolearn): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-s3action-properties"></a>

`BucketName`  <a name="cfn-iot-topicrule-s3action-bucketname"></a>
The Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CannedAcl`  <a name="cfn-iot-topicrule-s3action-cannedacl"></a>
The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see [S3 canned ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl).
*Required*: No
*Type*: String
*Allowed values*: `private | public-read | public-read-write | aws-exec-read | authenticated-read | bucket-owner-read | bucket-owner-full-control | log-delivery-write`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-iot-topicrule-s3action-key"></a>
The object key. For more information, see [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-topicrule-s3action-rolearn"></a>
The ARN of the IAM role that grants access.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
