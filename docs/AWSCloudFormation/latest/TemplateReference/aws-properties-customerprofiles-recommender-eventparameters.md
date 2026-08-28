---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-recommender-eventparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Recommender EventParameters
<a name="aws-properties-customerprofiles-recommender-eventparameters"></a>

<a name="aws-properties-customerprofiles-recommender-eventparameters-description"></a>The `EventParameters` property type specifies Property description not available. for an [AWS::CustomerProfiles::Recommender](aws-resource-customerprofiles-recommender.md).

## Syntax
<a name="aws-properties-customerprofiles-recommender-eventparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-recommender-eventparameters-syntax.json"></a>

```
{
  "[EventType](#cfn-customerprofiles-recommender-eventparameters-eventtype)" : {{String}},
  "[EventValueThreshold](#cfn-customerprofiles-recommender-eventparameters-eventvaluethreshold)" : {{Number}}
}
```

### YAML
<a name="aws-properties-customerprofiles-recommender-eventparameters-syntax.yaml"></a>

```
  [EventType](#cfn-customerprofiles-recommender-eventparameters-eventtype): {{String}}
  [EventValueThreshold](#cfn-customerprofiles-recommender-eventparameters-eventvaluethreshold): {{Number}}
```

## Properties
<a name="aws-properties-customerprofiles-recommender-eventparameters-properties"></a>

`EventType`  <a name="cfn-customerprofiles-recommender-eventparameters-eventtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventValueThreshold`  <a name="cfn-customerprofiles-recommender-eventparameters-eventvaluethreshold"></a>
Property description not available.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
