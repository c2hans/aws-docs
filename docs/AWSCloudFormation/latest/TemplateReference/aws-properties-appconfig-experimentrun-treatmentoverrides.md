---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-experimentrun-treatmentoverrides.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::ExperimentRun TreatmentOverrides
<a name="aws-properties-appconfig-experimentrun-treatmentoverrides"></a>

Treatment assignment overrides that assign specific entity IDs to treatments, bypassing random assignment.

## Syntax
<a name="aws-properties-appconfig-experimentrun-treatmentoverrides-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-experimentrun-treatmentoverrides-syntax.json"></a>

```
{
  "[Inline](#cfn-appconfig-experimentrun-treatmentoverrides-inline)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-appconfig-experimentrun-treatmentoverrides-syntax.yaml"></a>

```
  [Inline](#cfn-appconfig-experimentrun-treatmentoverrides-inline): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-appconfig-experimentrun-treatmentoverrides-properties"></a>

`Inline`  <a name="cfn-appconfig-experimentrun-treatmentoverrides-inline"></a>
A map of entity IDs to treatment keys. Each entry assigns the specified entity to the specified treatment, bypassing random assignment.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
