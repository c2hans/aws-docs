---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResourceDataSyncS3Destination.html
---

# ResourceDataSyncS3Destination
<a name="API_ResourceDataSyncS3Destination"></a>

Information about the target S3 bucket for the resource data sync.

## Contents
<a name="API_ResourceDataSyncS3Destination_Contents"></a>

 ** BucketName **   <a name="systemsmanager-Type-ResourceDataSyncS3Destination-BucketName"></a>
The name of the S3 bucket where the aggregated data is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Region **   <a name="systemsmanager-Type-ResourceDataSyncS3Destination-Region"></a>
The AWS Region with the S3 bucket targeted by the resource data sync.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** SyncFormat **   <a name="systemsmanager-Type-ResourceDataSyncS3Destination-SyncFormat"></a>
A supported sync format. The following format is currently supported: JsonSerDe
Type: String
Valid Values: `JsonSerDe`
Required: Yes

 ** AWSKMSKeyARN **   <a name="systemsmanager-Type-ResourceDataSyncS3Destination-AWSKMSKeyARN"></a>
The ARN of an encryption key for a destination in Amazon S3. Must belong to the same Region as the destination S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*`
Required: No

 ** DestinationDataSharing **   <a name="systemsmanager-Type-ResourceDataSyncS3Destination-DestinationDataSharing"></a>
Enables destination data sharing. By default, this field is `null`.
Type: [ResourceDataSyncDestinationDataSharing](API_ResourceDataSyncDestinationDataSharing.md) object
Required: No

 ** Prefix **   <a name="systemsmanager-Type-ResourceDataSyncS3Destination-Prefix"></a>
An Amazon S3 prefix for the bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ResourceDataSyncS3Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ResourceDataSyncS3Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ResourceDataSyncS3Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ResourceDataSyncS3Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
