---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Entity.html
---

# Entity
<a name="API_Entity"></a>

An entity contains data that describes your product, its supported features, and how it can be used or launched by your customer.

## Contents
<a name="API_Entity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Type **   <a name="AWSMarketplaceService-Type-Entity-Type"></a>
The type of entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** Identifier **   <a name="AWSMarketplaceService-Type-Entity-Identifier"></a>
The identifier for the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-@]+$`
Required: No

## See Also
<a name="API_Entity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/Entity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/Entity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/Entity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
