---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-permissions-datalakeprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::Permissions DataLakePrincipal
<a name="aws-properties-lakeformation-permissions-datalakeprincipal"></a>

The Lake Formation principal.

## Syntax
<a name="aws-properties-lakeformation-permissions-datalakeprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-permissions-datalakeprincipal-syntax.json"></a>

```
{
  "[DataLakePrincipalIdentifier](#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-permissions-datalakeprincipal-syntax.yaml"></a>

```
  [DataLakePrincipalIdentifier](#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-permissions-datalakeprincipal-properties"></a>

`DataLakePrincipalIdentifier`  <a name="cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier"></a>
An identifier for the Lake Formation principal.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
