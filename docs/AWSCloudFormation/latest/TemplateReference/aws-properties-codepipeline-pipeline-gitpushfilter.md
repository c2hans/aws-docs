---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gitpushfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline GitPushFilter
<a name="aws-properties-codepipeline-pipeline-gitpushfilter"></a>

The event criteria that specify when a specified repository event will start the pipeline for the specified trigger configuration, such as the lists of Git tags to include and exclude.

## Syntax
<a name="aws-properties-codepipeline-pipeline-gitpushfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-gitpushfilter-syntax.json"></a>

```
{
  "[Branches](#cfn-codepipeline-pipeline-gitpushfilter-branches)" : {{GitBranchFilterCriteria}},
  "[FilePaths](#cfn-codepipeline-pipeline-gitpushfilter-filepaths)" : {{GitFilePathFilterCriteria}},
  "[Tags](#cfn-codepipeline-pipeline-gitpushfilter-tags)" : {{GitTagFilterCriteria}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-gitpushfilter-syntax.yaml"></a>

```
  [Branches](#cfn-codepipeline-pipeline-gitpushfilter-branches): {{
    GitBranchFilterCriteria}}
  [FilePaths](#cfn-codepipeline-pipeline-gitpushfilter-filepaths): {{
    GitFilePathFilterCriteria}}
  [Tags](#cfn-codepipeline-pipeline-gitpushfilter-tags): {{
    GitTagFilterCriteria}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-gitpushfilter-properties"></a>

`Branches`  <a name="cfn-codepipeline-pipeline-gitpushfilter-branches"></a>
The field that specifies to filter on branches for the push trigger configuration.
*Required*: No
*Type*: [GitBranchFilterCriteria](aws-properties-codepipeline-pipeline-gitbranchfiltercriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilePaths`  <a name="cfn-codepipeline-pipeline-gitpushfilter-filepaths"></a>
The field that specifies to filter on file paths for the push trigger configuration.
*Required*: No
*Type*: [GitFilePathFilterCriteria](aws-properties-codepipeline-pipeline-gitfilepathfiltercriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-codepipeline-pipeline-gitpushfilter-tags"></a>
The field that contains the details for the Git tags trigger configuration.
*Required*: No
*Type*: [GitTagFilterCriteria](aws-properties-codepipeline-pipeline-gittagfiltercriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
