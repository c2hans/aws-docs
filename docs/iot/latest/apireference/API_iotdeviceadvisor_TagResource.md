---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TagResource.html
---

# TagResource
<a name="API_iotdeviceadvisor_TagResource"></a>

Adds to and modifies existing tags of an IoT Device Advisor resource.

Requires permission to access the [TagResource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_TagResource_RequestSyntax"></a>

```
POST /tags/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_iotdeviceadvisor_TagResource_RequestSyntax) **   <a name="iot-iotdeviceadvisor_TagResource-request-uri-resourceArn"></a>
The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_iotdeviceadvisor_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_iotdeviceadvisor_TagResource_RequestSyntax) **   <a name="iot-iotdeviceadvisor_TagResource-request-tags"></a>
The tags to be attached to the IoT Device Advisor resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_iotdeviceadvisor_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_iotdeviceadvisor_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_iotdeviceadvisor_TagResource_Errors"></a>

 ** InternalServerException **
Sends an Internal Failure exception.
 ** message **
Sends an Internal Failure Exception message.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Sends a Resource Not Found exception.
 ** message **
Sends a Resource Not Found Exception message.
HTTP Status Code: 404

 ** ValidationException **
Sends a validation exception.
 ** message **
Sends a Validation Exception message.
HTTP Status Code: 400

## See Also
<a name="API_iotdeviceadvisor_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/TagResource)
