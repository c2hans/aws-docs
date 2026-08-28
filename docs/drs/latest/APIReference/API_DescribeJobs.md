---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeJobs.html
---

# DescribeJobs
<a name="API_DescribeJobs"></a>

Returns a list of Jobs. Use the JobsID and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are created by the StartRecovery, TerminateRecoveryInstances and StartFailbackLaunch APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to \*Support\* and only used in response to relevant support tickets.

## Request Syntax
<a name="API_DescribeJobs_RequestSyntax"></a>

```
POST /DescribeJobs HTTP/1.1
Content-type: application/json

{
   "filters": {
      "fromDate": "{{string}}",
      "jobIDs": [ "{{string}}" ],
      "toDate": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeJobs_RequestSyntax) **   <a name="drs-DescribeJobs-request-filters"></a>
A set of filters by which to return Jobs.
Type: [DescribeJobsRequestFilters](API_DescribeJobsRequestFilters.md) object
Required: No

 ** [maxResults](#API_DescribeJobs_RequestSyntax) **   <a name="drs-DescribeJobs-request-maxResults"></a>
Maximum number of Jobs to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_DescribeJobs_RequestSyntax) **   <a name="drs-DescribeJobs-request-nextToken"></a>
The token of the next Job to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "creationDateTime": "string",
         "endDateTime": "string",
         "initiatedBy": "string",
         "jobID": "string",
         "participatingResources": [
            {
               "launchStatus": "string",
               "participatingResourceID": { ... }
            }
         ],
         "participatingServers": [
            {
               "launchActionsStatus": {
                  "runs": [
                     {
                        "action": {
                           "actionCode": "string",
                           "actionId": "string",
                           "actionVersion": "string",
                           "active": boolean,
                           "category": "string",
                           "description": "string",
                           "name": "string",
                           "optional": boolean,
                           "order": number,
                           "parameters": {
                              "string" : {
                                 "type": "string",
                                 "value": "string"
                              }
                           },
                           "type": "string"
                        },
                        "failureReason": "string",
                        "runId": "string",
                        "status": "string"
                     }
                  ],
                  "ssmAgentDiscoveryDatetime": "string"
               },
               "launchStatus": "string",
               "recoveryInstanceID": "string",
               "sourceServerID": "string"
            }
         ],
         "status": "string",
         "tags": {
            "string" : "string"
         },
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeJobs_ResponseSyntax) **   <a name="drs-DescribeJobs-response-items"></a>
An array of Jobs.
Type: Array of [Job](API_Job.md) objects

 ** [nextToken](#API_DescribeJobs_ResponseSyntax) **   <a name="drs-DescribeJobs-response-nextToken"></a>
The token of the next Job to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DescribeJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
