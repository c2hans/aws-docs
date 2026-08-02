---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::DataLakeSettings DataLakePrincipal
<a name="aws-properties-lakeformation-datalakesettings-datalakeprincipal"></a>

The Lake Formation principal.

## Syntax
<a name="aws-properties-lakeformation-datalakesettings-datalakeprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-datalakesettings-datalakeprincipal-syntax.json"></a>

```
{
  "[DataLakePrincipalIdentifier](#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-datalakesettings-datalakeprincipal-syntax.yaml"></a>

```
  [DataLakePrincipalIdentifier](#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-datalakesettings-datalakeprincipal-properties"></a>

`DataLakePrincipalIdentifier`  <a name="cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier"></a>
An identifier for the Lake Formation principal.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
