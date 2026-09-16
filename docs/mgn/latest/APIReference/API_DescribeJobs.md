---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeJobs.html
---

# DescribeJobs
<a name="API_DescribeJobs"></a>

Returns a list of Jobs. Use the jobIDs and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDateTime - latest date first. Jobs are normally created by the StartTest, StartCutover, and TerminateTargetInstances APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to \*Support\* and only used in response to relevant support tickets.

## Request Syntax
<a name="API_DescribeJobs_RequestSyntax"></a>

```
POST /DescribeJobs HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
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

 ** [accountID](#API_DescribeJobs_RequestSyntax) **   <a name="mgn-DescribeJobs-request-accountID"></a>
Request to describe job log items by Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [filters](#API_DescribeJobs_RequestSyntax) **   <a name="mgn-DescribeJobs-request-filters"></a>
Request to describe Job log filters.
Type: [DescribeJobsRequestFilters](API_DescribeJobsRequestFilters.md) object
Required: No

 ** [maxResults](#API_DescribeJobs_RequestSyntax) **   <a name="mgn-DescribeJobs-request-maxResults"></a>
Request to describe job log items by max results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeJobs_RequestSyntax) **   <a name="mgn-DescribeJobs-request-nextToken"></a>
Request to describe job log items by next token.
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
         "participatingServers": [
            {
               "launchedEc2InstanceID": "string",
               "launchStatus": "string",
               "postLaunchActionsStatus": {
                  "postLaunchActionsLaunchStatusList": [
                     {
                        "executionID": "string",
                        "executionStatus": "string",
                        "failureReason": "string",
                        "ssmDocument": {
                           "actionName": "string",
                           "externalParameters": {
                              "string" : { ... }
                           },
                           "mustSucceedForCutover": boolean,
                           "parameters": {
                              "string" : [
                                 {
                                    "parameterName": "string",
                                    "parameterType": "string"
                                 }
                              ]
                           },
                           "ssmDocumentName": "string",
                           "timeoutSeconds": number
                        },
                        "ssmDocumentType": "string"
                     }
                  ],
                  "ssmAgentDiscoveryDatetime": "string"
               },
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

 ** [items](#API_DescribeJobs_ResponseSyntax) **   <a name="mgn-DescribeJobs-response-items"></a>
Request to describe Job log items.
Type: Array of [Job](API_Job.md) objects

 ** [nextToken](#API_DescribeJobs_ResponseSyntax) **   <a name="mgn-DescribeJobs-response-nextToken"></a>
Request to describe Job response by next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DescribeJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DescribeJobs)
