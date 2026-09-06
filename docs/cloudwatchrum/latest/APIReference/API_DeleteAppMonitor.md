---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteAppMonitor.html
---

# DeleteAppMonitor
<a name="API_DeleteAppMonitor"></a>

Deletes an existing app monitor. This immediately stops the collection of data.

## Request Syntax
<a name="API_DeleteAppMonitor_RequestSyntax"></a>

```
DELETE /appmonitor/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAppMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_DeleteAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-DeleteAppMonitor-request-uri-Name"></a>
The name of the app monitor to delete.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteAppMonitor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAppMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAppMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAppMonitor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

 ** InternalServerException **
Internal service exception.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
One of the arguments for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAppMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/DeleteAppMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/DeleteAppMonitor)
