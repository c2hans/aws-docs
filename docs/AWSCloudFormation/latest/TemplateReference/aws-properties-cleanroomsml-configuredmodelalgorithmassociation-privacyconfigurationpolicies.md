---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation PrivacyConfigurationPolicies
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies"></a>

Information about the privacy configuration policies for a configured model algorithm association.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-syntax.json"></a>

```
{
  "[TrainedModelExports](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodelexports)" : {{TrainedModelExportsConfigurationPolicy}},
  "[TrainedModelInferenceJobs](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodelinferencejobs)" : {{TrainedModelInferenceJobsConfigurationPolicy}},
  "[TrainedModels](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodels)" : {{TrainedModelsConfigurationPolicy}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-syntax.yaml"></a>

```
  [TrainedModelExports](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodelexports): {{
    TrainedModelExportsConfigurationPolicy}}
  [TrainedModelInferenceJobs](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodelinferencejobs): {{
    TrainedModelInferenceJobsConfigurationPolicy}}
  [TrainedModels](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodels): {{
    TrainedModelsConfigurationPolicy}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-properties"></a>

`TrainedModelExports`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodelexports"></a>
Specifies who will receive the trained model export.
*Required*: No
*Type*: [TrainedModelExportsConfigurationPolicy](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainedModelInferenceJobs`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodelinferencejobs"></a>
Specifies who will receive the trained model inference jobs.
*Required*: No
*Type*: [TrainedModelInferenceJobsConfigurationPolicy](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainedModels`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodels"></a>
Specifies who will receive the trained models.
*Required*: No
*Type*: [TrainedModelsConfigurationPolicy](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
