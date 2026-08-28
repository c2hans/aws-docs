---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bcmdataexports-export-dataquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Export DataQuery
<a name="aws-properties-bcmdataexports-export-dataquery"></a>

The SQL query of column selections and row filters from the data table you want.

## Syntax
<a name="aws-properties-bcmdataexports-export-dataquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bcmdataexports-export-dataquery-syntax.json"></a>

```
{
  "[QueryStatement](#cfn-bcmdataexports-export-dataquery-querystatement)" : {{String}},
  "[TableConfigurations](#cfn-bcmdataexports-export-dataquery-tableconfigurations)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-bcmdataexports-export-dataquery-syntax.yaml"></a>

```
  [QueryStatement](#cfn-bcmdataexports-export-dataquery-querystatement): {{String}}
  [TableConfigurations](#cfn-bcmdataexports-export-dataquery-tableconfigurations): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-bcmdataexports-export-dataquery-properties"></a>

`QueryStatement`  <a name="cfn-bcmdataexports-export-dataquery-querystatement"></a>
The query statement.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `1`
*Maximum*: `36000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableConfigurations`  <a name="cfn-bcmdataexports-export-dataquery-tableconfigurations"></a>
The table configuration.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
