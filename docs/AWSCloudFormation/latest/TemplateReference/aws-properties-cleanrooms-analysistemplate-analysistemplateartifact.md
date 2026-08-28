---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-analysistemplateartifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate AnalysisTemplateArtifact
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifact"></a>

The analysis template artifact.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifact-syntax.json"></a>

```
{
  "[Location](#cfn-cleanrooms-analysistemplate-analysistemplateartifact-location)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifact-syntax.yaml"></a>

```
  [Location](#cfn-cleanrooms-analysistemplate-analysistemplateartifact-location): {{
    S3Location}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifact-properties"></a>

`Location`  <a name="cfn-cleanrooms-analysistemplate-analysistemplateartifact-location"></a>
 The artifact location.
*Required*: Yes
*Type*: [S3Location](aws-properties-cleanrooms-analysistemplate-s3location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
