---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListKnowledgeBaseRefreshSchedules.html
---

# ListKnowledgeBaseRefreshSchedules

Lists the refresh schedules for an Amazon Quick Sight knowledge base. Currently, a knowledge base can have only one refresh schedule, so the list contains at most one schedule. Results are paginated. To retrieve the next page of results, use the `NextToken` value from the previous response.

## Request Syntax
<a name="API_ListKnowledgeBaseRefreshSchedules_RequestSyntax"></a>

```
GET /v1/accounts/{{AwsAccountId}}/knowledge-bases/{{KnowledgeBaseId}}/kb-refresh-schedules?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListKnowledgeBaseRefreshSchedules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListKnowledgeBaseRefreshSchedules_RequestSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the knowledge base.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: Yes

 ** [KnowledgeBaseId](#API_ListKnowledgeBaseRefreshSchedules_RequestSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-request-uri-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

 ** [MaxResults](#API_ListKnowledgeBaseRefreshSchedules_RequestSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-request-uri-MaxResults"></a>
The maximum number of results to return in a single page. Valid values are 1 through 100. If you don't specify a value, the default is 25.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListKnowledgeBaseRefreshSchedules_RequestSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-request-uri-NextToken"></a>
The token for the next set of results. If you don't specify a value, the request returns the first page of results.
Length Constraints: Minimum length of 1. Maximum length of 800.

## Request Body
<a name="API_ListKnowledgeBaseRefreshSchedules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListKnowledgeBaseRefreshSchedules_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "KnowledgeBaseArn": "string",
   "NextToken": "string",
   "RequestId": "string",
   "ScheduleSummaries": [
      {
         "ScheduleFrequency": {
            "Interval": "string",
            "RefreshOnDay": {
               "DayOfMonth": "string",
               "DayOfWeek": "string"
            }
         },
         "ScheduleId": "string",
         "StartTime": number,
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListKnowledgeBaseRefreshSchedules_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListKnowledgeBaseRefreshSchedules_ResponseSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [KnowledgeBaseArn](#API_ListKnowledgeBaseRefreshSchedules_ResponseSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-response-KnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base that the schedules apply to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [ScheduleSummaries](#API_ListKnowledgeBaseRefreshSchedules_ResponseSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-response-ScheduleSummaries"></a>
A list of refresh schedules for the knowledge base.
Type: Array of [KnowledgeBaseRefreshScheduleSummary](API_KnowledgeBaseRefreshScheduleSummary.md) objects

 ** [NextToken](#API_ListKnowledgeBaseRefreshSchedules_ResponseSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [RequestId](#API_ListKnowledgeBaseRefreshSchedules_ResponseSyntax) **   <a name="QS-ListKnowledgeBaseRefreshSchedules-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_ListKnowledgeBaseRefreshSchedules_Errors"></a>

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

 ** InvalidNextTokenException **
The `NextToken` value isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

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
<a name="API_ListKnowledgeBaseRefreshSchedules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListKnowledgeBaseRefreshSchedules)
