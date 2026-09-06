---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DescribeDeviceEc2Instances.html
---

# DescribeDeviceEc2Instances
<a name="API_devicemanagement_DescribeDeviceEc2Instances"></a>

Checks the current state of the Amazon EC2-compatible instances. The output is similar to `describeDevice`, but the results are sourced from the device cache in the AWS Cloud and include a subset of the available fields.

## Request Syntax
<a name="API_devicemanagement_DescribeDeviceEc2Instances_RequestSyntax"></a>

```
POST /managed-device/{{managedDeviceId}}/resources/ec2/describe HTTP/1.1
Content-type: application/json

{
   "instanceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_devicemanagement_DescribeDeviceEc2Instances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [managedDeviceId](#API_devicemanagement_DescribeDeviceEc2Instances_RequestSyntax) **   <a name="Snowball-devicemanagement_DescribeDeviceEc2Instances-request-uri-managedDeviceId"></a>
The ID of the managed device.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_devicemanagement_DescribeDeviceEc2Instances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [instanceIds](#API_devicemanagement_DescribeDeviceEc2Instances_RequestSyntax) **   <a name="Snowball-devicemanagement_DescribeDeviceEc2Instances-request-instanceIds"></a>
A list of instance IDs associated with the managed device.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_devicemanagement_DescribeDeviceEc2Instances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "instances": [
      {
         "instance": {
            "amiLaunchIndex": number,
            "blockDeviceMappings": [
               {
                  "deviceName": "string",
                  "ebs": {
                     "attachTime": number,
                     "deleteOnTermination": boolean,
                     "status": "string",
                     "volumeId": "string"
                  }
               }
            ],
            "cpuOptions": {
               "coreCount": number,
               "threadsPerCore": number
            },
            "createdAt": number,
            "imageId": "string",
            "instanceId": "string",
            "instanceType": "string",
            "privateIpAddress": "string",
            "publicIpAddress": "string",
            "rootDeviceName": "string",
            "securityGroups": [
               {
                  "groupId": "string",
                  "groupName": "string"
               }
            ],
            "state": {
               "code": number,
               "name": "string"
            },
            "updatedAt": number
         },
         "lastUpdatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_devicemanagement_DescribeDeviceEc2Instances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instances](#API_devicemanagement_DescribeDeviceEc2Instances_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDeviceEc2Instances-response-instances"></a>
A list of structures containing information about each instance.
Type: Array of [InstanceSummary](API_devicemanagement_InstanceSummary.md) objects

## Errors
<a name="API_devicemanagement_DescribeDeviceEc2Instances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_devicemanagement_DescribeDeviceEc2Instances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)
