---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateActionInput.html
---

# CreateExperimentTemplateActionInput
<a name="API_CreateExperimentTemplateActionInput"></a>

Specifies an action for an experiment template.

For more information, see [Actions](https://docs.aws.amazon.com/fis/latest/userguide/actions.html) in the * AWS Fault Injection Service User Guide*.

## Contents
<a name="API_CreateExperimentTemplateActionInput_Contents"></a>

 ** actionId **   <a name="fis-Type-CreateExperimentTemplateActionInput-actionId"></a>
The ID of the action. The format of the action ID is: aws:*service-name*:*action-type*.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: Yes

 ** description **   <a name="fis-Type-CreateExperimentTemplateActionInput-description"></a>
A description for the action.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** parameters **   <a name="fis-Type-CreateExperimentTemplateActionInput-parameters"></a>
The parameters for the action, if applicable.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `[\S]+`
Required: No

 ** startAfter **   <a name="fis-Type-CreateExperimentTemplateActionInput-startAfter"></a>
The name of the action that must be completed before the current action starts. Omit this parameter to run the action at the start of the experiment.
Type: Array of strings
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** targets **   <a name="fis-Type-CreateExperimentTemplateActionInput-targets"></a>
The targets for the action.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Maximum length of 64.
Value Pattern: `[\S]+`
Required: No

## See Also
<a name="API_CreateExperimentTemplateActionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/CreateExperimentTemplateActionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/CreateExperimentTemplateActionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/CreateExperimentTemplateActionInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
