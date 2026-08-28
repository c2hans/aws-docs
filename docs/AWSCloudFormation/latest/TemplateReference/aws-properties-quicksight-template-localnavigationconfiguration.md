---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-localnavigationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template LocalNavigationConfiguration
<a name="aws-properties-quicksight-template-localnavigationconfiguration"></a>

The navigation configuration for `CustomActionNavigationOperation`.

## Syntax
<a name="aws-properties-quicksight-template-localnavigationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-localnavigationconfiguration-syntax.json"></a>

```
{
  "[TargetSheetId](#cfn-quicksight-template-localnavigationconfiguration-targetsheetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-localnavigationconfiguration-syntax.yaml"></a>

```
  [TargetSheetId](#cfn-quicksight-template-localnavigationconfiguration-targetsheetid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-localnavigationconfiguration-properties"></a>

`TargetSheetId`  <a name="cfn-quicksight-template-localnavigationconfiguration-targetsheetid"></a>
The sheet that is targeted for navigation in the same analysis.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
