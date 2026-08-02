---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateJob.html
---

# UpdateJob
<a name="API_UpdateJob"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

While a job's `JobState` value is `New`, you can update some of the information associated with a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.

## Request Syntax
<a name="API_UpdateJob_RequestSyntax"></a>

```
{
   "AddressId": "{{string}}",
   "Description": "{{string}}",
   "ForwardingAddressId": "{{string}}",
   "JobId": "{{string}}",
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
   "PickupDetails": {
      "DevicePickupId": "{{string}}",
      "Email": "{{string}}",
      "IdentificationExpirationDate": {{number}},
      "IdentificationIssuingOrg": "{{string}}",
      "IdentificationNumber": "{{string}}",
      "Name": "{{string}}",
      "PhoneNumber": "{{string}}"
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
   "ShippingOption": "{{string}}",
   "SnowballCapacityPreference": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddressId](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-AddressId"></a>
The ID of the updated [Address](API_Address.md) object.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [Description](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-Description"></a>
The updated description of this job's [JobMetadata](API_JobMetadata.md) object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [ForwardingAddressId](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-ForwardingAddressId"></a>
This field is not supported in your region.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [JobId](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-JobId"></a>
The job ID of the job that you want to update, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [Notification](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-Notification"></a>
The new or updated [Notification](API_Notification.md) object.
Type: [Notification](API_Notification.md) object
Required: No

 ** [OnDeviceServiceConfiguration](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-OnDeviceServiceConfiguration"></a>
Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. AWS Snowball Edge supports Amazon S3 and NFS (Network File System).
Type: [OnDeviceServiceConfiguration](API_OnDeviceServiceConfiguration.md) object
Required: No

 ** [PickupDetails](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-PickupDetails"></a>
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).
Information identifying the person picking up the device.
Type: [PickupDetails](API_PickupDetails.md) object
Required: No

 ** [Resources](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-Resources"></a>
The updated `JobResource` object, or the updated [JobResource](API_JobResource.md) object.
Type: [JobResource](API_JobResource.md) object
Required: No

 ** [RoleARN](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-RoleARN"></a>
The new role Amazon Resource Name (ARN) that you want to associate with this job. To create a role ARN, use the [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) AWS Identity and Access Management (IAM) API action.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:iam::[0-9]{12}:role/.*`
Required: No

 ** [ShippingOption](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-ShippingOption"></a>
The updated shipping option value of this job's [ShippingDetails](API_ShippingDetails.md) object.
Type: String
Valid Values: `SECOND_DAY | NEXT_DAY | EXPRESS | STANDARD`
Required: No

 ** [SnowballCapacityPreference](#API_UpdateJob_RequestSyntax) **   <a name="Snowball-UpdateJob-request-SnowballCapacityPreference"></a>
The updated `SnowballCapacityPreference` of this job's [JobMetadata](API_JobMetadata.md) object.
For information about Snowball Edge device types, see [Device hardware information](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html) in the Snowball Edge Developer Guide.
Type: String
Valid Values: `T50 | T80 | T100 | T42 | T98 | T8 | T14 | T32 | NoPreference | T240 | T13`
Required: No

## Response Elements
<a name="API_UpdateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterLimitExceededException **
Job creation failed. Currently, clusters support five nodes. If you have fewer than five nodes for your cluster and you have more nodes to create for this cluster, try again and create jobs until your cluster has exactly five nodes.
HTTP Status Code: 400

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
The provided AWS Key Management Service key lacks the permissions to perform the specified [CreateJob](API_CreateJob.md) or [UpdateJob](#API_UpdateJob) action.
HTTP Status Code: 400

## See Also
<a name="API_UpdateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/UpdateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/UpdateJob)
