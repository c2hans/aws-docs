---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateEventConfigurationByResourceTypes.html
---

# UpdateEventConfigurationByResourceTypes
<a name="API_UpdateEventConfigurationByResourceTypes"></a>

Update the event configuration based on resource types.

## Request Syntax
<a name="API_UpdateEventConfigurationByResourceTypes_RequestSyntax"></a>

```
PATCH /event-configurations-resource-types HTTP/1.1
Content-type: application/json

{
   "ConnectionStatus": {
      "LoRaWAN": {
         "WirelessGatewayEventTopic": "{{string}}"
      }
   },
   "DeviceRegistrationState": {
      "Sidewalk": {
         "WirelessDeviceEventTopic": "{{string}}"
      }
   },
   "Join": {
      "LoRaWAN": {
         "WirelessDeviceEventTopic": "{{string}}"
      }
   },
   "MessageDeliveryStatus": {
      "Sidewalk": {
         "WirelessDeviceEventTopic": "{{string}}"
      }
   },
   "Proximity": {
      "Sidewalk": {
         "WirelessDeviceEventTopic": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateEventConfigurationByResourceTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateEventConfigurationByResourceTypes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConnectionStatus](#API_UpdateEventConfigurationByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateEventConfigurationByResourceTypes-request-ConnectionStatus"></a>
Connection status resource type event configuration object for enabling and disabling wireless gateway topic.
Type: [ConnectionStatusResourceTypeEventConfiguration](API_ConnectionStatusResourceTypeEventConfiguration.md) object
Required: No

 ** [DeviceRegistrationState](#API_UpdateEventConfigurationByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateEventConfigurationByResourceTypes-request-DeviceRegistrationState"></a>
Device registration state resource type event configuration object for enabling and disabling wireless gateway topic.
Type: [DeviceRegistrationStateResourceTypeEventConfiguration](API_DeviceRegistrationStateResourceTypeEventConfiguration.md) object
Required: No

 ** [Join](#API_UpdateEventConfigurationByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateEventConfigurationByResourceTypes-request-Join"></a>
Join resource type event configuration object for enabling and disabling wireless device topic.
Type: [JoinResourceTypeEventConfiguration](API_JoinResourceTypeEventConfiguration.md) object
Required: No

 ** [MessageDeliveryStatus](#API_UpdateEventConfigurationByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateEventConfigurationByResourceTypes-request-MessageDeliveryStatus"></a>
Message delivery status resource type event configuration object for enabling and disabling wireless device topic.
Type: [MessageDeliveryStatusResourceTypeEventConfiguration](API_MessageDeliveryStatusResourceTypeEventConfiguration.md) object
Required: No

 ** [Proximity](#API_UpdateEventConfigurationByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateEventConfigurationByResourceTypes-request-Proximity"></a>
Proximity resource type event configuration object for enabling and disabling wireless gateway topic.
Type: [ProximityResourceTypeEventConfiguration](API_ProximityResourceTypeEventConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateEventConfigurationByResourceTypes_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateEventConfigurationByResourceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateEventConfigurationByResourceTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEventConfigurationByResourceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateEventConfigurationByResourceTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
