---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StateTransition.html
---

# StateTransition
<a name="API_StateTransition"></a>

Information about the state transition of a supervisor.

## Contents
<a name="API_StateTransition_Contents"></a>

 ** State **   <a name="connect-Type-StateTransition-State"></a>
The state of the transition.
Type: String
Valid Values: `INITIAL | CONNECTED | DISCONNECTED | MISSED`
Required: No

 ** StateEndTimestamp **   <a name="connect-Type-StateTransition-StateEndTimestamp"></a>
The date and time when the state ended in UTC time.
Type: Timestamp
Required: No

 ** StateStartTimestamp **   <a name="connect-Type-StateTransition-StateStartTimestamp"></a>
The date and time when the state started in UTC time.
Type: Timestamp
Required: No

## See Also
<a name="API_StateTransition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StateTransition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StateTransition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StateTransition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
