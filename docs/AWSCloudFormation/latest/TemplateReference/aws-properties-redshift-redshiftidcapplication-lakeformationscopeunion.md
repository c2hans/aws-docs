---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-redshiftidcapplication-lakeformationscopeunion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::RedshiftIdcApplication LakeFormationScopeUnion
<a name="aws-properties-redshift-redshiftidcapplication-lakeformationscopeunion"></a>

A list of scopes set up for Lake Formation integration.

## Syntax
<a name="aws-properties-redshift-redshiftidcapplication-lakeformationscopeunion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-redshiftidcapplication-lakeformationscopeunion-syntax.json"></a>

```
{
  "[LakeFormationQuery](#cfn-redshift-redshiftidcapplication-lakeformationscopeunion-lakeformationquery)" : {{LakeFormationQuery}}
}
```

### YAML
<a name="aws-properties-redshift-redshiftidcapplication-lakeformationscopeunion-syntax.yaml"></a>

```
  [LakeFormationQuery](#cfn-redshift-redshiftidcapplication-lakeformationscopeunion-lakeformationquery): {{
    LakeFormationQuery}}
```

## Properties
<a name="aws-properties-redshift-redshiftidcapplication-lakeformationscopeunion-properties"></a>

`LakeFormationQuery`  <a name="cfn-redshift-redshiftidcapplication-lakeformationscopeunion-lakeformationquery"></a>
The Lake Formation scope.
*Required*: No
*Type*: [LakeFormationQuery](aws-properties-redshift-redshiftidcapplication-lakeformationquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
