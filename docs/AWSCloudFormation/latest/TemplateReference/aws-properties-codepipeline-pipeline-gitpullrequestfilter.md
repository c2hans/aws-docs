---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gitpullrequestfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline GitPullRequestFilter
<a name="aws-properties-codepipeline-pipeline-gitpullrequestfilter"></a>

The event criteria for the pull request trigger configuration, such as the lists of branches or file paths to include and exclude.

The following are valid values for the events for this filter:
+ CLOSED
+ OPEN
+ UPDATED

## Syntax
<a name="aws-properties-codepipeline-pipeline-gitpullrequestfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-gitpullrequestfilter-syntax.json"></a>

```
{
  "[Branches](#cfn-codepipeline-pipeline-gitpullrequestfilter-branches)" : {{GitBranchFilterCriteria}},
  "[Events](#cfn-codepipeline-pipeline-gitpullrequestfilter-events)" : {{[ String, ... ]}},
  "[FilePaths](#cfn-codepipeline-pipeline-gitpullrequestfilter-filepaths)" : {{GitFilePathFilterCriteria}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-gitpullrequestfilter-syntax.yaml"></a>

```
  [Branches](#cfn-codepipeline-pipeline-gitpullrequestfilter-branches): {{
    GitBranchFilterCriteria}}
  [Events](#cfn-codepipeline-pipeline-gitpullrequestfilter-events): {{
    - String}}
  [FilePaths](#cfn-codepipeline-pipeline-gitpullrequestfilter-filepaths): {{
    GitFilePathFilterCriteria}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-gitpullrequestfilter-properties"></a>

`Branches`  <a name="cfn-codepipeline-pipeline-gitpullrequestfilter-branches"></a>
The field that specifies to filter on branches for the pull request trigger configuration.
*Required*: No
*Type*: [GitBranchFilterCriteria](aws-properties-codepipeline-pipeline-gitbranchfiltercriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Events`  <a name="cfn-codepipeline-pipeline-gitpullrequestfilter-events"></a>
The field that specifies which pull request events to filter on (OPEN, UPDATED, CLOSED) for the trigger configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilePaths`  <a name="cfn-codepipeline-pipeline-gitpullrequestfilter-filepaths"></a>
The field that specifies to filter on file paths for the pull request trigger configuration.
*Required*: No
*Type*: [GitFilePathFilterCriteria](aws-properties-codepipeline-pipeline-gitfilepathfiltercriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
