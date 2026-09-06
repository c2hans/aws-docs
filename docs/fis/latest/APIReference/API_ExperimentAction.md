---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentAction.html
---

# ExperimentAction
<a name="API_ExperimentAction"></a>

Describes the action for an experiment.

## Contents
<a name="API_ExperimentAction_Contents"></a>

 ** actionId **   <a name="fis-Type-ExperimentAction-actionId"></a>
The ID of the action.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

 ** description **   <a name="fis-Type-ExperimentAction-description"></a>
The description for the action.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** endTime **   <a name="fis-Type-ExperimentAction-endTime"></a>
The time that the action ended.
Type: Timestamp
Required: No

 ** parameters **   <a name="fis-Type-ExperimentAction-parameters"></a>
The parameters for the action.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `[\S]+`
Required: No

 ** startAfter **   <a name="fis-Type-ExperimentAction-startAfter"></a>
The name of the action that must be completed before this action starts.
Type: Array of strings
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** startTime **   <a name="fis-Type-ExperimentAction-startTime"></a>
The time that the action started.
Type: Timestamp
Required: No

 ** state **   <a name="fis-Type-ExperimentAction-state"></a>
The state of the action.
Type: [ExperimentActionState](API_ExperimentActionState.md) object
Required: No

 ** targets **   <a name="fis-Type-ExperimentAction-targets"></a>
The targets for the action.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Maximum length of 64.
Value Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentAction)
