---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateCluster.html
---

# CreateCluster
<a name="API_CreateCluster"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Creates an empty cluster. Each cluster supports five nodes. You use the [CreateJob](API_CreateJob.md) action separately to create the jobs for each of these nodes. The cluster does not ship until these five node jobs have been created.

## Request Syntax
<a name="API_CreateCluster_RequestSyntax"></a>

```
{
   "AddressId": "{{string}}",
   "Description": "{{string}}",
   "ForceCreateJobs": {{boolean}},
   "ForwardingAddressId": "{{string}}",
   "InitialClusterSize": {{number}},
   "JobType": "{{string}}",
   "KmsKeyARN": "{{string}}",
   "LongTermPricingIds": [ "{{string}}" ],
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
<a name="API_CreateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddressId](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-AddressId"></a>
The ID for the address that you want the cluster shipped to.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [Description](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-Description"></a>
An optional description of this specific cluster, for example `Environmental Data Cluster-01`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [ForceCreateJobs](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-ForceCreateJobs"></a>
Force to create cluster when user attempts to overprovision or underprovision a cluster. A cluster is overprovisioned or underprovisioned if the initial size of the cluster is more (overprovisioned) or less (underprovisioned) than what needed to meet capacity requirement specified with `OnDeviceServiceConfiguration`.
Type: Boolean
Required: No

 ** [ForwardingAddressId](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-ForwardingAddressId"></a>
This field is not supported in your region.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [InitialClusterSize](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-InitialClusterSize"></a>
If provided, each job will be automatically created and associated with the new cluster. If not provided, will be treated as 0.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 16.
Required: No

 ** [JobType](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-JobType"></a>
The type of job for this cluster. Currently, the only job type supported for clusters is `LOCAL_USE`.
For information about Snowball Edge device types, [Device hardware information](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html) in the Snowball Edge Developer Guide.
Type: String
Valid Values: `IMPORT | EXPORT | LOCAL_USE`
Required: Yes

 ** [KmsKeyARN](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-KmsKeyARN"></a>
The `KmsKeyARN` value that you want to associate with this cluster. `KmsKeyARN` values are created by using the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) API action in AWS Key Management Service (AWS KMS).
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`
Required: No

 ** [LongTermPricingIds](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-LongTermPricingIds"></a>
Lists long-term pricing id that will be used to associate with jobs automatically created for the new cluster.
Type: Array of strings
Length Constraints: Fixed length of 41.
Pattern: `LTPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [Notification](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-Notification"></a>
The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.
Type: [Notification](API_Notification.md) object
Required: No

 ** [OnDeviceServiceConfiguration](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-OnDeviceServiceConfiguration"></a>
Specifies the service or services on the Snowball Edge device that your transferred data will be exported from or imported into. AWS Snowball Edge device clusters support Amazon S3 and NFS (Network File System).
Type: [OnDeviceServiceConfiguration](API_OnDeviceServiceConfiguration.md) object
Required: No

 ** [RemoteManagement](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-RemoteManagement"></a>
Allows you to securely operate and manage Snow devices in a cluster remotely from outside of your internal network. When set to `INSTALLED_AUTOSTART`, remote management will automatically be available when the device arrives at your location. Otherwise, you need to use the Snowball Client to manage the device.
Type: String
Valid Values: `INSTALLED_ONLY | INSTALLED_AUTOSTART | NOT_INSTALLED`
Required: No

 ** [Resources](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-Resources"></a>
The resources associated with the cluster job. These resources include Amazon S3 buckets and optional AWS Lambda functions written in the Python language.
Type: [JobResource](API_JobResource.md) object
Required: No

 ** [RoleARN](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-RoleARN"></a>
The `RoleARN` that you want to associate with this cluster. `RoleArn` values are created by using the [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) API action in AWS Identity and Access Management (IAM).
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:iam::[0-9]{12}:role/.*`
Required: No

 ** [ShippingOption](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-ShippingOption"></a>
The shipping speed for each node in this cluster. This speed doesn't dictate how soon you'll get each Snowball Edge device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows:
+ In Australia, you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day.
+ In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
+ In India, Snow devices are delivered in one to seven days.
+ In the United States of America (US), you have access to one-day shipping and two-day shipping.
+ In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.
+ In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
+ In India, Snow devices are delivered in one to seven days.
+ In the US, you have access to one-day shipping and two-day shipping.
Type: String
Valid Values: `SECOND_DAY | NEXT_DAY | EXPRESS | STANDARD`
Required: Yes

 ** [SnowballCapacityPreference](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-SnowballCapacityPreference"></a>
If your job is being created in one of the US regions, you have the option of specifying what size Snow device you'd like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.
For information about Snowball Edge device types, see [Device hardware information](/snowball/latest/developer-guide/device-differences.html) in the Snowball Edge Developer Guide.
Type: String
Valid Values: `T50 | T80 | T100 | T42 | T98 | T8 | T14 | T32 | NoPreference | T240 | T13`
Required: No

 ** [SnowballType](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-SnowballType"></a>
The type of Snow Family devices to use for this cluster.
For cluster jobs, AWS Snowball Edge currently supports only the `EDGE` device type.
For information about Snowball Edge device types, see [Device hardware information](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html) in the Snowball Edge Developer Guide.
Type: String
Valid Values: `STANDARD | EDGE | EDGE_C | EDGE_CG | EDGE_S | SNC1_HDD | SNC1_SSD | V3_5C | V3_5S | RACK_5U_C`
Required: Yes

 ** [TaxDocuments](#API_CreateCluster_RequestSyntax) **   <a name="Snowball-CreateCluster-request-TaxDocuments"></a>
The tax documents required in your AWS Region.
Type: [TaxDocuments](API_TaxDocuments.md) object
Required: No

## Response Syntax
<a name="API_CreateCluster_ResponseSyntax"></a>

```
{
   "ClusterId": "string",
   "JobListEntries": [
      {
         "CreationDate": number,
         "Description": "string",
         "IsMaster": boolean,
         "JobId": "string",
         "JobState": "string",
         "JobType": "string",
         "SnowballType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterId](#API_CreateCluster_ResponseSyntax) **   <a name="Snowball-CreateCluster-response-ClusterId"></a>
The automatically generated ID for a cluster.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `CID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [JobListEntries](#API_CreateCluster_ResponseSyntax) **   <a name="Snowball-CreateCluster-response-JobListEntries"></a>
List of jobs created for this cluster. For syntax, see [ListJobsResult$JobListEntries](http://amazonaws.com/snowball/latest/api-reference/API_ListJobs.html#API_ListJobs_ResponseSyntax) in this guide.
Type: Array of [JobListEntry](API_JobListEntry.md) objects

## Errors
<a name="API_CreateCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
The provided AWS Key Management Service key lacks the permissions to perform the specified [CreateJob](API_CreateJob.md) or [UpdateJob](API_UpdateJob.md) action.
HTTP Status Code: 400

## See Also
<a name="API_CreateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/CreateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/CreateCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
