---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IdNamespaceAssociation IdMappingConfig
<a name="aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig"></a>

The configuration settings for the ID mapping table.

## Syntax
<a name="aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig-syntax.json"></a>

```
{
  "[AllowUseAsDimensionColumn](#cfn-cleanrooms-idnamespaceassociation-idmappingconfig-allowuseasdimensioncolumn)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig-syntax.yaml"></a>

```
  [AllowUseAsDimensionColumn](#cfn-cleanrooms-idnamespaceassociation-idmappingconfig-allowuseasdimensioncolumn): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig-properties"></a>

`AllowUseAsDimensionColumn`  <a name="cfn-cleanrooms-idnamespaceassociation-idmappingconfig-allowuseasdimensioncolumn"></a>
An indicator as to whether you can use your column as a dimension column in the ID mapping table (`TRUE`) or not (`FALSE`).
Default is `FALSE`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
