---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StartSigningJobParameter.html
---

# StartSigningJobParameter
<a name="API_StartSigningJobParameter"></a>

Information required to start a signing job.

## Contents
<a name="API_StartSigningJobParameter_Contents"></a>

 ** destination **   <a name="iot-Type-StartSigningJobParameter-destination"></a>
The location to write the code-signed file.
Type: [Destination](API_Destination.md) object
Required: No

 ** signingProfileName **   <a name="iot-Type-StartSigningJobParameter-signingProfileName"></a>
The code-signing profile name.
Type: String
Required: No

 ** signingProfileParameter **   <a name="iot-Type-StartSigningJobParameter-signingProfileParameter"></a>
Describes the code-signing profile.
Type: [SigningProfileParameter](API_SigningProfileParameter.md) object
Required: No

## See Also
<a name="API_StartSigningJobParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StartSigningJobParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StartSigningJobParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StartSigningJobParameter)
