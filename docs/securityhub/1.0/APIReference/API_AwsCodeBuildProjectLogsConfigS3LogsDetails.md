---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCodeBuildProjectLogsConfigS3LogsDetails.html
---

# AwsCodeBuildProjectLogsConfigS3LogsDetails
<a name="API_AwsCodeBuildProjectLogsConfigS3LogsDetails"></a>

Information about logs built to an S3 bucket for a build project.

## Contents
<a name="API_AwsCodeBuildProjectLogsConfigS3LogsDetails_Contents"></a>

 ** EncryptionDisabled **   <a name="securityhub-Type-AwsCodeBuildProjectLogsConfigS3LogsDetails-EncryptionDisabled"></a>
Whether to disable encryption of the S3 build log output.
Type: Boolean
Required: No

 ** Location **   <a name="securityhub-Type-AwsCodeBuildProjectLogsConfigS3LogsDetails-Location"></a>
The ARN of the S3 bucket and the path prefix for S3 logs.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsCodeBuildProjectLogsConfigS3LogsDetails-Status"></a>
The current status of the S3 build logs.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCodeBuildProjectLogsConfigS3LogsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCodeBuildProjectLogsConfigS3LogsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCodeBuildProjectLogsConfigS3LogsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCodeBuildProjectLogsConfigS3LogsDetails)
