---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation TrainedModelInferenceMaxOutputSize
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize"></a>

Information about the maximum output size for a trained model inference job.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-syntax.json"></a>

```
{
  "[Unit](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-unit)" : {{String}},
  "[Value](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-syntax.yaml"></a>

```
  [Unit](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-unit): {{String}}
  [Value](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-value): {{Number}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-properties"></a>

`Unit`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-unit"></a>
The measurement unit to use.
*Required*: Yes
*Type*: String
*Allowed values*: `GB`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-value"></a>
The maximum output size value.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
