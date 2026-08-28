---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_TaxBreakdownItem.html
---

# TaxBreakdownItem
<a name="API_marketplace-agreements_TaxBreakdownItem"></a>

Represents a single tax breakdown entry with amount, rate, and type.

## Contents
<a name="API_marketplace-agreements_TaxBreakdownItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** amount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_TaxBreakdownItem-amount"></a>
The estimated tax amount.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** rate **   <a name="AWSMarketplaceService-Type-marketplace-agreements_TaxBreakdownItem-rate"></a>
The tax rate, in decimals.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_TaxBreakdownItem-type"></a>
The type of tax (for example, VAT, ST, or GST).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-agreements_TaxBreakdownItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/TaxBreakdownItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/TaxBreakdownItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/TaxBreakdownItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
