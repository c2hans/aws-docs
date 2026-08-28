---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListDevices.html
---

# ListDevices
<a name="API_devicemanagement_ListDevices"></a>

Returns a list of all devices on your AWS account that have AWS Snow Device Management enabled in the AWS Region where the command is run.

## Request Syntax
<a name="API_devicemanagement_ListDevices_RequestSyntax"></a>

```
GET /managed-devices?jobId={{jobId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_devicemanagement_ListDevices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_devicemanagement_ListDevices_RequestSyntax) **   <a name="Snowball-devicemanagement_ListDevices-request-uri-jobId"></a>
The ID of the job used to order the device.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [maxResults](#API_devicemanagement_ListDevices_RequestSyntax) **   <a name="Snowball-devicemanagement_ListDevices-request-uri-maxResults"></a>
The maximum number of devices to list per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_devicemanagement_ListDevices_RequestSyntax) **   <a name="Snowball-devicemanagement_ListDevices-request-uri-nextToken"></a>
A pagination token to continue to the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

## Request Body
<a name="API_devicemanagement_ListDevices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_devicemanagement_ListDevices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "devices": [
      {
         "associatedWithJob": "string",
         "managedDeviceArn": "string",
         "managedDeviceId": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_devicemanagement_ListDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [devices](#API_devicemanagement_ListDevices_ResponseSyntax) **   <a name="Snowball-devicemanagement_ListDevices-response-devices"></a>
A list of device structures that contain information about the device.
Type: Array of [DeviceSummary](API_devicemanagement_DeviceSummary.md) objects

 ** [nextToken](#API_devicemanagement_ListDevices_ResponseSyntax) **   <a name="Snowball-devicemanagement_ListDevices-response-nextToken"></a>
A pagination token to continue to the next page of devices.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

## Errors
<a name="API_devicemanagement_ListDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_devicemanagement_ListDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/ListDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/ListDevices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
