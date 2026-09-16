---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DisassociateBudgetFromResource.html
---

# DisassociateBudgetFromResource
<a name="API_DisassociateBudgetFromResource"></a>

Disassociates the specified budget from the specified resource.

## Request Syntax
<a name="API_DisassociateBudgetFromResource_RequestSyntax"></a>

```
{
   "BudgetName": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateBudgetFromResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [BudgetName](#API_DisassociateBudgetFromResource_RequestSyntax) **   <a name="servicecatalog-DisassociateBudgetFromResource-request-BudgetName"></a>
The name of the budget you want to disassociate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ResourceId](#API_DisassociateBudgetFromResource_RequestSyntax) **   <a name="servicecatalog-DisassociateBudgetFromResource-request-ResourceId"></a>
The resource identifier you want to disassociate from. Either a portfolio-id or a product-id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Elements
<a name="API_DisassociateBudgetFromResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateBudgetFromResource_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateBudgetFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource)
