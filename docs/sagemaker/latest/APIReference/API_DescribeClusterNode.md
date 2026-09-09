---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterNode.html
---

# DescribeClusterNode
<a name="API_DescribeClusterNode"></a>

Retrieves information of a node (also called a *instance* interchangeably) of a SageMaker HyperPod cluster.

## Request Syntax
<a name="API_DescribeClusterNode_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "NodeId": "{{string}}",
   "NodeLogicalId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeClusterNode_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_DescribeClusterNode_RequestSyntax) **   <a name="sagemaker-DescribeClusterNode-request-ClusterName"></a>
The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster in which the node is.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [NodeId](#API_DescribeClusterNode_RequestSyntax) **   <a name="sagemaker-DescribeClusterNode-request-NodeId"></a>
The ID of the SageMaker HyperPod cluster node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: No

 ** [NodeLogicalId](#API_DescribeClusterNode_RequestSyntax) **   <a name="sagemaker-DescribeClusterNode-request-NodeLogicalId"></a>
The logical identifier of the node to describe. You can specify either `NodeLogicalId` or `InstanceId`, but not both. `NodeLogicalId` can be used to describe nodes that are still being provisioned and don't yet have an `InstanceId` assigned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: No

## Response Syntax
<a name="API_DescribeClusterNode_ResponseSyntax"></a>

```
{
   "NodeDetails": {
      "CapacityType": "string",
      "CurrentImageId": "string",
      "CurrentImageReleaseVersion": "string",
      "DesiredImageId": "string",
      "DesiredImageReleaseVersion": "string",
      "ImageVersionStatus": "string",
      "InstanceGroupName": "string",
      "InstanceId": "string",
      "InstanceStatus": {
         "Message": "string",
         "Status": "string"
      },
      "InstanceStorageConfigs": [
         { ... }
      ],
      "InstanceType": "string",
      "KubernetesConfig": {
         "CurrentLabels": {
            "string" : "string"
         },
         "CurrentTaints": [
            {
               "Effect": "string",
               "Key": "string",
               "Value": "string"
            }
         ],
         "DesiredLabels": {
            "string" : "string"
         },
         "DesiredTaints": [
            {
               "Effect": "string",
               "Key": "string",
               "Value": "string"
            }
         ]
      },
      "LifeCycleConfig": {
         "OnCreate": "string",
         "OnInitComplete": "string",
         "SourceS3Uri": "string"
      },
      "NetworkInterface": {
         "InterfaceType": "string"
      },
      "NodeLogicalId": "string",
      "OverrideVpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      },
      "Placement": {
         "AvailabilityZone": "string",
         "AvailabilityZoneId": "string"
      },
      "PrivateDnsHostname": "string",
      "PrivatePrimaryIp": "string",
      "PrivatePrimaryIpv6": "string",
      "ThreadsPerCore": number,
      "UltraServerInfo": {
         "Id": "string",
         "Type": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeClusterNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NodeDetails](#API_DescribeClusterNode_ResponseSyntax) **   <a name="sagemaker-DescribeClusterNode-response-NodeDetails"></a>
The details of the SageMaker HyperPod cluster node.
Type: [ClusterNodeDetails](API_ClusterNodeDetails.md) object

## Errors
<a name="API_DescribeClusterNode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeClusterNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeClusterNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeClusterNode)
