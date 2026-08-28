---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-pipelinetriggerdeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline PipelineTriggerDeclaration
<a name="aws-properties-codepipeline-pipeline-pipelinetriggerdeclaration"></a>

Represents information about the specified trigger configuration, such as the filter criteria and the source stage for the action that contains the trigger.

**Note**
This is only supported for the `CodeStarSourceConnection` action type.

**Note**
When a trigger configuration is specified, default change detection for repository and branch commits is disabled.

## Syntax
<a name="aws-properties-codepipeline-pipeline-pipelinetriggerdeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-pipelinetriggerdeclaration-syntax.json"></a>

```
{
  "[GitConfiguration](#cfn-codepipeline-pipeline-pipelinetriggerdeclaration-gitconfiguration)" : {{GitConfiguration}},
  "[ProviderType](#cfn-codepipeline-pipeline-pipelinetriggerdeclaration-providertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-pipelinetriggerdeclaration-syntax.yaml"></a>

```
  [GitConfiguration](#cfn-codepipeline-pipeline-pipelinetriggerdeclaration-gitconfiguration): {{
    GitConfiguration}}
  [ProviderType](#cfn-codepipeline-pipeline-pipelinetriggerdeclaration-providertype): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-pipelinetriggerdeclaration-properties"></a>

`GitConfiguration`  <a name="cfn-codepipeline-pipeline-pipelinetriggerdeclaration-gitconfiguration"></a>
Provides the filter criteria and the source stage for the repository event that starts the pipeline, such as Git tags.
*Required*: No
*Type*: [GitConfiguration](aws-properties-codepipeline-pipeline-gitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderType`  <a name="cfn-codepipeline-pipeline-pipelinetriggerdeclaration-providertype"></a>
The source provider for the event, such as connections configured for a repository with Git tags, for the specified trigger configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `CodeStarSourceConnection`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
