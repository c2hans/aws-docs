---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeGuardrailChecks.html
---

# InvokeGuardrailChecks
<a name="API_runtime_InvokeGuardrailChecks"></a>

Evaluates messages against inline guardrail checks. You specify the check configurations directly in the request, and Amazon Bedrock returns per-check results with severity or confidence scores.

## Request Syntax
<a name="API_runtime_InvokeGuardrailChecks_RequestSyntax"></a>

```
POST /guardrail-checks/invoke HTTP/1.1
Content-type: application/json

{
   "checks": {
      "contentFilter": {
         "categories": [
            {
               "category": "{{string}}"
            }
         ]
      },
      "promptAttack": {
         "categories": [
            {
               "category": "{{string}}"
            }
         ]
      },
      "sensitiveInformation": {
         "entities": [
            {
               "type": "{{string}}"
            }
         ]
      }
   },
   "messages": [
      {
         "content": [
            { ... }
         ],
         "role": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_runtime_InvokeGuardrailChecks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_runtime_InvokeGuardrailChecks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [checks](#API_runtime_InvokeGuardrailChecks_RequestSyntax) **   <a name="bedrock-runtime_InvokeGuardrailChecks-request-checks"></a>
The inline check configurations that specify which guardrail checks to run against the messages.
Type: [GuardrailChecksConfig](API_runtime_GuardrailChecksConfig.md) object
Required: Yes

 ** [messages](#API_runtime_InvokeGuardrailChecks_RequestSyntax) **   <a name="bedrock-runtime_InvokeGuardrailChecks-request-messages"></a>
The messages to evaluate against the specified guardrail checks. Each message includes a role and one or more content blocks.
Type: Array of [GuardrailChecksMessage](API_runtime_GuardrailChecksMessage.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_runtime_InvokeGuardrailChecks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "results": {
      "contentFilter": {
         "results": [
            {
               "category": "string",
               "severityScore": number
            }
         ]
      },
      "promptAttack": {
         "results": [
            {
               "category": "string",
               "severityScore": number
            }
         ]
      },
      "sensitiveInformation": {
         "results": [
            {
               "beginOffset": number,
               "confidenceScore": number,
               "contentIndex": number,
               "endOffset": number,
               "messageIndex": number,
               "type": "string"
            }
         ],
         "truncated": boolean
      }
   },
   "usage": {
      "contentFilter": {
         "textUnits": number
      },
      "promptAttack": {
         "textUnits": number
      },
      "sensitiveInformation": {
         "textUnits": number
      }
   }
}
```

## Response Elements
<a name="API_runtime_InvokeGuardrailChecks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [results](#API_runtime_InvokeGuardrailChecks_ResponseSyntax) **   <a name="bedrock-runtime_InvokeGuardrailChecks-response-results"></a>
The per-check results containing findings from the guardrail evaluation.
Type: [GuardrailChecksResults](API_runtime_GuardrailChecksResults.md) object

 ** [usage](#API_runtime_InvokeGuardrailChecks_ResponseSyntax) **   <a name="bedrock-runtime_InvokeGuardrailChecks-response-usage"></a>
The per-check text unit consumption for the guardrail evaluation.
Type: [GuardrailChecksUsageResults](API_runtime_GuardrailChecksUsageResults.md) object

## Errors
<a name="API_runtime_InvokeGuardrailChecks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. For troubleshooting this error, see [InternalFailure](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure) in the Amazon Bedrock User Guide
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service isn't currently available. For troubleshooting this error, see [ServiceUnavailable](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable) in the Amazon Bedrock User Guide
HTTP Status Code: 503

 ** ThrottlingException **
Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error, see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide
HTTP Status Code: 400

## See Also
<a name="API_runtime_InvokeGuardrailChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/InvokeGuardrailChecks)
