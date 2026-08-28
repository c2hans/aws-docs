---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_FileSystemProtectionDescription.html
---

# FileSystemProtectionDescription
<a name="API_FileSystemProtectionDescription"></a>

Describes the protection on a file system.

## Contents
<a name="API_FileSystemProtectionDescription_Contents"></a>

 ** ReplicationOverwriteProtection **   <a name="efs-Type-FileSystemProtectionDescription-ReplicationOverwriteProtection"></a>
The status of the file system's replication overwrite protection.
+  `ENABLED` – The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is `ENABLED` by default.
+  `DISABLED` – The file system can be used as the destination file system in a replication configuration. The file system is read-only and can only be modified by EFS replication.
+  `REPLICATING` – The file system is being used as the destination file system in a replication configuration. The file system is read-only and is modified only by EFS replication.
If the replication configuration is deleted, the file system's replication overwrite protection is re-enabled, the file system becomes writeable.
Type: String
Valid Values: `ENABLED | DISABLED | REPLICATING`
Required: No

## See Also
<a name="API_FileSystemProtectionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/FileSystemProtectionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/FileSystemProtectionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/FileSystemProtectionDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
