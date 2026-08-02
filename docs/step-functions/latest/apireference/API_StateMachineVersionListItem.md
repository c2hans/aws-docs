---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateMachineVersionListItem.html
---

# StateMachineVersionListItem
<a name="API_StateMachineVersionListItem"></a>

Contains details about a specific state machine version.

## Contents
<a name="API_StateMachineVersionListItem_Contents"></a>

 ** creationDate **   <a name="StepFunctions-Type-StateMachineVersionListItem-creationDate"></a>
The creation date of a state machine version.
Type: Timestamp
Required: Yes

 ** stateMachineVersionArn **   <a name="StepFunctions-Type-StateMachineVersionListItem-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) that identifies a state machine version. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, `stateMachineARN:1`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_StateMachineVersionListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/StateMachineVersionListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/StateMachineVersionListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/StateMachineVersionListItem)
