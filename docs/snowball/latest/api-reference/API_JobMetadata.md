---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_JobMetadata.html
---

# JobMetadata
<a name="API_JobMetadata"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Contains information about a specific job including shipping information, job status, and other important metadata. This information is returned as a part of the response syntax of the `DescribeJob` action.

## Contents
<a name="API_JobMetadata_Contents"></a>

 ** AddressId **   <a name="Snowball-Type-JobMetadata-AddressId"></a>
The ID for the address that you want the Snow device shipped to.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** ClusterId **   <a name="Snowball-Type-JobMetadata-ClusterId"></a>
The 39-character ID for the cluster, for example `CID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** CreationDate **   <a name="Snowball-Type-JobMetadata-CreationDate"></a>
The creation date for this job.
Type: Timestamp
Required: No

 ** DataTransferProgress **   <a name="Snowball-Type-JobMetadata-DataTransferProgress"></a>
A value that defines the real-time status of a Snow device's data transfer while the device is at AWS. This data is only available while a job has a `JobState` value of `InProgress`, for both import and export jobs.
Type: [DataTransfer](API_DataTransfer.md) object
Required: No

 ** Description **   <a name="Snowball-Type-JobMetadata-Description"></a>
The description of the job, provided at job creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** DeviceConfiguration **   <a name="Snowball-Type-JobMetadata-DeviceConfiguration"></a>
The container for `SnowconeDeviceConfiguration`.
Type: [DeviceConfiguration](API_DeviceConfiguration.md) object
Required: No

 ** ForwardingAddressId **   <a name="Snowball-Type-JobMetadata-ForwardingAddressId"></a>
This field is not supported in your region.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** ImpactLevel **   <a name="Snowball-Type-JobMetadata-ImpactLevel"></a>
The highest impact level of data that will be stored or processed on the device, provided at job creation.
Type: String
Valid Values: `IL2 | IL4 | IL5 | IL6 | IL99`
Required: No

 ** JobId **   <a name="Snowball-Type-JobMetadata-JobId"></a>
The automatically generated ID for a job, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** JobLogInfo **   <a name="Snowball-Type-JobMetadata-JobLogInfo"></a>
Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snow device for your job part is being delivered to you.
Type: [JobLogs](API_JobLogs.md) object
Required: No

 ** JobState **   <a name="Snowball-Type-JobMetadata-JobState"></a>
The current status of the jobs.
Type: String
Valid Values: `New | PreparingAppliance | PreparingShipment | InTransitToCustomer | WithCustomer | InTransitToAWS | WithAWSSortingFacility | WithAWS | InProgress | Complete | Cancelled | Listing | Pending`
Required: No

 ** JobType **   <a name="Snowball-Type-JobMetadata-JobType"></a>
The type of job.
Type: String
Valid Values: `IMPORT | EXPORT | LOCAL_USE`
Required: No

 ** KmsKeyARN **   <a name="Snowball-Type-JobMetadata-KmsKeyARN"></a>
The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated with this job. This ARN was created using the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) API action in AWS KMS.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`
Required: No

 ** LongTermPricingId **   <a name="Snowball-Type-JobMetadata-LongTermPricingId"></a>
The ID of the long-term pricing type for the device.
Type: String
Length Constraints: Fixed length of 41.
Pattern: `LTPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** Notification **   <a name="Snowball-Type-JobMetadata-Notification"></a>
The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The `Notification` object is returned as a part of the response syntax of the `DescribeJob` action in the `JobMetadata` data type.
Type: [Notification](API_Notification.md) object
Required: No

 ** OnDeviceServiceConfiguration **   <a name="Snowball-Type-JobMetadata-OnDeviceServiceConfiguration"></a>
Represents metadata and configuration settings for services on an AWS Snowball Edge device.
Type: [OnDeviceServiceConfiguration](API_OnDeviceServiceConfiguration.md) object
Required: No

 ** PickupDetails **   <a name="Snowball-Type-JobMetadata-PickupDetails"></a>
Information identifying the person picking up the device.
Type: [PickupDetails](API_PickupDetails.md) object
Required: No

 ** RemoteManagement **   <a name="Snowball-Type-JobMetadata-RemoteManagement"></a>
Allows you to securely operate and manage Snowcone devices remotely from outside of your internal network. When set to `INSTALLED_AUTOSTART`, remote management will automatically be available when the device arrives at your location. Otherwise, you need to use the Snowball Client to manage the device.
Type: String
Valid Values: `INSTALLED_ONLY | INSTALLED_AUTOSTART | NOT_INSTALLED`
Required: No

 ** Resources **   <a name="Snowball-Type-JobMetadata-Resources"></a>
An array of `S3Resource` objects. Each `S3Resource` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into.
Type: [JobResource](API_JobResource.md) object
Required: No

 ** RoleARN **   <a name="Snowball-Type-JobMetadata-RoleARN"></a>
The role ARN associated with this job. This ARN was created using the [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) API action in AWS Identity and Access Management.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:iam::[0-9]{12}:role/.*`
Required: No

 ** ShippingDetails **   <a name="Snowball-Type-JobMetadata-ShippingDetails"></a>
A job's shipping information, including inbound and outbound tracking numbers and shipping speed options.
Type: [ShippingDetails](API_ShippingDetails.md) object
Required: No

 ** SnowballCapacityPreference **   <a name="Snowball-Type-JobMetadata-SnowballCapacityPreference"></a>
The Snow device capacity preference for this job, specified at job creation. In US regions, you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity Snowballs.
For information about Snowball Edge device types, see [Device hardware differences](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html) in the Snowball Edge Developer Guide.
Type: String
Valid Values: `T50 | T80 | T100 | T42 | T98 | T8 | T14 | T32 | NoPreference | T240 | T13`
Required: No

 ** SnowballId **   <a name="Snowball-Type-JobMetadata-SnowballId"></a>
Unique ID associated with a device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** SnowballType **   <a name="Snowball-Type-JobMetadata-SnowballType"></a>
The type of device used with this job.
Type: String
Valid Values: `STANDARD | EDGE | EDGE_C | EDGE_CG | EDGE_S | SNC1_HDD | SNC1_SSD | V3_5C | V3_5S | RACK_5U_C`
Required: No

 ** TaxDocuments **   <a name="Snowball-Type-JobMetadata-TaxDocuments"></a>
The metadata associated with the tax documents required in your AWS Region.
Type: [TaxDocuments](API_TaxDocuments.md) object
Required: No

## See Also
<a name="API_JobMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/JobMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/JobMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/JobMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
