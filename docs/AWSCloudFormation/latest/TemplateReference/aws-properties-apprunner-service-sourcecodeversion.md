---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-sourcecodeversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service SourceCodeVersion
<a name="aws-properties-apprunner-service-sourcecodeversion"></a>

Identifies a version of code that AWS App Runner refers to within a source code repository.

## Syntax
<a name="aws-properties-apprunner-service-sourcecodeversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-sourcecodeversion-syntax.json"></a>

```
{
  "[Type](#cfn-apprunner-service-sourcecodeversion-type)" : {{String}},
  "[Value](#cfn-apprunner-service-sourcecodeversion-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-sourcecodeversion-syntax.yaml"></a>

```
  [Type](#cfn-apprunner-service-sourcecodeversion-type): {{String}}
  [Value](#cfn-apprunner-service-sourcecodeversion-value): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-sourcecodeversion-properties"></a>

`Type`  <a name="cfn-apprunner-service-sourcecodeversion-type"></a>
The type of version identifier.
For a git-based repository, branches represent versions.
*Required*: Yes
*Type*: String
*Allowed values*: `BRANCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-apprunner-service-sourcecodeversion-value"></a>
A source code version.
For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
