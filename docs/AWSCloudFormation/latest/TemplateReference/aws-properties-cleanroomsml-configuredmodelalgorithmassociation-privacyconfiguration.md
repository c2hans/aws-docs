---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation PrivacyConfiguration
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration"></a>

Information about the privacy configuration for a configured model algorithm association.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration-syntax.json"></a>

```
{
  "[Policies](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration-policies)" : {{PrivacyConfigurationPolicies}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration-syntax.yaml"></a>

```
  [Policies](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration-policies): {{
    PrivacyConfigurationPolicies}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration-properties"></a>

`Policies`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration-policies"></a>
The privacy configuration policies for a configured model algorithm association.
*Required*: Yes
*Type*: [PrivacyConfigurationPolicies](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
