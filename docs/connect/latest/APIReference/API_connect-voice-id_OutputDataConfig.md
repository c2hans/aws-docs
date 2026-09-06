---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_OutputDataConfig.html
---

# OutputDataConfig
<a name="API_connect-voice-id_OutputDataConfig"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The configuration containing output file information for a batch job.

## Contents
<a name="API_connect-voice-id_OutputDataConfig_Contents"></a>

 ** S3Uri **   <a name="connect-Type-connect-voice-id_OutputDataConfig-S3Uri"></a>
The S3 path of the folder where Voice ID writes the job output file. It has a `*.out` extension. For example, if the input file name is `input-file.json` and the output folder path is `s3://output-bucket/output-folder`, the full output file path is `s3://output-bucket/output-folder/job-Id/input-file.json.out`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

 ** KmsKeyId **   <a name="connect-Type-connect-voice-id_OutputDataConfig-KmsKeyId"></a>
The identifier of the KMS key you want Voice ID to use to encrypt the output file of a speaker enrollment job/fraudster registration job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_connect-voice-id_OutputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/OutputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/OutputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/OutputDataConfig)
