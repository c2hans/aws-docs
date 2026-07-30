---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-hyperpodpropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection HyperPodPropertiesInput
<a name="aws-properties-datazone-connection-hyperpodpropertiesinput"></a>

The hyper pod properties of a AWS Glue properties patch.

## Syntax
<a name="aws-properties-datazone-connection-hyperpodpropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-hyperpodpropertiesinput-syntax.json"></a>

```
{
  "[ClusterName](#cfn-datazone-connection-hyperpodpropertiesinput-clustername)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-hyperpodpropertiesinput-syntax.yaml"></a>

```
  [ClusterName](#cfn-datazone-connection-hyperpodpropertiesinput-clustername): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-hyperpodpropertiesinput-properties"></a>

`ClusterName`  <a name="cfn-datazone-connection-hyperpodpropertiesinput-clustername"></a>
The cluster name the hyper pod properties.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
