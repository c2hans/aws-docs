---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-sourcesegments.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment SourceSegments
<a name="aws-properties-pinpoint-segment-sourcesegments"></a>

Specifies the base segment to build the segment on. A base segment, also called a *source segment*, defines the initial population of endpoints for a segment. When you add dimensions to the segment, Amazon Pinpoint filters the base segment by using the dimensions that you specify.

You can specify more than one dimensional segment or only one imported segment. If you specify an imported segment, the segment size estimate that displays on the Amazon Pinpoint console indicates the size of the imported segment without any filters applied to it.

## Syntax
<a name="aws-properties-pinpoint-segment-sourcesegments-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-sourcesegments-syntax.json"></a>

```
{
  "[Id](#cfn-pinpoint-segment-sourcesegments-id)" : {{String}},
  "[Version](#cfn-pinpoint-segment-sourcesegments-version)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-sourcesegments-syntax.yaml"></a>

```
  [Id](#cfn-pinpoint-segment-sourcesegments-id): {{String}}
  [Version](#cfn-pinpoint-segment-sourcesegments-version): {{Integer}}
```

## Properties
<a name="aws-properties-pinpoint-segment-sourcesegments-properties"></a>

`Id`  <a name="cfn-pinpoint-segment-sourcesegments-id"></a>
The unique identifier for the source segment.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-pinpoint-segment-sourcesegments-version"></a>
The version number of the source segment.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
