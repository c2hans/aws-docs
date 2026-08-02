---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_StopApplication.html
---

# StopApplication
<a name="API_StopApplication"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Stops a running application.

## Request Syntax
<a name="API_StopApplication_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/stop HTTP/1.1
Content-type: application/json

{
   "forceStop": {{boolean}}
}
```

## URI Request Parameters
<a name="API_StopApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_StopApplication_RequestSyntax) **   <a name="m2-StopApplication-request-uri-applicationId"></a>
The unique identifier of the application you want to stop.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_StopApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [forceStop](#API_StopApplication_RequestSyntax) **   <a name="m2-StopApplication-request-forceStop"></a>
Stopping an application process can take a long time. Setting this parameter to true lets you force stop the application so you don't need to wait until the process finishes to apply another action on the application. The default value is false.
Type: Boolean
Required: No

## Response Syntax
<a name="API_StopApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** ConflictException **
The parameters provided in the request conflict with existing resources.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

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
<a name="API_StopApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/StopApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/StopApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/StopApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/StopApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/StopApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/StopApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/StopApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/StopApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/StopApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/StopApplication)
