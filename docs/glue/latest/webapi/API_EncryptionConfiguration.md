---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

Specifies an encryption configuration.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** CloudWatchEncryption **   <a name="Glue-Type-EncryptionConfiguration-CloudWatchEncryption"></a>
The encryption configuration for Amazon CloudWatch.
Type: [CloudWatchEncryption](API_CloudWatchEncryption.md) object
Required: No

 ** DataQualityEncryption **   <a name="Glue-Type-EncryptionConfiguration-DataQualityEncryption"></a>
The encryption configuration for AWS Glue Data Quality assets.
Type: [DataQualityEncryption](API_DataQualityEncryption.md) object
Required: No

 ** JobBookmarksEncryption **   <a name="Glue-Type-EncryptionConfiguration-JobBookmarksEncryption"></a>
The encryption configuration for job bookmarks.
Type: [JobBookmarksEncryption](API_JobBookmarksEncryption.md) object
Required: No

 ** S3Encryption **   <a name="Glue-Type-EncryptionConfiguration-S3Encryption"></a>
The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.
Type: Array of [S3Encryption](API_S3Encryption.md) objects
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/EncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
