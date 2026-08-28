---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_Charge.html
---

# Charge
<a name="API_marketplace-agreements_Charge"></a>

Represents a charge associated with an agreement, including amount, timing, and purchase order details.

## Contents
<a name="API_marketplace-agreements_Charge_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Charge-agreementId"></a>
The unique identifier of the agreement that resulted in this charge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** agreementType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Charge-agreementType"></a>
The type of agreement that resulted in this charge (for example, `PurchaseAgreement`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: No

 ** amount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Charge-amount"></a>
The amount of the charge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Charge-currencyCode"></a>
The currency code for the charge amount.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Charge-id"></a>
The unique identifier of the charge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** purchaseOrderReference **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Charge-purchaseOrderReference"></a>
The purchase order reference associated with the charge, if any.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** revision **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Charge-revision"></a>
The revision number of the charge.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** time **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Charge-time"></a>
The date and time when the charge will be incurred. This is available only when the charge date is known.
Type: Timestamp
Required: No

## See Also
<a name="API_marketplace-agreements_Charge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/Charge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/Charge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/Charge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
