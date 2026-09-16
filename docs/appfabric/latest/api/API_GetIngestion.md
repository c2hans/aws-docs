---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_GetIngestion.html
---

# GetIngestion
<a name="API_GetIngestion"></a>

Returns information about an ingestion.

## Request Syntax
<a name="API_GetIngestion_RequestSyntax"></a>

```
GET /appbundles/{{appBundleIdentifier}}/ingestions/{{ingestionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIngestion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appBundleIdentifier](#API_GetIngestion_RequestSyntax) **   <a name="appfabric-GetIngestion-request-uri-appBundleIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [ingestionIdentifier](#API_GetIngestion_RequestSyntax) **   <a name="appfabric-GetIngestion-request-uri-ingestionIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_GetIngestion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIngestion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ingestion": {
      "app": "string",
      "appBundleArn": "string",
      "arn": "string",
      "createdAt": "string",
      "ingestionType": "string",
      "state": "string",
      "tenantId": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_GetIngestion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestion](#API_GetIngestion_ResponseSyntax) **   <a name="appfabric-GetIngestion-response-ingestion"></a>
Contains information about an ingestion.
Type: [Ingestion](API_Ingestion.md) object

## Errors
<a name="API_GetIngestion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request rate exceeds the limit.
 ** quotaCode **
The code for the quota exceeded.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
 ** serviceCode **
The code of the service.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
 ** fieldList **
The field list.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetIngestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/GetIngestion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/GetIngestion)
