---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPositionEstimate.html
---

# GetPositionEstimate
<a name="API_GetPositionEstimate"></a>

Get estimated position information as a payload in GeoJSON format. The payload measurement data is resolved using solvers that are provided by third-party vendors.

## Request Syntax
<a name="API_GetPositionEstimate_RequestSyntax"></a>

```
POST /position-estimate HTTP/1.1
Content-type: application/json

{
   "AdvancedConfiguration": {
      "WiFiCellular": {
         "ConfidencePercent": {{number}}
      }
   },
   "CellTowers": {
      "Cdma": [
         {
            "BaseLat": {{number}},
            "BaseLng": {{number}},
            "BaseStationId": {{number}},
            "CdmaLocalId": {
               "CdmaChannel": {{number}},
               "PnOffset": {{number}}
            },
            "CdmaNmr": [
               {
                  "BaseStationId": {{number}},
                  "CdmaChannel": {{number}},
                  "PilotPower": {{number}},
                  "PnOffset": {{number}}
               }
            ],
            "NetworkId": {{number}},
            "PilotPower": {{number}},
            "RegistrationZone": {{number}},
            "SystemId": {{number}}
         }
      ],
      "Gsm": [
         {
            "GeranCid": {{number}},
            "GsmLocalId": {
               "Bcch": {{number}},
               "Bsic": {{number}}
            },
            "GsmNmr": [
               {
                  "Bcch": {{number}},
                  "Bsic": {{number}},
                  "GlobalIdentity": {
                     "GeranCid": {{number}},
                     "Lac": {{number}}
                  },
                  "RxLevel": {{number}}
               }
            ],
            "GsmTimingAdvance": {{number}},
            "Lac": {{number}},
            "Mcc": {{number}},
            "Mnc": {{number}},
            "RxLevel": {{number}}
         }
      ],
      "Lte": [
         {
            "EutranCid": {{number}},
            "LteLocalId": {
               "Earfcn": {{number}},
               "Pci": {{number}}
            },
            "LteNmr": [
               {
                  "Earfcn": {{number}},
                  "EutranCid": {{number}},
                  "Pci": {{number}},
                  "Rsrp": {{number}},
                  "Rsrq": {{number}}
               }
            ],
            "LteTimingAdvance": {{number}},
            "Mcc": {{number}},
            "Mnc": {{number}},
            "NrCapable": {{boolean}},
            "Rsrp": {{number}},
            "Rsrq": {{number}},
            "Tac": {{number}}
         }
      ],
      "Tdscdma": [
         {
            "Lac": {{number}},
            "Mcc": {{number}},
            "Mnc": {{number}},
            "PathLoss": {{number}},
            "Rscp": {{number}},
            "TdscdmaLocalId": {
               "CellParams": {{number}},
               "Uarfcn": {{number}}
            },
            "TdscdmaNmr": [
               {
                  "CellParams": {{number}},
                  "PathLoss": {{number}},
                  "Rscp": {{number}},
                  "Uarfcn": {{number}},
                  "UtranCid": {{number}}
               }
            ],
            "TdscdmaTimingAdvance": {{number}},
            "UtranCid": {{number}}
         }
      ],
      "Wcdma": [
         {
            "Lac": {{number}},
            "Mcc": {{number}},
            "Mnc": {{number}},
            "PathLoss": {{number}},
            "Rscp": {{number}},
            "UtranCid": {{number}},
            "WcdmaLocalId": {
               "Psc": {{number}},
               "Uarfcndl": {{number}}
            },
            "WcdmaNmr": [
               {
                  "PathLoss": {{number}},
                  "Psc": {{number}},
                  "Rscp": {{number}},
                  "Uarfcndl": {{number}},
                  "UtranCid": {{number}}
               }
            ]
         }
      ]
   },
   "Gnss": {
      "AssistAltitude": {{number}},
      "AssistPosition": [ {{number}} ],
      "CaptureTime": {{number}},
      "CaptureTimeAccuracy": {{number}},
      "Payload": "{{string}}",
      "Use2DSolver": {{boolean}}
   },
   "Ip": {
      "IpAddress": "{{string}}"
   },
   "Timestamp": {{number}},
   "WiFiAccessPoints": [
      {
         "MacAddress": "{{string}}",
         "Rss": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetPositionEstimate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPositionEstimate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdvancedConfiguration](#API_GetPositionEstimate_RequestSyntax) **   <a name="iotwireless-GetPositionEstimate-request-AdvancedConfiguration"></a>
Optional configuration for customizing position measurement data.
Type: [AdvancedConfiguration](API_AdvancedConfiguration.md) object
Required: No

 ** [CellTowers](#API_GetPositionEstimate_RequestSyntax) **   <a name="iotwireless-GetPositionEstimate-request-CellTowers"></a>
Retrieves an estimated device position by resolving measurement data from cellular radio towers. The position is resolved using HERE's cellular-based solver.
Type: [CellTowers](API_CellTowers.md) object
Required: No

 ** [Gnss](#API_GetPositionEstimate_RequestSyntax) **   <a name="iotwireless-GetPositionEstimate-request-Gnss"></a>
Retrieves an estimated device position by resolving the global navigation satellite system (GNSS) scan data. The position is resolved using the GNSS solver powered by LoRa Cloud.
Type: [Gnss](API_Gnss.md) object
Required: No

 ** [Ip](#API_GetPositionEstimate_RequestSyntax) **   <a name="iotwireless-GetPositionEstimate-request-Ip"></a>
Retrieves an estimated device position by resolving the IP address information from the device. The position is resolved using MaxMind's IP-based solver.
Type: [Ip](API_Ip.md) object
Required: No

 ** [Timestamp](#API_GetPositionEstimate_RequestSyntax) **   <a name="iotwireless-GetPositionEstimate-request-Timestamp"></a>
Optional information that specifies the time when the position information will be resolved. It uses the Unix timestamp format. If not specified, the time at which the request was received will be used.
Type: Timestamp
Required: No

 ** [WiFiAccessPoints](#API_GetPositionEstimate_RequestSyntax) **   <a name="iotwireless-GetPositionEstimate-request-WiFiAccessPoints"></a>
Retrieves an estimated device position by resolving WLAN measurement data. The position is resolved using HERE's Wi-Fi based solver.
Type: Array of [WiFiAccessPoint](API_WiFiAccessPoint.md) objects
Required: No

## Response Syntax
<a name="API_GetPositionEstimate_ResponseSyntax"></a>

```
HTTP/1.1 200

{{GeoJsonPayload}}
```

## Response Elements
<a name="API_GetPositionEstimate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [GeoJsonPayload](#API_GetPositionEstimate_ResponseSyntax) **   <a name="iotwireless-GetPositionEstimate-response-GeoJsonPayload"></a>
The position information of the resource, displayed as a JSON payload. The payload is of type blob and uses the [GeoJSON](https://geojson.org/) format, which a format that's used to encode geographic data structures. A sample payload contains the timestamp information, the WGS84 coordinates of the location, and the accuracy and confidence level. For more information and examples, see [Resolve device location (console)](https://docs.aws.amazon.com/iot/latest/developerguide/location-resolve-console.html).

## Errors
<a name="API_GetPositionEstimate_Errors"></a>

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
<a name="API_GetPositionEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetPositionEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetPositionEstimate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
