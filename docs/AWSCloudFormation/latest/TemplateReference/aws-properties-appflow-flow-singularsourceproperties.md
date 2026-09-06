---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-singularsourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow SingularSourceProperties
<a name="aws-properties-appflow-flow-singularsourceproperties"></a>

 The properties that are applied when Singular is being used as a source.

## Syntax
<a name="aws-properties-appflow-flow-singularsourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-singularsourceproperties-syntax.json"></a>

```
{
  "[Object](#cfn-appflow-flow-singularsourceproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-singularsourceproperties-syntax.yaml"></a>

```
  [Object](#cfn-appflow-flow-singularsourceproperties-object): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-singularsourceproperties-properties"></a>

`Object`  <a name="cfn-appflow-flow-singularsourceproperties-object"></a>
 The object specified in the Singular flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-flow-singularsourceproperties--seealso"></a>
+ [SingularSourceProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SingularSourceProperties.html) in the *Amazon AppFlow API Reference*.
