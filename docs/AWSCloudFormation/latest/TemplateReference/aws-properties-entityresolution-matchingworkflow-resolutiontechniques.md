---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow ResolutionTechniques
<a name="aws-properties-entityresolution-matchingworkflow-resolutiontechniques"></a>

An object which defines the `resolutionType` and the `ruleBasedProperties`.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-resolutiontechniques-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-resolutiontechniques-syntax.json"></a>

```
{
  "[EnableRealTimeMatching](#cfn-entityresolution-matchingworkflow-resolutiontechniques-enablerealtimematching)" : {{Boolean}},
  "[ProviderProperties](#cfn-entityresolution-matchingworkflow-resolutiontechniques-providerproperties)" : {{ProviderProperties}},
  "[ResolutionType](#cfn-entityresolution-matchingworkflow-resolutiontechniques-resolutiontype)" : {{String}},
  "[RuleBasedProperties](#cfn-entityresolution-matchingworkflow-resolutiontechniques-rulebasedproperties)" : {{RuleBasedProperties}},
  "[RuleConditionProperties](#cfn-entityresolution-matchingworkflow-resolutiontechniques-ruleconditionproperties)" : {{RuleConditionProperties}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-resolutiontechniques-syntax.yaml"></a>

```
  [EnableRealTimeMatching](#cfn-entityresolution-matchingworkflow-resolutiontechniques-enablerealtimematching): {{Boolean}}
  [ProviderProperties](#cfn-entityresolution-matchingworkflow-resolutiontechniques-providerproperties): {{
    ProviderProperties}}
  [ResolutionType](#cfn-entityresolution-matchingworkflow-resolutiontechniques-resolutiontype): {{String}}
  [RuleBasedProperties](#cfn-entityresolution-matchingworkflow-resolutiontechniques-rulebasedproperties): {{
    RuleBasedProperties}}
  [RuleConditionProperties](#cfn-entityresolution-matchingworkflow-resolutiontechniques-ruleconditionproperties): {{
    RuleConditionProperties}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-resolutiontechniques-properties"></a>

`EnableRealTimeMatching`  <a name="cfn-entityresolution-matchingworkflow-resolutiontechniques-enablerealtimematching"></a>
Specifies whether real-time matching is enabled for the rule-based matching workflow. When you enable real-time matching, you can use the `GenerateMatchId` operation with the workflow.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProviderProperties`  <a name="cfn-entityresolution-matchingworkflow-resolutiontechniques-providerproperties"></a>
The properties of the provider service.
*Required*: No
*Type*: [ProviderProperties](aws-properties-entityresolution-matchingworkflow-providerproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolutionType`  <a name="cfn-entityresolution-matchingworkflow-resolutiontechniques-resolutiontype"></a>
The type of matching workflow to create. Specify one of the following types:
+ `RULE_MATCHING`: Match records using configurable rule-based criteria
+ `ML_MATCHING`: Match records using machine learning models
+ `PROVIDER`: Match records using a third-party matching provider
*Required*: No
*Type*: String
*Allowed values*: `RULE_MATCHING | ML_MATCHING | PROVIDER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleBasedProperties`  <a name="cfn-entityresolution-matchingworkflow-resolutiontechniques-rulebasedproperties"></a>
An object which defines the list of matching rules to run and has a field `rules`, which is a list of rule objects.
*Required*: No
*Type*: [RuleBasedProperties](aws-properties-entityresolution-matchingworkflow-rulebasedproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleConditionProperties`  <a name="cfn-entityresolution-matchingworkflow-resolutiontechniques-ruleconditionproperties"></a>
An object containing the `rules` for a matching workflow.
*Required*: No
*Type*: [RuleConditionProperties](aws-properties-entityresolution-matchingworkflow-ruleconditionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
