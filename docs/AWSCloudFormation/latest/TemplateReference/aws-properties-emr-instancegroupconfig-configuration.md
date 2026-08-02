---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig Configuration
<a name="aws-properties-emr-instancegroupconfig-configuration"></a>

`Configurations` is a property of the `AWS::EMR::Cluster` resource that specifies the configuration of applications on an Amazon EMR cluster.

Configurations are optional. You can use them to have EMR customize applications and software bundled with Amazon EMR when a cluster is created. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

**Note**
Applies only to Amazon EMR releases 4.0 and later.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-configuration-syntax.json"></a>

```
{
  "[Classification](#cfn-emr-instancegroupconfig-configuration-classification)" : {{String}},
  "[ConfigurationProperties](#cfn-emr-instancegroupconfig-configuration-configurationproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Configurations](#cfn-emr-instancegroupconfig-configuration-configurations)" : {{[ Configuration, ... ]}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-configuration-syntax.yaml"></a>

```
  [Classification](#cfn-emr-instancegroupconfig-configuration-classification): {{String}}
  [ConfigurationProperties](#cfn-emr-instancegroupconfig-configuration-configurationproperties): {{
    {{Key}}: {{Value}}}}
  [Configurations](#cfn-emr-instancegroupconfig-configuration-configurations): {{
    - Configuration}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-configuration-properties"></a>

`Classification`  <a name="cfn-emr-instancegroupconfig-configuration-classification"></a>
The classification within a configuration.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfigurationProperties`  <a name="cfn-emr-instancegroupconfig-configuration-configurationproperties"></a>
Within a configuration classification, a set of properties that represent the settings that you want to change in the configuration file. Duplicates not allowed.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configurations`  <a name="cfn-emr-instancegroupconfig-configuration-configurations"></a>
A list of additional configurations to apply within a configuration object.
*Required*: No
*Type*: Array of [Configuration](#aws-properties-emr-instancegroupconfig-configuration)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
