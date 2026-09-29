---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-redshiftidcapplication-serviceintegrationsunion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::RedshiftIdcApplication ServiceIntegrationsUnion
<a name="aws-properties-redshift-redshiftidcapplication-serviceintegrationsunion"></a>

A list of service integrations.

## Syntax
<a name="aws-properties-redshift-redshiftidcapplication-serviceintegrationsunion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-redshiftidcapplication-serviceintegrationsunion-syntax.json"></a>

```
{
  "[LakeFormation](#cfn-redshift-redshiftidcapplication-serviceintegrationsunion-lakeformation)" : {{[ LakeFormationScopeUnion, ... ]}},
  "[Redshift](#cfn-redshift-redshiftidcapplication-serviceintegrationsunion-redshift)" : {{[ RedshiftScopeUnion, ... ]}},
  "[S3AccessGrants](#cfn-redshift-redshiftidcapplication-serviceintegrationsunion-s3accessgrants)" : {{[ S3AccessGrantsScopeUnion, ... ]}}
}
```

### YAML
<a name="aws-properties-redshift-redshiftidcapplication-serviceintegrationsunion-syntax.yaml"></a>

```
  [LakeFormation](#cfn-redshift-redshiftidcapplication-serviceintegrationsunion-lakeformation): {{
    - LakeFormationScopeUnion}}
  [Redshift](#cfn-redshift-redshiftidcapplication-serviceintegrationsunion-redshift): {{
    - RedshiftScopeUnion}}
  [S3AccessGrants](#cfn-redshift-redshiftidcapplication-serviceintegrationsunion-s3accessgrants): {{
    - S3AccessGrantsScopeUnion}}
```

## Properties
<a name="aws-properties-redshift-redshiftidcapplication-serviceintegrationsunion-properties"></a>

`LakeFormation`  <a name="cfn-redshift-redshiftidcapplication-serviceintegrationsunion-lakeformation"></a>
A list of scopes set up for Lake Formation integration.
*Required*: No
*Type*: Array of [LakeFormationScopeUnion](aws-properties-redshift-redshiftidcapplication-lakeformationscopeunion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Redshift`  <a name="cfn-redshift-redshiftidcapplication-serviceintegrationsunion-redshift"></a>
A list of scopes set up for Amazon Redshift integration.
*Required*: No
*Type*: Array of [RedshiftScopeUnion](aws-properties-redshift-redshiftidcapplication-redshiftscopeunion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3AccessGrants`  <a name="cfn-redshift-redshiftidcapplication-serviceintegrationsunion-s3accessgrants"></a>
A list of scopes set up for S3 Access Grants integration.
*Required*: No
*Type*: Array of [S3AccessGrantsScopeUnion](aws-properties-redshift-redshiftidcapplication-s3accessgrantsscopeunion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
