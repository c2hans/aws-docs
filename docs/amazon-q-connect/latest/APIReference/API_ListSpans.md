---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ListSpans.html
---

# ListSpans
<a name="API_amazon-q-connect_ListSpans"></a>

Retrieves AI agent execution traces for a session, providing granular visibility into agent orchestration flows, LLM interactions, and tool invocations.

## Request Syntax
<a name="API_amazon-q-connect_ListSpans_RequestSyntax"></a>

```
GET /assistants/{{assistantId}}/sessions/{{sessionId}}/spans?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_ListSpans_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_ListSpans_RequestSyntax) **   <a name="connect-amazon-q-connect_ListSpans-request-uri-assistantId"></a>
UUID or ARN of the Connect AI Assistant resource
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [maxResults](#API_amazon-q-connect_ListSpans_RequestSyntax) **   <a name="connect-amazon-q-connect_ListSpans-request-uri-maxResults"></a>
Maximum number of spans to return per page
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_amazon-q-connect_ListSpans_RequestSyntax) **   <a name="connect-amazon-q-connect_ListSpans-request-uri-nextToken"></a>
Pagination token for retrieving the next page of results
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [sessionId](#API_amazon-q-connect_ListSpans_RequestSyntax) **   <a name="connect-amazon-q-connect_ListSpans-request-uri-sessionId"></a>
UUID or ARN of the Connect AI Session resource
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_ListSpans_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_ListSpans_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "spans": [
      {
         "assistantId": "string",
         "attributes": {
            "agentId": "string",
            "aiAgentArn": "string",
            "aiAgentId": "string",
            "aiAgentInvoker": "string",
            "aiAgentName": "string",
            "aiAgentOrchestratorUseCase": "string",
            "aiAgentType": "string",
            "aiAgentVersion": number,
            "cacheReadInputTokens": number,
            "cacheWriteInputTokens": number,
            "contactId": "string",
            "errorType": "string",
            "guardrailAssessments": [
               {
                  "action": "string",
                  "guardrailId": "string",
                  "guardrailName": "string",
                  "policies": [
                     {
                        "action": "string",
                        "details": "string",
                        "policyType": "string"
                     }
                  ],
                  "source": "string"
               }
            ],
            "initialContactId": "string",
            "inputMessages": [
               {
                  "messageId": "string",
                  "participant": "string",
                  "timestamp": number,
                  "values": [
                     { ... }
                  ]
               }
            ],
            "instanceArn": "string",
            "operationName": "string",
            "outputMessages": [
               {
                  "messageId": "string",
                  "participant": "string",
                  "timestamp": number,
                  "values": [
                     { ... }
                  ]
               }
            ],
            "promptArn": "string",
            "promptId": "string",
            "promptName": "string",
            "promptType": "string",
            "promptVersion": number,
            "providerName": "string",
            "requestMaxTokens": number,
            "requestModel": "string",
            "responseFinishReasons": [ "string" ],
            "responseModel": "string",
            "sessionName": "string",
            "systemInstructions": [
               { ... }
            ],
            "temperature": number,
            "timeToFirstTokenMs": number,
            "topP": number,
            "usageInputTokens": number,
            "usageOutputTokens": number,
            "usageTotalTokens": number
         },
         "endTimestamp": number,
         "originRequestId": "string",
         "parentSpanId": "string",
         "requestId": "string",
         "sessionId": "string",
         "spanId": "string",
         "spanName": "string",
         "spanType": "string",
         "startTimestamp": number,
         "status": "string",
         "statusDescription": "string"
      }
   ]
}
```

## Response Elements
<a name="API_amazon-q-connect_ListSpans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_amazon-q-connect_ListSpans_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListSpans-response-nextToken"></a>
Pagination token for retrieving additional results
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [spans](#API_amazon-q-connect_ListSpans_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListSpans-response-spans"></a>
Array of span objects for the session
Type: Array of [Span](API_amazon-q-connect_Span.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_amazon-q-connect_ListSpans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_ListSpans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/ListSpans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ListSpans)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
