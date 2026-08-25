---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun Configuration
<a name="aws-properties-emrcontainers-jobrun-configuration"></a>

A configuration specification to be used when provisioning virtual clusters, which can include configurations for applications and software bundled with Amazon EMR on EKS. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-configuration-syntax.json"></a>

```
{
  "[Classification](#cfn-emrcontainers-jobrun-configuration-classification)" : {{String}},
  "[Configurations](#cfn-emrcontainers-jobrun-configuration-configurations)" : {{[ Configuration, ... ]}},
  "[Properties](#cfn-emrcontainers-jobrun-configuration-properties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-configuration-syntax.yaml"></a>

```
  [Classification](#cfn-emrcontainers-jobrun-configuration-classification): {{String}}
  [Configurations](#cfn-emrcontainers-jobrun-configuration-configurations): {{
    - Configuration}}
  [Properties](#cfn-emrcontainers-jobrun-configuration-properties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-configuration-properties"></a>

`Classification`  <a name="cfn-emrcontainers-jobrun-configuration-classification"></a>
The classification within a configuration.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configurations`  <a name="cfn-emrcontainers-jobrun-configuration-configurations"></a>
A list of additional configurations to apply within a configuration object.
*Required*: No
*Type*: Array of [Configuration](#aws-properties-emrcontainers-jobrun-configuration)
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Properties`  <a name="cfn-emrcontainers-jobrun-configuration-properties"></a>
A set of properties specified within a configuration classification.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
