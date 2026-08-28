---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ListScheduleGroups.html
---

# ListScheduleGroups
<a name="API_ListScheduleGroups"></a>

Returns a paginated list of your schedule groups.

## Request Syntax
<a name="API_ListScheduleGroups_RequestSyntax"></a>

```
GET /schedule-groups?MaxResults={{MaxResults}}&NamePrefix={{NamePrefix}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListScheduleGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListScheduleGroups_RequestSyntax) **   <a name="scheduler-ListScheduleGroups-request-uri-MaxResults"></a>
If specified, limits the number of results returned by this operation. The operation also returns a `NextToken` which you can use in a subsequent operation to retrieve the next set of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NamePrefix](#API_ListScheduleGroups_RequestSyntax) **   <a name="scheduler-ListScheduleGroups-request-uri-NamePrefix"></a>
The name prefix that you can use to return a filtered list of your schedule groups.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`

 ** [NextToken](#API_ListScheduleGroups_RequestSyntax) **   <a name="scheduler-ListScheduleGroups-request-uri-NextToken"></a>
The token returned by a previous call to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListScheduleGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListScheduleGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ScheduleGroups": [
      {
         "Arn": "string",
         "CreationDate": number,
         "LastModificationDate": number,
         "Name": "string",
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListScheduleGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListScheduleGroups_ResponseSyntax) **   <a name="scheduler-ListScheduleGroups-response-NextToken"></a>
Indicates whether there are additional results to retrieve. If the value is null, there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [ScheduleGroups](#API_ListScheduleGroups_ResponseSyntax) **   <a name="scheduler-ListScheduleGroups-response-ScheduleGroups"></a>
The schedule groups that match the specified criteria.
Type: Array of [ScheduleGroupSummary](API_ScheduleGroupSummary.md) objects

## Errors
<a name="API_ListScheduleGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Unexpected error encountered while processing the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListScheduleGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/ListScheduleGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/ListScheduleGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
