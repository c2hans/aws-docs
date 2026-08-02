---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateCluster.html
---

# UpdateCluster
<a name="API_UpdateCluster"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

While a cluster's `ClusterState` value is in the `AwaitingQuorum` state, you can update some of the information associated with a cluster. Once the cluster changes to a different job state, usually 60 minutes after the cluster being created, this action is no longer available.

## Request Syntax
<a name="API_UpdateCluster_RequestSyntax"></a>

```
{
   "AddressId": "{{string}}",
   "ClusterId": "{{string}}",
   "Description": "{{string}}",
   "ForwardingAddressId": "{{string}}",
   "Notification": {
      "DevicePickupSnsTopicARN": "{{string}}",
      "JobStatesToNotify": [ "{{string}}" ],
      "NotifyAll": {{boolean}},
      "SnsTopicARN": "{{string}}"
   },
   "OnDeviceServiceConfiguration": {
      "EKSOnDeviceService": {
         "EKSAnywhereVersion": "{{string}}",
         "KubernetesVersion": "{{string}}"
      },
      "NFSOnDeviceService": {
         "StorageLimit": {{number}},
         "StorageUnit": "{{string}}"
      },
      "S3OnDeviceService": {
         "FaultTolerance": {{number}},
         "ServiceSize": {{number}},
         "StorageLimit": {{number}},
         "StorageUnit": "{{string}}"
      },
      "TGWOnDeviceService": {
         "StorageLimit": {{number}},
         "StorageUnit": "{{string}}"
      }
   },
   "Resources": {
      "Ec2AmiResources": [
         {
            "AmiId": "{{string}}",
            "SnowballAmiId": "{{string}}"
         }
      ],
      "LambdaResources": [
         {
            "EventTriggers": [
               {
                  "EventResourceARN": "{{string}}"
               }
            ],
            "LambdaArn": "{{string}}"
         }
      ],
      "S3Resources": [
         {
            "BucketArn": "{{string}}",
            "KeyRange": {
               "BeginMarker": "{{string}}",
               "EndMarker": "{{string}}"
            },
            "TargetOnDeviceServices": [
               {
                  "ServiceName": "{{string}}",
                  "TransferOption": "{{string}}"
               }
            ]
         }
      ]
   },
   "RoleARN": "{{string}}",
   "ShippingOption": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddressId](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-AddressId"></a>
The ID of the updated [Address](API_Address.md) object.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [ClusterId](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-ClusterId"></a>
The cluster ID of the cluster that you want to update, for example `CID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `CID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [Description](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-Description"></a>
The updated description of this cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [ForwardingAddressId](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-ForwardingAddressId"></a>
This field is not supported in your region.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [Notification](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-Notification"></a>
The new or updated [Notification](API_Notification.md) object.
Type: [Notification](API_Notification.md) object
Required: No

 ** [OnDeviceServiceConfiguration](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-OnDeviceServiceConfiguration"></a>
Specifies the service or services on the Snowball Edge device that your transferred data will be exported from or imported into. AWS Snowball Edge device clusters support Amazon S3 and NFS (Network File System).
Type: [OnDeviceServiceConfiguration](API_OnDeviceServiceConfiguration.md) object
Required: No

 ** [Resources](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-Resources"></a>
The updated arrays of [JobResource](API_JobResource.md) objects that can include updated [S3Resource](API_S3Resource.md) objects or [LambdaResource](API_LambdaResource.md) objects.
Type: [JobResource](API_JobResource.md) object
Required: No

 ** [RoleARN](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-RoleARN"></a>
The new role Amazon Resource Name (ARN) that you want to associate with this cluster. To create a role ARN, use the [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) API action in AWS Identity and Access Management (IAM).
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:iam::[0-9]{12}:role/.*`
Required: No

 ** [ShippingOption](#API_UpdateCluster_RequestSyntax) **   <a name="Snowball-UpdateCluster-request-ShippingOption"></a>
The updated shipping option value of this cluster's [ShippingDetails](API_ShippingDetails.md) object.
Type: String
Valid Values: `SECOND_DAY | NEXT_DAY | EXPRESS | STANDARD`
Required: No

## Response Elements
<a name="API_UpdateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** Ec2RequestFailedException **
Your user lacks the necessary Amazon EC2 permissions to perform the attempted action.
HTTP Status Code: 400

 ** InvalidInputCombinationException **
Job or cluster creation failed. One or more inputs were invalid. Confirm that the `SnowballType` value supports your `JobType`, and try again.
HTTP Status Code: 400

 ** InvalidJobStateException **
The action can't be performed because the job's current state doesn't allow that action to be performed.
HTTP Status Code: 400

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

 ** KMSRequestFailedException **
The provided AWS Key Management Service key lacks the permissions to perform the specified [CreateJob](API_CreateJob.md) or [UpdateJob](API_UpdateJob.md) action.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/UpdateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/UpdateCluster)
