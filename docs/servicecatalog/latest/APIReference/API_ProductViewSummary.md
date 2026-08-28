---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProductViewSummary.html
---

# ProductViewSummary
<a name="API_ProductViewSummary"></a>

Summary information about a product view.

## Contents
<a name="API_ProductViewSummary_Contents"></a>

 ** Distributor **   <a name="servicecatalog-Type-ProductViewSummary-Distributor"></a>
The distributor of the product. Contact the product administrator for the significance of this value.
Type: String
Required: No

 ** HasDefaultPath **   <a name="servicecatalog-Type-ProductViewSummary-HasDefaultPath"></a>
Indicates whether the product has a default path. If the product does not have a default path, call [ListLaunchPaths](API_ListLaunchPaths.md) to disambiguate between paths. Otherwise, [ListLaunchPaths](API_ListLaunchPaths.md) is not required, and the output of [ProductViewSummary](#API_ProductViewSummary) can be used directly with [DescribeProvisioningParameters](API_DescribeProvisioningParameters.md).
Type: Boolean
Required: No

 ** Id **   <a name="servicecatalog-Type-ProductViewSummary-Id"></a>
The product view identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Name **   <a name="servicecatalog-Type-ProductViewSummary-Name"></a>
The name of the product.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** Owner **   <a name="servicecatalog-Type-ProductViewSummary-Owner"></a>
The owner of the product. Contact the product administrator for the significance of this value.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** ProductId **   <a name="servicecatalog-Type-ProductViewSummary-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ShortDescription **   <a name="servicecatalog-Type-ProductViewSummary-ShortDescription"></a>
Short description of the product.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** SupportDescription **   <a name="servicecatalog-Type-ProductViewSummary-SupportDescription"></a>
The description of the support for this Product.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** SupportEmail **   <a name="servicecatalog-Type-ProductViewSummary-SupportEmail"></a>
The email contact information to obtain support for this Product.
Type: String
Length Constraints: Maximum length of 254.
Required: No

 ** SupportUrl **   <a name="servicecatalog-Type-ProductViewSummary-SupportUrl"></a>
The URL information to obtain support for this Product.
Type: String
Length Constraints: Maximum length of 2083.
Required: No

 ** Type **   <a name="servicecatalog-Type-ProductViewSummary-Type"></a>
The product type. Contact the product administrator for the significance of this value. If this value is `MARKETPLACE`, the product was created by AWS Marketplace.
Type: String
Length Constraints: Maximum length of 8191.
Valid Values: `CLOUD_FORMATION_TEMPLATE | MARKETPLACE | TERRAFORM_OPEN_SOURCE | EXTERNAL | TERRAFORM_CLOUD`
Required: No

## See Also
<a name="API_ProductViewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProductViewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProductViewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProductViewSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
