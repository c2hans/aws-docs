---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster Configuration
<a name="aws-properties-emr-cluster-configuration"></a>

**Note**
Used only with Amazon EMR release 4.0 and later.

`Configuration` is a subproperty of `InstanceFleetConfig` or `InstanceGroupConfig`. `Configuration` specifies optional configurations for customizing open-source big data applications and environment parameters. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html) in the *Amazon EMR Release Guide*.

## Syntax
<a name="aws-properties-emr-cluster-configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-configuration-syntax.json"></a>

```
{
  "[Classification](#cfn-emr-cluster-configuration-classification)" : {{String}},
  "[ConfigurationProperties](#cfn-emr-cluster-configuration-configurationproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Configurations](#cfn-emr-cluster-configuration-configurations)" : {{[ Configuration, ... ]}}
}
```

### YAML
<a name="aws-properties-emr-cluster-configuration-syntax.yaml"></a>

```
  [Classification](#cfn-emr-cluster-configuration-classification): {{String}}
  [ConfigurationProperties](#cfn-emr-cluster-configuration-configurationproperties): {{
    {{Key}}: {{Value}}}}
  [Configurations](#cfn-emr-cluster-configuration-configurations): {{
    - Configuration}}
```

## Properties
<a name="aws-properties-emr-cluster-configuration-properties"></a>

`Classification`  <a name="cfn-emr-cluster-configuration-classification"></a>
The classification within a configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationProperties`  <a name="cfn-emr-cluster-configuration-configurationproperties"></a>
A list of additional configurations to apply within a configuration object.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configurations`  <a name="cfn-emr-cluster-configuration-configurations"></a>
A list of additional configurations to apply within a configuration object.
*Required*: No
*Type*: Array of [Configuration](#aws-properties-emr-cluster-configuration)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
