---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobTemplate TemplateParameterConfiguration
<a name="aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration"></a>

The configuration of a job template parameter.

## Syntax
<a name="aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-emrcontainers-jobtemplate-templateparameterconfiguration-defaultvalue)" : {{String}},
  "[Type](#cfn-emrcontainers-jobtemplate-templateparameterconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration-syntax.yaml"></a>

```
  [DefaultValue](#cfn-emrcontainers-jobtemplate-templateparameterconfiguration-defaultvalue): {{String}}
  [Type](#cfn-emrcontainers-jobtemplate-templateparameterconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration-properties"></a>

`DefaultValue`  <a name="cfn-emrcontainers-jobtemplate-templateparameterconfiguration-defaultvalue"></a>
The default value for the job template parameter.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-emrcontainers-jobtemplate-templateparameterconfiguration-type"></a>
The type of the job template parameter. Allowed values are: ‘STRING’, ‘NUMBER’.
*Required*: No
*Type*: String
*Allowed values*: `NUMBER | STRING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
