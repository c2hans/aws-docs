---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_BenefitAllocationSummary.html
---

# BenefitAllocationSummary
<a name="API_benefits_BenefitAllocationSummary"></a>

A summary view of a benefit allocation containing key information for list operations.

## Contents
<a name="API_benefits_BenefitAllocationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApplicableBenefitIds **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-ApplicableBenefitIds"></a>
The identifiers of the benefits applicable for this allocation.
Type: Array of strings
Pattern: `(arn:.+|ben-[0-9a-z]{14})`
Required: No

 ** Arn **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the benefit allocation.
Type: String
Required: No

 ** BenefitApplicationId **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-BenefitApplicationId"></a>
The identifier of the benefit application that resulted in this allocation.
Type: String
Pattern: `benappl-[0-9a-z]{14}`
Required: No

 ** BenefitId **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-BenefitId"></a>
The identifier of the benefit that this allocation is based on.
Type: String
Pattern: `(arn:.+|ben-[0-9a-z]{14})`
Required: No

 ** Catalog **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-Catalog"></a>
The catalog identifier that the benefit allocation belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-CreatedAt"></a>
The timestamp when the benefit allocation was created.
Type: Timestamp
Required: No

 ** ExpiresAt **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-ExpiresAt"></a>
The timestamp when the benefit allocation expires.
Type: Timestamp
Required: No

 ** FulfillmentTypes **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-FulfillmentTypes"></a>
The fulfillment types used for this benefit allocation.
Type: Array of strings
Valid Values: `CREDITS | CASH | ACCESS`
Required: No

 ** Id **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-Id"></a>
The unique identifier of the benefit allocation.
Type: String
Pattern: `benalloc-[0-9a-z]{14}`
Required: No

 ** Name **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-Name"></a>
The human-readable name of the benefit allocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Status **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-Status"></a>
The current status of the benefit allocation.
Type: String
Valid Values: `ACTIVE | INACTIVE | FULFILLED`
Required: No

 ** StatusReason **   <a name="AWSPartnerCentral-Type-benefits_BenefitAllocationSummary-StatusReason"></a>
Additional information explaining the current status of the benefit allocation.
Type: String
Required: No

## See Also
<a name="API_benefits_BenefitAllocationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/BenefitAllocationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/BenefitAllocationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/BenefitAllocationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
