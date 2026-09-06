---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ReportConfigurationS3Output.html
---

# ReportConfigurationS3Output
<a name="API_ReportConfigurationS3Output"></a>

Describes the S3 destination for the experiment report.

## Contents
<a name="API_ReportConfigurationS3Output_Contents"></a>

 ** bucketName **   <a name="fis-Type-ReportConfigurationS3Output-bucketName"></a>
The name of the S3 bucket where the experiment report will be stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[\S]+`
Required: No

 ** prefix **   <a name="fis-Type-ReportConfigurationS3Output-prefix"></a>
The prefix of the S3 bucket where the experiment report will be stored.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ReportConfigurationS3Output_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ReportConfigurationS3Output)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ReportConfigurationS3Output)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ReportConfigurationS3Output)
