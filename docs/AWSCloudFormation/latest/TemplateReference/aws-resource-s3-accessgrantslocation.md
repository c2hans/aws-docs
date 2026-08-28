---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-accessgrantslocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::AccessGrantsLocation
<a name="aws-resource-s3-accessgrantslocation"></a>

The `AWS::S3::AccessGrantsLocation` resource creates the S3 data location that you would like to register in your S3 Access Grants instance. Your S3 data must be in the same Region as your S3 Access Grants instance. The location can be one of the following:
+ The default S3 location `s3://`
+ A bucket - `S3://<bucket-name>`
+ A bucket and prefix - `S3://<bucket-name>/<prefix>`

When you register a location, you must include the IAM role that has permission to manage the S3 location that you are registering. Give S3 Access Grants permission to assume this role [using a policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location.html). S3 Access Grants assumes this role to manage access to the location and to vend temporary credentials to grantees or client applications.

Permissions
You must have the `s3:CreateAccessGrantsLocation` permission to use this resource.

Additional Permissions
You must also have the following permission for the specified IAM role: `iam:PassRole`

## Syntax
<a name="aws-resource-s3-accessgrantslocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3-accessgrantslocation-syntax.json"></a>

```
{
  "Type" : "AWS::S3::AccessGrantsLocation",
  "Properties" : {
      "[IamRoleArn](#cfn-s3-accessgrantslocation-iamrolearn)" : {{String}},
      "[LocationScope](#cfn-s3-accessgrantslocation-locationscope)" : {{String}},
      "[Tags](#cfn-s3-accessgrantslocation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-s3-accessgrantslocation-syntax.yaml"></a>

```
Type: AWS::S3::AccessGrantsLocation
Properties:
  [IamRoleArn](#cfn-s3-accessgrantslocation-iamrolearn): {{String}}
  [LocationScope](#cfn-s3-accessgrantslocation-locationscope): {{String}}
  [Tags](#cfn-s3-accessgrantslocation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-s3-accessgrantslocation-properties"></a>

`IamRoleArn`  <a name="cfn-s3-accessgrantslocation-iamrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants assumes this role to manage access to the registered location.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationScope`  <a name="cfn-s3-accessgrantslocation-locationscope"></a>
The S3 URI path to the location that you are registering. The location scope can be the default S3 location `s3://`, the S3 path to a bucket, or the S3 path to a bucket and prefix. A prefix in S3 is a string of characters at the beginning of an object key name used to organize the objects that you store in your S3 buckets. For example, object key names that start with the `engineering/` prefix or object key names that start with the `marketing/campaigns/` prefix.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-s3-accessgrantslocation-tags"></a>
The AWS resource tags that you are adding to the S3 Access Grants location. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3-accessgrantslocation-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3-accessgrantslocation-return-values"></a>

### Ref
<a name="aws-resource-s3-accessgrantslocation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns some information about the S3 data location.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3-accessgrantslocation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3-accessgrantslocation-return-values-fn--getatt-fn--getatt"></a>

`AccessGrantsLocationArn`  <a name="AccessGrantsLocationArn-fn::getatt"></a>
The ARN of the location you are registering.

`AccessGrantsLocationId`  <a name="AccessGrantsLocationId-fn::getatt"></a>
The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
