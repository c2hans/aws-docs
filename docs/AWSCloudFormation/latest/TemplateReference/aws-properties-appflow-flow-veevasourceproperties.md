---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-veevasourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow VeevaSourceProperties
<a name="aws-properties-appflow-flow-veevasourceproperties"></a>

 The properties that are applied when using Veeva as a flow source.

## Syntax
<a name="aws-properties-appflow-flow-veevasourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-veevasourceproperties-syntax.json"></a>

```
{
  "[DocumentType](#cfn-appflow-flow-veevasourceproperties-documenttype)" : {{String}},
  "[IncludeAllVersions](#cfn-appflow-flow-veevasourceproperties-includeallversions)" : {{Boolean}},
  "[IncludeRenditions](#cfn-appflow-flow-veevasourceproperties-includerenditions)" : {{Boolean}},
  "[IncludeSourceFiles](#cfn-appflow-flow-veevasourceproperties-includesourcefiles)" : {{Boolean}},
  "[Object](#cfn-appflow-flow-veevasourceproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-veevasourceproperties-syntax.yaml"></a>

```
  [DocumentType](#cfn-appflow-flow-veevasourceproperties-documenttype): {{String}}
  [IncludeAllVersions](#cfn-appflow-flow-veevasourceproperties-includeallversions): {{Boolean}}
  [IncludeRenditions](#cfn-appflow-flow-veevasourceproperties-includerenditions): {{Boolean}}
  [IncludeSourceFiles](#cfn-appflow-flow-veevasourceproperties-includesourcefiles): {{Boolean}}
  [Object](#cfn-appflow-flow-veevasourceproperties-object): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-veevasourceproperties-properties"></a>

`DocumentType`  <a name="cfn-appflow-flow-veevasourceproperties-documenttype"></a>
The document type specified in the Veeva document extract flow.
*Required*: No
*Type*: String
*Pattern*: `[\s\w_-]+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeAllVersions`  <a name="cfn-appflow-flow-veevasourceproperties-includeallversions"></a>
Boolean value to include All Versions of files in Veeva document extract flow.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeRenditions`  <a name="cfn-appflow-flow-veevasourceproperties-includerenditions"></a>
Boolean value to include file renditions in Veeva document extract flow.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeSourceFiles`  <a name="cfn-appflow-flow-veevasourceproperties-includesourcefiles"></a>
Boolean value to include source files in Veeva document extract flow.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Object`  <a name="cfn-appflow-flow-veevasourceproperties-object"></a>
 The object specified in the Veeva flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-flow-veevasourceproperties--seealso"></a>
+ [VeevaSourceProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_VeevaSourceProperties.html) in the *Amazon AppFlow API Reference*.
