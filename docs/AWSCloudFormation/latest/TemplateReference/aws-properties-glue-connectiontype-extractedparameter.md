---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-extractedparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ExtractedParameter
<a name="aws-properties-glue-connectiontype-extractedparameter"></a>

<a name="aws-properties-glue-connectiontype-extractedparameter-description"></a>The `ExtractedParameter` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-extractedparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-extractedparameter-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-glue-connectiontype-extractedparameter-defaultvalue)" : {{String}},
  "[Key](#cfn-glue-connectiontype-extractedparameter-key)" : {{String}},
  "[PropertyLocation](#cfn-glue-connectiontype-extractedparameter-propertylocation)" : {{String}},
  "[Value](#cfn-glue-connectiontype-extractedparameter-value)" : {{ResponseExtractionMapping}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-extractedparameter-syntax.yaml"></a>

```
  [DefaultValue](#cfn-glue-connectiontype-extractedparameter-defaultvalue): {{String}}
  [Key](#cfn-glue-connectiontype-extractedparameter-key): {{String}}
  [PropertyLocation](#cfn-glue-connectiontype-extractedparameter-propertylocation): {{String}}
  [Value](#cfn-glue-connectiontype-extractedparameter-value): {{
    ResponseExtractionMapping}}
```

## Properties
<a name="aws-properties-glue-connectiontype-extractedparameter-properties"></a>

`DefaultValue`  <a name="cfn-glue-connectiontype-extractedparameter-defaultvalue"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Key`  <a name="cfn-glue-connectiontype-extractedparameter-key"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropertyLocation`  <a name="cfn-glue-connectiontype-extractedparameter-propertylocation"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `HEADER | BODY | QUERY_PARAM | PATH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-glue-connectiontype-extractedparameter-value"></a>
Property description not available.
*Required*: No
*Type*: [ResponseExtractionMapping](aws-properties-glue-connectiontype-responseextractionmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
