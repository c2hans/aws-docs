---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-analysissource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate AnalysisSource
<a name="aws-properties-cleanrooms-analysistemplate-analysissource"></a>

The structure that defines the body of the analysis template.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-analysissource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-analysissource-syntax.json"></a>

```
{
  "[Artifacts](#cfn-cleanrooms-analysistemplate-analysissource-artifacts)" : {{AnalysisTemplateArtifacts}},
  "[Text](#cfn-cleanrooms-analysistemplate-analysissource-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-analysissource-syntax.yaml"></a>

```
  [Artifacts](#cfn-cleanrooms-analysistemplate-analysissource-artifacts): {{
    AnalysisTemplateArtifacts}}
  [Text](#cfn-cleanrooms-analysistemplate-analysissource-text): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-analysissource-properties"></a>

`Artifacts`  <a name="cfn-cleanrooms-analysistemplate-analysissource-artifacts"></a>
 The artifacts of the analysis source.
*Required*: No
*Type*: [AnalysisTemplateArtifacts](aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Text`  <a name="cfn-cleanrooms-analysistemplate-analysissource-text"></a>
The query text.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `90000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
