---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IdNamespaceAssociation IdNamespaceAssociationInputReferenceProperties
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties"></a>

Provides the information for the ID namespace association input reference properties.

## Syntax
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-syntax.json"></a>

```
{
  "[IdMappingWorkflowsSupported](#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-idmappingworkflowssupported)" : {{[ Json, ... ]}},
  "[IdNamespaceType](#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-idnamespacetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-syntax.yaml"></a>

```
  [IdMappingWorkflowsSupported](#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-idmappingworkflowssupported): {{
    - Json}}
  [IdNamespaceType](#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-idnamespacetype): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-properties"></a>

`IdMappingWorkflowsSupported`  <a name="cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-idmappingworkflowssupported"></a>
Defines how ID mapping workflows are supported for this ID namespace association.
*Required*: No
*Type*: Array of Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdNamespaceType`  <a name="cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-idnamespacetype"></a>
The ID namespace type for this ID namespace association.
*Required*: No
*Type*: String
*Allowed values*: `SOURCE | TARGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
