---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-analysisschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate AnalysisSchema
<a name="aws-properties-cleanrooms-analysistemplate-analysisschema"></a>

A relation within an analysis.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-analysisschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-analysisschema-syntax.json"></a>

```
{
  "[ReferencedTables](#cfn-cleanrooms-analysistemplate-analysisschema-referencedtables)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-analysisschema-syntax.yaml"></a>

```
  [ReferencedTables](#cfn-cleanrooms-analysistemplate-analysisschema-referencedtables): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-analysisschema-properties"></a>

`ReferencedTables`  <a name="cfn-cleanrooms-analysistemplate-analysisschema-referencedtables"></a>
The tables referenced in the analysis schema.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Update requires*: Updates are not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
