---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_InvokeAssistant.html
---

# InvokeAssistant
<a name="API_InvokeAssistant"></a>

Invokes SiteWise Assistant to start or continue a conversation.

## Request Syntax
<a name="API_InvokeAssistant_RequestSyntax"></a>

```
POST /assistant/invocation HTTP/1.1
Content-type: application/json

{
   "conversationId": "{{string}}",
   "enableTrace": {{boolean}},
   "message": "{{string}}"
}
```

## URI Request Parameters
<a name="API_InvokeAssistant_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_InvokeAssistant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [conversationId](#API_InvokeAssistant_RequestSyntax) **   <a name="iotsitewise-InvokeAssistant-request-conversationId"></a>
The ID assigned to a conversation. AWS IoT SiteWise automatically generates a unique ID for you, and this parameter is never required. However, if you prefer to have your own ID, you must specify it here in UUID format. If you specify your own ID, it must be globally unique.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [enableTrace](#API_InvokeAssistant_RequestSyntax) **   <a name="iotsitewise-InvokeAssistant-request-enableTrace"></a>
Specifies if to turn trace on or not. It is used to track the SiteWise Assistant's reasoning, and data access process.
Type: Boolean
Required: No

 ** [message](#API_InvokeAssistant_RequestSyntax) **   <a name="iotsitewise-InvokeAssistant-request-message"></a>
A text message sent to the SiteWise Assistant by the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: Yes

## Response Syntax
<a name="API_InvokeAssistant_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-iotsitewise-assistant-conversation-id: {{conversationId}}
Content-type: application/json

{
   "accessDeniedException": {
   },
   "conflictingOperationException": {
   },
   "internalFailureException": {
   },
   "invalidRequestException": {
   },
   "limitExceededException": {
   },
   "output": {
      "citations": [
         {
            "content": {
               "text": "string"
            },
            "reference": {
               "dataset": {
                  "datasetArn": "string",
                  "source": {
                     "arn": "string",
                     "location": {
                        "uri": "string"
                     }
                  }
               }
            }
         }
      ],
      "message": "string"
   },
   "resourceNotFoundException": {
   },
   "throttlingException": {
   },
   "trace": {
      "text": "string"
   }
}
```

## Response Elements
<a name="API_InvokeAssistant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [conversationId](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-conversationId"></a>
The ID of the conversation, in UUID format. This ID uniquely identifies the conversation within AWS IoT SiteWise.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-accessDeniedException"></a>
Access is denied.
Type: Exception
HTTP Status Code: 403

 ** [conflictingOperationException](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-conflictingOperationException"></a>
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
Type: Exception
HTTP Status Code: 409

 ** [internalFailureException](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-internalFailureException"></a>
 AWS IoT SiteWise can't process your request right now. Try again later.
Type: Exception
HTTP Status Code: 500

 ** [invalidRequestException](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-invalidRequestException"></a>
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
Type: Exception
HTTP Status Code: 400

 ** [limitExceededException](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-limitExceededException"></a>
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Exception
HTTP Status Code: 410

 ** [output](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-output"></a>
Contains the SiteWise Assistant's response.
Type: [InvocationOutput](API_InvocationOutput.md) object

 ** [resourceNotFoundException](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-resourceNotFoundException"></a>
The requested resource can't be found.
Type: Exception
HTTP Status Code: 404

 ** [throttlingException](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-throttlingException"></a>
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Exception
HTTP Status Code: 429

 ** [trace](#API_InvokeAssistant_ResponseSyntax) **   <a name="iotsitewise-InvokeAssistant-response-trace"></a>
Contains tracing information of the SiteWise Assistant's reasoning and data access.
Type: [Trace](API_Trace.md) object

## Errors
<a name="API_InvokeAssistant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_InvokeAssistant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/InvokeAssistant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/InvokeAssistant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
