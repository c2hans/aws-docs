---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_InputDataConfig.html
---

# InputDataConfig
<a name="API_connect-voice-id_InputDataConfig"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The configuration containing input file information for a batch job.

## Contents
<a name="API_connect-voice-id_InputDataConfig_Contents"></a>

 ** S3Uri **   <a name="connect-Type-connect-voice-id_InputDataConfig-S3Uri"></a>
The S3 location for the input manifest file that contains the list of individual enrollment or registration job requests.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

## See Also
<a name="API_connect-voice-id_InputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/InputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/InputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/InputDataConfig)
