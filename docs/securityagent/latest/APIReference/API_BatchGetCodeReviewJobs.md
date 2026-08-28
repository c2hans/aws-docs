---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetCodeReviewJobs.html
---

# BatchGetCodeReviewJobs
<a name="API_BatchGetCodeReviewJobs"></a>

Retrieves information about one or more code review jobs in an agent space.

## Request Syntax
<a name="API_BatchGetCodeReviewJobs_RequestSyntax"></a>

```
POST /BatchGetCodeReviewJobs HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "codeReviewJobIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetCodeReviewJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetCodeReviewJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetCodeReviewJobs_RequestSyntax) **   <a name="securityagent-BatchGetCodeReviewJobs-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the code review jobs.
Type: String
Required: Yes

 ** [codeReviewJobIds](#API_BatchGetCodeReviewJobs_RequestSyntax) **   <a name="securityagent-BatchGetCodeReviewJobs-request-codeReviewJobIds"></a>
The list of code review job identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetCodeReviewJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeReviewJobs": [
      {
         "codeRemediationStrategy": "string",
         "codeReviewId": "string",
         "codeReviewJobId": "string",
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
         "executionContext": [
            {
               "context": "string",
               "contextType": "string",
               "timestamp": "string"
            }
         ],
         "integratedRepositories": [
            {
               "branch": "string",
               "integrationId": "string",
               "providerResourceId": "string"
            }
         ],
         "logConfig": {
            "logGroup": "string",
            "logStream": "string"
         },
         "maxTaskHours": number,
         "overview": "string",
         "serviceRole": "string",
         "sourceCode": [
            {
               "s3Location": "string"
            }
         ],
         "status": "string",
         "steps": [
            {
               "createdAt": "string",
               "name": "string",
               "status": "string",
               "updatedAt": "string"
            }
         ],
         "title": "string",
         "updatedAt": "string"
      }
   ],
   "notFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetCodeReviewJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeReviewJobs](#API_BatchGetCodeReviewJobs_ResponseSyntax) **   <a name="securityagent-BatchGetCodeReviewJobs-response-codeReviewJobs"></a>
The list of code review jobs that were found.
Type: Array of [CodeReviewJob](API_CodeReviewJob.md) objects

 ** [notFound](#API_BatchGetCodeReviewJobs_ResponseSyntax) **   <a name="securityagent-BatchGetCodeReviewJobs-response-notFound"></a>
The list of code review job identifiers that were not found.
Type: Array of strings

## Errors
<a name="API_BatchGetCodeReviewJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetCodeReviewJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetCodeReviewJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetCodeReviewJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
