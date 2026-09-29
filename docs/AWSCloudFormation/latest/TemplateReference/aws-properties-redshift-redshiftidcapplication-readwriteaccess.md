---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-redshiftidcapplication-readwriteaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::RedshiftIdcApplication ReadWriteAccess
<a name="aws-properties-redshift-redshiftidcapplication-readwriteaccess"></a>

The S3 Access Grants scope.

## Syntax
<a name="aws-properties-redshift-redshiftidcapplication-readwriteaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-redshiftidcapplication-readwriteaccess-syntax.json"></a>

```
{
  "[Authorization](#cfn-redshift-redshiftidcapplication-readwriteaccess-authorization)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-redshiftidcapplication-readwriteaccess-syntax.yaml"></a>

```
  [Authorization](#cfn-redshift-redshiftidcapplication-readwriteaccess-authorization): {{String}}
```

## Properties
<a name="aws-properties-redshift-redshiftidcapplication-readwriteaccess-properties"></a>

`Authorization`  <a name="cfn-redshift-redshiftidcapplication-readwriteaccess-authorization"></a>
Determines whether the read/write scope is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
