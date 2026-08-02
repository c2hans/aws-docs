---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StopFlow.html
---

# StopFlow
<a name="API_StopFlow"></a>

 Stops a flow.

## Request Syntax
<a name="API_StopFlow_RequestSyntax"></a>

```
POST /v1/flows/stop/{{flowArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_StopFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_StopFlow_RequestSyntax) **   <a name="mediaconnect-StopFlow-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow that you want to stop.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

## Request Body
<a name="API_StopFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopFlow_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "flowArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StopFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_StopFlow_ResponseSyntax) **   <a name="mediaconnect-StopFlow-response-flowArn"></a>
 The ARN of the flow that you stopped.
Type: String

 ** [status](#API_StopFlow_ResponseSyntax) **   <a name="mediaconnect-StopFlow-response-status"></a>
 The status of the flow when the `StopFlow` process begins.
Type: String
Valid Values: `STANDBY | ACTIVE | UPDATING | DELETING | STARTING | STOPPING | ERROR`

## Errors
<a name="API_StopFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_StopFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/StopFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StopFlow)
