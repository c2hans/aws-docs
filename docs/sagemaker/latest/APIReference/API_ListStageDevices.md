---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListStageDevices.html
---

# ListStageDevices
<a name="API_ListStageDevices"></a>

Lists devices allocated to the stage, containing detailed device information and deployment status.

## Request Syntax
<a name="API_ListStageDevices_RequestSyntax"></a>

```
{
   "EdgeDeploymentPlanName": "{{string}}",
   "ExcludeDevicesDeployedInOtherStage": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StageName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStageDevices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EdgeDeploymentPlanName](#API_ListStageDevices_RequestSyntax) **   <a name="sagemaker-ListStageDevices-request-EdgeDeploymentPlanName"></a>
The name of the edge deployment plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ExcludeDevicesDeployedInOtherStage](#API_ListStageDevices_RequestSyntax) **   <a name="sagemaker-ListStageDevices-request-ExcludeDevicesDeployedInOtherStage"></a>
Toggle for excluding devices deployed in other stages.
Type: Boolean
Required: No

 ** [MaxResults](#API_ListStageDevices_RequestSyntax) **   <a name="sagemaker-ListStageDevices-request-MaxResults"></a>
The maximum number of requests to select.
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [NextToken](#API_ListStageDevices_RequestSyntax) **   <a name="sagemaker-ListStageDevices-request-NextToken"></a>
The response from the last list when returning a list large enough to neeed tokening.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [StageName](#API_ListStageDevices_RequestSyntax) **   <a name="sagemaker-ListStageDevices-request-StageName"></a>
The name of the stage in the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_ListStageDevices_ResponseSyntax"></a>

```
{
   "DeviceDeploymentSummaries": [
      {
         "DeployedStageName": "string",
         "Description": "string",
         "DeviceArn": "string",
         "DeviceDeploymentStatus": "string",
         "DeviceDeploymentStatusMessage": "string",
         "DeviceFleetName": "string",
         "DeviceName": "string",
         "EdgeDeploymentPlanArn": "string",
         "EdgeDeploymentPlanName": "string",
         "StageName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListStageDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeviceDeploymentSummaries](#API_ListStageDevices_ResponseSyntax) **   <a name="sagemaker-ListStageDevices-response-DeviceDeploymentSummaries"></a>
List of summaries of devices allocated to the stage.
Type: Array of [DeviceDeploymentSummary](API_DeviceDeploymentSummary.md) objects

 ** [NextToken](#API_ListStageDevices_ResponseSyntax) **   <a name="sagemaker-ListStageDevices-response-NextToken"></a>
The token to use when calling the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListStageDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListStageDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListStageDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListStageDevices)
