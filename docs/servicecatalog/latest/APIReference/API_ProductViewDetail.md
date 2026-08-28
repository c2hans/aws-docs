---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProductViewDetail.html
---

# ProductViewDetail
<a name="API_ProductViewDetail"></a>

Information about a product view.

## Contents
<a name="API_ProductViewDetail_Contents"></a>

 ** CreatedTime **   <a name="servicecatalog-Type-ProductViewDetail-CreatedTime"></a>
The UTC time stamp of the creation time.
Type: Timestamp
Required: No

 ** ProductARN **   <a name="servicecatalog-Type-ProductViewDetail-ProductARN"></a>
The ARN of the product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

 ** ProductViewSummary **   <a name="servicecatalog-Type-ProductViewDetail-ProductViewSummary"></a>
Summary information about the product view.
Type: [ProductViewSummary](API_ProductViewSummary.md) object
Required: No

 ** SourceConnection **   <a name="servicecatalog-Type-ProductViewDetail-SourceConnection"></a>
A top level `ProductViewDetail` response containing details about the product’s connection. AWS Service Catalog returns this field for the `CreateProduct`, `UpdateProduct`, `DescribeProductAsAdmin`, and `SearchProductAsAdmin` APIs. This response contains the same fields as the `ConnectionParameters` request, with the addition of the `LastSync` response.
Type: [SourceConnectionDetail](API_SourceConnectionDetail.md) object
Required: No

 ** Status **   <a name="servicecatalog-Type-ProductViewDetail-Status"></a>
The status of the product.
+  `AVAILABLE` - The product is ready for use.
+  `CREATING` - Product creation has started; the product is not ready for use.
+  `FAILED` - An action failed.
Type: String
Valid Values: `AVAILABLE | CREATING | FAILED`
Required: No

## See Also
<a name="API_ProductViewDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProductViewDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProductViewDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProductViewDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
