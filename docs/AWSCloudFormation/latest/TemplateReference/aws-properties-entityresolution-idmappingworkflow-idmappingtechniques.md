---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idmappingworkflow-idmappingtechniques.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow IdMappingTechniques
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingtechniques"></a>

An object which defines the ID mapping technique and any additional configurations.

## Syntax
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingtechniques-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingtechniques-syntax.json"></a>

```
{
  "[IdMappingType](#cfn-entityresolution-idmappingworkflow-idmappingtechniques-idmappingtype)" : {{String}},
  "[NormalizationVersion](#cfn-entityresolution-idmappingworkflow-idmappingtechniques-normalizationversion)" : {{String}},
  "[ProviderProperties](#cfn-entityresolution-idmappingworkflow-idmappingtechniques-providerproperties)" : {{ProviderProperties}},
  "[RuleBasedProperties](#cfn-entityresolution-idmappingworkflow-idmappingtechniques-rulebasedproperties)" : {{IdMappingRuleBasedProperties}}
}
```

### YAML
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingtechniques-syntax.yaml"></a>

```
  [IdMappingType](#cfn-entityresolution-idmappingworkflow-idmappingtechniques-idmappingtype): {{String}}
  [NormalizationVersion](#cfn-entityresolution-idmappingworkflow-idmappingtechniques-normalizationversion): {{String}}
  [ProviderProperties](#cfn-entityresolution-idmappingworkflow-idmappingtechniques-providerproperties): {{
    ProviderProperties}}
  [RuleBasedProperties](#cfn-entityresolution-idmappingworkflow-idmappingtechniques-rulebasedproperties): {{
    IdMappingRuleBasedProperties}}
```

## Properties
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingtechniques-properties"></a>

`IdMappingType`  <a name="cfn-entityresolution-idmappingworkflow-idmappingtechniques-idmappingtype"></a>
The type of ID mapping.
*Required*: No
*Type*: String
*Allowed values*: `PROVIDER | RULE_BASED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NormalizationVersion`  <a name="cfn-entityresolution-idmappingworkflow-idmappingtechniques-normalizationversion"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderProperties`  <a name="cfn-entityresolution-idmappingworkflow-idmappingtechniques-providerproperties"></a>
An object which defines any additional configurations required by the provider service.
*Required*: No
*Type*: [ProviderProperties](aws-properties-entityresolution-idmappingworkflow-providerproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleBasedProperties`  <a name="cfn-entityresolution-idmappingworkflow-idmappingtechniques-rulebasedproperties"></a>
 An object which defines any additional configurations required by rule-based matching.
*Required*: No
*Type*: [IdMappingRuleBasedProperties](aws-properties-entityresolution-idmappingworkflow-idmappingrulebasedproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
