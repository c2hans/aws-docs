---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-analysissourcemetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate AnalysisSourceMetadata
<a name="aws-properties-cleanrooms-analysistemplate-analysissourcemetadata"></a>

The analysis source metadata.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-analysissourcemetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-analysissourcemetadata-syntax.json"></a>

```
{
  "[Artifacts](#cfn-cleanrooms-analysistemplate-analysissourcemetadata-artifacts)" : {{AnalysisTemplateArtifactMetadata}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-analysissourcemetadata-syntax.yaml"></a>

```
  [Artifacts](#cfn-cleanrooms-analysistemplate-analysissourcemetadata-artifacts): {{
    AnalysisTemplateArtifactMetadata}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-analysissourcemetadata-properties"></a>

`Artifacts`  <a name="cfn-cleanrooms-analysistemplate-analysissourcemetadata-artifacts"></a>
 The artifacts of the analysis source metadata.
*Required*: Yes
*Type*: [AnalysisTemplateArtifactMetadata](aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
