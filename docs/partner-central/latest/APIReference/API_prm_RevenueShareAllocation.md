---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_RevenueShareAllocation.html
---

# RevenueShareAllocation
<a name="API_prm_RevenueShareAllocation"></a>

A single allocation change within a batch request.

## Contents
<a name="API_prm_RevenueShareAllocation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Action **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-Action"></a>
The operation type: CREATE or UPDATE.
Type: String
Valid Values: `CREATE | UPDATE`
Required: Yes

 ** CustomerAwsAccountId **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-CustomerAwsAccountId"></a>
The customer AWS account ID for this associated deal entity.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** EffectiveFrom **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-EffectiveFrom"></a>
The effective start date for this allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** EffectiveUntil **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-EffectiveUntil"></a>
The effective end date for this allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** EntityIdentifier **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-EntityIdentifier"></a>
The unique identifier of the associated deal entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`
Required: Yes

 ** EntityType **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-EntityType"></a>
The type of the associated deal entity.
Type: String
Valid Values: `OFFER | OPPORTUNITY`
Required: Yes

 ** RevenueSharePercent **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-RevenueSharePercent"></a>
Revenue share percentage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `\d{1,3}(\.\d{1,2})?`
Required: Yes

 ** RevenueAttributionAllocationId **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-RevenueAttributionAllocationId"></a>
The allocation to update. Required when Action is UPDATE.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `alloc-[a-z0-9]{13}`
Required: No

 ** Status **   <a name="AWSPartnerCentral-Type-prm_RevenueShareAllocation-Status"></a>
Allocation status. Defaults to ACTIVE on CREATE.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_prm_RevenueShareAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/RevenueShareAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/RevenueShareAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/RevenueShareAllocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
