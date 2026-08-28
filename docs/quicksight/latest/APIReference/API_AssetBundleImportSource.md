---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportSource.html
---

# AssetBundleImportSource
<a name="API_AssetBundleImportSource"></a>

The source of the asset bundle zip file that contains the data that you want to import. The file must be in `QUICKSIGHT_JSON` format.

## Contents
<a name="API_AssetBundleImportSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Body **   <a name="QS-Type-AssetBundleImportSource-Body"></a>
The bytes of the base64 encoded asset bundle import zip file. This file can't exceed 20 MB. If the size of the file that you want to upload is more than 20 MB, add the file to your Amazon S3 bucket and use `S3Uri` of the file for this operation.
If you are calling the API operations from the AWS SDK for Java, JavaScript, Python, or PHP, the SDK encodes base64 automatically to allow the direct setting of the zip file's bytes. If you are using an SDK for a different language or receiving related errors, try to base64 encode your data.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 20971520.
Required: No

 ** S3Uri **   <a name="QS-Type-AssetBundleImportSource-S3Uri"></a>
The Amazon S3 URI for an asset bundle import file that exists in an Amazon S3 bucket that the caller has read access to. The file must be a zip format file and can't exceed 1 GB.
Type: String
Pattern: `^(https|s3)://([^/]+)/?(.*)$`
Required: No

## See Also
<a name="API_AssetBundleImportSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
