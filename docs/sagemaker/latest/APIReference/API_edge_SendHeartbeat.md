---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_SendHeartbeat.html
---

# SendHeartbeat
<a name="API_edge_SendHeartbeat"></a>

Use to get the current status of devices registered on SageMaker Edge Manager.

## Request Syntax
<a name="API_edge_SendHeartbeat_RequestSyntax"></a>

```
POST /SendHeartbeat HTTP/1.1
Content-type: application/json

{
   "AgentMetrics": [
      {
         "Dimension": "{{string}}",
         "MetricName": "{{string}}",
         "Timestamp": {{number}},
         "Value": {{number}}
      }
   ],
   "AgentVersion": "{{string}}",
   "DeploymentResult": {
      "DeploymentEndTime": {{number}},
      "DeploymentModels": [
         {
            "DesiredState": "{{string}}",
            "ModelHandle": "{{string}}",
            "ModelName": "{{string}}",
            "ModelVersion": "{{string}}",
            "RollbackFailureReason": "{{string}}",
            "State": "{{string}}",
            "Status": "{{string}}",
            "StatusReason": "{{string}}"
         }
      ],
      "DeploymentName": "{{string}}",
      "DeploymentStartTime": {{number}},
      "DeploymentStatus": "{{string}}",
      "DeploymentStatusMessage": "{{string}}"
   },
   "DeviceFleetName": "{{string}}",
   "DeviceName": "{{string}}",
   "Models": [
      {
         "LatestInference": {{number}},
         "LatestSampleTime": {{number}},
         "ModelMetrics": [
            {
               "Dimension": "{{string}}",
               "MetricName": "{{string}}",
               "Timestamp": {{number}},
               "Value": {{number}}
            }
         ],
         "ModelName": "{{string}}",
         "ModelVersion": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_edge_SendHeartbeat_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_edge_SendHeartbeat_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AgentMetrics](#API_edge_SendHeartbeat_RequestSyntax) **   <a name="sagemaker-edge_SendHeartbeat-request-AgentMetrics"></a>
For internal use. Returns a list of SageMaker Edge Manager agent operating metrics.
Type: Array of [EdgeMetric](API_edge_EdgeMetric.md) objects
Required: No

 ** [AgentVersion](#API_edge_SendHeartbeat_RequestSyntax) **   <a name="sagemaker-edge_SendHeartbeat-request-AgentVersion"></a>
Returns the version of the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: Yes

 ** [DeploymentResult](#API_edge_SendHeartbeat_RequestSyntax) **   <a name="sagemaker-edge_SendHeartbeat-request-DeploymentResult"></a>
Returns the result of a deployment on the device.
Type: [DeploymentResult](API_edge_DeploymentResult.md) object
Required: No

 ** [DeviceFleetName](#API_edge_SendHeartbeat_RequestSyntax) **   <a name="sagemaker-edge_SendHeartbeat-request-DeviceFleetName"></a>
The name of the fleet to which the device belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
Required: Yes

 ** [DeviceName](#API_edge_SendHeartbeat_RequestSyntax) **   <a name="sagemaker-edge_SendHeartbeat-request-DeviceName"></a>
The unique name of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
Required: Yes

 ** [Models](#API_edge_SendHeartbeat_RequestSyntax) **   <a name="sagemaker-edge_SendHeartbeat-request-Models"></a>
Returns a list of models deployed on the the device.
Type: Array of [Model](API_edge_Model.md) objects
Required: No

## Response Syntax
<a name="API_edge_SendHeartbeat_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_edge_SendHeartbeat_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_edge_SendHeartbeat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal failure occurred. Try your request again. If the problem persists, contact AWS customer support.
HTTP Status Code: 400

## See Also
<a name="API_edge_SendHeartbeat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-edge-2020-09-23/SendHeartbeat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/SendHeartbeat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
