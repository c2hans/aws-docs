---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ListForms.html
---

# ListForms
<a name="API_ListForms"></a>

Retrieves a list of forms for a specified Amplify app and backend environment.

## Request Syntax
<a name="API_ListForms_RequestSyntax"></a>

```
GET /app/{{appId}}/environment/{{environmentName}}/forms?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListForms_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ListForms_RequestSyntax) **   <a name="amplifyuibuilder-ListForms-request-uri-appId"></a>
The unique ID for the Amplify app.
Required: Yes

 ** [environmentName](#API_ListForms_RequestSyntax) **   <a name="amplifyuibuilder-ListForms-request-uri-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Required: Yes

 ** [maxResults](#API_ListForms_RequestSyntax) **   <a name="amplifyuibuilder-ListForms-request-uri-maxResults"></a>
The maximum number of forms to retrieve.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListForms_RequestSyntax) **   <a name="amplifyuibuilder-ListForms-request-uri-nextToken"></a>
The token to request the next page of results.

## Request Body
<a name="API_ListForms_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListForms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "entities": [
      {
         "appId": "string",
         "dataType": {
            "dataSourceType": "string",
            "dataTypeName": "string"
         },
         "environmentName": "string",
         "formActionType": "string",
         "id": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListForms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entities](#API_ListForms_ResponseSyntax) **   <a name="amplifyuibuilder-ListForms-response-entities"></a>
The list of forms for the Amplify app.
Type: Array of [FormSummary](API_FormSummary.md) objects

 ** [nextToken](#API_ListForms_ResponseSyntax) **   <a name="amplifyuibuilder-ListForms-response-nextToken"></a>
The pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ListForms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ListForms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/ListForms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ListForms)
