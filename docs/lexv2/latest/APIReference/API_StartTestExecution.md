---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartTestExecution.html
---

# StartTestExecution
<a name="API_StartTestExecution"></a>

The action to start test set execution.

## Request Syntax
<a name="API_StartTestExecution_RequestSyntax"></a>

```
POST /testsets/{{testSetId}}/testexecutions HTTP/1.1
Content-type: application/json

{
   "apiMode": "{{string}}",
   "target": {
      "botAliasTarget": {
         "botAliasId": "{{string}}",
         "botId": "{{string}}",
         "localeId": "{{string}}"
      }
   },
   "testExecutionModality": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartTestExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testSetId](#API_StartTestExecution_RequestSyntax) **   <a name="lexv2-StartTestExecution-request-uri-testSetId"></a>
The test set Id for the test set execution.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_StartTestExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [apiMode](#API_StartTestExecution_RequestSyntax) **   <a name="lexv2-StartTestExecution-request-apiMode"></a>
Indicates whether we use streaming or non-streaming APIs for the test set execution. For streaming, StartConversation Runtime API is used. Whereas, for non-streaming, RecognizeUtterance and RecognizeText Amazon Lex Runtime API are used.
Type: String
Valid Values: `Streaming | NonStreaming`
Required: Yes

 ** [target](#API_StartTestExecution_RequestSyntax) **   <a name="lexv2-StartTestExecution-request-target"></a>
The target bot for the test set execution.
Type: [TestExecutionTarget](API_TestExecutionTarget.md) object
Required: Yes

 ** [testExecutionModality](#API_StartTestExecution_RequestSyntax) **   <a name="lexv2-StartTestExecution-request-testExecutionModality"></a>
Indicates whether audio or text is used.
Type: String
Valid Values: `Text | Audio`
Required: No

## Response Syntax
<a name="API_StartTestExecution_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "apiMode": "string",
   "creationDateTime": number,
   "target": {
      "botAliasTarget": {
         "botAliasId": "string",
         "botId": "string",
         "localeId": "string"
      }
   },
   "testExecutionId": "string",
   "testExecutionModality": "string",
   "testSetId": "string"
}
```

## Response Elements
<a name="API_StartTestExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [apiMode](#API_StartTestExecution_ResponseSyntax) **   <a name="lexv2-StartTestExecution-response-apiMode"></a>
Indicates whether we use streaming or non-streaming APIs for the test set execution. For streaming, StartConversation Amazon Lex Runtime API is used. Whereas for non-streaming, RecognizeUtterance and RecognizeText Amazon Lex Runtime API are used.
Type: String
Valid Values: `Streaming | NonStreaming`

 ** [creationDateTime](#API_StartTestExecution_ResponseSyntax) **   <a name="lexv2-StartTestExecution-response-creationDateTime"></a>
The creation date and time for the test set execution.
Type: Timestamp

 ** [target](#API_StartTestExecution_ResponseSyntax) **   <a name="lexv2-StartTestExecution-response-target"></a>
The target bot for the test set execution.
Type: [TestExecutionTarget](API_TestExecutionTarget.md) object

 ** [testExecutionId](#API_StartTestExecution_ResponseSyntax) **   <a name="lexv2-StartTestExecution-response-testExecutionId"></a>
The unique identifier of the test set execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testExecutionModality](#API_StartTestExecution_ResponseSyntax) **   <a name="lexv2-StartTestExecution-response-testExecutionModality"></a>
Indicates whether audio or text is used.
Type: String
Valid Values: `Text | Audio`

 ** [testSetId](#API_StartTestExecution_ResponseSyntax) **   <a name="lexv2-StartTestExecution-response-testSetId"></a>
The test set Id for the test set execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

## Errors
<a name="API_StartTestExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_StartTestExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/StartTestExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/StartTestExecution)
