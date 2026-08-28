---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetAgentSpaces.html
---

# BatchGetAgentSpaces
<a name="API_BatchGetAgentSpaces"></a>

Retrieves information about one or more agent spaces.

## Request Syntax
<a name="API_BatchGetAgentSpaces_RequestSyntax"></a>

```
POST /BatchGetAgentSpaces HTTP/1.1
Content-type: application/json

{
   "agentSpaceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetAgentSpaces_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetAgentSpaces_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceIds](#API_BatchGetAgentSpaces_RequestSyntax) **   <a name="securityagent-BatchGetAgentSpaces-request-agentSpaceIds"></a>
The list of agent space identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetAgentSpaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaces": [
      {
         "agentSpaceId": "string",
         "awsResources": {
            "iamRoles": [ "string" ],
            "lambdaFunctionArns": [ "string" ],
            "logGroups": [ "string" ],
            "s3Buckets": [ "string" ],
            "secretArns": [ "string" ],
            "vpcs": [
               {
                  "securityGroupArns": [ "string" ],
                  "subnetArns": [ "string" ],
                  "vpcArn": "string"
               }
            ]
         },
         "codeReviewSettings": {
            "controlsScanning": boolean,
            "generalPurposeScanning": boolean
         },
         "createdAt": "string",
         "description": "string",
         "kmsKeyId": "string",
         "name": "string",
         "targetDomainIds": [ "string" ],
         "updatedAt": "string"
      }
   ],
   "notFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetAgentSpaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaces](#API_BatchGetAgentSpaces_ResponseSyntax) **   <a name="securityagent-BatchGetAgentSpaces-response-agentSpaces"></a>
The list of agent spaces that were found.
Type: Array of [AgentSpace](API_AgentSpace.md) objects

 ** [notFound](#API_BatchGetAgentSpaces_ResponseSyntax) **   <a name="securityagent-BatchGetAgentSpaces-response-notFound"></a>
The list of agent space identifiers that were not found.
Type: Array of strings

## Errors
<a name="API_BatchGetAgentSpaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetAgentSpaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetAgentSpaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetAgentSpaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
