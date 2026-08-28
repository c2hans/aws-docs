---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediatailor-vodsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::VodSource
<a name="aws-resource-mediatailor-vodsource"></a>

The VOD source configuration parameters.

## Syntax
<a name="aws-resource-mediatailor-vodsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediatailor-vodsource-syntax.json"></a>

```
{
  "Type" : "AWS::MediaTailor::VodSource",
  "Properties" : {
      "[HttpPackageConfigurations](#cfn-mediatailor-vodsource-httppackageconfigurations)" : {{[ HttpPackageConfiguration, ... ]}},
      "[SourceLocationName](#cfn-mediatailor-vodsource-sourcelocationname)" : {{String}},
      "[Tags](#cfn-mediatailor-vodsource-tags)" : {{[ Tag, ... ]}},
      "[VodSourceName](#cfn-mediatailor-vodsource-vodsourcename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-mediatailor-vodsource-syntax.yaml"></a>

```
Type: AWS::MediaTailor::VodSource
Properties:
  [HttpPackageConfigurations](#cfn-mediatailor-vodsource-httppackageconfigurations): {{
    - HttpPackageConfiguration}}
  [SourceLocationName](#cfn-mediatailor-vodsource-sourcelocationname): {{String}}
  [Tags](#cfn-mediatailor-vodsource-tags): {{
    - Tag}}
  [VodSourceName](#cfn-mediatailor-vodsource-vodsourcename): {{String}}
```

## Properties
<a name="aws-resource-mediatailor-vodsource-properties"></a>

`HttpPackageConfigurations`  <a name="cfn-mediatailor-vodsource-httppackageconfigurations"></a>
The HTTP package configurations for the VOD source.
*Required*: Yes
*Type*: Array of [HttpPackageConfiguration](aws-properties-mediatailor-vodsource-httppackageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLocationName`  <a name="cfn-mediatailor-vodsource-sourcelocationname"></a>
The name of the source location that the VOD source is associated with.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mediatailor-vodsource-tags"></a>
The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediatailor-vodsource-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VodSourceName`  <a name="cfn-mediatailor-vodsource-vodsourcename"></a>
The name of the VOD source.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-mediatailor-vodsource-return-values"></a>

### Ref
<a name="aws-resource-mediatailor-vodsource-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediatailor-vodsource-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediatailor-vodsource-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
