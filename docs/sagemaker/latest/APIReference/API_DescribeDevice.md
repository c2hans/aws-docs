---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeDevice.html
---

# DescribeDevice
<a name="API_DescribeDevice"></a>

Describes the device.

## Request Syntax
<a name="API_DescribeDevice_RequestSyntax"></a>

```
{
   "DeviceFleetName": "{{string}}",
   "DeviceName": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDevice_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceFleetName](#API_DescribeDevice_RequestSyntax) **   <a name="sagemaker-DescribeDevice-request-DeviceFleetName"></a>
The name of the fleet the devices belong to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [DeviceName](#API_DescribeDevice_RequestSyntax) **   <a name="sagemaker-DescribeDevice-request-DeviceName"></a>
The unique ID of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [NextToken](#API_DescribeDevice_RequestSyntax) **   <a name="sagemaker-DescribeDevice-request-NextToken"></a>
Next token of device description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_DescribeDevice_ResponseSyntax"></a>

```
{
   "AgentVersion": "string",
   "Description": "string",
   "DeviceArn": "string",
   "DeviceFleetName": "string",
   "DeviceName": "string",
   "IotThingName": "string",
   "LatestHeartbeat": number,
   "MaxModels": number,
   "Models": [
      {
         "LatestInference": number,
         "LatestSampleTime": number,
         "ModelName": "string",
         "ModelVersion": "string"
      }
   ],
   "NextToken": "string",
   "RegistrationTime": number
}
```

## Response Elements
<a name="API_DescribeDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentVersion](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-AgentVersion"></a>
Edge Manager agent version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\ \_\.]+`

 ** [Description](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-Description"></a>
A description of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[-a-zA-Z0-9_.,;:! ]*`

 ** [DeviceArn](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-DeviceArn"></a>
The Amazon Resource Name (ARN) of the device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:[a-z\-]*:[a-z\-]*:\d{12}:[a-z\-]*/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [DeviceFleetName](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-DeviceFleetName"></a>
The name of the fleet the device belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [DeviceName](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-DeviceName"></a>
The unique identifier of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [IotThingName](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-IotThingName"></a>
The AWS Internet of Things (IoT) object thing name associated with the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [LatestHeartbeat](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-LatestHeartbeat"></a>
The last heartbeat received from the device.
Type: Timestamp

 ** [MaxModels](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-MaxModels"></a>
The maximum number of models.
Type: Integer

 ** [Models](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-Models"></a>
Models on the device.
Type: Array of [EdgeModel](API_EdgeModel.md) objects

 ** [NextToken](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-NextToken"></a>
The response from the last list when returning a list large enough to need tokening.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [RegistrationTime](#API_DescribeDevice_ResponseSyntax) **   <a name="sagemaker-DescribeDevice-response-RegistrationTime"></a>
The timestamp of the last registration or de-reregistration.
Type: Timestamp

## Errors
<a name="API_DescribeDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
