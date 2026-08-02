---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application InitialCapacityConfigKeyValuePair
<a name="aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair"></a>

<a name="aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair-description"></a>The `InitialCapacityConfigKeyValuePair` property type specifies Property description not available. for an [AWS::EMRServerless::Application](aws-resource-emrserverless-application.md).

## Syntax
<a name="aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair-syntax.json"></a>

```
{
  "[Key](#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-key)" : {{String}},
  "[Value](#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-value)" : {{InitialCapacityConfig}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair-syntax.yaml"></a>

```
  [Key](#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-key): {{String}}
  [Value](#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-value): {{
    InitialCapacityConfig}}
```

## Properties
<a name="aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair-properties"></a>

`Key`  <a name="cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]+[-_]*[a-zA-Z]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Value`  <a name="cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-value"></a>
Property description not available.
*Required*: Yes
*Type*: [InitialCapacityConfig](aws-properties-emrserverless-application-initialcapacityconfig.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
