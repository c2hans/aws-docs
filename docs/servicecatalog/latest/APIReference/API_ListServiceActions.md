---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListServiceActions.html
---

# ListServiceActions
<a name="API_ListServiceActions"></a>

Lists all self-service actions.

## Request Syntax
<a name="API_ListServiceActions_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PageSize": {{number}},
   "PageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListServiceActions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListServiceActions_RequestSyntax) **   <a name="servicecatalog-ListServiceActions-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PageSize](#API_ListServiceActions_RequestSyntax) **   <a name="servicecatalog-ListServiceActions-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListServiceActions_RequestSyntax) **   <a name="servicecatalog-ListServiceActions-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

## Response Syntax
<a name="API_ListServiceActions_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "ServiceActionSummaries": [
      {
         "DefinitionType": "string",
         "Description": "string",
         "Id": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServiceActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_ListServiceActions_ResponseSyntax) **   <a name="servicecatalog-ListServiceActions-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [ServiceActionSummaries](#API_ListServiceActions_ResponseSyntax) **   <a name="servicecatalog-ListServiceActions-response-ServiceActionSummaries"></a>
An object containing information about the service actions associated with the provisioning artifact.
Type: Array of [ServiceActionSummary](API_ServiceActionSummary.md) objects

## Errors
<a name="API_ListServiceActions_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListServiceActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListServiceActions)
