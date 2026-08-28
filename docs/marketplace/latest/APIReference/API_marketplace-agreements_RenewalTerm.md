---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RenewalTerm.html
---

# RenewalTerm
<a name="API_marketplace-agreements_RenewalTerm"></a>

Defines that on graceful expiration of the agreement (when the agreement ends on its pre-defined end date), a new agreement will be created using the accepted terms on the existing agreement. In other words, the agreement will be renewed. The presence of `RenewalTerm` in the offer document means that auto-renewal is allowed. Buyers will have the option to accept or decline auto-renewal at the offer acceptance/agreement creation. Buyers can also change this flag from `True` to `False` or `False` to `True` at anytime during the agreement's lifecycle.

## Contents
<a name="API_marketplace-agreements_RenewalTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** configuration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-configuration"></a>
Additional parameters specified by the acceptor while accepting the term.
Type: [RenewalTermConfiguration](API_marketplace-agreements_RenewalTermConfiguration.md) object
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-type"></a>
Category of the term being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_RenewalTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RenewalTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RenewalTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RenewalTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
