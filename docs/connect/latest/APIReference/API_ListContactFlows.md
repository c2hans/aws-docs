---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactFlows.html
---

# ListContactFlows
<a name="API_ListContactFlows"></a>

Provides information about the flows for the specified Connect Customer instance.

You can also create and update flows using the [Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html).

For more information about flows, see [Flows](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-contact-flows.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_ListContactFlows_RequestSyntax"></a>

```
GET /contact-flows-summary/{{InstanceId}}?contactFlowTypes={{ContactFlowTypes}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContactFlows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowTypes](#API_ListContactFlows_RequestSyntax) **   <a name="connect-ListContactFlows-request-uri-ContactFlowTypes"></a>
The type of flow.
Array Members: Maximum number of 10 items.
Valid Values: `CONTACT_FLOW | CUSTOMER_QUEUE | CUSTOMER_HOLD | CUSTOMER_WHISPER | AGENT_HOLD | AGENT_WHISPER | OUTBOUND_WHISPER | AGENT_TRANSFER | QUEUE_TRANSFER | CAMPAIGN`

 ** [InstanceId](#API_ListContactFlows_RequestSyntax) **   <a name="connect-ListContactFlows-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListContactFlows_RequestSyntax) **   <a name="connect-ListContactFlows-request-uri-MaxResults"></a>
The maximum number of results to return per page. The default MaxResult size is 100.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListContactFlows_RequestSyntax) **   <a name="connect-ListContactFlows-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListContactFlows_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContactFlows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowSummaryList": [
      {
         "Arn": "string",
         "ContactFlowState": "string",
         "ContactFlowStatus": "string",
         "ContactFlowType": "string",
         "Id": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContactFlows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowSummaryList](#API_ListContactFlows_ResponseSyntax) **   <a name="connect-ListContactFlows-response-ContactFlowSummaryList"></a>
Information about the flows.
Type: Array of [ContactFlowSummary](API_ContactFlowSummary.md) objects

 ** [NextToken](#API_ListContactFlows_ResponseSyntax) **   <a name="connect-ListContactFlows-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListContactFlows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListContactFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListContactFlows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListContactFlows)
