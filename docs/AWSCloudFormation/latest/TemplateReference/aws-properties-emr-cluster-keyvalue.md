---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-keyvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster KeyValue
<a name="aws-properties-emr-cluster-keyvalue"></a>

`KeyValue` is a subproperty of the `HadoopJarStepConfig` property type. `KeyValue` is used to pass parameters to a step.

## Syntax
<a name="aws-properties-emr-cluster-keyvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-keyvalue-syntax.json"></a>

```
{
  "[Key](#cfn-emr-cluster-keyvalue-key)" : {{String}},
  "[Value](#cfn-emr-cluster-keyvalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-cluster-keyvalue-syntax.yaml"></a>

```
  [Key](#cfn-emr-cluster-keyvalue-key): {{String}}
  [Value](#cfn-emr-cluster-keyvalue-value): {{String}}
```

## Properties
<a name="aws-properties-emr-cluster-keyvalue-properties"></a>

`Key`  <a name="cfn-emr-cluster-keyvalue-key"></a>
The unique identifier of a key-value pair.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-emr-cluster-keyvalue-value"></a>
The value part of the identified key.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
