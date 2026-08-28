---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_FairshareUtilizationDetail.html
---

# FairshareUtilizationDetail
<a name="API_FairshareUtilizationDetail"></a>

The fairshare utilization for a job queue, including the number of active shares and top capacity utilization.

## Contents
<a name="API_FairshareUtilizationDetail_Contents"></a>

 ** activeShareCount **   <a name="Batch-Type-FairshareUtilizationDetail-activeShareCount"></a>
The total number of active shares in the fairshare scheduling job queue that are currently utilizing capacity.
Type: Long
Required: No

 ** topCapacityUtilization **   <a name="Batch-Type-FairshareUtilizationDetail-topCapacityUtilization"></a>
A list of the top 20 shares with the highest capacity utilization, ordered by usage amount.
Type: Array of [FairshareCapacityUtilization](API_FairshareCapacityUtilization.md) objects
Required: No

## See Also
<a name="API_FairshareUtilizationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FairshareUtilizationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FairshareUtilizationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FairshareUtilizationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
