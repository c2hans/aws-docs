---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_CancelTagSyncTask.html
---

# CancelTagSyncTask
<a name="API_CancelTagSyncTask"></a>

Cancels the specified tag-sync task.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:CancelTagSyncTask` on the application group
+  `resource-groups:DeleteGroup`

## Request Syntax
<a name="API_CancelTagSyncTask_RequestSyntax"></a>

```
POST /cancel-tag-sync-task HTTP/1.1
Content-type: application/json

{
   "TaskArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelTagSyncTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CancelTagSyncTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TaskArn](#API_CancelTagSyncTask_RequestSyntax) **   <a name="ARG-CancelTagSyncTask-request-TaskArn"></a>
The Amazon resource name (ARN) of the tag-sync task.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}/tag-sync-task/[a-z0-9]{26}`
Required: Yes

## Response Syntax
<a name="API_CancelTagSyncTask_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelTagSyncTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelTagSyncTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request includes one or more parameters that violate validation rules.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request. Check permissions.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal error occurred while processing the request. Try again later.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The request uses an HTTP method that isn't allowed for the specified resource.
HTTP Status Code: 405

 ** TooManyRequestsException **
You've exceeded throttling limits by making too many requests in a period of time.
HTTP Status Code: 429

 ** UnauthorizedException **
The request was rejected because it doesn't have valid credentials for the target resource.
HTTP Status Code: 401

## See Also
<a name="API_CancelTagSyncTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/CancelTagSyncTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/CancelTagSyncTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
