---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_LatestServiceJobAttempt.html
---

# LatestServiceJobAttempt
<a name="API_LatestServiceJobAttempt"></a>

Information about the latest attempt of a service job. A Service job can transition from `SCHEDULED` back to `RUNNABLE` state when they encounter capacity constraints.

## Contents
<a name="API_LatestServiceJobAttempt_Contents"></a>

 ** serviceResourceId **   <a name="Batch-Type-LatestServiceJobAttempt-serviceResourceId"></a>
The service resource identifier associated with the service job attempt.
Type: [ServiceResourceId](API_ServiceResourceId.md) object
Required: No

## See Also
<a name="API_LatestServiceJobAttempt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/LatestServiceJobAttempt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/LatestServiceJobAttempt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/LatestServiceJobAttempt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
