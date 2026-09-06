---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetSagemakerServicecatalogPortfolioStatus.html
---

# GetSagemakerServicecatalogPortfolioStatus
<a name="API_GetSagemakerServicecatalogPortfolioStatus"></a>

Gets the status of Service Catalog in SageMaker. Service Catalog is used to create SageMaker projects.

## Response Syntax
<a name="API_GetSagemakerServicecatalogPortfolioStatus_ResponseSyntax"></a>

```
{
   "Status": "string"
}
```

## Response Elements
<a name="API_GetSagemakerServicecatalogPortfolioStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_GetSagemakerServicecatalogPortfolioStatus_ResponseSyntax) **   <a name="sagemaker-GetSagemakerServicecatalogPortfolioStatus-response-Status"></a>
Whether Service Catalog is enabled or disabled in SageMaker.
Type: String
Valid Values: `Enabled | Disabled`

## Errors
<a name="API_GetSagemakerServicecatalogPortfolioStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetSagemakerServicecatalogPortfolioStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GetSagemakerServicecatalogPortfolioStatus)
