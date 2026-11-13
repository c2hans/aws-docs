---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ProgramClockReferencePidConfiguration.html
---

# ProgramClockReferencePidConfiguration
<a name="API_ProgramClockReferencePidConfiguration"></a>

The configuration settings for the Program Clock Reference (PCR) Packet ID (PID).

## Contents
<a name="API_ProgramClockReferencePidConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** passthrough **   <a name="mediaconnect-Type-ProgramClockReferencePidConfiguration-passthrough"></a>
The PCR PID configuration that passes through the PCR PID from the source.
Type: [Passthrough](API_Passthrough.md) object
Required: No

 ** set **   <a name="mediaconnect-Type-ProgramClockReferencePidConfiguration-set"></a>
The PCR PID to use for the router output. MediaConnect applies this value only when the PCR is carried on its own PID. If the PCR is carried on an elementary stream, this value has no effect. If you also set the PMT PID, the two values must be different.
Type: Integer
Valid Range: Minimum value of 32. Maximum value of 8190.
Required: No

## See Also
<a name="API_ProgramClockReferencePidConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ProgramClockReferencePidConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ProgramClockReferencePidConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ProgramClockReferencePidConfiguration)
