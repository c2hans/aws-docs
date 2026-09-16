---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartClusterHealthCheck.html
---

# StartClusterHealthCheck
<a name="API_StartClusterHealthCheck"></a>

Start deep health checks for a SageMaker HyperPod cluster. You can use [DescribeClusterNode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterNode.html) API to track progress of the deep health checks. The unhealthy nodes will be automatically rebooted or replaced. Please see [ Resilience-related Kubernetes labels by SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-node-labels.html) for details.

## Request Syntax
<a name="API_StartClusterHealthCheck_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "DeepHealthCheckConfigurations": [
      {
         "DeepHealthChecks": [ "{{string}}" ],
         "InstanceGroupName": "{{string}}",
         "InstanceIds": [ "{{string}}" ]
      }
   ]
}
```

## Request Parameters
<a name="API_StartClusterHealthCheck_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_StartClusterHealthCheck_RequestSyntax) **   <a name="sagemaker-StartClusterHealthCheck-request-ClusterName"></a>
The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [DeepHealthCheckConfigurations](#API_StartClusterHealthCheck_RequestSyntax) **   <a name="sagemaker-StartClusterHealthCheck-request-DeepHealthCheckConfigurations"></a>
A list of configurations containing instance group names, EC2 instance IDs, and deep health checks to perform.
Type: Array of [InstanceGroupHealthCheckConfiguration](API_InstanceGroupHealthCheckConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Required: Yes

## Response Syntax
<a name="API_StartClusterHealthCheck_ResponseSyntax"></a>

```
{
   "ClusterArn": "string"
}
```

## Response Elements
<a name="API_StartClusterHealthCheck_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_StartClusterHealthCheck_ResponseSyntax) **   <a name="sagemaker-StartClusterHealthCheck-response-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the deep health checks were initiated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

## Errors
<a name="API_StartClusterHealthCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_StartClusterHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/StartClusterHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StartClusterHealthCheck)
