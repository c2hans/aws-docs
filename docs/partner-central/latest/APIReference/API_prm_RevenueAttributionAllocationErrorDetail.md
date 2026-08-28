---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_RevenueAttributionAllocationErrorDetail.html
---

# RevenueAttributionAllocationErrorDetail
<a name="API_prm_RevenueAttributionAllocationErrorDetail"></a>

Details of a validation error for a single revenue attribution allocation record.

## Contents
<a name="API_prm_RevenueAttributionAllocationErrorDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Action **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-Action"></a>
The action that was attempted.
Type: String
Valid Values: `CREATE | UPDATE`
Required: Yes

 ** CustomerAwsAccountId **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-CustomerAwsAccountId"></a>
The customer AWS account ID of the failing record.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** EffectiveFrom **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-EffectiveFrom"></a>
Effective start date of the failing record.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** EffectiveUntil **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-EffectiveUntil"></a>
Effective end date of the failing record.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** EntityId **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-EntityId"></a>
The deal entity identifier of the failing record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`
Required: Yes

 ** EntityType **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-EntityType"></a>
The deal entity type of the failing record.
Type: String
Valid Values: `OFFER | OPPORTUNITY`
Required: Yes

 ** ErrorCode **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-ErrorCode"></a>
Machine-readable error code.
Type: String
Valid Values: `ALLOCATION_CAP_EXCEEDED | RESOURCE_NOT_FOUND | IMMUTABLE_ALLOCATION | ACCESS_DENIED | INVALID_VALUE | CONCURRENT_MODIFICATION | INTERNAL_ERROR`
Required: Yes

 ** ErrorMessage **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-ErrorMessage"></a>
Human-readable error description.
Type: String
Required: Yes

 ** RevenueAttributionAllocationId **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationErrorDetail-RevenueAttributionAllocationId"></a>
The allocation identifier. Present for UPDATE actions; absent for CREATE actions.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `alloc-[a-z0-9]{13}`
Required: No

## See Also
<a name="API_prm_RevenueAttributionAllocationErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/RevenueAttributionAllocationErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/RevenueAttributionAllocationErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/RevenueAttributionAllocationErrorDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
