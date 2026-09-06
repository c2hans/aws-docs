---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_BatchAssociateClientDeviceWithCoreDevice.html
---

# BatchAssociateClientDeviceWithCoreDevice
<a name="API_BatchAssociateClientDeviceWithCoreDevice"></a>

Associates a list of client devices with a core device. Use this API operation to specify which client devices can discover a core device through cloud discovery. With cloud discovery, client devices connect to AWS IoT Greengrass to retrieve associated core devices' connectivity information and certificates. For more information, see [Connect client devices to core devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/connect-client-devices.html) in the * AWS IoT Greengrass V2 Developer Guide*.

**Note**
Client devices are local IoT devices that connect to and communicate with an AWS IoT Greengrass core device over MQTT. You can connect client devices to a core device to sync MQTT messages and data to AWS IoT Core and interact with client devices in Greengrass components. For more information, see [Interact with local IoT devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/interact-with-local-iot-devices.html) in the * AWS IoT Greengrass V2 Developer Guide*.

## Request Syntax
<a name="API_BatchAssociateClientDeviceWithCoreDevice_RequestSyntax"></a>

```
POST /greengrass/v2/coreDevices/{{coreDeviceThingName}}/associateClientDevices HTTP/1.1
Content-type: application/json

{
   "entries": [
      {
         "thingName": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchAssociateClientDeviceWithCoreDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [coreDeviceThingName](#API_BatchAssociateClientDeviceWithCoreDevice_RequestSyntax) **   <a name="greengrassv2-BatchAssociateClientDeviceWithCoreDevice-request-uri-coreDeviceThingName"></a>
The name of the core device. This is also the name of the AWS IoT thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_BatchAssociateClientDeviceWithCoreDevice_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [entries](#API_BatchAssociateClientDeviceWithCoreDevice_RequestSyntax) **   <a name="greengrassv2-BatchAssociateClientDeviceWithCoreDevice-request-entries"></a>
The list of client devices to associate.
Type: Array of [AssociateClientDeviceWithCoreDeviceEntry](API_AssociateClientDeviceWithCoreDeviceEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_BatchAssociateClientDeviceWithCoreDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errorEntries": [
      {
         "code": "string",
         "message": "string",
         "thingName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchAssociateClientDeviceWithCoreDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorEntries](#API_BatchAssociateClientDeviceWithCoreDevice_ResponseSyntax) **   <a name="greengrassv2-BatchAssociateClientDeviceWithCoreDevice-response-errorEntries"></a>
The list of any errors for the entries in the request. Each error entry contains the name of the AWS IoT thing that failed to associate.
Type: Array of [AssociateClientDeviceWithCoreDeviceErrorEntry](API_AssociateClientDeviceWithCoreDeviceErrorEntry.md) objects
Array Members: Maximum number of 100 items.

## Errors
<a name="API_BatchAssociateClientDeviceWithCoreDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
HTTP Status Code: 403

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** resourceId **
The ID of the resource that isn't found.
 ** resourceType **
The type of the resource that isn't found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.
 ** quotaCode **
The code for the quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
 ** serviceCode **
The code for the service in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** fields **
The list of fields that failed to validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_BatchAssociateClientDeviceWithCoreDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/BatchAssociateClientDeviceWithCoreDevice)
