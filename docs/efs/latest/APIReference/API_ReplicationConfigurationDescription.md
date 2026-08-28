---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_ReplicationConfigurationDescription.html
---

# ReplicationConfigurationDescription
<a name="API_ReplicationConfigurationDescription"></a>

Describes the replication configuration for a specific file system.

## Contents
<a name="API_ReplicationConfigurationDescription_Contents"></a>

 ** CreationTime **   <a name="efs-Type-ReplicationConfigurationDescription-CreationTime"></a>
Describes when the replication configuration was created.
Type: Timestamp
Required: Yes

 ** Destinations **   <a name="efs-Type-ReplicationConfigurationDescription-Destinations"></a>
An array of destination objects. Only one destination object is supported.
Type: Array of [Destination](API_Destination.md) objects
Required: Yes

 ** OriginalSourceFileSystemArn **   <a name="efs-Type-ReplicationConfigurationDescription-OriginalSourceFileSystemArn"></a>
The Amazon Resource Name (ARN) of the original source EFS file system in the replication configuration.
Type: String
Required: Yes

 ** SourceFileSystemArn **   <a name="efs-Type-ReplicationConfigurationDescription-SourceFileSystemArn"></a>
The Amazon Resource Name (ARN) of the current source file system in the replication configuration.
Type: String
Required: Yes

 ** SourceFileSystemId **   <a name="efs-Type-ReplicationConfigurationDescription-SourceFileSystemId"></a>
The ID of the source Amazon EFS file system that is being replicated.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
Required: Yes

 ** SourceFileSystemRegion **   <a name="efs-Type-ReplicationConfigurationDescription-SourceFileSystemRegion"></a>
The AWS Region in which the source EFS file system is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
Required: Yes

 ** SourceFileSystemOwnerId **   <a name="efs-Type-ReplicationConfigurationDescription-SourceFileSystemOwnerId"></a>
ID of the AWS account in which the source file system resides.
Type: String
Length Constraints: Maximum length of 14.
Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`
Required: No

## See Also
<a name="API_ReplicationConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
