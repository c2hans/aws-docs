---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation LogRedactionConfiguration
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration"></a>

The configuration for log redaction.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-syntax.json"></a>

```
{
  "[CustomEntityConfig](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-customentityconfig)" : {{CustomEntityConfig}},
  "[EntitiesToRedact](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-entitiestoredact)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-syntax.yaml"></a>

```
  [CustomEntityConfig](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-customentityconfig): {{
    CustomEntityConfig}}
  [EntitiesToRedact](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-entitiestoredact): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-properties"></a>

`CustomEntityConfig`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-customentityconfig"></a>
Specifies the configuration for custom entities in the context of log redaction.
*Required*: No
*Type*: [CustomEntityConfig](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntitiesToRedact`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-entitiestoredact"></a>
Specifies the entities to be redacted from logs. Entities to redact are "ALL\_PERSONALLY\_IDENTIFIABLE\_INFORMATION", "NUMBERS","CUSTOM". If CUSTOM is supplied or configured, custom patterns (customDataIdentifiers) should be provided, and the patterns will be redacted in logs or error messages.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
