---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DetachClusterNodeVolume.html
---

# DetachClusterNodeVolume
<a name="API_DetachClusterNodeVolume"></a>

 Detaches your Amazon Elastic Block Store (Amazon EBS) volume from a node in your EKS orchestrated SageMaker HyperPod cluster.

 This API works with the Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver to manage the lifecycle of persistent storage in your HyperPod EKS clusters.

## Request Syntax
<a name="API_DetachClusterNodeVolume_RequestSyntax"></a>

```
{
   "ClusterArn": "{{string}}",
   "NodeId": "{{string}}",
   "VolumeId": "{{string}}"
}
```

## Request Parameters
<a name="API_DetachClusterNodeVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterArn](#API_DetachClusterNodeVolume_RequestSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-request-ClusterArn"></a>
 The Amazon Resource Name (ARN) of your SageMaker HyperPod cluster containing the target node. Your cluster must use EKS as the orchestration and be in the `InService` state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [NodeId](#API_DetachClusterNodeVolume_RequestSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-request-NodeId"></a>
 The unique identifier of the cluster node from which you want to detach the volume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: Yes

 ** [VolumeId](#API_DetachClusterNodeVolume_RequestSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-request-VolumeId"></a>
 The unique identifier of your EBS volume that you want to detach. Your volume must be currently attached to the specified node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `vol-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: Yes

## Response Syntax
<a name="API_DetachClusterNodeVolume_ResponseSyntax"></a>

```
{
   "AttachTime": number,
   "ClusterArn": "string",
   "DeviceName": "string",
   "NodeId": "string",
   "Status": "string",
   "VolumeId": "string"
}
```

## Response Elements
<a name="API_DetachClusterNodeVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachTime](#API_DetachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-response-AttachTime"></a>
 The original timestamp when your volume was initially attached to the node.
Type: Timestamp

 ** [ClusterArn](#API_DetachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-response-ClusterArn"></a>
 The Amazon Resource Name (ARN) of your SageMaker HyperPod cluster where the volume detachment operation was performed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

 ** [DeviceName](#API_DetachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-response-DeviceName"></a>
 The device name assigned to your attached volume on the target instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `/dev/(xvd[a-z]|sd[b-z]|sd[f-p][1-6])`

 ** [NodeId](#API_DetachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-response-NodeId"></a>
 The unique identifier of the cluster node from which your volume was detached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`

 ** [Status](#API_DetachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-response-Status"></a>
 The current status of your volume detachment operation.
Type: String
Valid Values: `attaching | attached | detaching | detached | busy`

 ** [VolumeId](#API_DetachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-DetachClusterNodeVolume-response-VolumeId"></a>
 The unique identifier of your EBS volume that was detached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `vol-[a-f0-9]{8}(?:[a-f0-9]{9})?`

## Errors
<a name="API_DetachClusterNodeVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DetachClusterNodeVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DetachClusterNodeVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DetachClusterNodeVolume)
