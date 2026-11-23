---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteKnowledgeBaseRefreshSchedule.html
---

# DeleteKnowledgeBaseRefreshSchedule

Deletes the refresh schedule for an Amazon Quick Sight knowledge base. Delete the schedule when you no longer want the knowledge base to refresh automatically.

## Request Syntax
<a name="API_DeleteKnowledgeBaseRefreshSchedule_RequestSyntax"></a>

```
DELETE /v1/accounts/{{AwsAccountId}}/knowledge-bases/{{KnowledgeBaseId}}/kb-refresh-schedules/{{ScheduleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteKnowledgeBaseRefreshSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DeleteKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-DeleteKnowledgeBaseRefreshSchedule-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the knowledge base.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: Yes

 ** [KnowledgeBaseId](#API_DeleteKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-DeleteKnowledgeBaseRefreshSchedule-request-uri-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

 ** [ScheduleId](#API_DeleteKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-DeleteKnowledgeBaseRefreshSchedule-request-uri-ScheduleId"></a>
The unique identifier for the refresh schedule to delete.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z_=-][0-9a-zA-Z_=.-]*`
Required: Yes

## Request Body
<a name="API_DeleteKnowledgeBaseRefreshSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteKnowledgeBaseRefreshSchedule_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "KnowledgeBaseArn": "string",
   "RequestId": "string",
   "ScheduleId": "string"
}
```

## Response Elements
<a name="API_DeleteKnowledgeBaseRefreshSchedule_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteKnowledgeBaseRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteKnowledgeBaseRefreshSchedule-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [KnowledgeBaseArn](#API_DeleteKnowledgeBaseRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteKnowledgeBaseRefreshSchedule-response-KnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base that the schedule applied to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [ScheduleId](#API_DeleteKnowledgeBaseRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteKnowledgeBaseRefreshSchedule-response-ScheduleId"></a>
The unique identifier for the deleted refresh schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z_=-][0-9a-zA-Z_=.-]*`

 ** [RequestId](#API_DeleteKnowledgeBaseRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteKnowledgeBaseRefreshSchedule-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_DeleteKnowledgeBaseRefreshSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **
One or more preconditions aren't met.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DeleteKnowledgeBaseRefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteKnowledgeBaseRefreshSchedule)
