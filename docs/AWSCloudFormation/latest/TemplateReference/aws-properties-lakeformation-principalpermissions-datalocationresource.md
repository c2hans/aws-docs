---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-principalpermissions-datalocationresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::PrincipalPermissions DataLocationResource
<a name="aws-properties-lakeformation-principalpermissions-datalocationresource"></a>

A structure for a data location object where permissions are granted or revoked.

## Syntax
<a name="aws-properties-lakeformation-principalpermissions-datalocationresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-principalpermissions-datalocationresource-syntax.json"></a>

```
{
  "[CatalogId](#cfn-lakeformation-principalpermissions-datalocationresource-catalogid)" : {{String}},
  "[ResourceArn](#cfn-lakeformation-principalpermissions-datalocationresource-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-principalpermissions-datalocationresource-syntax.yaml"></a>

```
  [CatalogId](#cfn-lakeformation-principalpermissions-datalocationresource-catalogid): {{String}}
  [ResourceArn](#cfn-lakeformation-principalpermissions-datalocationresource-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-principalpermissions-datalocationresource-properties"></a>

`CatalogId`  <a name="cfn-lakeformation-principalpermissions-datalocationresource-catalogid"></a>
 The identifier for the Data Catalog where the location is registered with AWS Lake Formation.
*Required*: Yes
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceArn`  <a name="cfn-lakeformation-principalpermissions-datalocationresource-resourcearn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
