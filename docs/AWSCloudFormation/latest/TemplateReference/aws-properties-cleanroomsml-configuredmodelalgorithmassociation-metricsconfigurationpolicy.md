---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation MetricsConfigurationPolicy
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy"></a>

Provides the configuration policy for metrics generation.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy-syntax.json"></a>

```
{
  "[NoiseLevel](#cfn-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy-noiselevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy-syntax.yaml"></a>

```
  [NoiseLevel](#cfn-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy-noiselevel): {{String}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy-properties"></a>

`NoiseLevel`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy-noiselevel"></a>
The noise level for the generated metrics.
*Required*: Yes
*Type*: String
*Allowed values*: `HIGH | MEDIUM | LOW | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
