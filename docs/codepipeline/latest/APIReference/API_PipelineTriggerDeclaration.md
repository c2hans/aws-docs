---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PipelineTriggerDeclaration.html
---

# PipelineTriggerDeclaration
<a name="API_PipelineTriggerDeclaration"></a>

Represents information about the specified trigger configuration, such as the filter criteria and the source stage for the action that contains the trigger.

**Note**
This is only supported for the `CodeStarSourceConnection` action type.

**Note**
When a trigger configuration is specified, default change detection for repository and branch commits is disabled.

## Contents
<a name="API_PipelineTriggerDeclaration_Contents"></a>

 ** gitConfiguration **   <a name="CodePipeline-Type-PipelineTriggerDeclaration-gitConfiguration"></a>
Provides the filter criteria and the source stage for the repository event that starts the pipeline, such as Git tags.
Type: [GitConfiguration](API_GitConfiguration.md) object
Required: Yes

 ** providerType **   <a name="CodePipeline-Type-PipelineTriggerDeclaration-providerType"></a>
The source provider for the event, such as connections configured for a repository with Git tags, for the specified trigger configuration.
Type: String
Valid Values: `CodeStarSourceConnection`
Required: Yes

## See Also
<a name="API_PipelineTriggerDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineTriggerDeclaration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineTriggerDeclaration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineTriggerDeclaration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
