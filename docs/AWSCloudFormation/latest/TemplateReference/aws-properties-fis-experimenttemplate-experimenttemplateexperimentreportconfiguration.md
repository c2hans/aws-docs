---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate ExperimentTemplateExperimentReportConfiguration
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration"></a>

Describes the report configuration for the experiment template.

## Syntax
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-syntax.json"></a>

```
{
  "[DataSources](#cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-datasources)" : {{DataSources}},
  "[Outputs](#cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-outputs)" : {{Outputs}},
  "[PostExperimentDuration](#cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-postexperimentduration)" : {{String}},
  "[PreExperimentDuration](#cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-preexperimentduration)" : {{String}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-syntax.yaml"></a>

```
  [DataSources](#cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-datasources): {{
    DataSources}}
  [Outputs](#cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-outputs): {{
    Outputs}}
  [PostExperimentDuration](#cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-postexperimentduration): {{String}}
  [PreExperimentDuration](#cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-preexperimentduration): {{String}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-properties"></a>

`DataSources`  <a name="cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-datasources"></a>
The data sources for the experiment report.
*Required*: No
*Type*: [DataSources](aws-properties-fis-experimenttemplate-datasources.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Outputs`  <a name="cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-outputs"></a>
The output destinations of the experiment report.
*Required*: Yes
*Type*: [Outputs](aws-properties-fis-experimenttemplate-outputs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostExperimentDuration`  <a name="cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-postexperimentduration"></a>
The duration after the experiment end time for the data sources to include in the report.
*Required*: No
*Type*: String
*Pattern*: `[\S]+`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreExperimentDuration`  <a name="cfn-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration-preexperimentduration"></a>
The duration before the experiment start time for the data sources to include in the report.
*Required*: No
*Type*: String
*Pattern*: `[\S]+`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
