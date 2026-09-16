---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeCluster.html
---

# DescribeCluster
<a name="API_DescribeCluster"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns information about a specific cluster including shipping information, cluster status, and other important metadata.

## Request Syntax
<a name="API_DescribeCluster_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_DescribeCluster_RequestSyntax) **   <a name="Snowball-DescribeCluster-request-ClusterId"></a>
The automatically generated ID for a cluster.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `CID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeCluster_ResponseSyntax"></a>

```
{
   "ClusterMetadata": {
      "AddressId": "string",
      "ClusterId": "string",
      "ClusterState": "string",
      "CreationDate": number,
      "Description": "string",
      "ForwardingAddressId": "string",
      "JobType": "string",
      "KmsKeyARN": "string",
      "Notification": {
         "DevicePickupSnsTopicARN": "string",
         "JobStatesToNotify": [ "string" ],
         "NotifyAll": boolean,
         "SnsTopicARN": "string"
      },
      "OnDeviceServiceConfiguration": {
         "EKSOnDeviceService": {
            "EKSAnywhereVersion": "string",
            "KubernetesVersion": "string"
         },
         "NFSOnDeviceService": {
            "StorageLimit": number,
            "StorageUnit": "string"
         },
         "S3OnDeviceService": {
            "FaultTolerance": number,
            "ServiceSize": number,
            "StorageLimit": number,
            "StorageUnit": "string"
         },
         "TGWOnDeviceService": {
            "StorageLimit": number,
            "StorageUnit": "string"
         }
      },
      "Resources": {
         "Ec2AmiResources": [
            {
               "AmiId": "string",
               "SnowballAmiId": "string"
            }
         ],
         "LambdaResources": [
            {
               "EventTriggers": [
                  {
                     "EventResourceARN": "string"
                  }
               ],
               "LambdaArn": "string"
            }
         ],
         "S3Resources": [
            {
               "BucketArn": "string",
               "KeyRange": {
                  "BeginMarker": "string",
                  "EndMarker": "string"
               },
               "TargetOnDeviceServices": [
                  {
                     "ServiceName": "string",
                     "TransferOption": "string"
                  }
               ]
            }
         ]
      },
      "RoleARN": "string",
      "ShippingOption": "string",
      "SnowballType": "string",
      "TaxDocuments": {
         "IND": {
            "GSTIN": "string"
         }
      }
   }
}
```

## Response Elements
<a name="API_DescribeCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterMetadata](#API_DescribeCluster_ResponseSyntax) **   <a name="Snowball-DescribeCluster-response-ClusterMetadata"></a>
Information about a specific cluster, including shipping information, cluster status, and other important metadata.
Type: [ClusterMetadata](API_ClusterMetadata.md) object

## Errors
<a name="API_DescribeCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/DescribeCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/DescribeCluster)
