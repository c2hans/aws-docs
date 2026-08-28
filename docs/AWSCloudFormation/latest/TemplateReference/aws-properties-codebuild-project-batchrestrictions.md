---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-batchrestrictions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project BatchRestrictions
<a name="aws-properties-codebuild-project-batchrestrictions"></a>

Specifies restrictions for the batch build.

## Syntax
<a name="aws-properties-codebuild-project-batchrestrictions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-batchrestrictions-syntax.json"></a>

```
{
  "[ComputeTypesAllowed](#cfn-codebuild-project-batchrestrictions-computetypesallowed)" : {{[ String, ... ]}},
  "[MaximumBuildsAllowed](#cfn-codebuild-project-batchrestrictions-maximumbuildsallowed)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-codebuild-project-batchrestrictions-syntax.yaml"></a>

```
  [ComputeTypesAllowed](#cfn-codebuild-project-batchrestrictions-computetypesallowed): {{
    - String}}
  [MaximumBuildsAllowed](#cfn-codebuild-project-batchrestrictions-maximumbuildsallowed): {{Integer}}
```

## Properties
<a name="aws-properties-codebuild-project-batchrestrictions-properties"></a>

`ComputeTypesAllowed`  <a name="cfn-codebuild-project-batchrestrictions-computetypesallowed"></a>
An array of strings that specify the compute types that are allowed for the batch build. See [Build environment compute types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) in the *AWS CodeBuild User Guide* for these values.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBuildsAllowed`  <a name="cfn-codebuild-project-batchrestrictions-maximumbuildsallowed"></a>
Specifies the maximum number of builds allowed.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
