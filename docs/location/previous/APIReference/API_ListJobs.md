---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListJobs.html
---

# ListJobs
<a name="API_ListJobs"></a>

 `ListJobs` retrieves a list of jobs with optional filtering and pagination support.

For more information, see [Job concepts](https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
POST /metadata/v0/jobs/list-jobs HTTP/1.1
Content-type: application/json

{
   "Filter": {
      "JobStatus": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filter](#API_ListJobs_RequestSyntax) **   <a name="location-ListJobs-request-Filter"></a>
An optional structure containing criteria by which to filter job results.
Type: [JobsFilter](API_JobsFilter.md) object
Required: No

 ** [MaxResults](#API_ListJobs_RequestSyntax) **   <a name="location-ListJobs-request-MaxResults"></a>
Maximum number of jobs to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListJobs_RequestSyntax) **   <a name="location-ListJobs-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.
Required: No

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Entries": [
      {
         "Action": "string",
         "ActionOptions": {
            "ValidateAddress": {
               "AdditionalFeatures": [ "string" ]
            }
         },
         "CreatedAt": "string",
         "EndedAt": "string",
         "Error": {
            "Code": "string",
            "Messages": [ "string" ]
         },
         "ExecutionRoleArn": "string",
         "InputOptions": {
            "Format": "string",
            "Location": "string"
         },
         "JobArn": "string",
         "JobId": "string",
         "Name": "string",
         "OutputOptions": {
            "Format": "string",
            "Location": "string"
         },
         "Status": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_ListJobs_ResponseSyntax) **   <a name="location-ListJobs-response-Entries"></a>
List of jobs in your AWS account.
Type: Array of [ListJobsResponseEntry](API_ListJobsResponseEntry.md) objects

 ** [NextToken](#API_ListJobs_ResponseSyntax) **   <a name="location-ListJobs-response-NextToken"></a>
Token for retrieving the next page (present if more results available).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.

## Errors
<a name="API_ListJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/ListJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/ListJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/ListJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/ListJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/ListJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/ListJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/ListJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListJobs)
