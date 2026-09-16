---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSchedulerConfig.html
---

# UpdateClusterSchedulerConfig
<a name="API_UpdateClusterSchedulerConfig"></a>

Update the cluster policy configuration.

## Request Syntax
<a name="API_UpdateClusterSchedulerConfig_RequestSyntax"></a>

```
{
   "ClusterSchedulerConfigId": "{{string}}",
   "Description": "{{string}}",
   "SchedulerConfig": {
      "FairShare": "{{string}}",
      "IdleResourceSharing": "{{string}}",
      "PriorityClasses": [
         {
            "Name": "{{string}}",
            "Weight": {{number}}
         }
      ]
   },
   "TargetVersion": {{number}}
}
```

## Request Parameters
<a name="API_UpdateClusterSchedulerConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterSchedulerConfigId](#API_UpdateClusterSchedulerConfig_RequestSyntax) **   <a name="sagemaker-UpdateClusterSchedulerConfig-request-ClusterSchedulerConfigId"></a>
ID of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `[a-z0-9]{12}`
Required: Yes

 ** [Description](#API_UpdateClusterSchedulerConfig_RequestSyntax) **   <a name="sagemaker-UpdateClusterSchedulerConfig-request-Description"></a>
Description of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** [SchedulerConfig](#API_UpdateClusterSchedulerConfig_RequestSyntax) **   <a name="sagemaker-UpdateClusterSchedulerConfig-request-SchedulerConfig"></a>
Cluster policy configuration.
Type: [SchedulerConfig](API_SchedulerConfig.md) object
Required: No

 ** [TargetVersion](#API_UpdateClusterSchedulerConfig_RequestSyntax) **   <a name="sagemaker-UpdateClusterSchedulerConfig-request-TargetVersion"></a>
Target version.
Type: Integer
Required: Yes

## Response Syntax
<a name="API_UpdateClusterSchedulerConfig_ResponseSyntax"></a>

```
{
   "ClusterSchedulerConfigArn": "string",
   "ClusterSchedulerConfigVersion": number
}
```

## Response Elements
<a name="API_UpdateClusterSchedulerConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterSchedulerConfigArn](#API_UpdateClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-UpdateClusterSchedulerConfig-response-ClusterSchedulerConfigArn"></a>
ARN of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:cluster-scheduler-config/[a-z0-9]{12}`

 ** [ClusterSchedulerConfigVersion](#API_UpdateClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-UpdateClusterSchedulerConfig-response-ClusterSchedulerConfigVersion"></a>
Version of the cluster policy.
Type: Integer

## Errors
<a name="API_UpdateClusterSchedulerConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateClusterSchedulerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateClusterSchedulerConfig)
