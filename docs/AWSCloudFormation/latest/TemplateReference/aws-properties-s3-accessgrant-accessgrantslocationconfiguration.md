---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-accessgrant-accessgrantslocationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::AccessGrant AccessGrantsLocationConfiguration
<a name="aws-properties-s3-accessgrant-accessgrantslocationconfiguration"></a>

The configuration options of the S3 Access Grants location. It contains the `S3SubPrefix` field. The grant scope, the data to which you are granting access, is the result of appending the `Subprefix` field to the scope of the registered location.

## Syntax
<a name="aws-properties-s3-accessgrant-accessgrantslocationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-accessgrant-accessgrantslocationconfiguration-syntax.json"></a>

```
{
  "[S3SubPrefix](#cfn-s3-accessgrant-accessgrantslocationconfiguration-s3subprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-accessgrant-accessgrantslocationconfiguration-syntax.yaml"></a>

```
  [S3SubPrefix](#cfn-s3-accessgrant-accessgrantslocationconfiguration-s3subprefix): {{String}}
```

## Properties
<a name="aws-properties-s3-accessgrant-accessgrantslocationconfiguration-properties"></a>

`S3SubPrefix`  <a name="cfn-s3-accessgrant-accessgrantslocationconfiguration-s3subprefix"></a>
The `S3SubPrefix` is appended to the location scope creating the grant scope. Use this field to narrow the scope of the grant to a subset of the location scope. This field is required if the location scope is the default location `s3://` because you cannot create a grant for all of your S3 data in the Region and must narrow the scope. For example, if the location scope is the default location `s3://`, the `S3SubPrefx` can be a `<bucket-name>/*`, so the full grant scope path would be `s3://<bucket-name>/*`. Or the `S3SubPrefx` can be `<bucket-name>/<prefix-name>*`, so the full grant scope path would be `s3://<bucket-name>/<prefix-name>*`.
If the `S3SubPrefix` includes a prefix, append the wildcard character `*` after the prefix to indicate that you want to include all object key names in the bucket that start with that prefix.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
