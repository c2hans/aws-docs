---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListCoreDevices.html
---

# ListCoreDevices
<a name="API_ListCoreDevices"></a>

Retrieves a paginated list of Greengrass core devices.

**Note**
 AWS IoT Greengrass relies on individual devices to send status updates to the AWS Cloud. If the AWS IoT Greengrass Core software isn't running on the device, or if device isn't connected to the AWS Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.
Core devices send status updates at the following times:
When the AWS IoT Greengrass Core software starts
When the core device receives a deployment from the AWS Cloud
For Greengrass nucleus 2.12.2 and earlier, the core device sends status updates when the status of any component on the core device becomes `ERRORED` or `BROKEN`.
For Greengrass nucleus 2.12.3 and later, the core device sends status updates when the status of any component on the core device becomes `ERRORED`, `BROKEN`, `RUNNING`, or `FINISHED`.
At a [regular interval that you can configure](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss), which defaults to 24 hours
For AWS IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment
When the AWS IoT Greengrass Core software connects to the AWS Cloud, your device will be recognized as a core device.

## Request Syntax
<a name="API_ListCoreDevices_RequestSyntax"></a>

```
GET /greengrass/v2/coreDevices?maxResults={{maxResults}}&nextToken={{nextToken}}&runtime={{runtime}}&status={{status}}&thingGroupArn={{thingGroupArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCoreDevices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCoreDevices_RequestSyntax) **   <a name="greengrassv2-ListCoreDevices-request-uri-maxResults"></a>
The maximum number of results to be returned per paginated request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCoreDevices_RequestSyntax) **   <a name="greengrassv2-ListCoreDevices-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.

 ** [runtime](#API_ListCoreDevices_RequestSyntax) **   <a name="greengrassv2-ListCoreDevices-request-uri-runtime"></a>
The runtime to be used by the core device. The runtime can be:
+  `aws_nucleus_classic`
+  `aws_nucleus_lite`
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [status](#API_ListCoreDevices_RequestSyntax) **   <a name="greengrassv2-ListCoreDevices-request-uri-status"></a>
The core device status by which to filter. If you specify this parameter, the list includes only core devices that have this status. Choose one of the following options:
+  `HEALTHY` – The AWS IoT Greengrass Core software and all components run on the core device without issue.
+  `UNHEALTHY` – The AWS IoT Greengrass Core software or a component is in a failed state on the core device.
Valid Values: `HEALTHY | UNHEALTHY`

 ** [thingGroupArn](#API_ListCoreDevices_RequestSyntax) **   <a name="greengrassv2-ListCoreDevices-request-uri-thingGroupArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS IoT thing group by which to filter. If you specify this parameter, the list includes only core devices that have successfully deployed a deployment that targets the thing group. When you remove a core device from a thing group, the list continues to include that core device.
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:thinggroup/.+`

## Request Body
<a name="API_ListCoreDevices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCoreDevices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "coreDevices": [
      {
         "architecture": "string",
         "coreDeviceThingName": "string",
         "lastStatusUpdateTimestamp": number,
         "platform": "string",
         "runtime": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCoreDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [coreDevices](#API_ListCoreDevices_ResponseSyntax) **   <a name="greengrassv2-ListCoreDevices-response-coreDevices"></a>
A list that summarizes each core device.
Type: Array of [CoreDevice](API_CoreDevice.md) objects

 ** [nextToken](#API_ListCoreDevices_ResponseSyntax) **   <a name="greengrassv2-ListCoreDevices-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String

## Errors
<a name="API_ListCoreDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
HTTP Status Code: 403

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

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
<a name="API_ListCoreDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListCoreDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ListCoreDevices)
