---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ClusterMetadata.html
---

# ClusterMetadata
<a name="API_ClusterMetadata"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Contains metadata about a specific cluster.

## Contents
<a name="API_ClusterMetadata_Contents"></a>

 ** AddressId **   <a name="Snowball-Type-ClusterMetadata-AddressId"></a>
The automatically generated ID for a specific address.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** ClusterId **   <a name="Snowball-Type-ClusterMetadata-ClusterId"></a>
The automatically generated ID for a cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ClusterState **   <a name="Snowball-Type-ClusterMetadata-ClusterState"></a>
The current status of the cluster.
Type: String
Valid Values: `AwaitingQuorum | Pending | InUse | Complete | Cancelled`
Required: No

 ** CreationDate **   <a name="Snowball-Type-ClusterMetadata-CreationDate"></a>
The creation date for this cluster.
Type: Timestamp
Required: No

 ** Description **   <a name="Snowball-Type-ClusterMetadata-Description"></a>
The optional description of the cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ForwardingAddressId **   <a name="Snowball-Type-ClusterMetadata-ForwardingAddressId"></a>
This field is not supported in your region.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** JobType **   <a name="Snowball-Type-ClusterMetadata-JobType"></a>
The type of job for this cluster. Currently, the only job type supported for clusters is `LOCAL_USE`.
Type: String
Valid Values: `IMPORT | EXPORT | LOCAL_USE`
Required: No

 ** KmsKeyARN **   <a name="Snowball-Type-ClusterMetadata-KmsKeyARN"></a>
The `KmsKeyARN` Amazon Resource Name (ARN) associated with this cluster. This ARN was created using the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) API action in AWS Key Management Service (AWS KMS.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`
Required: No

 ** Notification **   <a name="Snowball-Type-ClusterMetadata-Notification"></a>
The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.
Type: [Notification](API_Notification.md) object
Required: No

 ** OnDeviceServiceConfiguration **   <a name="Snowball-Type-ClusterMetadata-OnDeviceServiceConfiguration"></a>
Represents metadata and configuration settings for services on an AWS Snowball Edge device.
Type: [OnDeviceServiceConfiguration](API_OnDeviceServiceConfiguration.md) object
Required: No

 ** Resources **   <a name="Snowball-Type-ClusterMetadata-Resources"></a>
The arrays of [JobResource](API_JobResource.md) objects that can include updated [S3Resource](API_S3Resource.md) objects or [LambdaResource](API_LambdaResource.md) objects.
Type: [JobResource](API_JobResource.md) object
Required: No

 ** RoleARN **   <a name="Snowball-Type-ClusterMetadata-RoleARN"></a>
The role ARN associated with this cluster. This ARN was created using the [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) API action in AWS Identity and Access Management (IAM).
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:iam::[0-9]{12}:role/.*`
Required: No

 ** ShippingOption **   <a name="Snowball-Type-ClusterMetadata-ShippingOption"></a>
The shipping speed for each node in this cluster. This speed doesn't dictate how soon you'll get each device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows:
+ In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.
+ In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
+ In India, Snow devices are delivered in one to seven days.
+ In the US, you have access to one-day shipping and two-day shipping.
Type: String
Valid Values: `SECOND_DAY | NEXT_DAY | EXPRESS | STANDARD`
Required: No

 ** SnowballType **   <a name="Snowball-Type-ClusterMetadata-SnowballType"></a>
The type of Snowball Edge device to use for this cluster.
For cluster jobs, AWS Snowball Edge currently supports only the `EDGE` device type.
Type: String
Valid Values: `STANDARD | EDGE | EDGE_C | EDGE_CG | EDGE_S | SNC1_HDD | SNC1_SSD | V3_5C | V3_5S | RACK_5U_C`
Required: No

 ** TaxDocuments **   <a name="Snowball-Type-ClusterMetadata-TaxDocuments"></a>
The tax documents required in your AWS Region.
Type: [TaxDocuments](API_TaxDocuments.md) object
Required: No

## See Also
<a name="API_ClusterMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ClusterMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ClusterMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ClusterMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
