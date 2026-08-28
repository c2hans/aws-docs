---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_SendConnectorEvent.html
---

# SendConnectorEvent
<a name="API_SendConnectorEvent"></a>

Relays third-party device events for a connector such as a new device or a device state change event.

## Request Syntax
<a name="API_SendConnectorEvent_RequestSyntax"></a>

```
POST /connector-event/{{ConnectorId}} HTTP/1.1
Content-type: application/json

{
   "ConnectorDeviceId": "{{string}}",
   "DeviceDiscoveryId": "{{string}}",
   "Devices": [
      {
         "CapabilityReport": {
            "endpoints": [
               {
                  "clientClusters": [ "{{string}}" ],
                  "clusters": [
                     {
                        "attributes": [
                           {
                              "id": "{{string}}",
                              "name": "{{string}}",
                              "value": {{JSON value}}
                           }
                        ],
                        "commands": [ "{{string}}" ],
                        "events": [ "{{string}}" ],
                        "fabricIndex": {{number}},
                        "featureMap": {{number}},
                        "generatedCommands": [ "{{string}}" ],
                        "id": "{{string}}",
                        "name": "{{string}}",
                        "publicId": "{{string}}",
                        "revision": {{number}},
                        "specVersion": "{{string}}"
                     }
                  ],
                  "deviceTypes": [ "{{string}}" ],
                  "id": "{{string}}",
                  "parts": [ "{{string}}" ],
                  "semanticTags": [ "{{string}}" ]
               }
            ],
            "nodeId": "{{string}}",
            "version": "{{string}}"
         },
         "CapabilitySchemas": [
            {
               "CapabilityId": "{{string}}",
               "ExtrinsicId": "{{string}}",
               "ExtrinsicVersion": {{number}},
               "Format": "{{string}}",
               "Schema": {{JSON value}}
            }
         ],
         "ConnectorDeviceId": "{{string}}",
         "ConnectorDeviceName": "{{string}}",
         "DeviceMetadata": {{JSON value}}
      }
   ],
   "MatterEndpoint": {
      "clusters": [
         {
            "attributes": {{JSON value}},
            "commands": {
               "{{string}}" : {{JSON value}}
            },
            "events": {
               "{{string}}" : {{JSON value}}
            },
            "id": "{{string}}"
         }
      ],
      "id": "{{string}}"
   },
   "Message": "{{string}}",
   "Operation": "{{string}}",
   "OperationVersion": "{{string}}",
   "StatusCode": {{number}},
   "TraceId": "{{string}}",
   "UserId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendConnectorEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorId](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-uri-ConnectorId"></a>
The id of the connector between the third-party cloud provider and IoT managed integrations.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

## Request Body
<a name="API_SendConnectorEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConnectorDeviceId](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-ConnectorDeviceId"></a>
The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).
This parameter is used for cloud-to-cloud devices only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: No

 ** [DeviceDiscoveryId](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-DeviceDiscoveryId"></a>
The id for the device discovery job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** [Devices](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-Devices"></a>
The list of devices.
Type: Array of [Device](API_Device.md) objects
Required: No

 ** [MatterEndpoint](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-MatterEndpoint"></a>
The device endpoint.
Type: [MatterEndpoint](API_MatterEndpoint.md) object
Required: No

 ** [Message](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-Message"></a>
The device state change event payload.
This parameter will include the following three fields:
+  `uri`: `schema auc://<PARTNER-DEVICE-ID>/ResourcePath` (The `Resourcepath` corresponds to an OCF resource.)
+  `op`: For device state changes, this field must populate as `n+d`.
+  `cn`: The content depends on the OCF resource referenced in `ResourcePath`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\sa-zA-Z0-9_.,@-]+`
Required: No

 ** [Operation](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-Operation"></a>
The Open Connectivity Foundation (OCF) operation requested to be performed on the managed thing.
The field op can have a value of "I" or "U". The field "cn" will contain the capability types.
Type: String
Valid Values: `DEVICE_COMMAND_RESPONSE | DEVICE_DISCOVERY | DEVICE_EVENT | DEVICE_COMMAND_REQUEST`
Required: Yes

 ** [OperationVersion](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-OperationVersion"></a>
The Open Connectivity Foundation (OCF) security specification version for the operation being requested on the managed thing. For more information, see [OCF Security Specification](https://openconnectivity.org/specs/OCF_Security_Specification_v1.0.0.pdf).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `[0-9.]+`
Required: No

 ** [StatusCode](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-StatusCode"></a>
The status code of the Open Connectivity Foundation (OCF) operation being performed on the managed thing.
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 550.
Required: No

 ** [TraceId](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-TraceId"></a>
The trace request identifier. This is generated by IoT managed integrations and can be used to trace this command and its related operations in CloudWatch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:=_-]+`
Required: No

 ** [UserId](#API_SendConnectorEvent_RequestSyntax) **   <a name="managedintegrations-SendConnectorEvent-request-UserId"></a>
The id of the third-party cloud provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: No

## Response Syntax
<a name="API_SendConnectorEvent_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "ConnectorId": "string"
}
```

## Response Elements
<a name="API_SendConnectorEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [ConnectorId](#API_SendConnectorEvent_ResponseSyntax) **   <a name="managedintegrations-SendConnectorEvent-response-ConnectorId"></a>
The id of the connector between the third-party cloud provider and IoT managed integrations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

## Errors
<a name="API_SendConnectorEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_SendConnectorEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/SendConnectorEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/SendConnectorEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
