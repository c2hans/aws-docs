---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_ServiceJobAttemptDetail.html
---

# ServiceJobAttemptDetail
<a name="API_ServiceJobAttemptDetail"></a>

Detailed information about an attempt to run a service job.

## Contents
<a name="API_ServiceJobAttemptDetail_Contents"></a>

 ** serviceResourceId **   <a name="Batch-Type-ServiceJobAttemptDetail-serviceResourceId"></a>
The service resource identifier associated with the service job attempt.
Type: [ServiceResourceId](API_ServiceResourceId.md) object
Required: No

 ** startedAt **   <a name="Batch-Type-ServiceJobAttemptDetail-startedAt"></a>
The Unix timestamp (in milliseconds) for when the service job attempt was started.
Type: Long
Required: No

 ** statusReason **   <a name="Batch-Type-ServiceJobAttemptDetail-statusReason"></a>
A string that provides additional details for the current status of the service job attempt.
Type: String
Required: No

 ** stoppedAt **   <a name="Batch-Type-ServiceJobAttemptDetail-stoppedAt"></a>
The Unix timestamp (in milliseconds) for when the service job attempt stopped running.
Type: Long
Required: No

## See Also
<a name="API_ServiceJobAttemptDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobAttemptDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobAttemptDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobAttemptDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
