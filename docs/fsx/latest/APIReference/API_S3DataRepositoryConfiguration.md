---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_S3DataRepositoryConfiguration.html
---

# S3DataRepositoryConfiguration
<a name="API_S3DataRepositoryConfiguration"></a>

The configuration for an Amazon S3 data repository linked to an Amazon FSx for Lustre file system with a data repository association. The configuration consists of an `AutoImportPolicy` that defines which file events on the data repository are automatically imported to the file system and an `AutoExportPolicy` that defines which file events on the file system are automatically exported to the data repository. File events are when files or directories are added, changed, or deleted on the file system or the data repository.

**Note**
Data repository associations on Amazon File Cache don't use `S3DataRepositoryConfiguration` because they don't support automatic import or automatic export.

## Contents
<a name="API_S3DataRepositoryConfiguration_Contents"></a>

 ** AutoExportPolicy **   <a name="FSx-Type-S3DataRepositoryConfiguration-AutoExportPolicy"></a>
Specifies the type of updated objects (new, changed, deleted) that will be automatically exported from your file system to the linked S3 bucket.
Type: [AutoExportPolicy](API_AutoExportPolicy.md) object
Required: No

 ** AutoImportPolicy **   <a name="FSx-Type-S3DataRepositoryConfiguration-AutoImportPolicy"></a>
Specifies the type of updated objects (new, changed, deleted) that will be automatically imported from the linked S3 bucket to your file system.
Type: [AutoImportPolicy](API_AutoImportPolicy.md) object
Required: No

## See Also
<a name="API_S3DataRepositoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/S3DataRepositoryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/S3DataRepositoryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/S3DataRepositoryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
