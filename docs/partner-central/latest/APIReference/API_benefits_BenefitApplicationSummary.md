---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_BenefitApplicationSummary.html
---

# BenefitApplicationSummary
<a name="API_benefits_BenefitApplicationSummary"></a>

A summary view of a benefit application containing key information for list operations.

## Contents
<a name="API_benefits_BenefitApplicationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the benefit application.
Type: String
Required: No

 ** AssociatedResources **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-AssociatedResources"></a>
AWS resources that are associated with this benefit application.
Type: Array of strings
Pattern: `arn:aws:([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.+)`
Required: No

 ** BenefitApplicationDetails **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-BenefitApplicationDetails"></a>
Additional attributes and metadata associated with the benefit application.
Type: String to string map
Required: No

 ** BenefitId **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-BenefitId"></a>
The identifier of the benefit being requested in this application.
Type: String
Pattern: `(arn:.+|ben-[0-9a-z]{14})`
Required: No

 ** Catalog **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-Catalog"></a>
The catalog identifier that the benefit application belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-CreatedAt"></a>
The timestamp when the benefit application was created.
Type: Timestamp
Required: No

 ** FulfillmentTypes **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-FulfillmentTypes"></a>
The fulfillment types requested for this benefit application.
Type: Array of strings
Valid Values: `CREDITS | CASH | ACCESS`
Required: No

 ** Id **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-Id"></a>
The unique identifier of the benefit application.
Type: String
Pattern: `benappl-[0-9a-z]{14}`
Required: No

 ** Name **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-Name"></a>
The human-readable name of the benefit application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Programs **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-Programs"></a>
The AWS partner programs associated with this benefit application.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** Stage **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-Stage"></a>
The current stage in the benefit application processing workflow..
Type: String
Required: No

 ** Status **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-Status"></a>
The current processing status of the benefit application.
Type: String
Valid Values: `PENDING_SUBMISSION | IN_REVIEW | ACTION_REQUIRED | APPROVED | REJECTED | CANCELED`
Required: No

 ** UpdatedAt **   <a name="AWSPartnerCentral-Type-benefits_BenefitApplicationSummary-UpdatedAt"></a>
The timestamp when the benefit application was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_benefits_BenefitApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/BenefitApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/BenefitApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/BenefitApplicationSummary)
