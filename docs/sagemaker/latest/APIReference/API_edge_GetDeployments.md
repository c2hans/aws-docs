---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_GetDeployments.html
---

# GetDeployments
<a name="API_edge_GetDeployments"></a>

Use to get the active deployments from a device.

## Request Syntax
<a name="API_edge_GetDeployments_RequestSyntax"></a>

```
POST /GetDeployments HTTP/1.1
Content-type: application/json

{
   "DeviceFleetName": "{{string}}",
   "DeviceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_edge_GetDeployments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_edge_GetDeployments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeviceFleetName](#API_edge_GetDeployments_RequestSyntax) **   <a name="sagemaker-edge_GetDeployments-request-DeviceFleetName"></a>
The name of the fleet to which the device belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
Required: Yes

 ** [DeviceName](#API_edge_GetDeployments_RequestSyntax) **   <a name="sagemaker-edge_GetDeployments-request-DeviceName"></a>
The unique name of the device from which you want to get the configuration of active deployments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
Required: Yes

## Response Syntax
<a name="API_edge_GetDeployments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Deployments": [
      {
         "Definitions": [
            {
               "Checksum": {
                  "Sum": "string",
                  "Type": "string"
               },
               "ModelHandle": "string",
               "S3Url": "string",
               "State": "string"
            }
         ],
         "DeploymentName": "string",
         "FailureHandlingPolicy": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_edge_GetDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Deployments](#API_edge_GetDeployments_ResponseSyntax) **   <a name="sagemaker-edge_GetDeployments-response-Deployments"></a>
Returns a list of the configurations of the active deployments on the device.
Type: Array of [EdgeDeployment](API_edge_EdgeDeployment.md) objects

## Errors
<a name="API_edge_GetDeployments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal failure occurred. Try your request again. If the problem persists, contact AWS customer support.
HTTP Status Code: 400

## See Also
<a name="API_edge_GetDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-edge-2020-09-23/GetDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/GetDeployments)
