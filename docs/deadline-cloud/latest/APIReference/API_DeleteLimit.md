---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteLimit.html
---

# DeleteLimit
<a name="API_DeleteLimit"></a>

Removes a limit from the specified farm. Before you delete a limit you must use the `DeleteQueueLimitAssociation` operation to remove the association with any queues.

## Request Syntax
<a name="API_DeleteLimit_RequestSyntax"></a>

```
DELETE /2023-10-12/farms/{{farmId}}/limits/{{limitId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteLimit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_DeleteLimit_RequestSyntax) **   <a name="deadlinecloud-DeleteLimit-request-uri-farmId"></a>
The unique identifier of the farm that contains the limit to delete.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [limitId](#API_DeleteLimit_RequestSyntax) **   <a name="deadlinecloud-DeleteLimit-request-uri-limitId"></a>
The unique identifier of the limit to delete.
Pattern: `limit-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_DeleteLimit_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteLimit_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DeleteLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/DeleteLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/DeleteLimit)
