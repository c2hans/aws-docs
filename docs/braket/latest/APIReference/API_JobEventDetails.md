---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_JobEventDetails.html
---

# JobEventDetails
<a name="API_JobEventDetails"></a>

Details about the type and time events that occurred related to the Amazon Braket hybrid job.

## Contents
<a name="API_JobEventDetails_Contents"></a>

 ** eventType **   <a name="braket-Type-JobEventDetails-eventType"></a>
The type of event that occurred related to the Amazon Braket hybrid job.
Type: String
Valid Values: `WAITING_FOR_PRIORITY | QUEUED_FOR_EXECUTION | STARTING_INSTANCE | DOWNLOADING_DATA | RUNNING | DEPRIORITIZED_DUE_TO_INACTIVITY | UPLOADING_RESULTS | COMPLETED | FAILED | MAX_RUNTIME_EXCEEDED | CANCELLED`
Required: No

 ** message **   <a name="braket-Type-JobEventDetails-message"></a>
A message describing the event that occurred related to the Amazon Braket hybrid job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2500.
Required: No

 ** timeOfEvent **   <a name="braket-Type-JobEventDetails-timeOfEvent"></a>
The time of the event that occurred related to the Amazon Braket hybrid job.
Type: Timestamp
Required: No

## See Also
<a name="API_JobEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/JobEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/JobEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/JobEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
