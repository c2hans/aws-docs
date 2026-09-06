---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ListSchedules.html
---

# ListSchedules
<a name="API_ListSchedules"></a>

Lists the DataBrew schedules that are defined.

## Request Syntax
<a name="API_ListSchedules_RequestSyntax"></a>

```
GET /schedules?jobName={{JobName}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSchedules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobName](#API_ListSchedules_RequestSyntax) **   <a name="databrew-ListSchedules-request-uri-JobName"></a>
The name of the job that these schedules apply to.
Length Constraints: Minimum length of 1. Maximum length of 240.

 ** [MaxResults](#API_ListSchedules_RequestSyntax) **   <a name="databrew-ListSchedules-request-uri-MaxResults"></a>
The maximum number of results to return in this request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListSchedules_RequestSyntax) **   <a name="databrew-ListSchedules-request-uri-NextToken"></a>
The token returned by a previous call to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.

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
         "AccountId": "string",
         "CreateDate": number,
         "CreatedBy": "string",
         "CronExpression": "string",
         "JobNames": [ "string" ],
         "LastModifiedBy": "string",
         "LastModifiedDate": number,
         "Name": "string",
         "ResourceArn": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListSchedules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Schedules](#API_ListSchedules_ResponseSyntax) **   <a name="databrew-ListSchedules-response-Schedules"></a>
A list of schedules that are defined.
Type: Array of [Schedule](API_Schedule.md) objects

 ** [NextToken](#API_ListSchedules_ResponseSyntax) **   <a name="databrew-ListSchedules-response-NextToken"></a>
A token that you can use in a subsequent call to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListSchedules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListSchedules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/ListSchedules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ListSchedules)
