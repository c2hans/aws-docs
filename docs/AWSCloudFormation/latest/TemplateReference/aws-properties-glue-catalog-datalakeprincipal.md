---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-datalakeprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog DataLakePrincipal
<a name="aws-properties-glue-catalog-datalakeprincipal"></a>

The AWS Lake Formation principal.

## Syntax
<a name="aws-properties-glue-catalog-datalakeprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-datalakeprincipal-syntax.json"></a>

```
{
  "[DataLakePrincipalIdentifier](#cfn-glue-catalog-datalakeprincipal-datalakeprincipalidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-datalakeprincipal-syntax.yaml"></a>

```
  [DataLakePrincipalIdentifier](#cfn-glue-catalog-datalakeprincipal-datalakeprincipalidentifier): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-datalakeprincipal-properties"></a>

`DataLakePrincipalIdentifier`  <a name="cfn-glue-catalog-datalakeprincipal-datalakeprincipalidentifier"></a>
An identifier for the AWS Lake Formation principal.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
