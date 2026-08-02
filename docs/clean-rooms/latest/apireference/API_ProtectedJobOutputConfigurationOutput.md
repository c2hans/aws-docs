---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJobOutputConfigurationOutput.html
---

# ProtectedJobOutputConfigurationOutput
<a name="API_ProtectedJobOutputConfigurationOutput"></a>

 The protected job output configuration output.

## Contents
<a name="API_ProtectedJobOutputConfigurationOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** member **   <a name="API-Type-ProtectedJobOutputConfigurationOutput-member"></a>
 The member output configuration for a protected job.
Type: [ProtectedJobMemberOutputConfigurationOutput](API_ProtectedJobMemberOutputConfigurationOutput.md) object
Required: No

 ** s3 **   <a name="API-Type-ProtectedJobOutputConfigurationOutput-s3"></a>
If present, the output for a protected job with an `S3` output type.
Type: [ProtectedJobS3OutputConfigurationOutput](API_ProtectedJobS3OutputConfigurationOutput.md) object
Required: No

## See Also
<a name="API_ProtectedJobOutputConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJobOutputConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJobOutputConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJobOutputConfigurationOutput)
