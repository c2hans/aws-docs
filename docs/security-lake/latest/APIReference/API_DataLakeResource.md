---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeResource.html
---

# DataLakeResource
<a name="API_DataLakeResource"></a>

Provides details of Amazon Security Lake object.

## Contents
<a name="API_DataLakeResource_Contents"></a>

 ** dataLakeArn **   <a name="securitylake-Type-DataLakeResource-dataLakeArn"></a>
The Amazon Resource Name (ARN) created by you to provide to the subscriber. For more information about ARNs and how to use them in policies, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws|aws-us-gov|aws-cn):securitylake:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9][A-Za-z0-9_/.\-]{0,127}`
Required: Yes

 ** region **   <a name="securitylake-Type-DataLakeResource-region"></a>
The AWS Regions where Security Lake is enabled.
Type: String
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`
Required: Yes

 ** createStatus **   <a name="securitylake-Type-DataLakeResource-createStatus"></a>
Retrieves the status of the `CreateDatalake` API call for an account in Amazon Security Lake.
Type: String
Valid Values: `INITIALIZED | PENDING | COMPLETED | FAILED`
Required: No

 ** encryptionConfiguration **   <a name="securitylake-Type-DataLakeResource-encryptionConfiguration"></a>
Provides encryption details of Amazon Security Lake object.
Type: [DataLakeEncryptionConfiguration](API_DataLakeEncryptionConfiguration.md) object
Required: No

 ** lifecycleConfiguration **   <a name="securitylake-Type-DataLakeResource-lifecycleConfiguration"></a>
Provides lifecycle details of Amazon Security Lake object.
Type: [DataLakeLifecycleConfiguration](API_DataLakeLifecycleConfiguration.md) object
Required: No

 ** replicationConfiguration **   <a name="securitylake-Type-DataLakeResource-replicationConfiguration"></a>
Provides replication details of Amazon Security Lake object.
Type: [DataLakeReplicationConfiguration](API_DataLakeReplicationConfiguration.md) object
Required: No

 ** s3BucketArn **   <a name="securitylake-Type-DataLakeResource-s3BucketArn"></a>
The ARN for the Amazon Security Lake Amazon S3 bucket.
Type: String
Required: No

 ** updateStatus **   <a name="securitylake-Type-DataLakeResource-updateStatus"></a>
The status of the last `UpdateDataLake `or `DeleteDataLake` API request.
Type: [DataLakeUpdateStatus](API_DataLakeUpdateStatus.md) object
Required: No

## See Also
<a name="API_DataLakeResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
