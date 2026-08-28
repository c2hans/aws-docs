---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ManifestConfig.html
---

# ManifestConfig
<a name="API_ManifestConfig"></a>

Configures a manifest, which is a list of files or objects that you want AWS DataSync to transfer. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html).

## Contents
<a name="API_ManifestConfig_Contents"></a>

 ** Action **   <a name="DataSync-Type-ManifestConfig-Action"></a>
Specifies what DataSync uses the manifest for.
Type: String
Valid Values: `TRANSFER`
Required: No

 ** Format **   <a name="DataSync-Type-ManifestConfig-Format"></a>
Specifies the file format of your manifest. For more information, see [Creating a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-create).
Type: String
Valid Values: `CSV`
Required: No

 ** Source **   <a name="DataSync-Type-ManifestConfig-Source"></a>
Specifies the manifest that you want DataSync to use and where it's hosted.
You must specify this parameter if you're configuring a new manifest on or after February 7, 2024.
If you don't, you'll get a 400 status code and `ValidationException` error stating that you're missing the IAM role for DataSync to access the S3 bucket where you're hosting your manifest. For more information, see [Providing DataSync access to your manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access).
Type: [SourceManifestConfig](API_SourceManifestConfig.md) object
Required: No

## See Also
<a name="API_ManifestConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ManifestConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ManifestConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ManifestConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
