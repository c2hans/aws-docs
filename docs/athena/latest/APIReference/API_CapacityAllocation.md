---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CapacityAllocation.html
---

# CapacityAllocation
<a name="API_CapacityAllocation"></a>

Contains the submission time of a single allocation request for a capacity reservation and the most recent status of the attempted allocation.

## Contents
<a name="API_CapacityAllocation_Contents"></a>

 ** RequestTime **   <a name="athena-Type-CapacityAllocation-RequestTime"></a>
The time when the capacity allocation was requested.
Type: Timestamp
Required: Yes

 ** Status **   <a name="athena-Type-CapacityAllocation-Status"></a>
The status of the capacity allocation.
Type: String
Valid Values: `PENDING | SUCCEEDED | FAILED`
Required: Yes

 ** RequestCompletionTime **   <a name="athena-Type-CapacityAllocation-RequestCompletionTime"></a>
The time when the capacity allocation request was completed.
Type: Timestamp
Required: No

 ** StatusMessage **   <a name="athena-Type-CapacityAllocation-StatusMessage"></a>
The status message of the capacity allocation.
Type: String
Required: No

## See Also
<a name="API_CapacityAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CapacityAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CapacityAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CapacityAllocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
