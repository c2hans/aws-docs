---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateAction.html
---

# ExperimentTemplateAction
<a name="API_ExperimentTemplateAction"></a>

Describes an action for an experiment template.

## Contents
<a name="API_ExperimentTemplateAction_Contents"></a>

 ** actionId **   <a name="fis-Type-ExperimentTemplateAction-actionId"></a>
The ID of the action.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

 ** description **   <a name="fis-Type-ExperimentTemplateAction-description"></a>
A description for the action.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** parameters **   <a name="fis-Type-ExperimentTemplateAction-parameters"></a>
The parameters for the action.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `[\S]+`
Required: No

 ** startAfter **   <a name="fis-Type-ExperimentTemplateAction-startAfter"></a>
The name of the action that must be completed before the current action starts.
Type: Array of strings
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** targets **   <a name="fis-Type-ExperimentTemplateAction-targets"></a>
The targets for the action.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Maximum length of 64.
Value Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentTemplateAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTemplateAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTemplateAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTemplateAction)
