---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ListSchedules.html
---

# ListSchedules
<a name="API_ListSchedules"></a>

Returns a paginated list of your EventBridge Scheduler schedules.

## Request Syntax
<a name="API_ListSchedules_RequestSyntax"></a>

```
GET /schedules?MaxResults={{MaxResults}}&NamePrefix={{NamePrefix}}&NextToken={{NextToken}}&ScheduleGroup={{GroupName}}&State={{State}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSchedules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [GroupName](#API_ListSchedules_RequestSyntax) **   <a name="scheduler-ListSchedules-request-uri-GroupName"></a>
If specified, only lists the schedules whose associated schedule group matches the given filter.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`

 ** [MaxResults](#API_ListSchedules_RequestSyntax) **   <a name="scheduler-ListSchedules-request-uri-MaxResults"></a>
If specified, limits the number of results returned by this operation. The operation also returns a `NextToken` which you can use in a subsequent operation to retrieve the next set of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NamePrefix](#API_ListSchedules_RequestSyntax) **   <a name="scheduler-ListSchedules-request-uri-NamePrefix"></a>
Schedule name prefix to return the filtered list of resources.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`

 ** [NextToken](#API_ListSchedules_RequestSyntax) **   <a name="scheduler-ListSchedules-request-uri-NextToken"></a>
The token returned by a previous call to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [State](#API_ListSchedules_RequestSyntax) **   <a name="scheduler-ListSchedules-request-uri-State"></a>
If specified, only lists the schedules whose current state matches the given filter.
Valid Values: `ENABLED | DISABLED`

## Request Body
<a name="API_ListSchedules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSchedules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Schedules": [
      {
         "Arn": "string",
         "CreationDate": number,
         "GroupName": "string",
         "LastModificationDate": number,
         "Name": "string",
         "State": "string",
         "Target": {
            "Arn": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListSchedules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSchedules_ResponseSyntax) **   <a name="scheduler-ListSchedules-response-NextToken"></a>
Indicates whether there are additional results to retrieve. If the value is null, there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Schedules](#API_ListSchedules_ResponseSyntax) **   <a name="scheduler-ListSchedules-response-Schedules"></a>
The schedules that match the specified criteria.
Type: Array of [ScheduleSummary](API_ScheduleSummary.md) objects

## Errors
<a name="API_ListSchedules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListSchedules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/ListSchedules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/ListSchedules)
