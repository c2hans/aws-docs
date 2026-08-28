---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_BenefitSummary.html
---

# BenefitSummary
<a name="API_benefits_BenefitSummary"></a>

A summary view of a benefit containing key information for list operations.

## Contents
<a name="API_benefits_BenefitSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-benefits_BenefitSummary-Arn"></a>
The Amazon Resource Name (ARN) of the benefit.
Type: String
Required: No

 ** Catalog **   <a name="AWSPartnerCentral-Type-benefits_BenefitSummary-Catalog"></a>
The catalog identifier that the benefit belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** Description **   <a name="AWSPartnerCentral-Type-benefits_BenefitSummary-Description"></a>
A brief description of the benefit and its purpose.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** FulfillmentTypes **   <a name="AWSPartnerCentral-Type-benefits_BenefitSummary-FulfillmentTypes"></a>
The available fulfillment types for this benefit.
Type: Array of strings
Valid Values: `CREDITS | CASH | ACCESS`
Required: No

 ** Id **   <a name="AWSPartnerCentral-Type-benefits_BenefitSummary-Id"></a>
The unique identifier of the benefit.
Type: String
Pattern: `ben-[0-9a-z]{14}`
Required: No

 ** Name **   <a name="AWSPartnerCentral-Type-benefits_BenefitSummary-Name"></a>
The human-readable name of the benefit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Programs **   <a name="AWSPartnerCentral-Type-benefits_BenefitSummary-Programs"></a>
The AWS partner programs that this benefit is associated with.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** Status **   <a name="AWSPartnerCentral-Type-benefits_BenefitSummary-Status"></a>
The current status of the benefit.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_benefits_BenefitSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/BenefitSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/BenefitSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/BenefitSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
