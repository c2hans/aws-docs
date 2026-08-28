---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-gluedatacatalog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow GlueDataCatalog
<a name="aws-properties-appflow-flow-gluedatacatalog"></a>

<a name="aws-properties-appflow-flow-gluedatacatalog-description"></a>The `GlueDataCatalog` property type specifies Property description not available. for an [AWS::AppFlow::Flow](aws-resource-appflow-flow.md).

## Syntax
<a name="aws-properties-appflow-flow-gluedatacatalog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-gluedatacatalog-syntax.json"></a>

```
{
  "[DatabaseName](#cfn-appflow-flow-gluedatacatalog-databasename)" : {{String}},
  "[RoleArn](#cfn-appflow-flow-gluedatacatalog-rolearn)" : {{String}},
  "[TablePrefix](#cfn-appflow-flow-gluedatacatalog-tableprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-gluedatacatalog-syntax.yaml"></a>

```
  [DatabaseName](#cfn-appflow-flow-gluedatacatalog-databasename): {{String}}
  [RoleArn](#cfn-appflow-flow-gluedatacatalog-rolearn): {{String}}
  [TablePrefix](#cfn-appflow-flow-gluedatacatalog-tableprefix): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-gluedatacatalog-properties"></a>

`DatabaseName`  <a name="cfn-appflow-flow-gluedatacatalog-databasename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-appflow-flow-gluedatacatalog-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:iam:.*:[0-9]+:.*`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TablePrefix`  <a name="cfn-appflow-flow-gluedatacatalog-tableprefix"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
