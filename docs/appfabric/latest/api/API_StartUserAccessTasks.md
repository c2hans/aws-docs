---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_StartUserAccessTasks.html
---

# StartUserAccessTasks
<a name="API_StartUserAccessTasks"></a>

Starts the tasks to search user access status for a specific email address.

The tasks are stopped when the user access status data is found. The tasks are terminated when the API calls to the application time out.

## Request Syntax
<a name="API_StartUserAccessTasks_RequestSyntax"></a>

```
POST /useraccess/start HTTP/1.1
Content-type: application/json

{
   "appBundleIdentifier": "{{string}}",
   "email": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartUserAccessTasks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartUserAccessTasks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appBundleIdentifier](#API_StartUserAccessTasks_RequestSyntax) **   <a name="appfabric-StartUserAccessTasks-request-appBundleIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [email](#API_StartUserAccessTasks_RequestSyntax) **   <a name="appfabric-StartUserAccessTasks-request-email"></a>
The email address of the target user.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 320.
Pattern: `[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*`
Required: Yes

## Response Syntax
<a name="API_StartUserAccessTasks_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "userAccessTasksList": [
      {
         "app": "string",
         "error": {
            "errorCode": "string",
            "errorMessage": "string"
         },
         "taskId": "string",
         "tenantId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_StartUserAccessTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [userAccessTasksList](#API_StartUserAccessTasks_ResponseSyntax) **   <a name="appfabric-StartUserAccessTasks-response-userAccessTasksList"></a>
Contains a list of user access task information.
Type: Array of [UserAccessTaskItem](API_UserAccessTaskItem.md) objects

## Errors
<a name="API_StartUserAccessTasks_Errors"></a>

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
<a name="API_StartUserAccessTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/StartUserAccessTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/StartUserAccessTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
