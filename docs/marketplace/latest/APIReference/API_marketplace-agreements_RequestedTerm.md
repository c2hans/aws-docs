---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RequestedTerm.html
---

# RequestedTerm
<a name="API_marketplace-agreements_RequestedTerm"></a>

Defines what is being accepted as part of the agreement creation or update request, and it includes their configurations.

## Contents
<a name="API_marketplace-agreements_RequestedTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RequestedTerm-id"></a>
The unique identifier of the term in the agreement proposal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** configuration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RequestedTerm-configuration"></a>
Additional configuration for the requested terms. This configuration is applicable only to the terms that accept a customer-provided configuration, such as `ConfigurableUpfrontPricingTerm`.
Type: [RequestedTermConfiguration](API_marketplace-agreements_RequestedTermConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_marketplace-agreements_RequestedTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RequestedTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RequestedTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RequestedTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
