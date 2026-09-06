---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PendingDeploymentSummary.html
---

# PendingDeploymentSummary
<a name="API_PendingDeploymentSummary"></a>

The summary of an in-progress deployment when an endpoint is creating or updating with a new endpoint configuration.

## Contents
<a name="API_PendingDeploymentSummary_Contents"></a>

 ** EndpointConfigName **   <a name="sagemaker-Type-PendingDeploymentSummary-EndpointConfigName"></a>
The name of the endpoint configuration used in the deployment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ProductionVariants **   <a name="sagemaker-Type-PendingDeploymentSummary-ProductionVariants"></a>
An array of [PendingProductionVariantSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PendingProductionVariantSummary.html) objects, one for each model hosted behind this endpoint for the in-progress deployment.
Type: Array of [PendingProductionVariantSummary](API_PendingProductionVariantSummary.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ShadowProductionVariants **   <a name="sagemaker-Type-PendingDeploymentSummary-ShadowProductionVariants"></a>
An array of [PendingProductionVariantSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PendingProductionVariantSummary.html) objects, one for each model hosted behind this endpoint in shadow mode with production traffic replicated from the model specified on `ProductionVariants` for the in-progress deployment.
Type: Array of [PendingProductionVariantSummary](API_PendingProductionVariantSummary.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** StartTime **   <a name="sagemaker-Type-PendingDeploymentSummary-StartTime"></a>
The start time of the deployment.
Type: Timestamp
Required: No

## See Also
<a name="API_PendingDeploymentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PendingDeploymentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PendingDeploymentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PendingDeploymentSummary)
