---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_QuantumTaskSummary.html
---

# QuantumTaskSummary
<a name="API_QuantumTaskSummary"></a>

Includes information about a quantum task.

## Contents
<a name="API_QuantumTaskSummary_Contents"></a>

 ** createdAt **   <a name="braket-Type-QuantumTaskSummary-createdAt"></a>
The time at which the quantum task was created.
Type: Timestamp
Required: Yes

 ** deviceArn **   <a name="braket-Type-QuantumTaskSummary-deviceArn"></a>
The ARN of the device the quantum task ran on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** outputS3Bucket **   <a name="braket-Type-QuantumTaskSummary-outputS3Bucket"></a>
The S3 bucket where the quantum task result file is stored.
Type: String
Required: Yes

 ** outputS3Directory **   <a name="braket-Type-QuantumTaskSummary-outputS3Directory"></a>
The folder in the S3 bucket where the quantum task result file is stored.
Type: String
Required: Yes

 ** quantumTaskArn **   <a name="braket-Type-QuantumTaskSummary-quantumTaskArn"></a>
The ARN of the quantum task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** shots **   <a name="braket-Type-QuantumTaskSummary-shots"></a>
The shots used for the quantum task.
Type: Long
Required: Yes

 ** status **   <a name="braket-Type-QuantumTaskSummary-status"></a>
The status of the quantum task.
Type: String
Valid Values: `CREATED | QUEUED | RUNNING | COMPLETED | FAILED | CANCELLING | CANCELLED`
Required: Yes

 ** endedAt **   <a name="braket-Type-QuantumTaskSummary-endedAt"></a>
The time at which the quantum task finished.
Type: Timestamp
Required: No

 ** tags **   <a name="braket-Type-QuantumTaskSummary-tags"></a>
Displays the key, value pairs of tags associated with this quantum task.
Type: String to string map
Required: No

## See Also
<a name="API_QuantumTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/QuantumTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/QuantumTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/QuantumTaskSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
