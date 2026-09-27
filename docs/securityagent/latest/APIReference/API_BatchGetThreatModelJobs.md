---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetThreatModelJobs.html
---

# BatchGetThreatModelJobs
<a name="API_BatchGetThreatModelJobs"></a>

Retrieves information about one or more threat model jobs in an agent space.

## Request Syntax
<a name="API_BatchGetThreatModelJobs_RequestSyntax"></a>

```
POST /BatchGetThreatModelJobs HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "threatModelJobIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetThreatModelJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetThreatModelJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetThreatModelJobs_RequestSyntax) **   <a name="securityagent-BatchGetThreatModelJobs-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the threat model jobs.
Type: String
Required: Yes

 ** [threatModelJobIds](#API_BatchGetThreatModelJobs_RequestSyntax) **   <a name="securityagent-BatchGetThreatModelJobs-request-threatModelJobIds"></a>
The list of threat model job identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetThreatModelJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notFound": [ "string" ],
   "threatModelJobs": [
      {
         "agentSpaceId": "string",
         "createdAt": "string",
         "documents": [
            {
               "artifactId": "string",
               "integratedDocument": {
                  "integrationId": "string",
                  "resourceId": "string"
               },
               "s3Location": "string"
            }
         ],
         "errorInformation": {
            "code": "string",
            "message": "string"
         },
         "executionEndTime": "string",
         "executionStartTime": "string",
         "integratedRepositories": [
            {
               "branch": "string",
               "integrationId": "string",
               "providerResourceId": "string"
            }
         ],
         "reportDestination": {
            "containerId": "string",
            "documentId": "string",
            "integrationId": "string",
            "parentId": "string"
         },
         "scopeDocs": [
            {
               "artifactId": "string",
               "integratedDocument": {
                  "integrationId": "string",
                  "resourceId": "string"
               },
               "s3Location": "string"
            }
         ],
         "sourceCode": [
            {
               "s3Location": "string"
            }
         ],
         "status": "string",
         "systemOverview": "string",
         "threatModelId": "string",
         "threatModelJobId": "string",
         "title": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetThreatModelJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notFound](#API_BatchGetThreatModelJobs_ResponseSyntax) **   <a name="securityagent-BatchGetThreatModelJobs-response-notFound"></a>
The list of threat model job identifiers that were not found.
Type: Array of strings

 ** [threatModelJobs](#API_BatchGetThreatModelJobs_ResponseSyntax) **   <a name="securityagent-BatchGetThreatModelJobs-response-threatModelJobs"></a>
The list of threat model jobs that were found.
Type: Array of [ThreatModelJob](API_ThreatModelJob.md) objects

## Errors
<a name="API_BatchGetThreatModelJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetThreatModelJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetThreatModelJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetThreatModelJobs)
