---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-recommendationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource RecommendationConfiguration
<a name="aws-properties-datazone-datasource-recommendationconfiguration"></a>

The recommendation configuration for the data source.

## Syntax
<a name="aws-properties-datazone-datasource-recommendationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-recommendationconfiguration-syntax.json"></a>

```
{
  "[EnableBusinessNameGeneration](#cfn-datazone-datasource-recommendationconfiguration-enablebusinessnamegeneration)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-recommendationconfiguration-syntax.yaml"></a>

```
  [EnableBusinessNameGeneration](#cfn-datazone-datasource-recommendationconfiguration-enablebusinessnamegeneration): {{Boolean}}
```

## Properties
<a name="aws-properties-datazone-datasource-recommendationconfiguration-properties"></a>

`EnableBusinessNameGeneration`  <a name="cfn-datazone-datasource-recommendationconfiguration-enablebusinessnamegeneration"></a>
Specifies whether automatic business name generation is to be enabled or not as part of the recommendation configuration.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
