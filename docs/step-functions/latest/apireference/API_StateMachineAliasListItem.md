---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateMachineAliasListItem.html
---

# StateMachineAliasListItem
<a name="API_StateMachineAliasListItem"></a>

Contains details about a specific state machine alias.

## Contents
<a name="API_StateMachineAliasListItem_Contents"></a>

 ** creationDate **   <a name="StepFunctions-Type-StateMachineAliasListItem-creationDate"></a>
The creation date of a state machine alias.
Type: Timestamp
Required: Yes

 ** stateMachineAliasArn **   <a name="StepFunctions-Type-StateMachineAliasListItem-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) that identifies a state machine alias. The alias ARN is a combination of state machine ARN and the alias name separated by a colon (:). For example, `stateMachineARN:PROD`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_StateMachineAliasListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/StateMachineAliasListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/StateMachineAliasListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/StateMachineAliasListItem)
