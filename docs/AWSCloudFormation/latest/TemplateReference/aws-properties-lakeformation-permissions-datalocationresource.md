---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-permissions-datalocationresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::Permissions DataLocationResource
<a name="aws-properties-lakeformation-permissions-datalocationresource"></a>

A structure for a data location object where permissions are granted or revoked.

## Syntax
<a name="aws-properties-lakeformation-permissions-datalocationresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-permissions-datalocationresource-syntax.json"></a>

```
{
  "[CatalogId](#cfn-lakeformation-permissions-datalocationresource-catalogid)" : {{String}},
  "[S3Resource](#cfn-lakeformation-permissions-datalocationresource-s3resource)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-permissions-datalocationresource-syntax.yaml"></a>

```
  [CatalogId](#cfn-lakeformation-permissions-datalocationresource-catalogid): {{String}}
  [S3Resource](#cfn-lakeformation-permissions-datalocationresource-s3resource): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-permissions-datalocationresource-properties"></a>

`CatalogId`  <a name="cfn-lakeformation-permissions-datalocationresource-catalogid"></a>
The identifier for the Data Catalog. By default, it is the account ID of the caller.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Resource`  <a name="cfn-lakeformation-permissions-datalocationresource-s3resource"></a>
The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
