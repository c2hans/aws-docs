---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListDatastores.html
---

# ListDatastores
<a name="API_ListDatastores"></a>

List data stores.

## Request Syntax
<a name="API_ListDatastores_RequestSyntax"></a>

```
GET /datastore?datastoreStatus={{datastoreStatus}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDatastores_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreStatus](#API_ListDatastores_RequestSyntax) **   <a name="healthimaging-ListDatastores-request-uri-datastoreStatus"></a>
The data store status.
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING | DELETED`

 ** [maxResults](#API_ListDatastores_RequestSyntax) **   <a name="healthimaging-ListDatastores-request-uri-maxResults"></a>
Valid Range: Minimum value of 1. Maximum value of 50.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListDatastores_RequestSyntax) **   <a name="healthimaging-ListDatastores-request-uri-nextToken"></a>
The pagination token used to request the list of data stores on the next page.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

## Request Body
<a name="API_ListDatastores_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDatastores_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datastoreSummaries": [
      {
         "createdAt": number,
         "datastoreArn": "string",
         "datastoreId": "string",
         "datastoreName": "string",
         "datastoreStatus": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDatastores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datastoreSummaries](#API_ListDatastores_ResponseSyntax) **   <a name="healthimaging-ListDatastores-response-datastoreSummaries"></a>
The list of summaries of data stores.
Type: Array of [DatastoreSummary](API_DatastoreSummary.md) objects

 ** [nextToken](#API_ListDatastores_ResponseSyntax) **   <a name="healthimaging-ListDatastores-response-nextToken"></a>
The pagination token used to retrieve the list of data stores on the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

## Errors
<a name="API_ListDatastores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_ListDatastores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/ListDatastores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/ListDatastores)
