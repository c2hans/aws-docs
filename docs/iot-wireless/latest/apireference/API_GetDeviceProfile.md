---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetDeviceProfile.html
---

# GetDeviceProfile
<a name="API_GetDeviceProfile"></a>

Gets information about a device profile.

## Request Syntax
<a name="API_GetDeviceProfile_RequestSyntax"></a>

```
GET /device-profiles/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDeviceProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetDeviceProfile_RequestSyntax) **   <a name="iotwireless-GetDeviceProfile-request-uri-Id"></a>
The ID of the resource to get.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetDeviceProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDeviceProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string",
   "LoRaWAN": {
      "ClassBTimeout": number,
      "ClassCTimeout": number,
      "FactoryPresetFreqsList": [ number ],
      "MacVersion": "string",
      "MaxDutyCycle": number,
      "MaxEirp": number,
      "PingSlotDr": number,
      "PingSlotFreq": number,
      "PingSlotPeriod": number,
      "RegParamsRevision": "string",
      "RfRegion": "string",
      "RxDataRate2": number,
      "RxDelay1": number,
      "RxDrOffset1": number,
      "RxFreq2": number,
      "Supports32BitFCnt": boolean,
      "SupportsClassB": boolean,
      "SupportsClassC": boolean,
      "SupportsJoin": boolean
   },
   "Name": "string",
   "Sidewalk": {
      "ApplicationServerPublicKey": "string",
      "DakCertificateMetadata": [
         {
            "ApId": "string",
            "CertificateId": "string",
            "DeviceTypeId": "string",
            "FactorySupport": boolean,
            "MaxAllowedSignature": number
         }
      ],
      "QualificationStatus": boolean
   }
}
```

## Response Elements
<a name="API_GetDeviceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetDeviceProfile_ResponseSyntax) **   <a name="iotwireless-GetDeviceProfile-response-Arn"></a>
The Amazon Resource Name of the resource.
Type: String

 ** [Id](#API_GetDeviceProfile_ResponseSyntax) **   <a name="iotwireless-GetDeviceProfile-response-Id"></a>
The ID of the device profile.
Type: String
Length Constraints: Maximum length of 256.

 ** [LoRaWAN](#API_GetDeviceProfile_ResponseSyntax) **   <a name="iotwireless-GetDeviceProfile-response-LoRaWAN"></a>
Information about the device profile.
Type: [LoRaWANDeviceProfile](API_LoRaWANDeviceProfile.md) object

 ** [Name](#API_GetDeviceProfile_ResponseSyntax) **   <a name="iotwireless-GetDeviceProfile-response-Name"></a>
The name of the resource.
Type: String
Length Constraints: Maximum length of 256.

 ** [Sidewalk](#API_GetDeviceProfile_ResponseSyntax) **   <a name="iotwireless-GetDeviceProfile-response-Sidewalk"></a>
Information about the Sidewalk parameters in the device profile.
Type: [SidewalkGetDeviceProfile](API_SidewalkGetDeviceProfile.md) object

## Errors
<a name="API_GetDeviceProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

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
<a name="API_GetDeviceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetDeviceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetDeviceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
