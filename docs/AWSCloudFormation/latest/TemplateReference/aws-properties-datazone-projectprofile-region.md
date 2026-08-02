---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-projectprofile-region.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectProfile Region
<a name="aws-properties-datazone-projectprofile-region"></a>

The AWS Region.

## Syntax
<a name="aws-properties-datazone-projectprofile-region-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-projectprofile-region-syntax.json"></a>

```
{
  "[RegionName](#cfn-datazone-projectprofile-region-regionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-projectprofile-region-syntax.yaml"></a>

```
  [RegionName](#cfn-datazone-projectprofile-region-regionname): {{String}}
```

## Properties
<a name="aws-properties-datazone-projectprofile-region-properties"></a>

`RegionName`  <a name="cfn-datazone-projectprofile-region-regionname"></a>
The AWS Region name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]$`
*Minimum*: `4`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
