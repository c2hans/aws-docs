---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-workflow-definitionrepository.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Workflow DefinitionRepository
<a name="aws-properties-omics-workflow-definitionrepository"></a>

Contains information about a source code repository that hosts the workflow definition files.

## Syntax
<a name="aws-properties-omics-workflow-definitionrepository-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-workflow-definitionrepository-syntax.json"></a>

```
{
  "[connectionArn](#cfn-omics-workflow-definitionrepository-connectionarn)" : {{String}},
  "[excludeFilePatterns](#cfn-omics-workflow-definitionrepository-excludefilepatterns)" : {{[ String, ... ]}},
  "[fullRepositoryId](#cfn-omics-workflow-definitionrepository-fullrepositoryid)" : {{String}},
  "[sourceReference](#cfn-omics-workflow-definitionrepository-sourcereference)" : {{SourceReference}}
}
```

### YAML
<a name="aws-properties-omics-workflow-definitionrepository-syntax.yaml"></a>

```
  [connectionArn](#cfn-omics-workflow-definitionrepository-connectionarn): {{String}}
  [excludeFilePatterns](#cfn-omics-workflow-definitionrepository-excludefilepatterns): {{
    - String}}
  [fullRepositoryId](#cfn-omics-workflow-definitionrepository-fullrepositoryid): {{String}}
  [sourceReference](#cfn-omics-workflow-definitionrepository-sourcereference): {{
    SourceReference}}
```

## Properties
<a name="aws-properties-omics-workflow-definitionrepository-properties"></a>

`connectionArn`  <a name="cfn-omics-workflow-definitionrepository-connectionarn"></a>
The Amazon Resource Name (ARN) of the connection to the source code repository.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[\\w]+)*:.+:.+:[0-9]{12}:.+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`excludeFilePatterns`  <a name="cfn-omics-workflow-definitionrepository-excludefilepatterns"></a>
A list of file patterns to exclude when retrieving the workflow definition from the repository.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`fullRepositoryId`  <a name="cfn-omics-workflow-definitionrepository-fullrepositoryid"></a>
The full repository identifier, including the repository owner and name. For example, 'repository-owner/repository-name'.
*Required*: No
*Type*: String
*Pattern*: `.+/.+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`sourceReference`  <a name="cfn-omics-workflow-definitionrepository-sourcereference"></a>
The source reference for the repository, such as a branch name, tag, or commit ID.
*Required*: No
*Type*: [SourceReference](aws-properties-omics-workflow-sourcereference.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
