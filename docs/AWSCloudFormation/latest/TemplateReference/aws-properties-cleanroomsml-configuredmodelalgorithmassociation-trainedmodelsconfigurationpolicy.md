---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation TrainedModelsConfigurationPolicy
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy"></a>

The configuration policy for the trained models.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-syntax.json"></a>

```
{
  "[ContainerLogs](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-containerlogs)" : {{[ LogsConfigurationPolicy, ... ]}},
  "[ContainerMetrics](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-containermetrics)" : {{MetricsConfigurationPolicy}},
  "[MaxArtifactSize](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-maxartifactsize)" : {{TrainedModelArtifactMaxSize}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-syntax.yaml"></a>

```
  [ContainerLogs](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-containerlogs): {{
    - LogsConfigurationPolicy}}
  [ContainerMetrics](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-containermetrics): {{
    MetricsConfigurationPolicy}}
  [MaxArtifactSize](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-maxartifactsize): {{
    TrainedModelArtifactMaxSize}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-properties"></a>

`ContainerLogs`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-containerlogs"></a>
The container for the logs of the trained model.
*Required*: No
*Type*: Array of [LogsConfigurationPolicy](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerMetrics`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-containermetrics"></a>
The container for the metrics of the trained model.
*Required*: No
*Type*: [MetricsConfigurationPolicy](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxArtifactSize`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-maxartifactsize"></a>
The maximum size limit for trained model artifacts as defined in the configuration policy. This setting helps enforce consistent size limits across trained models in the collaboration.
*Required*: No
*Type*: [TrainedModelArtifactMaxSize](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
