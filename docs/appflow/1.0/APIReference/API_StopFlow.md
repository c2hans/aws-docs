---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_StopFlow.html
---

# StopFlow
<a name="API_StopFlow"></a>

 Deactivates the existing flow. For on-demand flows, this operation returns an `unsupportedOperationException` error message. For schedule and event-triggered flows, this operation deactivates the flow.

## Request Syntax
<a name="API_StopFlow_RequestSyntax"></a>

```
POST /stop-flow HTTP/1.1
Content-type: application/json

{
   "flowName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopFlow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [flowName](#API_StopFlow_RequestSyntax) **   <a name="appflow-StopFlow-request-flowName"></a>
 The specified name of the flow. Spaces are not allowed. Use underscores (\_) or hyphens (-) only.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: Yes

## Response Syntax
<a name="API_StopFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowArn": "string",
   "flowStatus": "string"
}
```

## Response Elements
<a name="API_StopFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_StopFlow_ResponseSyntax) **   <a name="appflow-StopFlow-response-flowArn"></a>
 The flow's Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:appflow:.*:[0-9]+:.*`

 ** [flowStatus](#API_StopFlow_ResponseSyntax) **   <a name="appflow-StopFlow-response-flowStatus"></a>
 Indicates the current status of the flow.
Type: String
Valid Values: `Active | Deprecated | Deleted | Draft | Errored | Suspended`

## Errors
<a name="API_StopFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
 There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again.
HTTP Status Code: 409

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** UnsupportedOperationException **
 The requested operation is not supported for the current flow.
HTTP Status Code: 400

## Examples
<a name="API_StopFlow_Examples"></a>

### StopFlow example
<a name="API_StopFlow_Example_1"></a>

This example shows a sample request and response for the `StopFlow` API.

#### Sample Request
<a name="API_StopFlow_Example_1_Request"></a>

```
{
  "flowName": "name"
}
```

#### Sample Response
<a name="API_StopFlow_Example_1_Response"></a>

```
{
  "flowArn": "arn:aws:appflow:region:<AccountId>:flow/test_flow_ondemand_1",
  "flowStatus": "Suspended"
}
```

## See Also
<a name="API_StopFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/StopFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/StopFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/StopFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/StopFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/StopFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/StopFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/StopFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/StopFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/StopFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/StopFlow)
