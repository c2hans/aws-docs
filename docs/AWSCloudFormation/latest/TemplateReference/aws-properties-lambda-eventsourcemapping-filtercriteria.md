---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-filtercriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping FilterCriteria
<a name="aws-properties-lambda-eventsourcemapping-filtercriteria"></a>

 An object that contains the filters for an event source.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-filtercriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-filtercriteria-syntax.json"></a>

```
{
  "[Filters](#cfn-lambda-eventsourcemapping-filtercriteria-filters)" : {{[ Filter, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-filtercriteria-syntax.yaml"></a>

```
  [Filters](#cfn-lambda-eventsourcemapping-filtercriteria-filters): {{
    - Filter}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-filtercriteria-properties"></a>

`Filters`  <a name="cfn-lambda-eventsourcemapping-filtercriteria-filters"></a>
 A list of filters.
*Required*: No
*Type*: Array of [Filter](aws-properties-lambda-eventsourcemapping-filter.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
