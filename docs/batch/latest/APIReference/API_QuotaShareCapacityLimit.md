---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_QuotaShareCapacityLimit.html
---

# QuotaShareCapacityLimit
<a name="API_QuotaShareCapacityLimit"></a>

Defines the capacity limit for a quota share, or the type and maximum quantity of a particular resource that can be allocated to jobs in the quota share without borrowing.

## Contents
<a name="API_QuotaShareCapacityLimit_Contents"></a>

 ** capacityUnit **   <a name="Batch-Type-QuotaShareCapacityLimit-capacityUnit"></a>
The unit of compute capacity for the capacityLimit. For example, `ml.m5.large`.
Type: String
Required: Yes

 ** maxCapacity **   <a name="Batch-Type-QuotaShareCapacityLimit-maxCapacity"></a>
The maximum capacity available for the quota share. This value represents the maximum quantity of a resource that can be allocated to jobs in the quota share without borrowing.
Type: Integer
Required: Yes

## See Also
<a name="API_QuotaShareCapacityLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QuotaShareCapacityLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QuotaShareCapacityLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QuotaShareCapacityLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
