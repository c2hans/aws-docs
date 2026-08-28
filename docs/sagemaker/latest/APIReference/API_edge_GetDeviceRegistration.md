---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_GetDeviceRegistration.html
---

# GetDeviceRegistration
<a name="API_edge_GetDeviceRegistration"></a>

Use to check if a device is registered with SageMaker Edge Manager.

## Request Syntax
<a name="API_edge_GetDeviceRegistration_RequestSyntax"></a>

```
POST /GetDeviceRegistration HTTP/1.1
Content-type: application/json

{
   "DeviceFleetName": "{{string}}",
   "DeviceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_edge_GetDeviceRegistration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_edge_GetDeviceRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeviceFleetName](#API_edge_GetDeviceRegistration_RequestSyntax) **   <a name="sagemaker-edge_GetDeviceRegistration-request-DeviceFleetName"></a>
The name of the fleet to which the device belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
Required: Yes

 ** [DeviceName](#API_edge_GetDeviceRegistration_RequestSyntax) **   <a name="sagemaker-edge_GetDeviceRegistration-request-DeviceName"></a>
The unique name of the device from which you want to get the registration status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
Required: Yes

## Response Syntax
<a name="API_edge_GetDeviceRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CacheTTL": "string",
   "DeviceRegistration": "string"
}
```

## Response Elements
<a name="API_edge_GetDeviceRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CacheTTL](#API_edge_GetDeviceRegistration_ResponseSyntax) **   <a name="sagemaker-edge_GetDeviceRegistration-response-CacheTTL"></a>
The amount of time, in seconds, that the registration status is stored on the device’s cache before it is refreshed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [DeviceRegistration](#API_edge_GetDeviceRegistration_ResponseSyntax) **   <a name="sagemaker-edge_GetDeviceRegistration-response-DeviceRegistration"></a>
Describes if the device is currently registered with SageMaker Edge Manager.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_edge_GetDeviceRegistration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal failure occurred. Try your request again. If the problem persists, contact AWS customer support.
HTTP Status Code: 400

## See Also
<a name="API_edge_GetDeviceRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-edge-2020-09-23/GetDeviceRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/GetDeviceRegistration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
