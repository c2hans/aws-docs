---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_CatalogItem.html
---

# CatalogItem
<a name="API_connect-customer-profiles_CatalogItem"></a>

Represents an item in the catalog with its complete set of attributes and metadata.

## Contents
<a name="API_connect-customer-profiles_CatalogItem_Contents"></a>

 ** AdditionalInformation **   <a name="connect-Type-connect-customer-profiles_CatalogItem-AdditionalInformation"></a>
Supplementary information about the catalog item beyond the basic description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** Attributes **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Attributes"></a>
Additional attributes or properties associated with the catalog item stored as key-value pairs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Category **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Category"></a>
The category to which the catalog item belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Code **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Code"></a>
The product code or SKU of the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_CatalogItem-CreatedAt"></a>
The timestamp when the catalog item was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Description"></a>
A detailed description of the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Id **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Id"></a>
The unique identifier for the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ImageLink **   <a name="connect-Type-connect-customer-profiles_CatalogItem-ImageLink"></a>
The URL link to the item's image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** Link **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Link"></a>
The URL link to the item's detailed page or external resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** Name **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Name"></a>
The display name of the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Price **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Price"></a>
The price of the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Type **   <a name="connect-Type-connect-customer-profiles_CatalogItem-Type"></a>
The type classification of the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** UpdatedAt **   <a name="connect-Type-connect-customer-profiles_CatalogItem-UpdatedAt"></a>
The timestamp when the catalog item was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_connect-customer-profiles_CatalogItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CatalogItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CatalogItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CatalogItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
