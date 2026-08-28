---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityTimedOutEventDetails.html
---

# ActivityTimedOutEventDetails
<a name="API_ActivityTimedOutEventDetails"></a>

Contains details about an activity timeout that occurred during an execution.

## Contents
<a name="API_ActivityTimedOutEventDetails_Contents"></a>

 ** cause **   <a name="StepFunctions-Type-ActivityTimedOutEventDetails-cause"></a>
A more detailed explanation of the cause of the timeout.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** error **   <a name="StepFunctions-Type-ActivityTimedOutEventDetails-error"></a>
The error code of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ActivityTimedOutEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ActivityTimedOutEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ActivityTimedOutEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ActivityTimedOutEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
