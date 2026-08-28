---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_VerifyDevicePosition.html
---

# VerifyDevicePosition
<a name="API_VerifyDevicePosition"></a>

Verifies the integrity of the device's position by determining if it was reported behind a proxy, and by comparing it to an inferred position estimated based on the device's state.

**Note**
The Location Integrity SDK provides enhanced features related to device verification, and it is available for use by request. To get access to the SDK, contact [Sales Support](https://aws.amazon.com/contact-us/sales-support/?pg=locationprice&cta=herobtn).

## Request Syntax
<a name="API_VerifyDevicePosition_RequestSyntax"></a>

```
POST /tracking/v0/trackers/{{TrackerName}}/positions/verify HTTP/1.1
Content-type: application/json

{
   "DeviceState": {
      "Accuracy": {
         "Horizontal": {{number}}
      },
      "CellSignals": {
         "LteCellDetails": [
            {
               "CellId": {{number}},
               "LocalId": {
                  "Earfcn": {{number}},
                  "Pci": {{number}}
               },
               "Mcc": {{number}},
               "Mnc": {{number}},
               "NetworkMeasurements": [
                  {
                     "CellId": {{number}},
                     "Earfcn": {{number}},
                     "Pci": {{number}},
                     "Rsrp": {{number}},
                     "Rsrq": {{number}}
                  }
               ],
               "NrCapable": {{boolean}},
               "Rsrp": {{number}},
               "Rsrq": {{number}},
               "Tac": {{number}},
               "TimingAdvance": {{number}}
            }
         ]
      },
      "DeviceId": "{{string}}",
      "Ipv4Address": "{{string}}",
      "Position": [ {{number}} ],
      "SampleTime": "{{string}}",
      "WiFiAccessPoints": [
         {
            "MacAddress": "{{string}}",
            "Rss": {{number}}
         }
      ]
   },
   "DistanceUnit": "{{string}}"
}
```

## URI Request Parameters
<a name="API_VerifyDevicePosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_VerifyDevicePosition_RequestSyntax) **   <a name="location-VerifyDevicePosition-request-uri-TrackerName"></a>
The name of the tracker resource to be associated with verification request.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_VerifyDevicePosition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeviceState](#API_VerifyDevicePosition_RequestSyntax) **   <a name="location-VerifyDevicePosition-request-DeviceState"></a>
The device's state, including position, IP address, cell signals and Wi-Fi access points.
Type: [DeviceState](API_DeviceState.md) object
Required: Yes

 ** [DistanceUnit](#API_VerifyDevicePosition_RequestSyntax) **   <a name="location-VerifyDevicePosition-request-DistanceUnit"></a>
The distance unit for the verification request.
Default Value: `Kilometers`
Type: String
Valid Values: `Kilometers | Miles`
Required: No

## Response Syntax
<a name="API_VerifyDevicePosition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeviceId": "string",
   "DistanceUnit": "string",
   "InferredState": {
      "Accuracy": {
         "Horizontal": number
      },
      "DeviationDistance": number,
      "Position": [ number ],
      "ProxyDetected": boolean
   },
   "ReceivedTime": "string",
   "SampleTime": "string"
}
```

## Response Elements
<a name="API_VerifyDevicePosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeviceId](#API_VerifyDevicePosition_ResponseSyntax) **   <a name="location-VerifyDevicePosition-response-DeviceId"></a>
The device identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`

 ** [DistanceUnit](#API_VerifyDevicePosition_ResponseSyntax) **   <a name="location-VerifyDevicePosition-response-DistanceUnit"></a>
The distance unit for the verification response.
Type: String
Valid Values: `Kilometers | Miles`

 ** [InferredState](#API_VerifyDevicePosition_ResponseSyntax) **   <a name="location-VerifyDevicePosition-response-InferredState"></a>
The inferred state of the device, given the provided position, IP address, cellular signals, and Wi-Fi- access points.
Type: [InferredState](API_InferredState.md) object

 ** [ReceivedTime](#API_VerifyDevicePosition_ResponseSyntax) **   <a name="location-VerifyDevicePosition-response-ReceivedTime"></a>
The timestamp for when the tracker resource received the device position in [ ISO 8601 ](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [SampleTime](#API_VerifyDevicePosition_ResponseSyntax) **   <a name="location-VerifyDevicePosition-response-SampleTime"></a>
The timestamp at which the device's position was determined. Uses [ ISO 8601 ](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

## Errors
<a name="API_VerifyDevicePosition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource that you've entered was not found in your AWS account.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_VerifyDevicePosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/VerifyDevicePosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/VerifyDevicePosition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
