---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_GetDevice.html
---

# GetDevice
<a name="API_GetDevice"></a>

Retrieves the devices available in Amazon Braket.

**Note**
For backwards compatibility with older versions of BraketSchemas, OpenQASM information is omitted from GetDevice API calls. To get this information the user-agent needs to present a recent version of the BraketSchemas (1.8.0 or later). The Braket SDK automatically reports this for you. If you do not see OpenQASM results in the GetDevice response when using a Braket SDK, you may need to set AWS\_EXECUTION\_ENV environment variable to configure user-agent. See the code examples provided below for how to do this for the AWS CLI, Boto3, and the Go, Java, and JavaScript/TypeScript SDKs.

## Request Syntax
<a name="API_GetDevice_RequestSyntax"></a>

```
GET /device/{{deviceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deviceArn](#API_GetDevice_RequestSyntax) **   <a name="braket-GetDevice-request-uri-deviceArn"></a>
The ARN of the device to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetDevice_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deviceArn": "string",
   "deviceCapabilities": "string",
   "deviceName": "string",
   "deviceQueueInfo": [
      {
         "queue": "string",
         "queuePriority": "string",
         "queueSize": "string"
      }
   ],
   "deviceStatus": "string",
   "deviceType": "string",
   "providerName": "string"
}
```

## Response Elements
<a name="API_GetDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deviceArn](#API_GetDevice_ResponseSyntax) **   <a name="braket-GetDevice-response-deviceArn"></a>
The ARN of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [deviceCapabilities](#API_GetDevice_ResponseSyntax) **   <a name="braket-GetDevice-response-deviceCapabilities"></a>
Details about the capabilities of the device.
Type: String

 ** [deviceName](#API_GetDevice_ResponseSyntax) **   <a name="braket-GetDevice-response-deviceName"></a>
The name of the device.
Type: String

 ** [deviceQueueInfo](#API_GetDevice_ResponseSyntax) **   <a name="braket-GetDevice-response-deviceQueueInfo"></a>
The number of quantum tasks and hybrid jobs currently queued on the device.
Type: Array of [DeviceQueueInfo](API_DeviceQueueInfo.md) objects

 ** [deviceStatus](#API_GetDevice_ResponseSyntax) **   <a name="braket-GetDevice-response-deviceStatus"></a>
The status of the device.
Type: String
Valid Values: `ONLINE | OFFLINE | RETIRED`

 ** [deviceType](#API_GetDevice_ResponseSyntax) **   <a name="braket-GetDevice-response-deviceType"></a>
The type of the device.
Type: String
Valid Values: `QPU | SIMULATOR`

 ** [providerName](#API_GetDevice_ResponseSyntax) **   <a name="braket-GetDevice-response-providerName"></a>
The name of the partner company for the device.
Type: String

## Errors
<a name="API_GetDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The API throttling rate limit is exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input request failed to satisfy constraints expected by Amazon Braket.
 ** programSetValidationFailures **
The validation failures in the program set submitted in the request.
 ** reason **
The reason for validation failure.
HTTP Status Code: 400

## Examples
<a name="API_GetDevice_Examples"></a>

### AWS CLI SDK example
<a name="API_GetDevice_Example_1"></a>

To set AWS\_EXECUTION\_ENV environment variable to configure user-agent when using the AWS CLI SDK:

```
% export AWS_EXECUTION_ENV="aws-cli BraketSchemas/1.8.0"
# Or for single execution
% AWS_EXECUTION_ENV="aws-cli BraketSchemas/1.8.0" aws braket <cmd> [options]
```

### Boto3 example
<a name="API_GetDevice_Example_2"></a>

To set AWS\_EXECUTION\_ENV environment variable to configure user-agent when using the Boto3:

```
import boto3
import botocore

client = boto3.client("braket", config=botocore.client.Config(user_agent_extra="BraketSchemas/1.8.0"))
```

### JavaScript/TypeScript (SDK v2) example
<a name="API_GetDevice_Example_3"></a>

To set AWS\_EXECUTION\_ENV environment variable to configure user-agent when using the JavaScript/TypeScript (SDK v2):

```
import Braket from 'aws-sdk/clients/braket';
const client = new Braket({ region: 'us-west-2', credentials: AWS_CREDENTIALS, customUserAgent: 'BraketSchemas/1.8.0'  });
```

### JavaScript/TypeScript (SDK v3) example
<a name="API_GetDevice_Example_4"></a>

To set AWS\_EXECUTION\_ENV environment variable to configure user-agent when using the JavaScript/TypeScript (SDK v3):

```
import { Braket } from '@aws-sdk/client-braket';
const client = new Braket({ region: 'us-west-2', credentials: AWS_CREDENTIALS, customUserAgent: 'BraketSchemas/1.8.0' });
```

### Go SDK example
<a name="API_GetDevice_Example_5"></a>

To set AWS\_EXECUTION\_ENV environment variable to configure user-agent when using the Go SDK:

```
os.Setenv("AWS_EXECUTION_ENV", "BraketGo BraketSchemas/1.8.0")
mySession := session.Must(session.NewSession())
svc := braket.New(mySession)
```

### Java SDK example
<a name="API_GetDevice_Example_6"></a>

To set AWS\_EXECUTION\_ENV environment variable to configure user-agent when using the Java SDK:

```
ClientConfiguration config = new ClientConfiguration();
config.setUserAgentSuffix("BraketSchemas/1.8.0");
BraketClient braketClient = BraketClientBuilder.standard().withClientConfiguration(config).build();
```

## See Also
<a name="API_GetDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/GetDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/GetDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/GetDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/GetDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/GetDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/GetDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/GetDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/GetDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/GetDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/GetDevice)
