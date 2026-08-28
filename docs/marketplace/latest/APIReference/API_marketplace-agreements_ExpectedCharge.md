---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ExpectedCharge.html
---

# ExpectedCharge
<a name="API_marketplace-agreements_ExpectedCharge"></a>

Estimated charge for the request.

## Contents
<a name="API_marketplace-agreements_ExpectedCharge_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** amount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ExpectedCharge-amount"></a>
The tax-exclusive amount of the charge. Only available when the charge amount is known.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** amountAfterTax **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ExpectedCharge-amountAfterTax"></a>
The tax-inclusive amount the acceptor has to pay. The amount is only present for fixed charges.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** estimatedTaxes **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ExpectedCharge-estimatedTaxes"></a>
Provides an aggregated view of estimated tax information for this specific charge.
Type: [EstimatedTaxes](API_marketplace-agreements_EstimatedTaxes.md) object
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ExpectedCharge-id"></a>
Unique identifier of the charge for a given agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** time **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ExpectedCharge-time"></a>
The date and time when the charge is due to be invoiced. This is available only when the charge date is known.
Type: Timestamp
Required: No

 ** timing **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ExpectedCharge-timing"></a>
Indicates when the charge amount will be incurred. Values include `ON_ACCEPTANCE` (charged immediately when the agreement request is accepted), `BILLING_PERIOD` (charged on each billing period), and `SCHEDULED` (charged at a predetermined future date).
Type: String
Valid Values: `ON_ACCEPTANCE | SCHEDULED | BILLING_PERIOD`
Required: No

## See Also
<a name="API_marketplace-agreements_ExpectedCharge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ExpectedCharge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ExpectedCharge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ExpectedCharge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
