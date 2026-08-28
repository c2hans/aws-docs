---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation CustomEntityConfig
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig"></a>

The configuration for defining custom patterns to be redacted from logs and error messages. This is for the CUSTOM config under entitiesToRedact. Both CustomEntityConfig and entitiesToRedact need to be present or not present.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig-syntax.json"></a>

```
{
  "[CustomDataIdentifiers](#cfn-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig-customdataidentifiers)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig-syntax.yaml"></a>

```
  [CustomDataIdentifiers](#cfn-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig-customdataidentifiers): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig-properties"></a>

`CustomDataIdentifiers`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig-customdataidentifiers"></a>
Defines data identifiers for the custom entity configuration. Provide this only if CUSTOM redaction is configured.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `200 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
