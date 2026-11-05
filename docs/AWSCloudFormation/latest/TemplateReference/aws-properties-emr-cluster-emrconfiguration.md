---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-emrconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster EMRConfiguration
<a name="aws-properties-emr-cluster-emrconfiguration"></a>

<a name="aws-properties-emr-cluster-emrconfiguration-description"></a>The `EMRConfiguration` property type specifies Property description not available. for an [AWS::EMR::Cluster](aws-resource-emr-cluster.md).

## Syntax
<a name="aws-properties-emr-cluster-emrconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-emrconfiguration-syntax.json"></a>

```
{
  "[Classification](#cfn-emr-cluster-emrconfiguration-classification)" : {{String}},
  "[ConfigurationProperties](#cfn-emr-cluster-emrconfiguration-configurationproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Configurations](#cfn-emr-cluster-emrconfiguration-configurations)" : {{[ EMRConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-emr-cluster-emrconfiguration-syntax.yaml"></a>

```
  [Classification](#cfn-emr-cluster-emrconfiguration-classification): {{String}}
  [ConfigurationProperties](#cfn-emr-cluster-emrconfiguration-configurationproperties): {{
    {{Key}}: {{Value}}}}
  [Configurations](#cfn-emr-cluster-emrconfiguration-configurations): {{
    - EMRConfiguration}}
```

## Properties
<a name="aws-properties-emr-cluster-emrconfiguration-properties"></a>

`Classification`  <a name="cfn-emr-cluster-emrconfiguration-classification"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ConfigurationProperties`  <a name="cfn-emr-cluster-emrconfiguration-configurationproperties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Configurations`  <a name="cfn-emr-cluster-emrconfiguration-configurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [EMRConfiguration](#aws-properties-emr-cluster-emrconfiguration)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
