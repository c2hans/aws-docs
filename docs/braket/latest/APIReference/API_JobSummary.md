---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_JobSummary.html
---

# JobSummary
<a name="API_JobSummary"></a>

Provides summary information about an Amazon Braket hybrid job.

## Contents
<a name="API_JobSummary_Contents"></a>

 ** createdAt **   <a name="braket-Type-JobSummary-createdAt"></a>
The time at which the Amazon Braket hybrid job was created.
Type: Timestamp
Required: Yes

 ** device **   <a name="braket-Type-JobSummary-device"></a>
The primary device used by an Amazon Braket hybrid job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** jobArn **   <a name="braket-Type-JobSummary-jobArn"></a>
The ARN of the Amazon Braket hybrid job.
Type: String
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:job/.*`
Required: Yes

 ** jobName **   <a name="braket-Type-JobSummary-jobName"></a>
The name of the Amazon Braket hybrid job.
Type: String
Required: Yes

 ** status **   <a name="braket-Type-JobSummary-status"></a>
The status of the Amazon Braket hybrid job.
Type: String
Valid Values: `QUEUED | RUNNING | COMPLETED | FAILED | CANCELLING | CANCELLED`
Required: Yes

 ** endedAt **   <a name="braket-Type-JobSummary-endedAt"></a>
The time at which the Amazon Braket hybrid job ended.
Type: Timestamp
Required: No

 ** startedAt **   <a name="braket-Type-JobSummary-startedAt"></a>
The time at which the Amazon Braket hybrid job was started.
Type: Timestamp
Required: No

 ** tags **   <a name="braket-Type-JobSummary-tags"></a>
Displays the key, value pairs of tags associated with this hybrid job.
Type: String to string map
Required: No

## See Also
<a name="API_JobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/JobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/JobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/JobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
