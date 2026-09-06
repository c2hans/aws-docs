---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GetApplicationVersion.html
---

# GetApplicationVersion
<a name="API_GetApplicationVersion"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Returns details about a specific version of a specific application.

## Request Syntax
<a name="API_GetApplicationVersion_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/versions/{{applicationVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplicationVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetApplicationVersion_RequestSyntax) **   <a name="m2-GetApplicationVersion-request-uri-applicationId"></a>
The unique identifier of the application.
Pattern: `\S{1,80}`
Required: Yes

 ** [applicationVersion](#API_GetApplicationVersion_RequestSyntax) **   <a name="m2-GetApplicationVersion-request-uri-applicationVersion"></a>
The specific version of the application.
Valid Range: Minimum value of 1.
Required: Yes

## Request Body
<a name="API_GetApplicationVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApplicationVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationVersion": number,
   "creationTime": number,
   "definitionContent": "string",
   "description": "string",
   "name": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_GetApplicationVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationVersion](#API_GetApplicationVersion_ResponseSyntax) **   <a name="m2-GetApplicationVersion-response-applicationVersion"></a>
The specific version of the application.
Type: Integer
Valid Range: Minimum value of 1.

 ** [creationTime](#API_GetApplicationVersion_ResponseSyntax) **   <a name="m2-GetApplicationVersion-response-creationTime"></a>
The timestamp when the application version was created.
Type: Timestamp

 ** [definitionContent](#API_GetApplicationVersion_ResponseSyntax) **   <a name="m2-GetApplicationVersion-response-definitionContent"></a>
The content of the application definition. This is a JSON object that contains the resource configuration and definitions that identify an application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65000.

 ** [description](#API_GetApplicationVersion_ResponseSyntax) **   <a name="m2-GetApplicationVersion-response-description"></a>
The application description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [name](#API_GetApplicationVersion_ResponseSyntax) **   <a name="m2-GetApplicationVersion-response-name"></a>
The name of the application version.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`

 ** [status](#API_GetApplicationVersion_ResponseSyntax) **   <a name="m2-GetApplicationVersion-response-status"></a>
The status of the application version.
Type: String
Valid Values: `Creating | Available | Failed`

 ** [statusReason](#API_GetApplicationVersion_ResponseSyntax) **   <a name="m2-GetApplicationVersion-response-statusReason"></a>
The reason for the reported status.
Type: String

## Errors
<a name="API_GetApplicationVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_GetApplicationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/GetApplicationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GetApplicationVersion)
