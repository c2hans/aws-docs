---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_RevenueAttributionAllocationSummary.html
---

# RevenueAttributionAllocationSummary
<a name="API_prm_RevenueAttributionAllocationSummary"></a>

Summary information about a revenue attribution allocation.

## Contents
<a name="API_prm_RevenueAttributionAllocationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomerAwsAccountId **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-CustomerAwsAccountId"></a>
The customer AWS account ID for this associated deal entity.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** EffectiveFrom **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-EffectiveFrom"></a>
First day of the effective month.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** EffectiveUntil **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-EffectiveUntil"></a>
Last day of the effective month.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** EntityIdentifier **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-EntityIdentifier"></a>
The unique identifier of the associated deal entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`
Required: Yes

 ** EntityType **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-EntityType"></a>
The type of the associated deal entity.
Type: String
Valid Values: `OFFER | OPPORTUNITY`
Required: Yes

 ** RevenueAttributionAllocationId **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-RevenueAttributionAllocationId"></a>
Unique allocation identifier.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `alloc-[a-z0-9]{13}`
Required: Yes

 ** RevenueAttributionIdentifier **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-RevenueAttributionIdentifier"></a>
The revenue attribution identifier.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`
Required: Yes

 ** RevenueSharePercent **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-RevenueSharePercent"></a>
Revenue share percentage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `\d{1,3}(\.\d{1,2})?`
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-Status"></a>
Current allocation status.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** EntityName **   <a name="AWSPartnerCentral-Type-prm_RevenueAttributionAllocationSummary-EntityName"></a>
The display name of the associated deal entity.
Type: String
Required: No

## See Also
<a name="API_prm_RevenueAttributionAllocationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/RevenueAttributionAllocationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/RevenueAttributionAllocationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/RevenueAttributionAllocationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
