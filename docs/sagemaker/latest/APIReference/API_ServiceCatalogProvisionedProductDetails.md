---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ServiceCatalogProvisionedProductDetails.html
---

# ServiceCatalogProvisionedProductDetails
<a name="API_ServiceCatalogProvisionedProductDetails"></a>

Details of a provisioned service catalog product. For information about service catalog, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).

## Contents
<a name="API_ServiceCatalogProvisionedProductDetails_Contents"></a>

 ** ProvisionedProductId **   <a name="sagemaker-Type-ServiceCatalogProvisionedProductDetails-ProvisionedProductId"></a>
The ID of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisionedProductStatusMessage **   <a name="sagemaker-Type-ServiceCatalogProvisionedProductDetails-ProvisionedProductStatusMessage"></a>
The current status of the product.
+  `AVAILABLE` - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
+  `UNDER_CHANGE` - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
+  `TAINTED` - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
+  `ERROR` - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
+  `PLAN_IN_PROGRESS` - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.
Type: String
Pattern: `.*`
Required: No

## See Also
<a name="API_ServiceCatalogProvisionedProductDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ServiceCatalogProvisionedProductDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ServiceCatalogProvisionedProductDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ServiceCatalogProvisionedProductDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
