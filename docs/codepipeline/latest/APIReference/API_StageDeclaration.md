---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StageDeclaration.html
---

# StageDeclaration
<a name="API_StageDeclaration"></a>

Represents information about a stage and its definition.

## Contents
<a name="API_StageDeclaration_Contents"></a>

 ** actions **   <a name="CodePipeline-Type-StageDeclaration-actions"></a>
The actions included in a stage.
Type: Array of [ActionDeclaration](API_ActionDeclaration.md) objects
Required: Yes

 ** name **   <a name="CodePipeline-Type-StageDeclaration-name"></a>
The name of the stage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9.@\-_]+`
Required: Yes

 ** beforeEntry **   <a name="CodePipeline-Type-StageDeclaration-beforeEntry"></a>
The method to use when a stage allows entry. For example, configuring this field for conditions will allow entry to the stage when the conditions are met.
Type: [BeforeEntryConditions](API_BeforeEntryConditions.md) object
Required: No

 ** blockers **   <a name="CodePipeline-Type-StageDeclaration-blockers"></a>
Reserved for future use.
Type: Array of [BlockerDeclaration](API_BlockerDeclaration.md) objects
Required: No

 ** onFailure **   <a name="CodePipeline-Type-StageDeclaration-onFailure"></a>
The method to use when a stage has not completed successfully. For example, configuring this field for rollback will roll back a failed stage automatically to the last successful pipeline execution in the stage.
Type: [FailureConditions](API_FailureConditions.md) object
Required: No

 ** onSuccess **   <a name="CodePipeline-Type-StageDeclaration-onSuccess"></a>
The method to use when a stage has succeeded. For example, configuring this field for conditions will allow the stage to succeed when the conditions are met.
Type: [SuccessConditions](API_SuccessConditions.md) object
Required: No

## See Also
<a name="API_StageDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StageDeclaration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StageDeclaration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StageDeclaration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
