---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-projectsourceversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project ProjectSourceVersion
<a name="aws-properties-codebuild-project-projectsourceversion"></a>

 A source identifier and its corresponding version.

## Syntax
<a name="aws-properties-codebuild-project-projectsourceversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-projectsourceversion-syntax.json"></a>

```
{
  "[SourceIdentifier](#cfn-codebuild-project-projectsourceversion-sourceidentifier)" : {{String}},
  "[SourceVersion](#cfn-codebuild-project-projectsourceversion-sourceversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-project-projectsourceversion-syntax.yaml"></a>

```
  [SourceIdentifier](#cfn-codebuild-project-projectsourceversion-sourceidentifier): {{String}}
  [SourceVersion](#cfn-codebuild-project-projectsourceversion-sourceversion): {{String}}
```

## Properties
<a name="aws-properties-codebuild-project-projectsourceversion-properties"></a>

`SourceIdentifier`  <a name="cfn-codebuild-project-projectsourceversion-sourceidentifier"></a>
An identifier for a source in the build project. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceVersion`  <a name="cfn-codebuild-project-projectsourceversion-sourceversion"></a>
The source version for the corresponding source identifier. If specified, must be one of:
+ For CodeCommit: the commit ID, branch, or Git tag to use.
+ For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example, `pr/25`). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
+ For GitLab: the commit ID, branch, or Git tag to use.
+ For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
+ For Amazon S3: the version ID of the object that represents the build input ZIP file to use.
 For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the *AWS CodeBuild User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
