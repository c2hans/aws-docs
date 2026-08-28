---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEdgeDeploymentPlan.html
---

# DescribeEdgeDeploymentPlan
<a name="API_DescribeEdgeDeploymentPlan"></a>

Describes an edge deployment plan with deployment status per stage.

## Request Syntax
<a name="API_DescribeEdgeDeploymentPlan_RequestSyntax"></a>

```
{
   "EdgeDeploymentPlanName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEdgeDeploymentPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EdgeDeploymentPlanName](#API_DescribeEdgeDeploymentPlan_RequestSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-request-EdgeDeploymentPlanName"></a>
The name of the deployment plan to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MaxResults](#API_DescribeEdgeDeploymentPlan_RequestSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-request-MaxResults"></a>
The maximum number of results to select (50 by default).
Type: Integer
Valid Range: Maximum value of 10.
Required: No

 ** [NextToken](#API_DescribeEdgeDeploymentPlan_RequestSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-request-NextToken"></a>
If the edge deployment plan has enough stages to require tokening, then this is the response from the last list of stages returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_DescribeEdgeDeploymentPlan_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "DeviceFleetName": "string",
   "EdgeDeploymentFailed": number,
   "EdgeDeploymentPending": number,
   "EdgeDeploymentPlanArn": "string",
   "EdgeDeploymentPlanName": "string",
   "EdgeDeploymentSuccess": number,
   "LastModifiedTime": number,
   "ModelConfigs": [
      {
         "EdgePackagingJobName": "string",
         "ModelHandle": "string"
      }
   ],
   "NextToken": "string",
   "Stages": [
      {
         "DeploymentConfig": {
            "FailureHandlingPolicy": "string"
         },
         "DeploymentStatus": {
            "EdgeDeploymentFailedInStage": number,
            "EdgeDeploymentPendingInStage": number,
            "EdgeDeploymentStageStartTime": number,
            "EdgeDeploymentStatusMessage": "string",
            "EdgeDeploymentSuccessInStage": number,
            "StageStatus": "string"
         },
         "DeviceSelectionConfig": {
            "DeviceNameContains": "string",
            "DeviceNames": [ "string" ],
            "DeviceSubsetType": "string",
            "Percentage": number
         },
         "StageName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEdgeDeploymentPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-CreationTime"></a>
The time when the edge deployment plan was created.
Type: Timestamp

 ** [DeviceFleetName](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-DeviceFleetName"></a>
The device fleet used for this edge deployment plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [EdgeDeploymentFailed](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-EdgeDeploymentFailed"></a>
The number of edge devices that failed the deployment.
Type: Integer

 ** [EdgeDeploymentPending](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-EdgeDeploymentPending"></a>
The number of edge devices yet to pick up deployment, or in progress.
Type: Integer

 ** [EdgeDeploymentPlanArn](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-EdgeDeploymentPlanArn"></a>
The ARN of edge deployment plan.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z\-]*:\d{12}:edge-deployment/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [EdgeDeploymentPlanName](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-EdgeDeploymentPlanName"></a>
The name of the edge deployment plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [EdgeDeploymentSuccess](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-EdgeDeploymentSuccess"></a>
The number of edge devices with the successful deployment.
Type: Integer

 ** [LastModifiedTime](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-LastModifiedTime"></a>
The time when the edge deployment plan was last updated.
Type: Timestamp

 ** [ModelConfigs](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-ModelConfigs"></a>
List of models associated with the edge deployment plan.
Type: Array of [EdgeDeploymentModelConfig](API_EdgeDeploymentModelConfig.md) objects

 ** [NextToken](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-NextToken"></a>
Token to use when calling the next set of stages in the edge deployment plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [Stages](#API_DescribeEdgeDeploymentPlan_ResponseSyntax) **   <a name="sagemaker-DescribeEdgeDeploymentPlan-response-Stages"></a>
List of stages in the edge deployment plan.
Type: Array of [DeploymentStageStatusSummary](API_DeploymentStageStatusSummary.md) objects

## Errors
<a name="API_DescribeEdgeDeploymentPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEdgeDeploymentPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeEdgeDeploymentPlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
