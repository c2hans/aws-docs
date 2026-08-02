---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionSummary.html
---

# ActionSummary
<a name="API_ActionSummary"></a>

Summary information for an Amazon Q Business plugin action.

## Contents
<a name="API_ActionSummary_Contents"></a>

 ** actionIdentifier **   <a name="qbusiness-Type-ActionSummary-actionIdentifier"></a>
The identifier of an Amazon Q Business plugin action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** description **   <a name="qbusiness-Type-ActionSummary-description"></a>
The description of an Amazon Q Business plugin action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** displayName **   <a name="qbusiness-Type-ActionSummary-displayName"></a>
The display name assigned by Amazon Q Business to a plugin action. You can't modify this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** instructionExample **   <a name="qbusiness-Type-ActionSummary-instructionExample"></a>
An Amazon Q Business suggested prompt and end user can use to invoke a plugin action. This value can be modified and sent as input to initiate an action. For example:
+ Create a Jira task
+ Create a chat assistant task to find the root cause of a specific incident
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ActionSummary)
