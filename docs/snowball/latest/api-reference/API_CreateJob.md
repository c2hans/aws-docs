---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateJob.html
---

# CreateJob
<a name="API_CreateJob"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Creates a job to import or export data between Amazon S3 and your on-premises data center. Your AWS account must have the right trust policies and permissions in place to create a job for a Snow device. If you're creating a job for a node in a cluster, you only need to provide the `clusterId` value; the other job attributes are inherited from the cluster.

**Note**
Only the Snowball Edge device type is supported when ordering clustered jobs.
The device capacity is optional.
Availability of device types differ by AWS Region. For more information about Region availability, see [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?p=ngi&loc=4).

**Snow Family devices and their capacities.**
+ Device type: **V3\_5C**
  + Capacity: T32
  + Description: Snowball Edge Compute Optimized

+ Device type: **V3\_5S**
  + Capacity: T240
  + Description: Snowball Edge Storage Optimized 210TB

## Request Syntax
<a name="API_CreateJob_RequestSyntax"></a>

```
{
   "AddressId": "{{string}}",
   "ClusterId": "{{string}}",
   "Description": "{{string}}",
   "DeviceConfiguration": {
      "SnowconeDeviceConfiguration": {
         "WirelessConnection": {
            "IsWifiEnabled": {{boolean}}
         }
      }
   },
   "ForwardingAddressId": "{{string}}",
   "ImpactLevel": "{{string}}",
   "JobType": "{{string}}",
   "KmsKeyARN": "{{string}}",
   "LongTermPricingId": "{{string}}",
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
   "RemoteManagement": "{{string}}",
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
   "SnowballCapacityPreference": "{{string}}",
   "SnowballType": "{{string}}",
   "TaxDocuments": {
      "IND": {
         "GSTIN": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_CreateJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddressId](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-AddressId"></a>
The ID for the address that you want the Snow device shipped to.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [ClusterId](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-ClusterId"></a>
The ID of a cluster. If you're creating a job for a node in a cluster, you need to provide only this `clusterId` value. The other job attributes are inherited from the cluster.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `CID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [Description](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-Description"></a>
Defines an optional description of this specific job, for example `Important Photos 2016-08-11`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\s\-\_\.\:]+$`
Required: No

 ** [DeviceConfiguration](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-DeviceConfiguration"></a>
Defines the device configuration for an AWS Snowball Edge job.
For information about Snowball Edge device types, see [Device hardware information](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html) in the Snowball Edge Developer Guide.
Type: [DeviceConfiguration](API_DeviceConfiguration.md) object
Required: No

 ** [ForwardingAddressId](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-ForwardingAddressId"></a>
This field is not supported in your Region.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [ImpactLevel](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-ImpactLevel"></a>
The highest impact level of data that will be stored or processed on the device, provided at job creation.
Type: String
Valid Values: `IL2 | IL4 | IL5 | IL6 | IL99`
Required: No

 ** [JobType](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-JobType"></a>
Defines the type of job that you're creating.
Type: String
Valid Values: `IMPORT | EXPORT | LOCAL_USE`
Required: No

 ** [KmsKeyARN](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-KmsKeyARN"></a>
The `KmsKeyARN` that you want to associate with this job. `KmsKeyARN`s are created using the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) AWS Key Management Service (KMS) API action.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`
Required: No

 ** [LongTermPricingId](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-LongTermPricingId"></a>
The ID of the long-term pricing type for the device.
Type: String
Length Constraints: Fixed length of 41.
Pattern: `LTPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [Notification](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-Notification"></a>
Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.
Type: [Notification](API_Notification.md) object
Required: No

 ** [OnDeviceServiceConfiguration](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-OnDeviceServiceConfiguration"></a>
Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. AWS Snow Family supports Amazon S3 and NFS (Network File System).
Type: [OnDeviceServiceConfiguration](API_OnDeviceServiceConfiguration.md) object
Required: No

 ** [PickupDetails](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-PickupDetails"></a>
Information identifying the person picking up the device.
Type: [PickupDetails](API_PickupDetails.md) object
Required: No

 ** [RemoteManagement](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-RemoteManagement"></a>
Allows you to securely operate and manage Snowcone devices remotely from outside of your internal network. When set to `INSTALLED_AUTOSTART`, remote management will automatically be available when the device arrives at your location. Otherwise, you need to use the Snowball Edge client to manage the device. When set to `NOT_INSTALLED`, remote management will not be available on the device.
Type: String
Valid Values: `INSTALLED_ONLY | INSTALLED_AUTOSTART | NOT_INSTALLED`
Required: No

 ** [Resources](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-Resources"></a>
Defines the Amazon S3 buckets associated with this job.
With `IMPORT` jobs, you specify the bucket or buckets that your transferred data will be imported into.
With `EXPORT` jobs, you specify the bucket or buckets that your transferred data will be exported from. Optionally, you can also specify a `KeyRange` value. If you choose to export a range, you define the length of the range by providing either an inclusive `BeginMarker` value, an inclusive `EndMarker` value, or both. Ranges are UTF-8 binary sorted.
Type: [JobResource](API_JobResource.md) object
Required: No

 ** [RoleARN](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-RoleARN"></a>
The `RoleARN` that you want to associate with this job. `RoleArn`s are created using the [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) AWS Identity and Access Management (IAM) API action.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:iam::[0-9]{12}:role/.*`
Required: No

 ** [ShippingOption](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-ShippingOption"></a>
The shipping speed for this job. This speed doesn't dictate how soon you'll get the Snow device, rather it represents how quickly the Snow device moves to its destination while in transit. Regional shipping speeds are as follows:
+ In Australia, you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day.
+ In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
+ In India, Snow devices are delivered in one to seven days.
+ In the US, you have access to one-day shipping and two-day shipping.
Type: String
Valid Values: `SECOND_DAY | NEXT_DAY | EXPRESS | STANDARD`
Required: No

 ** [SnowballCapacityPreference](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-SnowballCapacityPreference"></a>
If your job is being created in one of the US regions, you have the option of specifying what size Snow device you'd like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.
For information about Snowball Edge device types, see [Device hardware information](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html) in the Snowball Edge Developer Guide.
Type: String
Valid Values: `T50 | T80 | T100 | T42 | T98 | T8 | T14 | T32 | NoPreference | T240 | T13`
Required: No

 ** [SnowballType](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-SnowballType"></a>
The type of Snow Family devices to use for this job.
For cluster jobs, AWS Snowball Edge currently supports only the `EDGE` device type.
The type of AWS Snow device to use for this job. Currently, the only supported device type for cluster jobs is `EDGE`.
For more information, see [Device hardware information](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html) in the Snowball Edge Developer Guide.
Type: String
Valid Values: `STANDARD | EDGE | EDGE_C | EDGE_CG | EDGE_S | SNC1_HDD | SNC1_SSD | V3_5C | V3_5S | RACK_5U_C`
Required: No

 ** [TaxDocuments](#API_CreateJob_RequestSyntax) **   <a name="Snowball-CreateJob-request-TaxDocuments"></a>
The tax documents required in your AWS Region.
Type: [TaxDocuments](API_TaxDocuments.md) object
Required: No

## Response Syntax
<a name="API_CreateJob_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements
<a name="API_CreateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_CreateJob_ResponseSyntax) **   <a name="Snowball-CreateJob-response-JobId"></a>
The automatically generated ID for a job, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_CreateJob_Errors"></a>

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

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

 ** KMSRequestFailedException **
The provided AWS Key Management Service key lacks the permissions to perform the specified [CreateJob](#API_CreateJob) or [UpdateJob](API_UpdateJob.md) action.
HTTP Status Code: 400

## See Also
<a name="API_CreateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/CreateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/CreateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/CreateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/CreateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/CreateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/CreateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/CreateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/CreateJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/CreateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/CreateJob)
