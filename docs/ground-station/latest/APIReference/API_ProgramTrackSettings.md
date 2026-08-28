---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ProgramTrackSettings.html
---

# ProgramTrackSettings
<a name="API_ProgramTrackSettings"></a>

Program track settings for an antenna during a contact.

## Contents
<a name="API_ProgramTrackSettings_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** azEl **   <a name="groundstation-Type-ProgramTrackSettings-azEl"></a>
Program track settings for [AzElEphemeris](API_AzElEphemeris.md).
Type: [AzElProgramTrackSettings](API_AzElProgramTrackSettings.md) object
Required: No

 ** oem **   <a name="groundstation-Type-ProgramTrackSettings-oem"></a>
Program track settings for [OEMEphemeris](API_OEMEphemeris.md).
Type: [OemProgramTrackSettings](API_OemProgramTrackSettings.md) object
Required: No

 ** tle **   <a name="groundstation-Type-ProgramTrackSettings-tle"></a>
Program track settings for [TLEEphemeris](API_TLEEphemeris.md).
Type: [TleProgramTrackSettings](API_TleProgramTrackSettings.md) object
Required: No

## See Also
<a name="API_ProgramTrackSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ProgramTrackSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ProgramTrackSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ProgramTrackSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
