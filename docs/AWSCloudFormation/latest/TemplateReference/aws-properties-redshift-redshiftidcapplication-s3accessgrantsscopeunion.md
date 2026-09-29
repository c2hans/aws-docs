---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-redshiftidcapplication-s3accessgrantsscopeunion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::RedshiftIdcApplication S3AccessGrantsScopeUnion
<a name="aws-properties-redshift-redshiftidcapplication-s3accessgrantsscopeunion"></a>

A list of scopes set up for S3 Access Grants integration.

## Syntax
<a name="aws-properties-redshift-redshiftidcapplication-s3accessgrantsscopeunion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-redshiftidcapplication-s3accessgrantsscopeunion-syntax.json"></a>

```
{
  "[ReadWriteAccess](#cfn-redshift-redshiftidcapplication-s3accessgrantsscopeunion-readwriteaccess)" : {{ReadWriteAccess}}
}
```

### YAML
<a name="aws-properties-redshift-redshiftidcapplication-s3accessgrantsscopeunion-syntax.yaml"></a>

```
  [ReadWriteAccess](#cfn-redshift-redshiftidcapplication-s3accessgrantsscopeunion-readwriteaccess): {{
    ReadWriteAccess}}
```

## Properties
<a name="aws-properties-redshift-redshiftidcapplication-s3accessgrantsscopeunion-properties"></a>

`ReadWriteAccess`  <a name="cfn-redshift-redshiftidcapplication-s3accessgrantsscopeunion-readwriteaccess"></a>
The S3 Access Grants scope.
*Required*: No
*Type*: [ReadWriteAccess](aws-properties-redshift-redshiftidcapplication-readwriteaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
