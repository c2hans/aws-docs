---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListInstalledComponents.html
---

# ListInstalledComponents
<a name="API_ListInstalledComponents"></a>

Retrieves a paginated list of the components that a Greengrass core device runs. By default, this list doesn't include components that are deployed as dependencies of other components. To include dependencies in the response, set the `topologyFilter` parameter to `ALL`.

**Note**
 AWS IoT Greengrass relies on individual devices to send status updates to the AWS Cloud. If the AWS IoT Greengrass Core software isn't running on the device, or if device isn't connected to the AWS Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.
Core devices send status updates at the following times:
When the AWS IoT Greengrass Core software starts
When the core device receives a deployment from the AWS Cloud
When the status of any component on the core device becomes `BROKEN`
At a [regular interval that you can configure](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss), which defaults to 24 hours
For AWS IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment

## Request Syntax
<a name="API_ListInstalledComponents_RequestSyntax"></a>

```
GET /greengrass/v2/coreDevices/{{coreDeviceThingName}}/installedComponents?maxResults={{maxResults}}&nextToken={{nextToken}}&topologyFilter={{topologyFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInstalledComponents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [coreDeviceThingName](#API_ListInstalledComponents_RequestSyntax) **   <a name="greengrassv2-ListInstalledComponents-request-uri-coreDeviceThingName"></a>
The name of the core device. This is also the name of the AWS IoT thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [maxResults](#API_ListInstalledComponents_RequestSyntax) **   <a name="greengrassv2-ListInstalledComponents-request-uri-maxResults"></a>
The maximum number of results to be returned per paginated request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListInstalledComponents_RequestSyntax) **   <a name="greengrassv2-ListInstalledComponents-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.

 ** [topologyFilter](#API_ListInstalledComponents_RequestSyntax) **   <a name="greengrassv2-ListInstalledComponents-request-uri-topologyFilter"></a>
The filter for the list of components. Choose from the following options:
+  `ALL` – The list includes all components installed on the core device.
+  `ROOT` – The list includes only *root* components, which are components that you specify in a deployment. When you choose this option, the list doesn't include components that the core device installs as dependencies of other components.
Default: `ROOT`
Valid Values: `ALL | ROOT`

## Request Body
<a name="API_ListInstalledComponents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInstalledComponents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "installedComponents": [
      {
         "componentName": "string",
         "componentVersion": "string",
         "isRoot": boolean,
         "lastInstallationSource": "string",
         "lastReportedTimestamp": number,
         "lastStatusChangeTimestamp": number,
         "lifecycleState": "string",
         "lifecycleStateDetails": "string",
         "lifecycleStatusCodes": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInstalledComponents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [installedComponents](#API_ListInstalledComponents_ResponseSyntax) **   <a name="greengrassv2-ListInstalledComponents-response-installedComponents"></a>
A list that summarizes each component on the core device.
Greengrass nucleus v2.7.0 or later is required to get an accurate `lastStatusChangeTimestamp` response. This response can be inaccurate in earlier Greengrass nucleus versions.
Greengrass nucleus v2.8.0 or later is required to get an accurate `lastInstallationSource` and `lastReportedTimestamp` response. This response can be inaccurate or null in earlier Greengrass nucleus versions.
Type: Array of [InstalledComponent](API_InstalledComponent.md) objects

 ** [nextToken](#API_ListInstalledComponents_ResponseSyntax) **   <a name="greengrassv2-ListInstalledComponents-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String

## Errors
<a name="API_ListInstalledComponents_Errors"></a>

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
<a name="API_ListInstalledComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListInstalledComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ListInstalledComponents)
