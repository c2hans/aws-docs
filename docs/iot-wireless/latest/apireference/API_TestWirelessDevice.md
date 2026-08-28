---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_TestWirelessDevice.html
---

# TestWirelessDevice
<a name="API_TestWirelessDevice"></a>

Simulates a provisioned device by sending an uplink data payload of `Hello`.

## Request Syntax
<a name="API_TestWirelessDevice_RequestSyntax"></a>

```
POST /wireless-devices/{{Id}}/test HTTP/1.1
```

## URI Request Parameters
<a name="API_TestWirelessDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_TestWirelessDevice_RequestSyntax) **   <a name="iotwireless-TestWirelessDevice-request-uri-Id"></a>
The ID of the wireless device to test.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_TestWirelessDevice_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_TestWirelessDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Result": "string"
}
```

## Response Elements
<a name="API_TestWirelessDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Result](#API_TestWirelessDevice_ResponseSyntax) **   <a name="iotwireless-TestWirelessDevice-response-Result"></a>
The result returned by the test.
Type: String
Length Constraints: Maximum length of 2048.

## Errors
<a name="API_TestWirelessDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_TestWirelessDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/TestWirelessDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/TestWirelessDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
