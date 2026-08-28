---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation TrainedModelExportsConfigurationPolicy
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy"></a>

Information about how the trained model exports are configured.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-syntax.json"></a>

```
{
  "[FilesToExport](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-filestoexport)" : {{[ String, ... ]}},
  "[MaxSize](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-maxsize)" : {{TrainedModelExportsMaxSize}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-syntax.yaml"></a>

```
  [FilesToExport](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-filestoexport): {{
    - String}}
  [MaxSize](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-maxsize): {{
    TrainedModelExportsMaxSize}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-properties"></a>

`FilesToExport`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-filestoexport"></a>
The files that are exported during the trained model export job.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxSize`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-maxsize"></a>
The maximum size of the data that can be exported.
*Required*: Yes
*Type*: [TrainedModelExportsMaxSize](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
