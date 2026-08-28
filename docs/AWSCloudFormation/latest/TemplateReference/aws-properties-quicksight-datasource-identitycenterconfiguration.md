---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-identitycenterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource IdentityCenterConfiguration
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration"></a>

The parameters for an IAM Identity Center configuration.

## Syntax
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration-syntax.json"></a>

```
{
  "[EnableIdentityPropagation](#cfn-quicksight-datasource-identitycenterconfiguration-enableidentitypropagation)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration-syntax.yaml"></a>

```
  [EnableIdentityPropagation](#cfn-quicksight-datasource-identitycenterconfiguration-enableidentitypropagation): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration-properties"></a>

`EnableIdentityPropagation`  <a name="cfn-quicksight-datasource-identitycenterconfiguration-enableidentitypropagation"></a>
A Boolean option that controls whether Trusted Identity Propagation should be used.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
