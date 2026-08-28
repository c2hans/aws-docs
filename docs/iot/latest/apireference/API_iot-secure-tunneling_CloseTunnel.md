---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_CloseTunnel.html
---

# CloseTunnel
<a name="API_iot-secure-tunneling_CloseTunnel"></a>

Closes a tunnel identified by the unique tunnel id. When a `CloseTunnel` request is received, we close the WebSocket connections between the client and proxy server so no data can be transmitted.

Requires permission to access the [CloseTunnel](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iot-secure-tunneling_CloseTunnel_RequestSyntax"></a>

```
{
   "delete": {{boolean}},
   "tunnelId": "{{string}}"
}
```

## Request Parameters
<a name="API_iot-secure-tunneling_CloseTunnel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [delete](#API_iot-secure-tunneling_CloseTunnel_RequestSyntax) **   <a name="iot-iot-secure-tunneling_CloseTunnel-request-delete"></a>
When set to true, AWS IoT Secure Tunneling deletes the tunnel data immediately.
Type: Boolean
Required: No

 ** [tunnelId](#API_iot-secure-tunneling_CloseTunnel_RequestSyntax) **   <a name="iot-iot-secure-tunneling_CloseTunnel-request-tunnelId"></a>
The ID of the tunnel to close.
Type: String
Pattern: `[a-zA-Z0-9_\-+=:]{1,128}`
Required: Yes

## Response Elements
<a name="API_iot-secure-tunneling_CloseTunnel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_iot-secure-tunneling_CloseTunnel_Errors"></a>

 ** ResourceNotFoundException **
Thrown when an operation is attempted on a resource that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_iot-secure-tunneling_CloseTunnel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsecuretunneling-2018-10-05/CloseTunnel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/CloseTunnel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
