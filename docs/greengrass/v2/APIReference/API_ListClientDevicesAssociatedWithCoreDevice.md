---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListClientDevicesAssociatedWithCoreDevice.html
---

# ListClientDevicesAssociatedWithCoreDevice
<a name="API_ListClientDevicesAssociatedWithCoreDevice"></a>

Retrieves a paginated list of client devices that are associated with a core device.

## Request Syntax
<a name="API_ListClientDevicesAssociatedWithCoreDevice_RequestSyntax"></a>

```
GET /greengrass/v2/coreDevices/{{coreDeviceThingName}}/associatedClientDevices?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListClientDevicesAssociatedWithCoreDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [coreDeviceThingName](#API_ListClientDevicesAssociatedWithCoreDevice_RequestSyntax) **   <a name="greengrassv2-ListClientDevicesAssociatedWithCoreDevice-request-uri-coreDeviceThingName"></a>
The name of the core device. This is also the name of the AWS IoT thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [maxResults](#API_ListClientDevicesAssociatedWithCoreDevice_RequestSyntax) **   <a name="greengrassv2-ListClientDevicesAssociatedWithCoreDevice-request-uri-maxResults"></a>
The maximum number of results to be returned per paginated request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListClientDevicesAssociatedWithCoreDevice_RequestSyntax) **   <a name="greengrassv2-ListClientDevicesAssociatedWithCoreDevice-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.

## Request Body
<a name="API_ListClientDevicesAssociatedWithCoreDevice_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListClientDevicesAssociatedWithCoreDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associatedClientDevices": [
      {
         "associationTimestamp": number,
         "thingName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListClientDevicesAssociatedWithCoreDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedClientDevices](#API_ListClientDevicesAssociatedWithCoreDevice_ResponseSyntax) **   <a name="greengrassv2-ListClientDevicesAssociatedWithCoreDevice-response-associatedClientDevices"></a>
A list that describes the client devices that are associated with the core device.
Type: Array of [AssociatedClientDevice](API_AssociatedClientDevice.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [nextToken](#API_ListClientDevicesAssociatedWithCoreDevice_ResponseSyntax) **   <a name="greengrassv2-ListClientDevicesAssociatedWithCoreDevice-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String

## Errors
<a name="API_ListClientDevicesAssociatedWithCoreDevice_Errors"></a>

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
<a name="API_ListClientDevicesAssociatedWithCoreDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ListClientDevicesAssociatedWithCoreDevice)
