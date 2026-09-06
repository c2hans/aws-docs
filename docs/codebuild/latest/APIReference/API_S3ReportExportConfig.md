---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_S3ReportExportConfig.html
---

# S3ReportExportConfig
<a name="API_S3ReportExportConfig"></a>

 Information about the S3 bucket where the raw data of a report are exported.

## Contents
<a name="API_S3ReportExportConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** bucket **   <a name="CodeBuild-Type-S3ReportExportConfig-bucket"></a>
 The name of the S3 bucket where the raw data of a report are exported.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** bucketOwner **   <a name="CodeBuild-Type-S3ReportExportConfig-bucketOwner"></a>
The AWS account identifier of the owner of the Amazon S3 bucket. This allows report data to be exported to an Amazon S3 bucket that is owned by an account other than the account running the build.
Type: String
Required: No

 ** encryptionDisabled **   <a name="CodeBuild-Type-S3ReportExportConfig-encryptionDisabled"></a>
 A boolean value that specifies if the results of a report are encrypted.
Type: Boolean
Required: No

 ** encryptionKey **   <a name="CodeBuild-Type-S3ReportExportConfig-encryptionKey"></a>
 The encryption key for the report's encrypted raw data.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** packaging **   <a name="CodeBuild-Type-S3ReportExportConfig-packaging"></a>
 The type of build output artifact to create. Valid values include:
+  `NONE`: CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.
+  `ZIP`: CodeBuild creates a ZIP file with the raw data in the output bucket.
Type: String
Valid Values: `ZIP | NONE`
Required: No

 ** path **   <a name="CodeBuild-Type-S3ReportExportConfig-path"></a>
 The path to the exported report's raw data results.
Type: String
Required: No

## See Also
<a name="API_S3ReportExportConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/S3ReportExportConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/S3ReportExportConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/S3ReportExportConfig)
