---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_DocumentItem.html
---

# DocumentItem
<a name="API_marketplace-discovery_DocumentItem"></a>

A legal document associated with a legal term, such as a EULA or data subscription agreement.

## Contents
<a name="API_marketplace-discovery_DocumentItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DocumentItem-type"></a>
The category of the legal document, such as `StandardEula` or `CustomEula`.
Type: String
Valid Values: `CustomEula | CustomDsa | EnterpriseEula | StandardEula | StandardDsa`
Required: Yes

 ** url **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DocumentItem-url"></a>
The URL where the legal document can be accessed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

 ** version **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DocumentItem-version"></a>
The version of the standard contract, if applicable.
Type: String
Required: No

## See Also
<a name="API_marketplace-discovery_DocumentItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/DocumentItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/DocumentItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/DocumentItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
