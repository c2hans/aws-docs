---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CancelCapacityTask.html
---

# CancelCapacityTask
<a name="API_CancelCapacityTask"></a>

Cancels the capacity task.

## Request Syntax
<a name="API_CancelCapacityTask_RequestSyntax"></a>

```
POST /outposts/{{OutpostId}}/capacity/{{CapacityTaskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelCapacityTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CapacityTaskId](#API_CancelCapacityTask_RequestSyntax) **   <a name="outposts-CancelCapacityTask-request-uri-CapacityTaskId"></a>
ID of the capacity task that you want to cancel.
Length Constraints: Fixed length of 21.
Pattern: `^cap-[a-f0-9]{17}$`
Required: Yes

 ** [OutpostId](#API_CancelCapacityTask_RequestSyntax) **   <a name="outposts-CancelCapacityTask-request-uri-OutpostIdentifier"></a>
ID or ARN of the Outpost associated with the capacity task that you want to cancel.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_CancelCapacityTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelCapacityTask_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelCapacityTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelCapacityTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource causing the conflict.
 ** ResourceType **
The type of the resource causing the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CancelCapacityTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/CancelCapacityTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CancelCapacityTask)
