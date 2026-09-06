---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_BatchGetUserAccessTasks.html
---

# BatchGetUserAccessTasks
<a name="API_BatchGetUserAccessTasks"></a>

Gets user access details in a batch request.

This action polls data from the tasks that are kicked off by the `StartUserAccessTasks` action.

## Request Syntax
<a name="API_BatchGetUserAccessTasks_RequestSyntax"></a>

```
POST /useraccess/batchget HTTP/1.1
Content-type: application/json

{
   "appBundleIdentifier": "{{string}}",
   "taskIdList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetUserAccessTasks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetUserAccessTasks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appBundleIdentifier](#API_BatchGetUserAccessTasks_RequestSyntax) **   <a name="appfabric-BatchGetUserAccessTasks-request-appBundleIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [taskIdList](#API_BatchGetUserAccessTasks_RequestSyntax) **   <a name="appfabric-BatchGetUserAccessTasks-request-taskIdList"></a>
The tasks IDs to use for the request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_BatchGetUserAccessTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "userAccessResultsList": [
      {
         "app": "string",
         "email": "string",
         "resultStatus": "string",
         "taskError": {
            "errorCode": "string",
            "errorMessage": "string"
         },
         "taskId": "string",
         "tenantDisplayName": "string",
         "tenantId": "string",
         "userFirstName": "string",
         "userFullName": "string",
         "userId": "string",
         "userLastName": "string",
         "userStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetUserAccessTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [userAccessResultsList](#API_BatchGetUserAccessTasks_ResponseSyntax) **   <a name="appfabric-BatchGetUserAccessTasks-response-userAccessResultsList"></a>
Contains a list of user access results.
Type: Array of [UserAccessResultItem](API_UserAccessResultItem.md) objects

## Errors
<a name="API_BatchGetUserAccessTasks_Errors"></a>

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
<a name="API_BatchGetUserAccessTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/BatchGetUserAccessTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/BatchGetUserAccessTasks)
