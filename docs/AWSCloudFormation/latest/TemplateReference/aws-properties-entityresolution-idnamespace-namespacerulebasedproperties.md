---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idnamespace-namespacerulebasedproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdNamespace NamespaceRuleBasedProperties
<a name="aws-properties-entityresolution-idnamespace-namespacerulebasedproperties"></a>

 The rule-based properties of an ID namespace. These properties define how the ID namespace can be used in an ID mapping workflow.

## Syntax
<a name="aws-properties-entityresolution-idnamespace-namespacerulebasedproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idnamespace-namespacerulebasedproperties-syntax.json"></a>

```
{
  "[AttributeMatchingModel](#cfn-entityresolution-idnamespace-namespacerulebasedproperties-attributematchingmodel)" : {{String}},
  "[RecordMatchingModels](#cfn-entityresolution-idnamespace-namespacerulebasedproperties-recordmatchingmodels)" : {{[ String, ... ]}},
  "[RuleDefinitionTypes](#cfn-entityresolution-idnamespace-namespacerulebasedproperties-ruledefinitiontypes)" : {{[ String, ... ]}},
  "[Rules](#cfn-entityresolution-idnamespace-namespacerulebasedproperties-rules)" : {{[ Rule, ... ]}}
}
```

### YAML
<a name="aws-properties-entityresolution-idnamespace-namespacerulebasedproperties-syntax.yaml"></a>

```
  [AttributeMatchingModel](#cfn-entityresolution-idnamespace-namespacerulebasedproperties-attributematchingmodel): {{String}}
  [RecordMatchingModels](#cfn-entityresolution-idnamespace-namespacerulebasedproperties-recordmatchingmodels): {{
    - String}}
  [RuleDefinitionTypes](#cfn-entityresolution-idnamespace-namespacerulebasedproperties-ruledefinitiontypes): {{
    - String}}
  [Rules](#cfn-entityresolution-idnamespace-namespacerulebasedproperties-rules): {{
    - Rule}}
```

## Properties
<a name="aws-properties-entityresolution-idnamespace-namespacerulebasedproperties-properties"></a>

`AttributeMatchingModel`  <a name="cfn-entityresolution-idnamespace-namespacerulebasedproperties-attributematchingmodel"></a>
The comparison type. You can either choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel`.
If you choose `ONE_TO_ONE`, the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.
If you choose `MANY_TO_MANY`, the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A matches the value of `BusinessEmail` field of Profile B, the two profiles are matched on the `Email` attribute type.
*Required*: No
*Type*: String
*Allowed values*: `ONE_TO_ONE | MANY_TO_MANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordMatchingModels`  <a name="cfn-entityresolution-idnamespace-namespacerulebasedproperties-recordmatchingmodels"></a>
 The type of matching record that is allowed to be used in an ID mapping workflow.
If the value is set to `ONE_SOURCE_TO_ONE_TARGET`, only one record in the source is matched to one record in the target.
If the value is set to `MANY_SOURCE_TO_ONE_TARGET`, all matching records in the source are matched to one record in the target.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleDefinitionTypes`  <a name="cfn-entityresolution-idnamespace-namespacerulebasedproperties-ruledefinitiontypes"></a>
 The sets of rules you can use in an ID mapping workflow. The limitations specified for the source and target must be compatible.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-entityresolution-idnamespace-namespacerulebasedproperties-rules"></a>
 The rules for the ID namespace.
*Required*: No
*Type*: Array of [Rule](aws-properties-entityresolution-idnamespace-rule.md)
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
