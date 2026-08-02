---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AssociateBudgetWithResource.html
---

# AssociateBudgetWithResource
<a name="API_AssociateBudgetWithResource"></a>

Associates the specified budget with the specified resource.

## Request Syntax
<a name="API_AssociateBudgetWithResource_RequestSyntax"></a>

```
{
   "BudgetName": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateBudgetWithResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [BudgetName](#API_AssociateBudgetWithResource_RequestSyntax) **   <a name="servicecatalog-AssociateBudgetWithResource-request-BudgetName"></a>
The name of the budget you want to associate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ResourceId](#API_AssociateBudgetWithResource_RequestSyntax) **   <a name="servicecatalog-AssociateBudgetWithResource-request-ResourceId"></a>
 The resource identifier. Either a portfolio-id or a product-id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Elements
<a name="API_AssociateBudgetWithResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateBudgetWithResource_Errors"></a>

 ** DuplicateResourceException **
The specified resource is a duplicate.
HTTP Status Code: 400

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_AssociateBudgetWithResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/AssociateBudgetWithResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociateBudgetWithResource)
