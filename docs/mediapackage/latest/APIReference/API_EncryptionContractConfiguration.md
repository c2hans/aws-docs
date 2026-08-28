---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_EncryptionContractConfiguration.html
---

# EncryptionContractConfiguration
<a name="API_EncryptionContractConfiguration"></a>

Configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

## Contents
<a name="API_EncryptionContractConfiguration_Contents"></a>

 ** PresetSpeke20Audio **   <a name="mediapackage-Type-EncryptionContractConfiguration-PresetSpeke20Audio"></a>
A collection of audio encryption presets.
Value description:
+ PRESET-AUDIO-1 - Use one content key to encrypt all of the audio tracks in your stream.
+ PRESET-AUDIO-2 - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks.
+ PRESET-AUDIO-3 - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels.
+ SHARED - Use the same content key for all of the audio and video tracks in your stream.
+ UNENCRYPTED - Don't encrypt any of the audio tracks in your stream.
Type: String
Valid Values: `PRESET_AUDIO_1 | PRESET_AUDIO_2 | PRESET_AUDIO_3 | SHARED | UNENCRYPTED`
Required: Yes

 ** PresetSpeke20Video **   <a name="mediapackage-Type-EncryptionContractConfiguration-PresetSpeke20Video"></a>
A collection of video encryption presets.
Value description:
+ PRESET-VIDEO-1 - Use one content key to encrypt all of the video tracks in your stream.
+ PRESET-VIDEO-2 - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks.
+ PRESET-VIDEO-3 - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks.
+ PRESET-VIDEO-4 - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
+ PRESET-VIDEO-5 - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
+ PRESET-VIDEO-6 - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
+ PRESET-VIDEO-7 - Use one content key to encrypt all of the SD\+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
+ PRESET-VIDEO-8 - Use one content key to encrypt all of the SD\+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
+ SHARED - Use the same content key for all of the video and audio tracks in your stream.
+ UNENCRYPTED - Don't encrypt any of the video tracks in your stream.
Type: String
Valid Values: `PRESET_VIDEO_1 | PRESET_VIDEO_2 | PRESET_VIDEO_3 | PRESET_VIDEO_4 | PRESET_VIDEO_5 | PRESET_VIDEO_6 | PRESET_VIDEO_7 | PRESET_VIDEO_8 | SHARED | UNENCRYPTED`
Required: Yes

## See Also
<a name="API_EncryptionContractConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/EncryptionContractConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/EncryptionContractConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/EncryptionContractConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
