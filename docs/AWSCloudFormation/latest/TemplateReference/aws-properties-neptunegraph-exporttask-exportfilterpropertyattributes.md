---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-neptunegraph-exporttask-exportfilterpropertyattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::ExportTask ExportFilterPropertyAttributes
<a name="aws-properties-neptunegraph-exporttask-exportfilterpropertyattributes"></a>

<a name="aws-properties-neptunegraph-exporttask-exportfilterpropertyattributes-description"></a>The `ExportFilterPropertyAttributes` property type specifies Property description not available. for an [AWS::NeptuneGraph::ExportTask](aws-resource-neptunegraph-exporttask.md).

## Syntax
<a name="aws-properties-neptunegraph-exporttask-exportfilterpropertyattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-neptunegraph-exporttask-exportfilterpropertyattributes-syntax.json"></a>

```
{
  "[MultiValueHandling](#cfn-neptunegraph-exporttask-exportfilterpropertyattributes-multivaluehandling)" : {{String}},
  "[OutputType](#cfn-neptunegraph-exporttask-exportfilterpropertyattributes-outputtype)" : {{String}},
  "[SourcePropertyName](#cfn-neptunegraph-exporttask-exportfilterpropertyattributes-sourcepropertyname)" : {{String}}
}
```

### YAML
<a name="aws-properties-neptunegraph-exporttask-exportfilterpropertyattributes-syntax.yaml"></a>

```
  [MultiValueHandling](#cfn-neptunegraph-exporttask-exportfilterpropertyattributes-multivaluehandling): {{String}}
  [OutputType](#cfn-neptunegraph-exporttask-exportfilterpropertyattributes-outputtype): {{String}}
  [SourcePropertyName](#cfn-neptunegraph-exporttask-exportfilterpropertyattributes-sourcepropertyname): {{String}}
```

## Properties
<a name="aws-properties-neptunegraph-exporttask-exportfilterpropertyattributes-properties"></a>

`MultiValueHandling`  <a name="cfn-neptunegraph-exporttask-exportfilterpropertyattributes-multivaluehandling"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `TO_LIST | PICK_FIRST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputType`  <a name="cfn-neptunegraph-exporttask-exportfilterpropertyattributes-outputtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourcePropertyName`  <a name="cfn-neptunegraph-exporttask-exportfilterpropertyattributes-sourcepropertyname"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
