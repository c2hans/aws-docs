---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEdgeDeploymentPlan.html
---

# CreateEdgeDeploymentPlan
<a name="API_CreateEdgeDeploymentPlan"></a>

Creates an edge deployment plan, consisting of multiple stages. Each stage may have a different deployment configuration and devices.

## Request Syntax
<a name="API_CreateEdgeDeploymentPlan_RequestSyntax"></a>

```
{
   "DeviceFleetName": "{{string}}",
   "EdgeDeploymentPlanName": "{{string}}",
   "ModelConfigs": [
      {
         "EdgePackagingJobName": "{{string}}",
         "ModelHandle": "{{string}}"
      }
   ],
   "Stages": [
      {
         "DeploymentConfig": {
            "FailureHandlingPolicy": "{{string}}"
         },
         "DeviceSelectionConfig": {
            "DeviceNameContains": "{{string}}",
            "DeviceNames": [ "{{string}}" ],
            "DeviceSubsetType": "{{string}}",
            "Percentage": {{number}}
         },
         "StageName": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateEdgeDeploymentPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceFleetName](#API_CreateEdgeDeploymentPlan_RequestSyntax) **   <a name="sagemaker-CreateEdgeDeploymentPlan-request-DeviceFleetName"></a>
The device fleet used for this edge deployment plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [EdgeDeploymentPlanName](#API_CreateEdgeDeploymentPlan_RequestSyntax) **   <a name="sagemaker-CreateEdgeDeploymentPlan-request-EdgeDeploymentPlanName"></a>
The name of the edge deployment plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ModelConfigs](#API_CreateEdgeDeploymentPlan_RequestSyntax) **   <a name="sagemaker-CreateEdgeDeploymentPlan-request-ModelConfigs"></a>
List of models associated with the edge deployment plan.
Type: Array of [EdgeDeploymentModelConfig](API_EdgeDeploymentModelConfig.md) objects
Required: Yes

 ** [Stages](#API_CreateEdgeDeploymentPlan_RequestSyntax) **   <a name="sagemaker-CreateEdgeDeploymentPlan-request-Stages"></a>
List of stages of the edge deployment plan. The number of stages is limited to 10 per deployment.
Type: Array of [DeploymentStage](API_DeploymentStage.md) objects
Required: No

 ** [Tags](#API_CreateEdgeDeploymentPlan_RequestSyntax) **   <a name="sagemaker-CreateEdgeDeploymentPlan-request-Tags"></a>
List of tags with which to tag the edge deployment plan.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateEdgeDeploymentPlan_ResponseSyntax"></a>

```
{
   "EdgeDeploymentPlanArn": "string"
}
```

## Response Elements
<a name="API_CreateEdgeDeploymentPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EdgeDeploymentPlanArn](#API_CreateEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-CreateEdgeDeploymentPlan-response-EdgeDeploymentPlanArn"></a>
The ARN of the edge deployment plan.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z\-]*:\d{12}:edge-deployment/?[a-zA-Z_0-9+=,.@\-_/]+`

## Errors
<a name="API_CreateEdgeDeploymentPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateEdgeDeploymentPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)
