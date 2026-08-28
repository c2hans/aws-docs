---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_Resource.html
---

# Resource
<a name="API_marketplace-discovery_Resource"></a>

A resource that provides supplementary information about a product, such as documentation links, support contacts, or usage instructions.

## Contents
<a name="API_marketplace-discovery_Resource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** contentType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Resource-contentType"></a>
The format of the resource content, such as a URL, email address, or text.
Type: String
Valid Values: `EMAIL | PHONE_NUMBER | LINK | OTHER`
Required: Yes

 ** resourceType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Resource-resourceType"></a>
The category of the resource, such as manufacturer support or usage instructions.
Type: String
Valid Values: `MANUFACTURER_SUPPORT | MANUFACTURER_INSTRUCTIONS`
Required: Yes

 ** value **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Resource-value"></a>
The resource content. Interpretation depends on the content type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Resource-displayName"></a>
An optional human-readable label for the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_marketplace-discovery_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
