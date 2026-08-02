---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_DocumentItem.html
---

# DocumentItem
<a name="API_marketplace-agreements_DocumentItem"></a>

Includes the list of references to legal resources proposed by the proposer to the acceptor. Each `DocumentItem` refers to an individual reference.

## Contents
<a name="API_marketplace-agreements_DocumentItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_DocumentItem-type"></a>
Category of the document. Document types include:
+  `CustomEula` – A custom EULA provided by you as seller. A URL for a EULA stored in an accessible Amazon S3 bucket is required for this document type.
+  `CustomDsa` – A custom Data Subscription Agreement (DSA) provided by you as seller. A URL for a DSA stored in an accessible Amazon S3 bucket is required for this document type.
+  `StandardEula` – The Standard Contract for AWS Marketplace (SCMP). For more information about SCMP, see the AWS Marketplace Seller Guide. You don’t provide a URL for this type because it’s managed by AWS Marketplace.
+  `StandardDsa` – DSA for AWS Marketplace. For more information about the DSA, see the AWS Data Exchange User Guide. You don’t provide a URL for this type because it’s managed by AWS Marketplace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** url **   <a name="AWSMarketplaceService-Type-marketplace-agreements_DocumentItem-url"></a>
A URL to the legal document for buyers to read. Required when `Type` is `CustomEula`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** version **   <a name="AWSMarketplaceService-Type-marketplace-agreements_DocumentItem-version"></a>
Version of standard contracts provided by AWS Marketplace. Required when Type is `StandardEula` or `StandardDsa`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-agreements_DocumentItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/DocumentItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/DocumentItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/DocumentItem)
