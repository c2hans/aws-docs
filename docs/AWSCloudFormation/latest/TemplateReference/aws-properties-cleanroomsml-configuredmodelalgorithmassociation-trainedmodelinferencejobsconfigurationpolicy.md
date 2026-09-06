---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation TrainedModelInferenceJobsConfigurationPolicy
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy"></a>

Provides configuration information for the trained model inference job.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-syntax.json"></a>

```
{
  "[ContainerLogs](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-containerlogs)" : {{[ LogsConfigurationPolicy, ... ]}},
  "[MaxOutputSize](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-maxoutputsize)" : {{TrainedModelInferenceMaxOutputSize}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-syntax.yaml"></a>

```
  [ContainerLogs](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-containerlogs): {{
    - LogsConfigurationPolicy}}
  [MaxOutputSize](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-maxoutputsize): {{
    TrainedModelInferenceMaxOutputSize}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-properties"></a>

`ContainerLogs`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-containerlogs"></a>
The logs container for the trained model inference job.
*Required*: No
*Type*: Array of [LogsConfigurationPolicy](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxOutputSize`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-maxoutputsize"></a>
The maximum allowed size of the output of the trained model inference job.
*Required*: No
*Type*: [TrainedModelInferenceMaxOutputSize](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
