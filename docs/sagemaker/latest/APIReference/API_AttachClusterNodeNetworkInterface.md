---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AttachClusterNodeNetworkInterface.html
---

# AttachClusterNodeNetworkInterface
<a name="API_AttachClusterNodeNetworkInterface"></a>

 Attaches an elastic network interface (ENI) to a node in a HyperPod cluster.

 To use this operation, you must have the `sagemaker:AttachClusterNodeNetworkInterface` permission.

## Request Syntax
<a name="API_AttachClusterNodeNetworkInterface_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "NetworkInterfaceId": "{{string}}",
   "NodeId": "{{string}}"
}
```

## Request Parameters
<a name="API_AttachClusterNodeNetworkInterface_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_AttachClusterNodeNetworkInterface_RequestSyntax) **   <a name="sagemaker-AttachClusterNodeNetworkInterface-request-ClusterName"></a>
 The name or Amazon Resource Name (ARN) of the SageMaker HyperPod cluster that contains the target node.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [NetworkInterfaceId](#API_AttachClusterNodeNetworkInterface_RequestSyntax) **   <a name="sagemaker-AttachClusterNodeNetworkInterface-request-NetworkInterfaceId"></a>
 The unique identifier of the elastic network interface (ENI) to attach.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 21.
Pattern: `eni-[0-9a-f]{8}(?:[0-9a-f]{9})?`
Required: Yes

 ** [NodeId](#API_AttachClusterNodeNetworkInterface_RequestSyntax) **   <a name="sagemaker-AttachClusterNodeNetworkInterface-request-NodeId"></a>
 The unique identifier of the cluster node to which you want to attach the network interface. The node must belong to your specified HyperPod cluster and cannot be part of a Restricted Instance Group (RIG).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: Yes

## Response Syntax
<a name="API_AttachClusterNodeNetworkInterface_ResponseSyntax"></a>

```
{
   "AttachmentId": "string",
   "ClusterArn": "string",
   "NetworkInterfaceId": "string",
   "NodeId": "string"
}
```

## Response Elements
<a name="API_AttachClusterNodeNetworkInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentId](#API_AttachClusterNodeNetworkInterface_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeNetworkInterface-response-AttachmentId"></a>
 The unique identifier of the network interface attachment. Use this value to reference or detach the network interface later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 28.
Pattern: `eni-attach-[0-9a-f]{8}(?:[0-9a-f]{9})?`

 ** [ClusterArn](#API_AttachClusterNodeNetworkInterface_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeNetworkInterface-response-ClusterArn"></a>
 The Amazon Resource Name (ARN) of your SageMaker HyperPod cluster where the network interface attachment operation was performed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

 ** [NetworkInterfaceId](#API_AttachClusterNodeNetworkInterface_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeNetworkInterface-response-NetworkInterfaceId"></a>
 The unique identifier of the elastic network interface (ENI) that was attached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 21.
Pattern: `eni-[0-9a-f]{8}(?:[0-9a-f]{9})?`

 ** [NodeId](#API_AttachClusterNodeNetworkInterface_ResponseSyntax) **   <a name="sagemaker-AttachClusterNodeNetworkInterface-response-NodeId"></a>
 The unique identifier of the cluster node where your network interface was attached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`

## Errors
<a name="API_AttachClusterNodeNetworkInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_AttachClusterNodeNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AttachClusterNodeNetworkInterface)
