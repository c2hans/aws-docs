---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostAllocationTagBackfillRequest.html
---

# CostAllocationTagBackfillRequest
<a name="API_CostAllocationTagBackfillRequest"></a>

 The cost allocation tag backfill request structure that contains metadata and details of a certain backfill.

## Contents
<a name="API_CostAllocationTagBackfillRequest_Contents"></a>

 ** BackfillFrom **   <a name="awscostmanagement-Type-CostAllocationTagBackfillRequest-BackfillFrom"></a>
 The date the backfill starts from.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** BackfillStatus **   <a name="awscostmanagement-Type-CostAllocationTagBackfillRequest-BackfillStatus"></a>
 The status of the cost allocation tag backfill request.
Type: String
Valid Values: `SUCCEEDED | PROCESSING | FAILED`
Required: No

 ** CompletedAt **   <a name="awscostmanagement-Type-CostAllocationTagBackfillRequest-CompletedAt"></a>
 The backfill completion time.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** LastUpdatedAt **   <a name="awscostmanagement-Type-CostAllocationTagBackfillRequest-LastUpdatedAt"></a>
 The time when the backfill status was last updated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** RequestedAt **   <a name="awscostmanagement-Type-CostAllocationTagBackfillRequest-RequestedAt"></a>
 The time when the backfill was requested.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

## See Also
<a name="API_CostAllocationTagBackfillRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostAllocationTagBackfillRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostAllocationTagBackfillRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostAllocationTagBackfillRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
