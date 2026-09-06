---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::PrincipalPermissions DataLakePrincipal
<a name="aws-properties-lakeformation-principalpermissions-datalakeprincipal"></a>

The AWS Lake Formation principal.

## Syntax
<a name="aws-properties-lakeformation-principalpermissions-datalakeprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-principalpermissions-datalakeprincipal-syntax.json"></a>

```
{
  "[DataLakePrincipalIdentifier](#cfn-lakeformation-principalpermissions-datalakeprincipal-datalakeprincipalidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-principalpermissions-datalakeprincipal-syntax.yaml"></a>

```
  [DataLakePrincipalIdentifier](#cfn-lakeformation-principalpermissions-datalakeprincipal-datalakeprincipalidentifier): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-principalpermissions-datalakeprincipal-properties"></a>

`DataLakePrincipalIdentifier`  <a name="cfn-lakeformation-principalpermissions-datalakeprincipal-datalakeprincipalidentifier"></a>
An identifier for the AWS Lake Formation principal.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
