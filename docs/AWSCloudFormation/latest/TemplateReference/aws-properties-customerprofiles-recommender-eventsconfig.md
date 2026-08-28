---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-recommender-eventsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Recommender EventsConfig
<a name="aws-properties-customerprofiles-recommender-eventsconfig"></a>

<a name="aws-properties-customerprofiles-recommender-eventsconfig-description"></a>The `EventsConfig` property type specifies Property description not available. for an [AWS::CustomerProfiles::Recommender](aws-resource-customerprofiles-recommender.md).

## Syntax
<a name="aws-properties-customerprofiles-recommender-eventsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-recommender-eventsconfig-syntax.json"></a>

```
{
  "[EventParametersList](#cfn-customerprofiles-recommender-eventsconfig-eventparameterslist)" : {{[ EventParameters, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-recommender-eventsconfig-syntax.yaml"></a>

```
  [EventParametersList](#cfn-customerprofiles-recommender-eventsconfig-eventparameterslist): {{
    - EventParameters}}
```

## Properties
<a name="aws-properties-customerprofiles-recommender-eventsconfig-properties"></a>

`EventParametersList`  <a name="cfn-customerprofiles-recommender-eventsconfig-eventparameterslist"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [EventParameters](aws-properties-customerprofiles-recommender-eventparameters.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
