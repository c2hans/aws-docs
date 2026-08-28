---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idmappingworkflow-idmappingrulebasedproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow IdMappingRuleBasedProperties
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingrulebasedproperties"></a>

 An object that defines the list of matching rules to run in an ID mapping workflow.

## Syntax
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingrulebasedproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingrulebasedproperties-syntax.json"></a>

```
{
  "[AttributeMatchingModel](#cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-attributematchingmodel)" : {{String}},
  "[RecordMatchingModel](#cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-recordmatchingmodel)" : {{String}},
  "[RuleDefinitionType](#cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-ruledefinitiontype)" : {{String}},
  "[Rules](#cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-rules)" : {{[ Rule, ... ]}}
}
```

### YAML
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingrulebasedproperties-syntax.yaml"></a>

```
  [AttributeMatchingModel](#cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-attributematchingmodel): {{String}}
  [RecordMatchingModel](#cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-recordmatchingmodel): {{String}}
  [RuleDefinitionType](#cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-ruledefinitiontype): {{String}}
  [Rules](#cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-rules): {{
    - Rule}}
```

## Properties
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingrulebasedproperties-properties"></a>

`AttributeMatchingModel`  <a name="cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-attributematchingmodel"></a>
The comparison type. You can either choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel`.
If you choose `ONE_TO_ONE`, the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.
If you choose `MANY_TO_MANY`, the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A matches the value of the `BusinessEmail` field of Profile B, the two profiles are matched on the `Email` attribute type.
*Required*: Yes
*Type*: String
*Allowed values*: `ONE_TO_ONE | MANY_TO_MANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordMatchingModel`  <a name="cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-recordmatchingmodel"></a>
 The type of matching record that is allowed to be used in an ID mapping workflow.
If the value is set to `ONE_SOURCE_TO_ONE_TARGET`, only one record in the source can be matched to the same record in the target.
If the value is set to `MANY_SOURCE_TO_ONE_TARGET`, multiple records in the source can be matched to one record in the target.
*Required*: Yes
*Type*: String
*Allowed values*: `ONE_SOURCE_TO_ONE_TARGET | MANY_SOURCE_TO_ONE_TARGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleDefinitionType`  <a name="cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-ruledefinitiontype"></a>
 The set of rules you can use in an ID mapping workflow. The limitations specified for the source or target to define the match rules must be compatible.
*Required*: No
*Type*: String
*Allowed values*: `SOURCE | TARGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-entityresolution-idmappingworkflow-idmappingrulebasedproperties-rules"></a>
 The rules that can be used for ID mapping.
*Required*: No
*Type*: Array of [Rule](aws-properties-entityresolution-idmappingworkflow-rule.md)
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
