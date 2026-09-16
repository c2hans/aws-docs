---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeTestExecution.html
---

# DescribeTestExecution
<a name="API_DescribeTestExecution"></a>

Gets metadata information about the test execution.

## Request Syntax
<a name="API_DescribeTestExecution_RequestSyntax"></a>

```
GET /testexecutions/{{testExecutionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTestExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testExecutionId](#API_DescribeTestExecution_RequestSyntax) **   <a name="lexv2-DescribeTestExecution-request-uri-testExecutionId"></a>
The execution Id of the test set execution.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeTestExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTestExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiMode": "string",
   "creationDateTime": number,
   "failureReasons": [ "string" ],
   "lastUpdatedDateTime": number,
   "target": {
      "botAliasTarget": {
         "botAliasId": "string",
         "botId": "string",
         "localeId": "string"
      }
   },
   "testExecutionId": "string",
   "testExecutionModality": "string",
   "testExecutionStatus": "string",
   "testSetId": "string",
   "testSetName": "string"
}
```

## Response Elements
<a name="API_DescribeTestExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiMode](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-apiMode"></a>
Indicates whether we use streaming or non-streaming APIs are used for the test set execution. For streaming, `StartConversation` Amazon Lex Runtime API is used. Whereas for non-streaming, `RecognizeUtterance` and `RecognizeText` Amazon Lex Runtime API is used.
Type: String
Valid Values: `Streaming | NonStreaming`

 ** [creationDateTime](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-creationDateTime"></a>
The execution creation date and time for the test set execution.
Type: Timestamp

 ** [failureReasons](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-failureReasons"></a>
Reasons for the failure of the test set execution.
Type: Array of strings

 ** [lastUpdatedDateTime](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-lastUpdatedDateTime"></a>
The date and time of the last update for the execution.
Type: Timestamp

 ** [target](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-target"></a>
The target bot for the test set execution details.
Type: [TestExecutionTarget](API_TestExecutionTarget.md) object

 ** [testExecutionId](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-testExecutionId"></a>
The execution Id for the test set execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testExecutionModality](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-testExecutionModality"></a>
Indicates whether test set is audio or text.
Type: String
Valid Values: `Text | Audio`

 ** [testExecutionStatus](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-testExecutionStatus"></a>
The test execution status for the test execution.
Type: String
Valid Values: `Pending | Waiting | InProgress | Completed | Failed | Stopping | Stopped`

 ** [testSetId](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-testSetId"></a>
The test set Id for the test set execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testSetName](#API_DescribeTestExecution_ResponseSyntax) **   <a name="lexv2-DescribeTestExecution-response-testSetName"></a>
The test set name of the test set execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

## Errors
<a name="API_DescribeTestExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeTestExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeTestExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeTestExecution)
