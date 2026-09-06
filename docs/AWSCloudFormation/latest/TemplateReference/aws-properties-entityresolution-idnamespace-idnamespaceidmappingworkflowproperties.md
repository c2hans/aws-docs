---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdNamespace IdNamespaceIdMappingWorkflowProperties
<a name="aws-properties-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties"></a>

An object containing `idMappingType`, `providerProperties`, and `ruleBasedProperties`.

## Syntax
<a name="aws-properties-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-syntax.json"></a>

```
{
  "[IdMappingType](#cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-idmappingtype)" : {{String}},
  "[ProviderProperties](#cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-providerproperties)" : {{NamespaceProviderProperties}},
  "[RuleBasedProperties](#cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-rulebasedproperties)" : {{NamespaceRuleBasedProperties}}
}
```

### YAML
<a name="aws-properties-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-syntax.yaml"></a>

```
  [IdMappingType](#cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-idmappingtype): {{String}}
  [ProviderProperties](#cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-providerproperties): {{
    NamespaceProviderProperties}}
  [RuleBasedProperties](#cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-rulebasedproperties): {{
    NamespaceRuleBasedProperties}}
```

## Properties
<a name="aws-properties-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-properties"></a>

`IdMappingType`  <a name="cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-idmappingtype"></a>
The type of ID mapping.
*Required*: Yes
*Type*: String
*Allowed values*: `PROVIDER | RULE_BASED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderProperties`  <a name="cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-providerproperties"></a>
An object which defines any additional configurations required by the provider service.
*Required*: No
*Type*: [NamespaceProviderProperties](aws-properties-entityresolution-idnamespace-namespaceproviderproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleBasedProperties`  <a name="cfn-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties-rulebasedproperties"></a>
 An object which defines any additional configurations required by rule-based matching.
*Required*: No
*Type*: [NamespaceRuleBasedProperties](aws-properties-entityresolution-idnamespace-namespacerulebasedproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
