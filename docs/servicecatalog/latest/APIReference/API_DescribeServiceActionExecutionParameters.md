---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeServiceActionExecutionParameters.html
---

# DescribeServiceActionExecutionParameters
<a name="API_DescribeServiceActionExecutionParameters"></a>

Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.

## Request Syntax
<a name="API_DescribeServiceActionExecutionParameters_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "ProvisionedProductId": "{{string}}",
   "ServiceActionId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeServiceActionExecutionParameters_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeServiceActionExecutionParameters_RequestSyntax) **   <a name="servicecatalog-DescribeServiceActionExecutionParameters-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [ProvisionedProductId](#API_DescribeServiceActionExecutionParameters_RequestSyntax) **   <a name="servicecatalog-DescribeServiceActionExecutionParameters-request-ProvisionedProductId"></a>
The identifier of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ServiceActionId](#API_DescribeServiceActionExecutionParameters_RequestSyntax) **   <a name="servicecatalog-DescribeServiceActionExecutionParameters-request-ServiceActionId"></a>
The self-service action identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_DescribeServiceActionExecutionParameters_ResponseSyntax"></a>

```
{
   "ServiceActionParameters": [
      {
         "DefaultValues": [ "string" ],
         "Name": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeServiceActionExecutionParameters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServiceActionParameters](#API_DescribeServiceActionExecutionParameters_ResponseSyntax) **   <a name="servicecatalog-DescribeServiceActionExecutionParameters-response-ServiceActionParameters"></a>
The parameters of the self-service action.
Type: Array of [ExecutionParameter](API_ExecutionParameter.md) objects

## Errors
<a name="API_DescribeServiceActionExecutionParameters_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeServiceActionExecutionParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters)
