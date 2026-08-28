---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-coderepository.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service CodeRepository
<a name="aws-properties-apprunner-service-coderepository"></a>

Describes a source code repository.

## Syntax
<a name="aws-properties-apprunner-service-coderepository-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-coderepository-syntax.json"></a>

```
{
  "[CodeConfiguration](#cfn-apprunner-service-coderepository-codeconfiguration)" : {{CodeConfiguration}},
  "[RepositoryUrl](#cfn-apprunner-service-coderepository-repositoryurl)" : {{String}},
  "[SourceCodeVersion](#cfn-apprunner-service-coderepository-sourcecodeversion)" : {{SourceCodeVersion}},
  "[SourceDirectory](#cfn-apprunner-service-coderepository-sourcedirectory)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-coderepository-syntax.yaml"></a>

```
  [CodeConfiguration](#cfn-apprunner-service-coderepository-codeconfiguration): {{
    CodeConfiguration}}
  [RepositoryUrl](#cfn-apprunner-service-coderepository-repositoryurl): {{String}}
  [SourceCodeVersion](#cfn-apprunner-service-coderepository-sourcecodeversion): {{
    SourceCodeVersion}}
  [SourceDirectory](#cfn-apprunner-service-coderepository-sourcedirectory): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-coderepository-properties"></a>

`CodeConfiguration`  <a name="cfn-apprunner-service-coderepository-codeconfiguration"></a>
Configuration for building and running the service from a source code repository.
`CodeConfiguration` is required only for `CreateService` request.
*Required*: No
*Type*: [CodeConfiguration](aws-properties-apprunner-service-codeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepositoryUrl`  <a name="cfn-apprunner-service-coderepository-repositoryurl"></a>
The location of the repository that contains the source code.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceCodeVersion`  <a name="cfn-apprunner-service-coderepository-sourcecodeversion"></a>
The version that should be used within the source code repository.
*Required*: Yes
*Type*: [SourceCodeVersion](aws-properties-apprunner-service-sourcecodeversion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceDirectory`  <a name="cfn-apprunner-service-coderepository-sourcedirectory"></a>
The path of the directory that stores source code and configuration files. The build and start commands also execute from here. The path is absolute from root and, if not specified, defaults to the repository root.
*Required*: No
*Type*: String
*Pattern*: `[^\x00]+`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
