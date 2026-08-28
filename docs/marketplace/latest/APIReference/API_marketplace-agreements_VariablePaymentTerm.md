---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_VariablePaymentTerm.html
---

# VariablePaymentTerm
<a name="API_marketplace-agreements_VariablePaymentTerm"></a>

Defines a payment model where sellers can submit variable payment requests up to a maximum charge amount, with configurable approval strategies and expiration timelines.

## Contents
<a name="API_marketplace-agreements_VariablePaymentTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** configuration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_VariablePaymentTerm-configuration"></a>
Additional parameters specified by the acceptor while accepting the term.
Type: [VariablePaymentTermConfiguration](API_marketplace-agreements_VariablePaymentTermConfiguration.md) object
Required: No

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_VariablePaymentTerm-currencyCode"></a>
Defines the currency for the prices mentioned in the term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_VariablePaymentTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** maxTotalChargeAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_VariablePaymentTerm-maxTotalChargeAmount"></a>
The maximum total amount that can be charged to the customer through variable payment requests under this term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_VariablePaymentTerm-type"></a>
Type of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_VariablePaymentTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/VariablePaymentTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/VariablePaymentTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/VariablePaymentTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
