---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_AttributionSummary.html
---

# AttributionSummary
<a name="API_prm_AttributionSummary"></a>

Summary representation of a revenue attribution returned in list operations.

## Contents
<a name="API_prm_AttributionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TenancyModel **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-TenancyModel"></a>
The tenancy model for this revenue attribution.
Type: String
Valid Values: `MULTI_TENANT | SINGLE_TENANT`
Required: Yes

 ** Arn **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-Arn"></a>
The Amazon Resource Name (ARN) of the revenue attribution.
Type: String
Required: No

 ** Catalog **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-Catalog"></a>
The catalog that the revenue attribution belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: No

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-CreatedDate"></a>
The date when the revenue attribution was created.
Type: Timestamp
Required: No

 ** EffectiveFrom **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-EffectiveFrom"></a>
The date from which this revenue attribution is effective, derived from the earliest allocation start date (YYYY-MM-DD).
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** EffectiveUntil **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-EffectiveUntil"></a>
The date until which this revenue attribution is effective, derived from the latest allocation end date (YYYY-MM-DD).
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** Id **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-Id"></a>
The unique identifier of the revenue attribution.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`
Required: No

 ** LastModifiedDate **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-LastModifiedDate"></a>
The date when the revenue attribution was last modified.
Type: Timestamp
Required: No

 ** LatestRevision **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-LatestRevision"></a>
The latest revision of the revenue attribution resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: No

 ** MarketplaceProduct **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-MarketplaceProduct"></a>
The AWS Marketplace product attributes associated with this attribution, if set.
Type: [MarketplaceProductSummary](API_prm_MarketplaceProductSummary.md) object
Required: No

 ** Name **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-Name"></a>
The display name of the revenue attribution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TotalActiveRevenueAttributionAllocationCount **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-TotalActiveRevenueAttributionAllocationCount"></a>
The total number of allocations under this revenue attribution whose Status is ACTIVE.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TotalRevenueAttributionAllocationCount **   <a name="AWSPartnerCentral-Type-prm_AttributionSummary-TotalRevenueAttributionAllocationCount"></a>
The total number of allocations under this revenue attribution, counting both ACTIVE and INACTIVE.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_prm_AttributionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/AttributionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/AttributionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/AttributionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
