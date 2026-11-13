---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SingleProgramTransportStreamPidMapConfiguration.html
---

# SingleProgramTransportStreamPidMapConfiguration
<a name="API_SingleProgramTransportStreamPidMapConfiguration"></a>

The configuration settings for remapping the identification numbers of elementary streams and program identifiers of a single-program transport stream. For more information, see [PID remapping](https://docs.aws.amazon.com/mediaconnect/latest/ug/processors-pid-remapping.html) in the * AWS Elemental MediaConnect User Guide*.

## Contents
<a name="API_SingleProgramTransportStreamPidMapConfiguration_Contents"></a>

 ** defaultAction **   <a name="mediaconnect-Type-SingleProgramTransportStreamPidMapConfiguration-defaultAction"></a>
The action to apply to an elementary stream that doesn't match any rule. For more information, see [Rule actions](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-writing-rules.html#pid-remapping-actions) in the * AWS Elemental MediaConnect User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** rules **   <a name="mediaconnect-Type-SingleProgramTransportStreamPidMapConfiguration-rules"></a>
The ordered list of up to 32 rules that determine the action for each elementary stream. MediaConnect applies the first rule that matches. For more information, see [Rules](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-writing-rules.html) in the * AWS Elemental MediaConnect User Guide*.
Type: Array of [PidMapRule](API_PidMapRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Required: Yes

 ** auto **   <a name="mediaconnect-Type-SingleProgramTransportStreamPidMapConfiguration-auto"></a>
The settings for automatic Packet ID (PID) assignment. The default start PID is 512, with 32 PIDs per program.
Type: [AutoPidMapConfiguration](API_AutoPidMapConfiguration.md) object
Required: No

 ** programClockReferencePid **   <a name="mediaconnect-Type-SingleProgramTransportStreamPidMapConfiguration-programClockReferencePid"></a>
The Program Clock Reference (PCR) PID settings for the router output. By default, the router output passes through the PCR PID from the source. For more information, see [PCR placement](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-transport-stream-settings.html#pid-remapping-pcr-placement) in the * AWS Elemental MediaConnect User Guide*.
Type: [ProgramClockReferencePidConfiguration](API_ProgramClockReferencePidConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** programMapTablePid **   <a name="mediaconnect-Type-SingleProgramTransportStreamPidMapConfiguration-programMapTablePid"></a>
The Program Map Table (PMT) PID settings for the router output. By default, the router output passes through the PMT PID from the source. For more information, see [Transport stream settings](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-transport-stream-settings.html) in the * AWS Elemental MediaConnect User Guide*.
Type: [ProgramMapTablePidConfiguration](API_ProgramMapTablePidConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** programNumber **   <a name="mediaconnect-Type-SingleProgramTransportStreamPidMapConfiguration-programNumber"></a>
The program number settings for the router output. By default, the router output passes through the program number from the source. For more information, see [Transport stream settings](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-transport-stream-settings.html) in the * AWS Elemental MediaConnect User Guide*.
Type: [ProgramNumberConfiguration](API_ProgramNumberConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** transportStreamId **   <a name="mediaconnect-Type-SingleProgramTransportStreamPidMapConfiguration-transportStreamId"></a>
The transport stream ID (TSID) settings for the router output. By default, the router output passes through the TSID from the source. For more information, see [Transport stream settings](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-transport-stream-settings.html) in the * AWS Elemental MediaConnect User Guide*.
Type: [TransportStreamIdConfiguration](API_TransportStreamIdConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_SingleProgramTransportStreamPidMapConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SingleProgramTransportStreamPidMapConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SingleProgramTransportStreamPidMapConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SingleProgramTransportStreamPidMapConfiguration)
