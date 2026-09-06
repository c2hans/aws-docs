---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-configurationobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application ConfigurationObject
<a name="aws-properties-emrserverless-application-configurationobject"></a>

A configuration specification to be used when provisioning an application. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

## Syntax
<a name="aws-properties-emrserverless-application-configurationobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-configurationobject-syntax.json"></a>

```
{
  "[Classification](#cfn-emrserverless-application-configurationobject-classification)" : {{String}},
  "[Configurations](#cfn-emrserverless-application-configurationobject-configurations)" : {{[ ConfigurationObject, ... ]}},
  "[Properties](#cfn-emrserverless-application-configurationobject-properties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-configurationobject-syntax.yaml"></a>

```
  [Classification](#cfn-emrserverless-application-configurationobject-classification): {{String}}
  [Configurations](#cfn-emrserverless-application-configurationobject-configurations): {{
    - ConfigurationObject}}
  [Properties](#cfn-emrserverless-application-configurationobject-properties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-emrserverless-application-configurationobject-properties"></a>

`Classification`  <a name="cfn-emrserverless-application-configurationobject-classification"></a>
The classification within a configuration.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Configurations`  <a name="cfn-emrserverless-application-configurationobject-configurations"></a>
A list of additional configurations to apply within a configuration object.
*Required*: No
*Type*: Array of [ConfigurationObject](#aws-properties-emrserverless-application-configurationobject)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Properties`  <a name="cfn-emrserverless-application-configurationobject-properties"></a>
A set of properties specified within a configuration classification.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z]+[-a-zA-Z0-9_.]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
