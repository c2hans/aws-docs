---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_DeleteSchedule.html
---

# DeleteSchedule
<a name="API_DeleteSchedule"></a>

Deletes the specified schedule.

## Request Syntax
<a name="API_DeleteSchedule_RequestSyntax"></a>

```
DELETE /schedules/{{Name}}?clientToken={{ClientToken}}&groupName={{GroupName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientToken](#API_DeleteSchedule_RequestSyntax) **   <a name="scheduler-DeleteSchedule-request-uri-ClientToken"></a>
 Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`

 ** [GroupName](#API_DeleteSchedule_RequestSyntax) **   <a name="scheduler-DeleteSchedule-request-uri-GroupName"></a>
The name of the schedule group associated with this schedule. If you omit this, the default schedule group is used.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`

 ** [Name](#API_DeleteSchedule_RequestSyntax) **   <a name="scheduler-DeleteSchedule-request-uri-Name"></a>
The name of the schedule to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: Yes

## Request Body
<a name="API_DeleteSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteSchedule_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting the resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error encountered while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/DeleteSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/DeleteSchedule)
