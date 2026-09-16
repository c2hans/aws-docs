---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_GetProvisionedProductOutputs.html
---

# GetProvisionedProductOutputs
<a name="API_GetProvisionedProductOutputs"></a>

This API takes either a `ProvisonedProductId` or a `ProvisionedProductName`, along with a list of one or more output keys, and responds with the key/value pairs of those outputs.

## Request Syntax
<a name="API_GetProvisionedProductOutputs_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "OutputKeys": [ "{{string}}" ],
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "ProvisionedProductId": "{{string}}",
   "ProvisionedProductName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetProvisionedProductOutputs_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_GetProvisionedProductOutputs_RequestSyntax) **   <a name="servicecatalog-GetProvisionedProductOutputs-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [OutputKeys](#API_GetProvisionedProductOutputs_RequestSyntax) **   <a name="servicecatalog-GetProvisionedProductOutputs-request-OutputKeys"></a>
The list of keys that the API should return with their values. If none are provided, the API will return all outputs of the provisioned product.
Type: Array of strings
Array Members: Maximum number of 60 items.
Required: No

 ** [PageSize](#API_GetProvisionedProductOutputs_RequestSyntax) **   <a name="servicecatalog-GetProvisionedProductOutputs-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_GetProvisionedProductOutputs_RequestSyntax) **   <a name="servicecatalog-GetProvisionedProductOutputs-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [ProvisionedProductId](#API_GetProvisionedProductOutputs_RequestSyntax) **   <a name="servicecatalog-GetProvisionedProductOutputs-request-ProvisionedProductId"></a>
The identifier of the provisioned product that you want the outputs from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [ProvisionedProductName](#API_GetProvisionedProductOutputs_RequestSyntax) **   <a name="servicecatalog-GetProvisionedProductOutputs-request-ProvisionedProductName"></a>
The name of the provisioned product that you want the outputs from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`
Required: No

## Response Syntax
<a name="API_GetProvisionedProductOutputs_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "Outputs": [
      {
         "Description": "string",
         "OutputKey": "string",
         "OutputValue": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetProvisionedProductOutputs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_GetProvisionedProductOutputs_ResponseSyntax) **   <a name="servicecatalog-GetProvisionedProductOutputs-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [Outputs](#API_GetProvisionedProductOutputs_ResponseSyntax) **   <a name="servicecatalog-GetProvisionedProductOutputs-response-Outputs"></a>
Information about the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.
Type: Array of [RecordOutput](API_RecordOutput.md) objects

## Errors
<a name="API_GetProvisionedProductOutputs_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_GetProvisionedProductOutputs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs)
