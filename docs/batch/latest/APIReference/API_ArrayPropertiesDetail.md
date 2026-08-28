---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_ArrayPropertiesDetail.html
---

# ArrayPropertiesDetail
<a name="API_ArrayPropertiesDetail"></a>

An object that represents the array properties of a job.

## Contents
<a name="API_ArrayPropertiesDetail_Contents"></a>

 ** index **   <a name="Batch-Type-ArrayPropertiesDetail-index"></a>
The job index within the array that's associated with this job. This parameter is returned for array job children.
Type: Integer
Required: No

 ** size **   <a name="Batch-Type-ArrayPropertiesDetail-size"></a>
The size of the array job. This parameter is returned for parent array jobs.
Type: Integer
Required: No

 ** statusSummary **   <a name="Batch-Type-ArrayPropertiesDetail-statusSummary"></a>
A summary of the number of array job children in each available job status. This parameter is returned for parent array jobs.
Type: String to integer map
Required: No

 ** statusSummaryLastUpdatedAt **   <a name="Batch-Type-ArrayPropertiesDetail-statusSummaryLastUpdatedAt"></a>
The Unix timestamp (in milliseconds) for when the `statusSummary` was last updated.
Type: Long
Required: No

## See Also
<a name="API_ArrayPropertiesDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ArrayPropertiesDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ArrayPropertiesDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ArrayPropertiesDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
