---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate AnalysisTemplateArtifactMetadata
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata"></a>

The analysis template artifact metadata.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata-syntax.json"></a>

```
{
  "[AdditionalArtifactHashes](#cfn-cleanrooms-analysistemplate-analysistemplateartifactmetadata-additionalartifacthashes)" : {{[ Hash, ... ]}},
  "[EntryPointHash](#cfn-cleanrooms-analysistemplate-analysistemplateartifactmetadata-entrypointhash)" : {{Hash}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata-syntax.yaml"></a>

```
  [AdditionalArtifactHashes](#cfn-cleanrooms-analysistemplate-analysistemplateartifactmetadata-additionalartifacthashes): {{
    - Hash}}
  [EntryPointHash](#cfn-cleanrooms-analysistemplate-analysistemplateartifactmetadata-entrypointhash): {{
    Hash}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata-properties"></a>

`AdditionalArtifactHashes`  <a name="cfn-cleanrooms-analysistemplate-analysistemplateartifactmetadata-additionalartifacthashes"></a>
 Additional artifact hashes for the analysis template.
*Required*: No
*Type*: Array of [Hash](aws-properties-cleanrooms-analysistemplate-hash.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntryPointHash`  <a name="cfn-cleanrooms-analysistemplate-analysistemplateartifactmetadata-entrypointhash"></a>
 The hash of the entry point for the analysis template artifact metadata.
*Required*: Yes
*Type*: [Hash](aws-properties-cleanrooms-analysistemplate-hash.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
