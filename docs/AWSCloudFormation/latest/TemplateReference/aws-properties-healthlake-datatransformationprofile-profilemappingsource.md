---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-datatransformationprofile-profilemappingsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::DataTransformationProfile ProfileMappingSource
<a name="aws-properties-healthlake-datatransformationprofile-profilemappingsource"></a>

Contains raw content to use as the source when creating a data transformation profile directly from a mapping.

## Syntax
<a name="aws-properties-healthlake-datatransformationprofile-profilemappingsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-datatransformationprofile-profilemappingsource-syntax.json"></a>

```
{
  "[ProfileMapping](#cfn-healthlake-datatransformationprofile-profilemappingsource-profilemapping)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-healthlake-datatransformationprofile-profilemappingsource-syntax.yaml"></a>

```
  [ProfileMapping](#cfn-healthlake-datatransformationprofile-profilemappingsource-profilemapping): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-healthlake-datatransformationprofile-profilemappingsource-properties"></a>

`ProfileMapping`  <a name="cfn-healthlake-datatransformationprofile-profilemappingsource-profilemapping"></a>
The content as a map of file paths to profile strings.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
