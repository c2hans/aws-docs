---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_RunCacheListItem.html
---

# RunCacheListItem
<a name="API_RunCacheListItem"></a>

List entry for one run cache.

## Contents
<a name="API_RunCacheListItem_Contents"></a>

 ** arn **   <a name="omics-Type-RunCacheListItem-arn"></a>
Unique resource identifier for the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`
Required: No

 ** cacheBehavior **   <a name="omics-Type-RunCacheListItem-cacheBehavior"></a>
Default cache behavior for the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CACHE_ON_FAILURE | CACHE_ALWAYS`
Required: No

 ** cacheS3Uri **   <a name="omics-Type-RunCacheListItem-cacheS3Uri"></a>
The S3 uri for the run cache data.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])(/(.{0,1024}))?`
Required: No

 ** creationTime **   <a name="omics-Type-RunCacheListItem-creationTime"></a>
The time that this run cache was created (an ISO 8601 formatted string).
Type: Timestamp
Required: No

 ** id **   <a name="omics-Type-RunCacheListItem-id"></a>
The identifier for this run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** name **   <a name="omics-Type-RunCacheListItem-name"></a>
The name of the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** status **   <a name="omics-Type-RunCacheListItem-status"></a>
The run cache status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `ACTIVE | DELETED | FAILED`
Required: No

## See Also
<a name="API_RunCacheListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/RunCacheListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/RunCacheListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/RunCacheListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
