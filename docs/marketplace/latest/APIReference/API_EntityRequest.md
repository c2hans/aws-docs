---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_EntityRequest.html
---

# EntityRequest
<a name="API_EntityRequest"></a>

An object that contains entity ID and the catalog in which the entity is present.

## Contents
<a name="API_EntityRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Catalog **   <a name="AWSMarketplaceService-Type-EntityRequest-Catalog"></a>
The name of the catalog the entity is present in. The only value at this time is `AWSMarketplace`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** EntityId **   <a name="AWSMarketplaceService-Type-EntityRequest-EntityId"></a>
The ID of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: Yes

## See Also
<a name="API_EntityRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/EntityRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/EntityRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/EntityRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
