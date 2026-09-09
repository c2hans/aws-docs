---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AttachClusterNodeVolume.html
---

# AttachClusterNodeVolume
<a name="API_AttachClusterNodeVolume"></a>

 Attaches your Amazon Elastic Block Store (Amazon EBS) volume to a node in your EKS orchestrated HyperPod cluster.

 This API works with the Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver to manage the lifecycle of persistent storage in your HyperPod EKS clusters.

## Request Syntax
<a name="API_AttachClusterNodeVolume_RequestSyntax"></a>

```
{
   "ClusterArn": "{{string}}",
   "NodeId": "{{string}}",
   "VolumeId": "{{string}}"
}
```

## Request Parameters
<a name="API_AttachClusterNodeVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterArn](#API_AttachClusterNodeVolume_RequestSyntax) **   <a name="sagemaker-AttachClusterNodeVolume-request-ClusterArn"></a>
 The Amazon Resource Name (ARN) of your SageMaker HyperPod cluster containing the target node. Your cluster must use EKS as the orchestration and be in the `InService` state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [NodeId](#API_AttachClusterNodeVolume_RequestSyntax) **   <a name="sagemaker-AttachClusterNodeVolume-request-NodeId"></a>
 The unique identifier of the cluster node to which you want to attach the volume. The node must belong to your specified HyperPod cluster and cannot be part of a Restricted Instance Group (RIG).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: Yes

 ** [VolumeId](#API_AttachClusterNodeVolume_RequestSyntax) **   <a name="sagemaker-AttachClusterNodeVolume-request-VolumeId"></a>
 The unique identifier of your EBS volume to attach. The volume must be in the `available` state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `vol-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: Yes

## Response Syntax
<a name="API_AttachClusterNodeVolume_ResponseSyntax"></a>

```
{
   "ClusterArn": "string",
   "DeviceName": "string",
   "NodeId": "string",
   "Status": "string",
   "VolumeId": "string"
}
```

## Response Elements
<a name="API_AttachClusterNodeVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_AttachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeVolume-response-ClusterArn"></a>
 The Amazon Resource Name (ARN) of your SageMaker HyperPod cluster where the volume attachment operation was performed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

 ** [DeviceName](#API_AttachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeVolume-response-DeviceName"></a>
 The device name assigned to your attached volume on the target instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `/dev/(xvd[a-z]|sd[b-z]|sd[f-p][1-6])`

 ** [NodeId](#API_AttachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeVolume-response-NodeId"></a>
 The unique identifier of the cluster node where your volume was attached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`

 ** [Status](#API_AttachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeVolume-response-Status"></a>
 The current status of your volume attachment operation.
Type: String
Valid Values: `attaching | attached | detaching | detached | busy`

 ** [VolumeId](#API_AttachClusterNodeVolume_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeVolume-response-VolumeId"></a>
 The unique identifier of your EBS volume that was attached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `vol-[a-f0-9]{8}(?:[a-f0-9]{9})?`

## Errors
<a name="API_AttachClusterNodeVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_AttachClusterNodeVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/AttachClusterNodeVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AttachClusterNodeVolume)
