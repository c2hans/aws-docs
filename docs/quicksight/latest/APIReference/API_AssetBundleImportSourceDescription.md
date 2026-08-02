---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportSourceDescription.html
---

# AssetBundleImportSourceDescription
<a name="API_AssetBundleImportSourceDescription"></a>

A description of the import source that you provide at the start of an import job. This value is set to either `Body` or `S3Uri`, depending on how the `StartAssetBundleImportJobRequest` is configured.

## Contents
<a name="API_AssetBundleImportSourceDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Body **   <a name="QS-Type-AssetBundleImportSourceDescription-Body"></a>
An HTTPS download URL for the provided asset bundle that you optionally provided at the start of the import job. This URL is valid for five minutes after issuance. Call `DescribeAssetBundleExportJob` again for a fresh URL if needed. The downloaded asset bundle is a `.qs` zip file.
Type: String
Pattern: `^(https|s3)://([^/]+)/?(.*)$`
Required: No

 ** S3Uri **   <a name="QS-Type-AssetBundleImportSourceDescription-S3Uri"></a>
The Amazon S3 URI that you provided at the start of the import job.
Type: String
Pattern: `^(https|s3)://([^/]+)/?(.*)$`
Required: No

## See Also
<a name="API_AssetBundleImportSourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportSourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportSourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportSourceDescription)
