---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetFindings.html
---

# BatchGetFindings
<a name="API_BatchGetFindings"></a>

Retrieves information about one or more security findings in an agent space.

## Request Syntax
<a name="API_BatchGetFindings_RequestSyntax"></a>

```
POST /BatchGetFindings HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "findingIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetFindings_RequestSyntax) **   <a name="securityagent-BatchGetFindings-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the findings.
Type: String
Required: Yes

 ** [findingIds](#API_BatchGetFindings_RequestSyntax) **   <a name="securityagent-BatchGetFindings-request-findingIds"></a>
The list of finding identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findings": [
      {
         "agentSpaceId": "string",
         "alignmentRationale": "string",
         "attackScript": "string",
         "codeLocations": [
            {
               "filePath": "string",
               "label": "string",
               "lineEnd": number,
               "lineStart": number
            }
         ],
         "codeRemediationTask": {
            "status": "string",
            "statusReason": "string",
            "taskDetails": [
               {
                  "codeDiffLink": "string",
                  "pullRequestLink": "string",
                  "repoName": "string"
               }
            ]
         },
         "codeReviewId": "string",
         "codeReviewJobId": "string",
         "confidence": "string",
         "createdAt": "string",
         "customerNote": "string",
         "description": "string",
         "findingId": "string",
         "lastUpdatedBy": "string",
         "name": "string",
         "originalFindingId": "string",
         "pentestId": "string",
         "pentestJobId": "string",
         "reasoning": "string",
         "revalidationJobIds": [ "string" ],
         "riskLevel": "string",
         "riskScore": "string",
         "riskType": "string",
         "status": "string",
         "taskId": "string",
         "updatedAt": "string",
         "validationStatus": "string",
         "verificationScript": {
            "envVars": [
               {
                  "name": "string",
                  "value": "string"
               }
            ],
            "instructions": "string",
            "scriptType": "string",
            "scriptUrl": "string"
         }
      }
   ],
   "notFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findings](#API_BatchGetFindings_ResponseSyntax) **   <a name="securityagent-BatchGetFindings-response-findings"></a>
The list of findings that were found.
Type: Array of [Finding](API_Finding.md) objects

 ** [notFound](#API_BatchGetFindings_ResponseSyntax) **   <a name="securityagent-BatchGetFindings-response-notFound"></a>
The list of finding identifiers that were not found.
Type: Array of strings

## Errors
<a name="API_BatchGetFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
