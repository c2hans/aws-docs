---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_QuotaSharePolicy.html
---

# QuotaSharePolicy
<a name="API_QuotaSharePolicy"></a>

The quota share scheduling policy details for a job queue.

## Contents
<a name="API_QuotaSharePolicy_Contents"></a>

 ** idleResourceAssignmentStrategy **   <a name="Batch-Type-QuotaSharePolicy-idleResourceAssignmentStrategy"></a>
The strategy that determines how idle resources are assigned to quota shares that are borrowing capacity. Currently, only `FIFO` is supported.
Type: String
Valid Values: `FIFO`
Required: Yes

## See Also
<a name="API_QuotaSharePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QuotaSharePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QuotaSharePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QuotaSharePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
